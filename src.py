# coding=utf-8
from itertools import islice

urls = [url.replace("\n", "") for url in """
http://mpv.videocc.net/ef1fc5e977/3/ef1fc5e9776076cef5398a030a58c673_1.mp4?pid=1696745364113X1309165
🥝:
http://mpv.videocc.net/ef1fc5e977/9/ef1fc5e977a9c781b77e9111670de619_1.mp4?pid=1696745714308X1607220

🥝:
http://mpv.videocc.net/ef1fc5e977/f/ef1fc5e97720556421afffdc77db8bff_1.mp4?pid=1696745721706X1346928

🥝:
http://mpv.videocc.net/ef1fc5e977/3/ef1fc5e97733d136e3fb4fc48d7085b3_1.mp4?pid=1696745726758X1870153

🥝:
http://mpv.videocc.net/ef1fc5e977/8/ef1fc5e9777b7b8a30de4b33edae0718_1.mp4?pid=1696745730731X1899574

🥝:
http://mpv.videocc.net/ef1fc5e977/0/ef1fc5e977ed7e93cef97639712be220_1.mp4?pid=1696745735780X1984214

🥝:
http://mpv.videocc.net/ef1fc5e977/8/ef1fc5e977613dc1ba097b1c903ffce8_1.mp4?pid=1696745741574X1751115

🥝:
http://mpv.videocc.net/ef1fc5e977/f/ef1fc5e977ea2c9d143f0dea8fbb350f_1.mp4?pid=1696745747665X1521144

🥝:
http://mpv.videocc.net/ef1fc5e977/0/ef1fc5e977ec684dafb1aebcf62cbeb0_1.mp4?pid=1696745752662X1124484

🥝:
http://mpv.videocc.net/ef1fc5e977/f/ef1fc5e9770c9473b2ef8780bd181fcf_1.mp4?pid=1696745759082X1866059

🥝:
http://mpv.videocc.net/ef1fc5e977/7/ef1fc5e977175e5e11f0a03f91f74067_1.mp4?pid=1696745763614X1140943

🥝:
http://mpv.videocc.net/ef1fc5e977/3/ef1fc5e97767ae45c2bb6e5327f38c03_1.mp4?pid=1696745768230X1315976

🥝:
http://mpv.videocc.net/ef1fc5e977/5/ef1fc5e9775be329ce493b11c50022b5_1.mp4?pid=1696745775354X1345687

🥝:
http://mpv.videocc.net/ef1fc5e977/a/ef1fc5e9777528452ceebcc78d69b42a_2.mp4?pid=1696745780288X1643155

🥝:
http://mpv.videocc.net/ef1fc5e977/d/ef1fc5e977007875f39c399d9ad1061d_2.mp4?pid=1696745785769X1301946

🥝:
http://mpv.videocc.net/ef1fc5e977/c/ef1fc5e977817a753d55ac6678cc226c_1.mp4?pid=1696745802820X1859788

🥝:
http://mpv.videocc.net/ef1fc5e977/a/ef1fc5e977db6a3b7beeebd83fe6788a_1.mp4?pid=1696745806786X1008630

🥝:
http://mpv.videocc.net/ef1fc5e977/6/ef1fc5e9774154b3efbba97502583eb6_2.mp4?pid=1696745813357X1295728

🥝:
http://mpv.videocc.net/ef1fc5e977/c/ef1fc5e97761cc0c7eabed3eec1cafbc_1.mp4?pid=1696745818628X1651945

🥝:
http://mpv.videocc.net/ef1fc5e977/5/ef1fc5e9773512b950e4fa1a6390d295_2.mp4?pid=1696745824316X1599138

🥝:
http://mpv.videocc.net/ef1fc5e977/1/ef1fc5e977d00227be180d58329b8da1_1.mp4?pid=1696745936967X1964095

🥝:
http://mpv.videocc.net/ef1fc5e977/9/ef1fc5e977e0f5f4e982a0eef97cae09_2.mp4?pid=1696745940714X1808437

🥝:
http://mpv.videocc.net/ef1fc5e977/8/ef1fc5e97714ad79880f117a491100e8_2.mp4?pid=1696745946590X1103262

🥝:
http://mpv.videocc.net/ef1fc5e977/e/ef1fc5e977c23c967edb16739a0fcd7e_1.mp4?pid=1696745954239X1589578

🥝:
http://mpv.videocc.net/ef1fc5e977/1/ef1fc5e977688aa974bc8d0ce9a19d51_1.mp4?pid=1696745958318X1708179

🥝:
http://mpv.videocc.net/ef1fc5e977/d/ef1fc5e977b396b0f3f2e4ef31f0bfed_2.mp4?pid=1696745963184X1099305

🥝:
http://mpv.videocc.net/ef1fc5e977/a/ef1fc5e977f51c42c4a9ea6ce600971a_1.mp4?pid=1696746039808X1078716

🥝:
http://mpv.videocc.net/ef1fc5e977/1/ef1fc5e97765bc855fc3347450fb0691_1.mp4?pid=1696746045036X1396317

🥝:
http://mpv.videocc.net/ef1fc5e977/e/ef1fc5e977075fc39099f786ecbf0a9e_2.mp4?pid=1696746060241X1356473
🥝:
http://mpv.videocc.net/ef1fc5e977/f/ef1fc5e977efa54e6a279b1ea0eac68f_2.mp4?pid=1696746233350X1008199

🥝:
http://mpv.videocc.net/ef1fc5e977/0/ef1fc5e977d8c505dc80d22b5e87fa60_2.mp4?pid=1696746315247X1920471

🥝:
http://mpv.videocc.net/ef1fc5e977/f/ef1fc5e97741091413ed8f0f8c3d157f_1.mp4?pid=1696746319652X1521078

🥝:
http://mpv.videocc.net/ef1fc5e977/0/ef1fc5e9778c13790b2337b9b73c4c80_1.mp4?pid=1696746323687X1898045

🥝:
http://mpv.videocc.net/ef1fc5e977/6/ef1fc5e977a25fc11dbbca7292234a06_1.mp4?pid=1696746328285X1129247

🥝:
http://mpv.videocc.net/ef1fc5e977/2/ef1fc5e977fe388c8c991bf6fd340a82_1.mp4?pid=1696746332018X1161227

🥝:
http://mpv.videocc.net/ef1fc5e977/0/ef1fc5e977781990f4f2d67f3a55b5d0_2.mp4?pid=1696746334743X1728133

🥝:
http://mpv.videocc.net/ef1fc5e977/3/ef1fc5e977d7c41395f82124709deff3_2.mp4?pid=1696746407296X1745593

🥝:
http://mpv.videocc.net/ef1fc5e977/f/ef1fc5e97704cb510ee9c1ad09a702bf_1.mp4?pid=1696746413076X1694519

🥝:
http://mpv.videocc.net/ef1fc5e977/e/ef1fc5e977d2c3e480c0aad7899f47ce_2.mp4?pid=1696746417228X1752161

🥝:
http://mpv.videocc.net/ef1fc5e977/9/ef1fc5e977aaea3cb6c068e9bac8b219_1.mp4?pid=1696746422814X1434818

🥝:
http://mpv.videocc.net/ef1fc5e977/9/ef1fc5e97700bdabadfff3ce79725d49_1.mp4?pid=1696746428385X1771684

🥝:
http://mpv.videocc.net/ef1fc5e977/5/ef1fc5e9775fe7685164fcd478bcf255_1.mp4?pid=1696746433379X1038327

🥝:
http://mpv.videocc.net/ef1fc5e977/f/ef1fc5e9770c3a4f6ad8c561d5f2b21f_1.mp4?pid=1696746438776X1745491

🥝:
http://mpv.videocc.net/ef1fc5e977/f/ef1fc5e977b5d8b7f794c16b19a6e52f_2.mp4?pid=1696746442808X1444395

🥝:
http://mpv.videocc.net/ef1fc5e977/b/ef1fc5e977a30482c21a1f6ef9005bdb_1.mp4?pid=1696746447038X1450792

🥝:
http://mpv.videocc.net/ef1fc5e977/0/ef1fc5e977845a6b9084aa2a71e77710_2.mp4?pid=1696746458060X1833767

🥝:
http://mpv.videocc.net/ef1fc5e977/3/ef1fc5e977cb8726e6377b2c87a4db33_2.mp4?pid=1696746463716X1089008

🥝:
http://mpv.videocc.net/ef1fc5e977/c/ef1fc5e9777790c14c76b24c52fab95c_1.mp4?pid=1696746468709X1530589

🥝:
http://mpv.videocc.net/ef1fc5e977/0/ef1fc5e977e7b9ea541a0d5e63ebd980_2.mp4?pid=1696746472613X1445529

🥝:
http://mpv.videocc.net/ef1fc5e977/b/ef1fc5e977aef9cfa7b51a5ddf47b3fb_2.mp4?pid=1696746477303X1573384

🥝:
http://mpv.videocc.net/ef1fc5e977/8/ef1fc5e977715512e5d84a03ee376aa8_2.mp4?pid=1696746482743X1077453

🥝:
http://mpv.videocc.net/ef1fc5e977/e/ef1fc5e977eb69b4f33e4490ce700fce_1.mp4?pid=1696746487461X1304609

🥝:
http://mpv.videocc.net/ef1fc5e977/2/ef1fc5e977c90d29e16df11e31a1e722_1.mp4?pid=1696746494108X1472560""".split("🥝:")]


def chunks(data, SIZE=2):
    it = iter(data)
    for i in range(0, len(data), SIZE):
        yield list(islice(it, SIZE))


url_chunks = chunks(urls)
