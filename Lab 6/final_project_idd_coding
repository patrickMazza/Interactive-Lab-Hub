import time
from adafruit_servokit import ServoKit
import board
from adafruit_apds9960.apds9960 import APDS9960
from gtts import gTTS
import os
import pyglet
from time import sleep

i2c = board.I2C()
apds = APDS9960(i2c)

apds.enable_proximity = True

# Set channels to the number of servo channels on your kit.
# There are 16 channels on the PCA9685 chip.
kit = ServoKit(channels=16)

# Name and set up the servo according to the channel you are using.
servo = kit.servo[0]

# Set the pulse width range of your servo for PWM control of rotating 0-180 degree (min_pulse, max_pulse)
# Each servo might be different, you can normally find this information in the servo datasheet
servo.set_pulse_width_range(1500, 1620)

while apds.proximity <= 5:
    time.sleep(1)
while True:
    try:
        # Set the servo to 180 degree position
        servo.angle = 180
        time.sleep(100)
        # Set the servo to 0 degree position
        servo.angle = 0
        time.sleep(2)
        
    except KeyboardInterrupt:
        # Once interrupted, set the servo back to 0 degree position
        servo.angle = 0
        time.sleep(0.5)
        break
