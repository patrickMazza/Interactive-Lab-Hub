# SPDX-FileCopyrightText: 2017 Tony DiCola for Adafruit Industries
# SPDX-License-Identifier: MIT

# Simple test of the MPR121 capacitive touch sensor library.
# Will print out a message when any of the 12 capacitive touch inputs of the
# board are touched.  Open the serial REPL after running to see the output.
# Author: Tony DiCola
import time
import board
import busio
import qwiic_oled_display
import sys

# Import MPR121 module.
import adafruit_mpr121

# Create I2C bus.
i2c = busio.I2C(board.SCL, board.SDA)
mpr121 = adafruit_mpr121.MPR121(i2c)
# Create MPR121 object.

myOLED = qwiic_oled_display.QwiicOledDisplay()

if myOLED.is_connected() == False:
    print("The Qwiic OLED Display isn't connected to the system. Please check your connection", file=sys.stderr)


myOLED.begin()

# Loop forever testing each input and printing when they're touched.
while True:
    # Loop through all 12 inputs (0-11).
  #  for i in range(1):
        # Call is_touched and pass it then number of the input.  If it's touched
        # it will return True, otherwise it will return False.
    

    
    #  To actually draw anything on the display, you must call the display() function. 
   

    if mpr121[8].value:
        myOLED.begin()
        myOLED.clear(myOLED.PAGE)  #  Clear the display's buffer
        print("Box {} was touched this is the first value".format(8))
        myOLED.print("Box {} was touched this is the first value".format(8))  #  Add "Hello World" to buffer

    elif mpr121[7].value:
        myOLED.begin()
        myOLED.clear(myOLED.ALL)  #  Clear the display's buffer
        print("Box {} was touched this is the second value".format(7))
        myOLED.print("Box {} was touched this is the second value".format(7))  #  Add "Hello World" to buffer

    elif mpr121[3].value:
        myOLED.begin()
        myOLED.clear(myOLED.ALL)  #  Clear the display's buffer
        print("Box {} was touched this is the third value".format(3))
        myOLED.print("Box {} was touched this is the third value".format(3))  #  Add "Hello World" to buffer

    elif mpr121[4].value:
        myOLED.begin()
        myOLED.clear(myOLED.ALL)  #  Clear the display's buffer
        print("Box {} was touched this is the fourth value".format(4))
        myOLED.print("Box {} was touched this is the fourth value".format(4))  #  Add "Hello World" to buffer

    elif mpr121[10].value:
        myOLED.begin()
        myOLED.clear(myOLED.ALL)  #  Clear the display's buffer
        print("Box {} was touched this is the fifth value".format(10))
        myOLED.print("Box {} was touched this is the fifth value".format(10))  #  Add "Hello World" to buffer

    elif mpr121[1].value:
        myOLED.begin()
        myOLED.clear(myOLED.ALL)  #  Clear the display's buffer
        print("Box {} was touched this is the sixth value".format(1))
        myOLED.print("Box {} was touched this is the sixth value".format(1))  #  Add "Hello World" to buffer

    elif mpr121[5].value:
        myOLED.begin()
        myOLED.clear(myOLED.ALL)  #  Clear the display's buffer
        print("Box {} was touched this is the seventh value".format(5))
        myOLED.print("Box {} was touched this is the seventh value".format(5))  #  Add "Hello World" to buffer

    elif mpr121[9].value:
        myOLED.begin()
        myOLED.clear(myOLED.ALL)  #  Clear the display's buffer
        print("Box {} was touched this is the eighth value".format(9))
        myOLED.print("Box {} was touched this is the eighth value".format(9))  #  Add "Hello World" to buffer

    elif mpr121[6].value:
        myOLED.begin()
        myOLED.clear(myOLED.ALL)  #  Clear the display's buffer
        print("Box {} was touched this is the nineth value".format(6))
        myOLED.print("Box {} was touched this is the nineth value".format(6))  #  Add "Hello World" to buffer

    elif mpr121[2].value:
        myOLED.begin()
        myOLED.clear(myOLED.ALL)  #  Clear the display's buffer
        print("Box {} was touched this is the tenth value".format(2))
        myOLED.print("Box {} was touched this is the tenth value".format(2))  #  Add "Hello World" to buffer


    myOLED.display()
    time.sleep(0.25)  # Small delay to keep from spamming output messages.
