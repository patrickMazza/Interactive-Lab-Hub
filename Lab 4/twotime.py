# Touches
import time
import board
import busio
import adafruit_mpr121
i2c = busio.I2C(board.SCL, board.SDA)
mpr121 = adafruit_mpr121.MPR121(i2c)

touched = mpr121.touched_pins
# Test if 0 and 11 are touched.
if touched[0] and touched[11]:
    print('Input 0 and 11 touched!')