# -*- coding: utf-8-*-
#pico用ライブラリをインポート
from machine import Pin, I2C
#timeライブラリをインポート
from time import sleep
#bme280ライブラリをインポート
from bme280 import BME280

#I2C通信の設定(16pinをsda, 17pinをscl)
i2c = I2C(0, sda = Pin(16), scl = Pin(17))
#BME280の初期設定
bme = BME280(i2c = i2c)

'''
bme280センサの計測を行う関数
'''
def sensor():
    #温度・湿度・気圧データを取得し、それぞれに格納
    temp, press, humi = bme.read_compensated_data()
    #温度,湿度,気圧のデータを計算
    temp = float(temp / 100)
    humi = float(humi / 1024)
    press = float((press // 256) / 100)
    #計測したデータを戻り値として返す
    return temp, humi, press

while True:
    #sensor関数を呼び出し、戻り値をdata,temp,press,humiに格納
    temp, humi, press = sensor()
    #文字型に変換して変数dataに格納
    #humi及びpressを小数点以下第二位で四捨五入
    data = 'Temp:' + str(temp) + '℃,' + 'Humi:' + str(round(humi, 2)) + '%,' + 'Press:' + str(round(press, 2)) + 'hPa'
    print(data)  #シリアル通信にてデータ送信
    sleep(1)     #1sec待機