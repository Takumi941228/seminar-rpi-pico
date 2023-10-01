# -*- coding: utf-8-*-
#pico用ライブラリをインポート
from machine import Pin, I2C
#timeライブラリをインポート
from time import sleep, localtime
#ssd1306ライブラリをインポート
import ssd1306

#I2C通信の設定(16pinをsda, 17pinをscl）
i2c = I2C(0, sda = Pin(16), scl = Pin(17))

#OLEDの初期設定（解像度128x64, i2c通信を選択）
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

while True:
    time = localtime()  # 日時をtuple型で取得
    oled.fill(0)  #oledの表示を削除
    oled.text("Rasp Pi Pico",0,0)  #x=0, y=0座標に文字を出力
    oled.text("Hello Python",0,10) #x=0, y=20座標に文字を出力
    #time[0]:year,[1]:month,[2]:day,[3]:hour,[4]:minute,[5]:second
    oled.text(str(time[0])+"/"+str(time[1])+"/"+str(time[2]),0,20)
    oled.text(str(time[3])+":"+str(time[4])+":"+str(time[5]),5,30)
    oled.show() #oledにデータを表示
