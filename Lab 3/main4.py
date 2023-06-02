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
    "Resarch buddy ready": {
        "text": 'The research Reader Buddy is ready, what research subject would you like me to read?',
        "filename": '/tmp/temp1.mp3'
    },
    #Improvement is implimenting txt file
    "phys": {
        "text": "String theorys holographic QCD duality makes predictions for hadron physics by building models that live in five-dimensional (5D) curved space. We show that finding the hadron mass spectrum in these models amounts to finding the eigenvalues of a one-dimensional differential equation identical in form to the Schrödinger equation. ",
        "filename": '/tmp/temp2.mp3'
    },
    "Art": {
        "text": "We present a scalable approach for semi-supervised learning on graph-structured data that is based on an efficient variant of convolutional neural networks which operate directly on graphs. We motivate the choice of our convolutional architecture via a localized first-order approximation of spectral graph convolutions.",
        "filename": '/tmp/temp3.mp3'
    },
    "HC": {
        "text": "Coordination of quality care for the growing population of cancer survivors with comorbidities remains poorly understood, especially among health disparity populations who are more likely to have comorbidities at the time of cancer diagnosis. This systematic review synthesized the literature from 2000 to 2022 on team-based care for cancer survivors ?",
        "filename": '/tmp/temp4.mp3'
    },
    "end_Paper": {
        "text": "Thats the end of the paper, did you want to read or re-read any other of the choices?",
        "filename": '/tmp/temp5.mp3'
    },
     "end_Paper1": {
        "text": "Thanks for studying!",
        "filename": '/tmp/temp6.mp3'
    },
    "redo": {
        "text": "sure here it is again",
        "filename": '/tmp/temp7.mp3'
    },
     "phys1": {
        "text": "String theorys holographic QCD duality makes predictions for hadron physics by building models that live in five-dimensional (5D) curved space. We show that finding the hadron mass spectrum in these models amounts to finding the eigenvalues of a one-dimensional differential equation identical in form to the Schrödinger equation. ",
        "filename": '/tmp/temp8.mp3'
    },
    "Art1": {
        "text": "We present a scalable approach for semi-supervised learning on graph-structured data that is based on an efficient variant of convolutional neural networks which operate directly on graphs. We motivate the choice of our convolutional architecture via a localized first-order approximation of spectral graph convolutions.",
        "filename": '/tmp/temp3.mp3'
    },
    "HC1": {
        "text": "Coordination of quality care for the growing population of cancer survivors with comorbidities remains poorly understood, especially among health disparity populations who are more likely to have comorbidities at the time of cancer diagnosis. This systematic review synthesized the literature from 2000 to 2022 on team-based care for cancer survivors ?",
        "filename": '/tmp/temp9.mp3'
    },
    "endStudy": {
        "text": "Ill be here when you need me, good luck studying!",
        "filename": '/tmp/temp10.mp3'
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
while apds.proximity <= 5:
    time.sleep(1)

print("Research Reader is on!")
say("Resarch buddy ready")

topic_Response = input("Pick the subject of the Research Paper you wanty to read: Physics, AI, Healthcare?")

if topic_Response == "Physics":
    say("phys")
elif topic_Response == "AI":
    say("Art")
elif topic_Response == "Healthcare":
    say("HC")

say("end_Paper")
reread = input("Did you want to re-read that paper (y/n)")

if reread == "y":
    say("redo")
    if topic_Response == "Physics":
        say("phys1")
    elif topic_Response == "AI":
        say("Art1")
    elif topic_Response == "Healthcare":
        say("HC1")
    say("end_Paper1")
else:
   # tts = gTTS(text=f"Ok, I will remind you in {reread} minutes.", lang='en')
   # filename_reminder = "/tmp/temp11.mp3"
   # tts.save(filename_reminder)

   # reminder_sound = pyglet.media.load(filename_reminder, streaming=False)
   # reminder_sound.play()

   # sleep(reminder_sound.duration)

   # input("Press Enter to be done")

    say("endStudy")





# ========= Cleanup ===========

#remove temporary files
for sound in sounds.values():
    os.remove(sound['filename']) 

os.remove(filename_reminder) 

print("removed all temp files")
