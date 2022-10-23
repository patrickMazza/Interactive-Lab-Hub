#arecord -f cd -r 16000 -d 5 -t wav recorded.wav && sox recorded.wav recorded_mono.wav remix 1,2
import time
import board
from adafruit_apds9960.apds9960 import APDS9960

i2c = board.I2C()

apds = APDS9960(i2c)
apds.enable_proximity = True
apds.enable_gesture = True


while True:
    gesture = apds.gesture()
    if gesture == 0x01:
        print("up")
    elif gesture == 0x02:
        print("down")
    elif gesture == 0x03:  
        print("left")
    elif gesture == 0x04:
        print("right")

pico2wave -w girlfriends.wav "How many girlfriends do you have?" && aplay girlfriends.wav

arecord -D hw:2,0 -f cd -c1 -r 48000 -d 5 -t wav recorded_mono.wav
python3 test_words.py recorded_mono.wav
