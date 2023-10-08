# coding=utf-8
from rich.progress import TextColumn, BarColumn, Progress

custom_columns = [
    TextColumn(
        "[bold blue]{task.fields[filename]}",
        justify="right"),

    BarColumn(
        bar_width=None,
        complete_style="yellow",
        finished_style="green"),
    TextColumn("{task.percentage:>3.2f}%"),
    TextColumn("[bold green]{task.fields[speed]} MB/s"),
    TextColumn("[bold cyan]{task.fields[file_size]}"),

]

downloads_progress = Progress(*custom_columns, auto_refresh=True, expand=True, transient=True)
