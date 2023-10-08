import threading
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed
from datetime import datetime
from pathlib import Path
from time import time

import requests

import src
from rich_progress import downloads_progress


class Downloader:
    def __init__(self, urls, progress, save_folder="./downloads"):
        self.urls = urls
        self.save_folder = save_folder
        self.progress_info = {}
        self.completed = set()
        Path(self.save_folder).mkdir(parents=True, exist_ok=True)
        self.all_tasks_done = threading.Event()  # 创建一个 Event 对象
        self.partial_done = threading.Event()
        self.download_progress = progress

    def download_mp4(self, url, file_index):
        response = requests.head(url)
        if response.status_code != 200:
            print(f"Failed to HEAD {url}: {response.status_code}")
            return

        total_size = int(response.headers.get('content-length', 0))
        filename = f"video_{file_index}.mp4"

        save_path = Path(self.save_folder) / filename
        resume_byte_pos = 0
        if save_path.exists():
            resume_byte_pos = save_path.stat().st_size

        custom_headers = {'Range': f"bytes={resume_byte_pos}-"}
        response = requests.get(url, headers=custom_headers, stream=True)

        if response.status_code == 416:
            with self.download_progress:
                self._single_handler(url)
        elif response.status_code == 200 or response.status_code == 206:

            # 初始化时间和已下载的字节数
            start_time = time()
            downloaded_size = resume_byte_pos
            speed = 0
            write_mode = 'wb' if resume_byte_pos == 0 else 'ab'
            # 设置超时和最小速度阈值
            timeout_seconds = 10  # 如果 60 秒内没有进展，则超时
            min_speed = 0.5  # 最小速度阈值，单位 MB/s

            last_check_time = datetime.now()
            last_downloaded_size = 0
            with self.download_progress:  # 注意这里的改动
                task_id = self.download_progress.add_task(
                    description=f"Downloading {filename[-10:]}",
                    total=total_size,
                    filename=filename,
                    speed="0.00",
                    file_size=f"{0.0}/{total_size / (1024 * 1024):.2f} MB"
                )
                with open(save_path, write_mode) as f:
                    for chunk in response.iter_content(chunk_size=1024):
                        if chunk:
                            # 超时检测
                            now = datetime.now()
                            elapsed_since_last_check = (
                                    now - last_check_time).total_seconds()
                            if elapsed_since_last_check >= timeout_seconds:
                                speed_since_last_check = (downloaded_size - last_downloaded_size) / (
                                        1024 * 1024) / elapsed_since_last_check

                                if speed_since_last_check < min_speed:
                                    print(
                                        f"Download too slow or timed out for {filename}. Restarting...")
                                    self.download_mp4(url, file_index)
                                    return

                                last_check_time = now
                                last_downloaded_size = downloaded_size
                            # 下载状态信息
                            downloaded_size += len(chunk)
                            elapsed_time = time() - start_time
                            if elapsed_time != 0:
                                speed = (downloaded_size / elapsed_time) / \
                                        (1024 * 1024)  # MB/s
                            percent_complete = (
                                                       downloaded_size / total_size) * 100
                            # 更新已下载和总大小
                            file_size_str = f"{downloaded_size / (1024 * 1024):.2f}/{total_size / (1024 * 1024):.2f} MB"
                            self.download_progress.update(
                                task_id,
                                completed=downloaded_size,
                                description=f"Downloading {filename[-10:]} {percent_complete:.2f}% @ {speed:.2f} MB/s",
                                speed=f"{speed:.2f}",
                                file_size=file_size_str  # 添加文件大小显示
                            )
                            f.write(chunk)
                        else:
                            print(f"Received an empty chunk for {url}.")
                self._single_handler(url)
        else:
            print(f"Failed to GET {filename}: {response.status_code}")
            self._single_handler(url)
            return

    def _single_handler(self, url):
        self.completed.add(url)
        self.download_progress.update(global_task_id, advance=1)
        self.partial_done.set()
        if len(self.completed) == len(self.urls):
            self.all_tasks_done.set()
        self.all_tasks_done.wait()

    def start_downloading(self, max_workers=10):
        with ThreadPoolExecutor(max_workers=300) as executor:
            futures = []
            # 刚开始运行8个
            for index, url in enumerate(self.urls[:max_workers]):
                try:
                    futures.append(
                        executor.submit(
                            self.download_mp4, url, index))
                except Exception as exc:
                    print(f"{url} generated an exception: {exc}")
            for index, url in enumerate(self.urls[max_workers:]):
                self.partial_done.wait()
                try:
                    futures.append(
                        executor.submit(
                            self.download_mp4, url, index))
                    if len(self.completed) == len(self.urls):
                        break
                    self.partial_done.clear()
                except Exception as exc:
                    print(f"{url} generated an exception: {exc}")
            for future in as_completed(futures):
                try:
                    future.result()
                except Exception as exc:
                    print(f"{future} generated an exception: {exc}")


if __name__ == "__main__":
    global_task_id = downloads_progress.add_task(
        description="Overall Progress",
        total=len(
            src.urls),
        completed=0,
        filename="Overall Progress",
        speed="0.00",
        file_size="0.00/0.00 MB")

    downloader = Downloader(src.urls, downloads_progress)
    downloader.start_downloading()
    print("\nAll downloads completed.")
