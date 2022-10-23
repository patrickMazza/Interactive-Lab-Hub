import time
import board
import busio
import qwiic_oled_display
import sys
import adafruit_mpr121

i2c = busio.I2C(board.SCL, board.SDA)

mpr121 = adafruit_mpr121.MPR121(i2c)
def runExample():
  print("\nSparkFun Qwiic OLED Display - Hello Example\n")
  myOLED = qwiic_oled_display.QwiicOledDisplay()
myOLED.begin()

    
while True:
    if mpr121[4].value:
            print("Box {} was touched this is the 1st value".format(4))
            myOLED.clear(myOLED.PAGE)  #  Clear the display's buffer
            myOLED.print("Hello World")
            myOLED.display()

    myOLED.print("Hello World")  #  Add "Hello World" to buffer
    elif mpr121[i].value != 4:
             print("wrong, score 0, restart")
time.sleep(0.25)  # Small delay to keep from spamming output messages.

runExample()