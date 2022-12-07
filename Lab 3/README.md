# Chatterboxes
**NAMES OF COLLABORATORS HERE**
[![Watch the video](https://user-images.githubusercontent.com/1128669/135009222-111fe522-e6ba-46ad-b6dc-d1633d21129c.png)](https://www.youtube.com/embed/Q8FWzLMobx0?start=19)

In this lab, we want you to design interaction with a speech-enabled device--something that listens and talks to you. This device can do anything *but* control lights (since we already did that in Lab 1).  First, we want you first to storyboard what you imagine the conversational interaction to be like. Then, you will use wizarding techniques to elicit examples of what people might say, ask, or respond.  We then want you to use the examples collected from at least two other people to inform the redesign of the device.

We will focus on **audio** as the main modality for interaction to start; these general techniques can be extended to **video**, **haptics** or other interactive mechanisms in the second part of the Lab.

## Prep for Part 1: Get the Latest Content and Pick up Additional Parts 

### Pick up Web Camera If You Don't Have One

Students who have not already received a web camera will receive their [IMISES web cameras](https://www.amazon.com/Microphone-Speaker-Balance-Conference-Streaming/dp/B0B7B7SYSY/ref=sr_1_3?keywords=webcam%2Bwith%2Bmicrophone%2Band%2Bspeaker&qid=1663090960&s=electronics&sprefix=webcam%2Bwith%2Bmicrophone%2Band%2Bsp%2Celectronics%2C123&sr=1-3&th=1) on Thursday at the beginning of lab. If you cannot make it to class on Thursday, please contact the TAs to ensure you get your web camera. 

### Get the Latest Content

As always, pull updates from the class Interactive-Lab-Hub to both your Pi and your own GitHub repo. There are 2 ways you can do so:

**\[recommended\]**Option 1: On the Pi, `cd` to your `Interactive-Lab-Hub`, pull the updates from upstream (class lab-hub) and push the updates back to your own GitHub repo. You will need the *personal access token* for this.

```
pi@ixe00:~$ cd Interactive-Lab-Hub
pi@ixe00:~/Interactive-Lab-Hub $ git pull upstream Fall2022
pi@ixe00:~/Interactive-Lab-Hub $ git add .
pi@ixe00:~/Interactive-Lab-Hub $ git commit -m "get lab3 updates"
pi@ixe00:~/Interactive-Lab-Hub $ git push
```

Option 2: On your your own GitHub repo, [create pull request](https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2022Fall/readings/Submitting%20Labs.md) to get updates from the class Interactive-Lab-Hub. After you have latest updates online, go on your Pi, `cd` to your `Interactive-Lab-Hub` and use `git pull` to get updates from your own GitHub repo.

## Part 1.

### Text to Speech 

In this part of lab, we are going to start peeking into the world of audio on your Pi! 

We will be using the microphone and speaker on your webcamera. In the home directory of your Pi, there is a folder called `text2speech` containing several shell scripts. `cd` to the folder and list out all the files by `ls`:

```
pi@ixe00:~/text2speech $ ls
Download        festival_demo.sh  GoogleTTS_demo.sh  pico2text_demo.sh
espeak_demo.sh  flite_demo.sh     lookdave.wav
```

You can run these shell files by typing `./filename`, for example, typing `./espeak_demo.sh` and see what happens. Take some time to look at each script and see how it works. You can see a script by typing `cat filename`. For instance:

```
pi@ixe00:~/text2speech $ cat festival_demo.sh 
#from: https://elinux.org/RPi_Text_to_Speech_(Speech_Synthesis)#Festival_Text_to_Speech

echo "Just what do you think you're doing, Dave?" | festival --tts
```

Now, you might wonder what exactly is a `.sh` file? Typically, a `.sh` file is a shell script which you can execute in a terminal. The example files we offer here are for you to figure out the ways to play with audio on your Pi!

You can also play audio files directly with `aplay filename`. Try typing `aplay lookdave.wav`.

\*\***Write your own shell file to use your favorite of these TTS engines to have your Pi greet you by name.**\*\*
(This shell file should be saved to your own repo for this lab.)

Bonus: If this topic is very exciting to you, you can try out this new TTS system we recently learned about: https://github.com/rhasspy/larynx

### Speech to Text

Now examine the `speech2text` folder. We are using a speech recognition engine, [Vosk](https://alphacephei.com/vosk/), which is made by researchers at Carnegie Mellon University. Vosk is amazing because it is an offline speech recognition engine; that is, all the processing for the speech recognition is happening onboard the Raspberry Pi. 

In particular, look at `test_words.py` and make sure you understand how the vocab is defined. 
Now, we need to find out where your webcam's audio device is connected to the Pi. Use `arecord -l` to get the card and device number:
```
pi@ixe00:~/speech2text $ arecord -l
**** List of CAPTURE Hardware Devices ****
card 1: Device [Usb Audio Device], device 0: USB Audio [USB Audio]
  Subdevices: 1/1
  Subdevice #0: subdevice #0
```
The example above shows a scenario where the audio device is at card 1, device 0. Now, use `nano vosk_demo_mic.sh` and change the `hw` parameter. In the case as shown above, change it to `hw:1,0`, which stands for card 1, device 0.  

Now, look at which camera you have. Do you have the cylinder camera (likely the case if you received it when we first handed out kits), change the `-r 16000` parameter to `-r 44100`. If you have the IMISES camera, check if your rate parameter says `-r 16000`. Save the file using Write Out and press enter.

Then try `./vosk_demo_mic.sh`

\*\***Write your own shell file that verbally asks for a numerical based input (such as a phone number, zipcode, number of pets, etc) and records the answer the respondent provides.**\*\*

### Serving Pages

In Lab 1, we served a webpage with flask. In this lab, you may find it useful to serve a webpage for the controller on a remote device. Here is a simple example of a webserver.

```
pi@ixe00:~/Interactive-Lab-Hub/Lab 3 $ python server.py
 * Serving Flask app "server" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 162-573-883
```
From a remote browser on the same network, check to make sure your webserver is working by going to `http://<YourPiIPAddress>:5000`. You should be able to see "Hello World" on the webpage.

### Storyboard


Storyboard and/or use a Verplank diagram to design a speech-enabled device. (Stuck? Make a device that talks for dogs. If that is too stupid, find an application that is better than that.) 

\*\***Post your storyboard and diagram here.**\*\*
![Note Sep 25, 2022](https://user-images.githubusercontent.com/112049036/192357985-f7c70b49-1b13-42d3-8662-1f3bf58913e8.jpg)


Write out what you imagine the dialogue to be. Use cards, post-its, or whatever method helps you develop alternatives or group responses. 

\*\***Please describe and document your process.**\*\*
The dialoge used here would be in an academic setting. The interaction I have designed is essentially a study buddy that reads a research paper while you are busy doing other studious activities. So the words that would be said durring this process would be ones of fustration or memorization. This could range from explitives to review definitions on a flashcard. In the interaction that was filmed, there is a student who is doing her math homework and is frustated because she also has to read a research paper. This promts her to ask the robot to read the research paper while she is doing her other homework so she can multitask effectivly. The user also can instruct the device to stop talking and resume at will of the user.

### Acting out the dialogue


https://user-images.githubusercontent.com/112049036/192150336-f0789f6d-40b2-4a4c-a19c-6948c8e2cc47.mp4



Find a partner, and *without sharing the script with your partner* try out the dialogue you've designed, where you (as the device designer) act as the device you are designing.  Please record this interaction (for example, using Zoom's record feature).

\*\***Describe if the dialogue seemed different than what you imagined when it was acted out, and how.**\*\*

### Wizarding with the Pi (optional)
In the [demo directory](./demo), you will find an example Wizard of Oz project. In that project, you can see how audio and sensor data is streamed from the Pi to a wizard controller that runs in the browser.  You may use this demo code as a template. By running the `app.py` script, you can see how audio and sensor data (Adafruit MPU-6050 6-DoF Accel and Gyro Sensor) is streamed from the Pi to a wizard controller that runs in the browser `http://<YouPiIPAddress>:5000`. You can control what the system says from the controller as well!

\*\***Describe if the dialogue seemed different than what you imagined, or when acted out, when it was wizarded, and how.**\*\*

The dialogue was in allignment with what I think would have happened. The user could not read the research paper and do her math at the same time so she instructed the device to read it out for her. This allowed her to keep doing her math while she listened. She also instructed the device to stop and resume which allowed her to effectivly use the device for the purpose that it was created.

# Lab 3 Part 2

For Part 2, you will redesign the interaction with the speech-enabled device using the data collected, as well as feedback from part 1.

## Prep for Part 2

1. What are concrete things that could use improvement in the design of your device? For example: wording, timing, anticipation of misunderstandings...
2. What are other modes of interaction _beyond speech_ that you might also use to clarify how to interact?
3. Make a new storyboard, diagram and/or script based on these reflections.

## Prototype your system

The system should:
* use the Raspberry Pi 
* use one or more sensors
* require participants to speak to it. 

*Document how the system works*
The user waves their hand over the Study buddy product to 

*Include videos or screencaptures of both the system and the controller.*
![2AA3318E-96A1-4555-9650-FC260B62AE49_1_105_c](https://user-images.githubusercontent.com/112049036/206267701-e1d5d4ad-6a66-4634-b90d-9dfdfe8ae58a.jpeg)
![9E389A45-EAC5-4EBD-B448-F7DE454961B6](https://user-images.githubusercontent.com/112049036/206267774-5edee67e-7fb5-4c1c-aa8d-b622a717761b.jpeg)
![49648106-BCE1-4BF8-9109-6E5F4603A254_1_105_c](https://user-images.githubusercontent.com/112049036/206267787-8e66e611-877c-424b-847e-880cb3bee40e.jpeg)

![4CA65F14-CB0E-4703-A530-410EDFEF744B_1_105_c](https://user-images.githubusercontent.com/112049036/206267881-a5f82165-93e1-447d-9100-fad6f7b4f754.jpeg)

![B5424269-DECA-4B92-8251-EAD1B0CF68F4_1_105_c](https://user-images.githubusercontent.com/112049036/206267901-3381feb5-4935-4dbb-91b0-905dfa3f2987.jpeg)

![9770DCA0-DDA4-473B-8999-4AD8130B8DD9_1_105_c](https://user-images.githubusercontent.com/112049036/206267916-4a8a1332-bd55-4994-9280-848e7662d490.jpeg)


## Test the system
Try to get at least two people to interact with your system. (Ideally, you would inform them that there is a wizard _after_ the interaction, but we recognize that can be hard.)

Jacob Test 1
https://youtube.com/shorts/CHD-zf_i9_E

Jacob Test 2
https://youtube.com/shorts/c_D5p03IOGM

Ken test 1
https://youtu.be/bs-qA78WMAQ


Answer the following:

### What worked well about the system and what didn't?
The system worked well with the way the proximity sensor worked with initiating the speach of the device. The system failed in how many different interactions could take place due to the fact that it wasn't an IOT(internet of things) device and had only three school subjects to choose from.

### What worked well about the controller and what didn't?

Controlling the device through the speach camera and proximity sensor was a seemless transition in how the participants interacted with the device. The only improvement I could think of is some type of sign inviting the participant to wave their hand over the sensor to initiate the start.

### What lessons can you take away from the WoZ interactions for designing a more autonomous version of the system?


I believe thebest way to avoid the WoZ interaction and make it automated is to make it an IOT (internet of things) device and have more subject from which the user can choose.

### How could you use your system to create a dataset of interaction? What other sensing modalities would make sense to capture?
I believe that we can make this system observe different gestures and different heights of proximity and distance to acsess different speeds of speach or subjects of reading. You can also impliment this into machine learning on the rasberry pi and you can make a model that predicts both different gestures and different heights of proximity and distance to acsess differnt speeds or subjects that can be stored in a database.


