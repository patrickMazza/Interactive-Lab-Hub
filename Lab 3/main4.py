import time
import board
from adafruit_apds9960.apds9960 import APDS9960
from gtts import gTTS
import os
import pyglet
from time import sleep

i2c = board.I2C()
apds = APDS9960(i2c)

apds.enable_proximity = True

sounds = {
    "Research Reader is on!": {
        "text": 'research paper',
        "filename": '/tmp/temp1.mp3'
    },
    "AC positive": {
        "text": "Ok, I turned off the AC.",
        "filename": '/tmp/temp2.mp3'
    },
    "reminder question": {
        "text": "When would you like me to remind you to close the window again?",
        "filename": '/tmp/temp3.mp3'
    },
    "no reminder": {
        "text": "Ok, I won't remind you",
        "filename": '/tmp/temp4.mp3'
    },
    "reminder": {
        "text": "It's time to close the window",
        "filename": '/tmp/temp5.mp3'
    }
}

def say(soundId):
    sound = pyglet.media.load(sounds[soundId]['filename'], streaming=False)
    sound.play()
    #prevent from killing
    sleep(sound.duration)

# Prepare sound files
for sound in sounds.values():
    tts = gTTS(text=sound['text'], lang='en')
    filename = sound['filename']
    tts.save(filename)



# ===== Interacation ========

print("Ready to help student read the paper!")
while apds.proximity <= 10:
    time.sleep(1)

print("Research Reader is on!")
say("research paper")

paper_response = input("Type in the subject of the Research Paper you wan to read: Physics, AI, Healthcare?")

if paper_response == "Physics":
    say("AC positive")
elif paper_response == "AI":
    say("Mario")
elif paper_response == "AI":
    say("Luigi")

say("reminder question")
response_reminder = input("Controller: Remind in minutes? (no reminder => 0)")

if response_reminder == "0":
    say("no reminder")
else:
    tts = gTTS(text=f"Ok, I will remind you in {response_reminder} minutes.", lang='en')
    filename_reminder = "/tmp/temp6.mp3"
    tts.save(filename_reminder)

    reminder_sound = pyglet.media.load(filename_reminder, streaming=False)
    reminder_sound.play()
    #prevent from killing
    sleep(reminder_sound.duration)

    input("Controller: Press any key to trigger reminder")

    say("reminder")





# ========= Cleanup ===========

#remove temporary files
for sound in sounds.values():
    os.remove(sound['filename']) 

os.remove(filename_reminder) 

print("removed all temp files")