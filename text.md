# プログラミング技術（Python入門）

## Raspberry Pi Picoについて

Raspberry Pi財団が独自に開発したARM Cortex M0+デュアルコアのRP2040マイコンを搭載した開発基板です。C/C++およびMicroPythonで開発が可能です。既存のRaspberry Piとは異なりLinux OSは搭載できません。

### [主な特徴](https://www.raspberrypi.com/products/raspberry-pi-pico/)

* Paspberry Pi設計のRP2040マイコン搭載
* USBを介しマスストレージを使ったドラッグアンドドロップによるプログラムの書き込みが可能
* USB 1.1 ホスト/デバイス両対応
* 低消費電力スリープモードおよびドーマントモードが利用可
* C/C++及びPython3ベースの組み込み用MicroPython言語による開発が可能
* 温度センサが搭載

### 仕様

- RP2040（デュアルコア ARM Cortex M0+プロセッサ）
- 最大動作周波数 133 MHz
- SRAM：264KB
- フラッシュメモリ：2MB
- インターフェース
    - GPIO x 26pin
    -  SPI x 2
    - I2C x 2
    - UART x 2
    - 12 bit ADC x 3
    - PWM x 16
    - プログラマブルI/Ox 8

### ピン配置

ピンレイアウトは下図の通りとなります。

![外観図](./image/img6.png)

### [Raspberry Pi Picoの環境構築](https://www.raspberrypi.com/documentation/microcontrollers/micropython.html)

以下のアドレスからRapberry Pi Pico用のUF2ファイルをダウンロードします。（Pico WはWi-Fiモジュール搭載用なので間違わないようにします。※日本未発売R4.9.22）

* <https://www.raspberrypi.com/documentation/microcontrollers/micropython.html>

* `BOOTSELボタン`を押したまま、PicoをPCのUSB ポートに接続します。Picoが接続されたら、`BOOTSELボタン`を放します。

* `RPI-RP2`と呼ばれるマスストレージデバイスとしてマウントされます。

![外観図](./image/img21.png)

* MicroPython UF2ファイルをRPI-RP2ボリュームに`ドラッグ＆ドロップ`します。Picoが再起動します。

### 配線

配線図は以下の図及び表にならって、配線します。

![外観図](./image/img14.png)

| Pico | pin| SSD1306 | BME280 |
| --- | --- | --- | --- |
| 3V3(OUT) | 36 | VCC | VDD |
| GND | 23 | GND | GND |
| SCL | 22 | SCL | SCK |
| SDA | 21 | SDA | SDI |
| 3V3(OUT) | 36 | --- | CSB |
| GND | 23 | --- | SDO |


## MicroPython用開発環境Thonnyについて

Raspberry Pi向けのPython開発環境Thonnyは、初心者向けの統合開発環境であり、最新のRaspberry Pi OSに標準でインストールされています。

### MicroPythonとは

マイクロコンピュータや組み込み機器で使われるプログラミング言語はC/C++が一般的ですが、初心者にとっては学習障壁が比較的高い言語でもあります。`「MicroPython」`はPython3と高い互換性があるプログラミング言語であるため、プログラミング初心者でも理解しやすいPythonの文法を使ってプログラミングすることができます。

* MicroPython - Python for microcontrollers
    * <http://micropython.org/>

### インタプリタの選択

ツール＜オプション からインタプリタの設定画面を開きます。

- Which kind of interpreter...code?
    - MicroPython(Raspberry Pi Pico)
- ポートまたはWebREPL
    - USBシリアルデバイス名@（自身のCOM番号）
- OK

![外観図](./image/img23.png)

### ライブラリのインストール

`SSD1306`及び`AE-BME280`をMicroPythonで開発する際に便利なライブラリがあるのでダウンロードします。

ツール＜パッケージを管理...、`ssd1306`で検索する。
- micropython_ssd1306
    - `https://github.com/stlehmann/micropython-ssd1306`

ツール＜パッケージを管理...、`bme280`で検索する。
- micropython_bme280
    - `https://github.com/stlehmann/micropython-ssd1306`

ライブラリがインストールされると以下のようにインストール項目に追加されます。

![外観図](./image/img22.png)

## 組み込みプログラミング

サンプルプログラムを実行し、Picoと各種センサについて学習します。

### LEDの制御

Raspberry Pi Picoに内蔵されているLED（`GPIO25pin`）を使用して、Lチカを行います。

* ファイル名（pico_led.py）
```python
# -*- coding: utf-8-*-
#pico用ライブラリをインポート
from machine import Pin
#timeライブラリをインポート
from time import sleep

#picoの内蔵led(GPIO25を出力ピンに定義)
led = Pin(25, Pin.OUT)

#無限ループ
while True:
    led.value(1) #led点灯
    sleep(1)     #1sec待機
    led.value(0) #led消灯
    sleep(1)     #isec待機
```

プログラムの実行をするには、`緑色のアイコン`をクリックします。止めるときは、`STOP`のアイコンです。

![外観図](./image/img28.png)

### OLEDの表示

有機ELディスプレイ（OLED）をPicoにI2C接続を行い、文字を表示します。

* ファイル名（pico_ssd1306.py）

```python
# -*- coding: utf-8-*-
#pico用ライブラリをインポート
from machine import Pin, I2C
#timeライブラリをインポート
from time import sleep, localtime
#ssd1306ライブラリをインポート
from ssd1306 import SSD1306_I2C

#I2C通信の設定(16pinをsda, 17pinをscl）
i2c = I2C(0, sda = Pin(16), scl = Pin(17))

#OLEDの初期設定（解像度128x64, i2c通信を選択）
oled = SSD1306_I2C(128, 64, i2c)

while True:
    time = localtime()  # 日時をtuple型で取得
    oled.fill(0)  #oledの表示を削除
    oled.text("Rasp Pi Pico",0,0)  #x=0, y=0座標に文字を出力
    oled.text("Hello Python",0,10) #x=0, y=20座標に文字を出力
    #time[0]:year,[1]:month,[2]:day,[3]:hour,[4]:minute,[5]:second
    oled.text(str(time[0])+"/"+str(time[1])+"/"+str(time[2]),0,20)
    oled.show() #oledにデータを表示
```

### BME280センサデータの取得

BME280センサをPicoにI2C接続を行いデータを取得し、シェル画面上に表示します。

* ファイル名（pico_bme280.py）

```python
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
    print(data)  #シリアル通信にてデータをシェルに表示
    sleep(1)     #1sec待機
```

正しく接続ができていれば、以下のようなセンサデータがshell画面に１秒間隔で表示されます。

![外観図](./image/img9.png)

# 課題プログラム

今までのサンプルコードを参考にして、以下の動作を可能にするプログラムを作成してください。

* １秒毎に温度・湿度・気圧を計測し、液晶ディスプレイに現在時刻とともに表示しなさい。表示する形は自由です。

* ある一定の温度値以上を計測した場合、Picoの任意のGPIOPINに接続されたLEDを点灯させなさい。また、通常は消灯させること。LEDを接続する際は、1kΩ程の保護抵抗を直接接続させ、極性に気をつけること。なお、センサ自体を指で温めると簡単に変動します。

* なお、センサから値を計測する際は、sensor関数を使用し、また、sensor関数から受け取ったデータ値とともに現在時刻を引数として、液晶ディスプレイに表示するためのmonitor関数を作成し、関数内で液晶の表示を行いなさい。
