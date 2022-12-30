import time
import board
import pwmio
import adafruit_mpr121
import busio
import neopixel
from song import*

from adafruit_apds9960.apds9960 import APDS9960

pixels = neopixel.NeoPixel(board.NEOPIXEL, 1)
i2c = busio.I2C(board.SCL1, board.SDA1)
touch_pad = adafruit_mpr121.MPR121(i2c)

apds = APDS9960(i2c)
apds.enable_proximity = True
apds.enable_gesture = True

tone = pwmio.PWMOut(board.A0, variable_frequency=True)
red = pwmio.PWMOut(board.TX)
green = pwmio.PWMOut(board.A2)
blue = pwmio.PWMOut(board.A3)

volume = 25000
tone.duty_cycle = volume  # 0-32768
rdex = 30000
gdex = 20000
bdex = 10000
notes = [277, 294, 311, 330, 349, 370, 392, 410, 440, 466]
tone_duration = 0.2
rest_duration = 0.01


def play_a_tone(freq):
    tone.duty_cycle = volume
    tone.frequency = freq


def play_a_rest(duration):
    tone.duty_cycle = 0
    time.sleep(duration)

def play_jinitaimei():
    play_a_tone(440)
    time.sleep(0.1)
    play_a_rest(0.05)
    play_a_tone(440)
    time.sleep(0.1)
    play_a_rest(0.05)
    play_a_tone(330)
    time.sleep(0.3)
    play_a_rest(0.1)
    play_a_tone(330)
    time.sleep(0.1)
    play_a_tone(440)
    time.sleep(0.3)
    play_a_rest(0.7)

    play_a_tone(440)
    time.sleep(0.1)
    play_a_rest(0.05)
    play_a_tone(440)
    time.sleep(0.1)
    play_a_rest(0.05)
    play_a_tone(440)
    time.sleep(0.1)
    play_a_rest(0.7)
    play_a_tone(330)
    time.sleep(0.1)
    play_a_rest(0.05)
    play_a_tone(330)
    time.sleep(0.1)
    play_a_rest(0.5)

    play_a_tone(440)
    time.sleep(0.1)
    play_a_rest(0.05)
    play_a_tone(440)
    time.sleep(0.1)
    play_a_rest(0.05)
    play_a_tone(330)
    time.sleep(0.3)
    play_a_rest(0.1)
    play_a_tone(330)
    time.sleep(0.1)
    play_a_tone(440)
    time.sleep(0.3)
    print("play a loaded song")

while True:
    touched = False
    gesture = apds.gesture()
    if gesture == 0x01:
        play_jinitaimei()
    if gesture == 0x02:
        for i in range(20):
            play_a_tone(song_1[i])
            time.sleep(0.2)
            touched = True
        print("play a loaded song")
    if gesture == 0x03:
        for i in range(20):
            play_a_tone(song_1[i])
            time.sleep(0.5)
            touched = True
        print("play a loaded song")

    if gesture == 0x04:
        for i in range(7):
            play_a_tone(song_2[i])
            time.sleep(0.3)
            touched = True
        print("play a loaded song")

    if touch_pad[0].value:
        print("Touched #{}!".format(0))
        play_a_tone(notes[0])
        pixels.fill((notes[0] / 2, 0, 0))
        touched = True
    if touch_pad[1].value:
        print("Touched #{}!".format(1))
        play_a_tone(notes[1])
        pixels.fill((0, 0, notes[2] / 2))
        touched = True
    if touch_pad[2].value:
        print("Touched #{}!".format(2))
        play_a_tone(notes[2])
        pixels.fill((0, notes[2] / 2, 0))
        touched = True
    if touch_pad[3].value:
        print("Touched #{}!".format(3))
        play_a_tone(notes[3])
        pixels.fill((notes[3] / 2, notes[3] / 2, 0))
        touched = True
    if touch_pad[4].value:
        print("Touched #{}!".format(4))
        play_a_tone(notes[4])
        pixels.fill((notes[4] / 2, 0, notes[4] / 2))
        touched = True
    if touch_pad[5].value:
        print("Touched #{}!".format(5))
        play_a_tone(notes[5])
        pixels.fill((notes[5] / 2, 0, notes[5] / 2))
        touched = True
    if touch_pad[6].value:
        print("Touched #{}!".format(6))
        play_a_tone(notes[6])
        pixels.fill((0, notes[6] / 2, notes[6] / 2))
        touched = True
    if touch_pad[7].value:
        print("Touched #{}!".format(7))
        play_a_tone(notes[7])
        pixels.fill((notes[7] / 2, notes[7] / 5, notes[7] / 7))
        touched = True
    if touch_pad[8].value:
        print("Touched #{}!".format(8))
        play_a_tone(notes[8])
        pixels.fill((notes[8] / 7, notes[8] / 3, notes[8] / 2))
        touched = True
    if touch_pad[9].value:
        print("Touched #{}!".format(9))
        play_a_tone(notes[9])
        pixels.fill((notes[9] / 4, notes[9] / 7, notes[9] / 2))
        touched = True
    if touch_pad[10].value:
        volume = volume + 100
        print("volume up")
        print(volume)
        if volume > 32768:
            volume = 32768
        pixels.fill((volume / 129, 0, 0))
    if touch_pad[11].value:
        volume = volume - 100
        print("volume down")
        print(volume)
        if volume < 0:
            volume = 0
        pixels.fill((0, 0, volume / 129))
    if touched is False:
        tone.duty_cycle = 0
        red.duty_cycle = 0
        green.duty_cycle = 0
        blue.duty_cycle = 0
        pixels.fill((0, 0, 0))
