# Observant Systems

**NAMES OF COLLABORATORS HERE**
Patrick Mazza

For lab this week, we focus on creating interactive systems that can detect and respond to events or stimuli in the environment of the Pi, like the Boat Detector we mentioned in lecture. 
Your **observant device** could, for example, count items, find objects, recognize an event or continuously monitor a room.

This lab will help you think through the design of observant systems, particularly corner cases that the algorithms need to be aware of.

## Prep

1. Spend about 10 Minutes doing the Listening exercise as described in [ListeningExercise.md](https://github.com/FAR-Lab/Interactive-Lab-Hub/blob/Fall2022/Lab%205/ListeningExercise.md)
2.  Install VNC on your laptop if you have not yet done so. This lab will actually require you to run script on your Pi through VNC so that you can see the video stream. Please refer to the [prep for Lab 2](https://github.com/FAR-Lab/Interactive-Lab-Hub/blob/Fall2022/Lab%202/prep.md), we offered the instruction at the bottom.
3.  Read about [OpenCV](https://opencv.org/about/), [MediaPipe](https://mediapipe.dev/), and [TeachableMachines](https://teachablemachine.withgoogle.com/).
4.  Read Belloti, et al.'s [Making Sense of Sensing Systems: Five Questions for Designers and Researchers](https://www.cc.gatech.edu/~keith/pubs/chi2002-sensing.pdf).

### For the lab, you will need:
1. Pull the new Github Repo.(Please wait until thursday morning. There are still some incompatabilities to make the assignment work.)
1. Raspberry Pi
1. Webcam 

### Deliverables for this lab are:
1. Show pictures, videos of the "sense-making" algorithms you tried.
1. Show the filledout answers for the Contextual Interaction Design Tool.
1. Show a video of how you embed one of these algorithms into your observant system.
1. Test, characterize your interactive device. Show faults in the detection and how the system handled it.

## Overview
Building upon the paper-airplane metaphor (we're understanding the material of machine learning for design), here are the four sections of the lab activity:

A) [Play](#part-a)

B) [Fold](#part-b)

C) [Flight test](#part-c)

D) [Reflect](#part-d)

---

### Part A
### Play with different sense-making algorithms.

#### OpenCV
A more traditional method to extract information out of images is provided with OpenCV. The RPI image provided to you comes with an optimized installation that can be accessed through python. We included 4 standard OpenCV examples: contour(blob) detection, face detection with the ``Haarcascade``, flow detection (a type of keypoint tracking), and standard object detection with the [Yolo](https://pjreddie.com/darknet/yolo/) darknet.

Most examples can be run with a screen (e.g. VNC or ssh -X or with an HDMI monitor), or with just the terminal. The examples are separated out into different folders. Each folder contains a ```HowToUse.md``` file, which explains how to run the python example. 

The following command is a nicer way you can run and see the flow of the `openCV-examples` we have included in your Pi. Instead of `ls`, the command we will be using here is `tree`. [Tree](http://mama.indstate.edu/users/ice/tree/) is a recursive directory colored listing command that produces a depth indented listing of files. Install `tree` first and `cd` to the `openCV-examples` folder and run the command:

```shell
pi@ixe00:~ $ sudo apt install tree
...
pi@ixe00:~ $ cd openCV-examples
pi@ixe00:~/openCV-examples $ tree -l
.
├── contours-detection
│   ├── contours.py
│   └── HowToUse.md
├── data
│   ├── slow_traffic_small.mp4
│   └── test.jpg
├── face-detection
│   ├── face-detection.py
│   ├── faces_detected.jpg
│   ├── haarcascade_eye_tree_eyeglasses.xml
│   ├── haarcascade_eye.xml
│   ├── haarcascade_frontalface_alt.xml
│   ├── haarcascade_frontalface_default.xml
│   └── HowToUse.md
├── flow-detection
│   ├── flow.png
│   ├── HowToUse.md
│   └── optical_flow.py
└── object-detection
    ├── detected_out.jpg
    ├── detect.py
    ├── frozen_inference_graph.pb
    ├── HowToUse.md
    └── ssd_mobilenet_v2_coco_2018_03_29.pbtxt
```

The flow detection might seem random, but consider [this recent research](https://cseweb.ucsd.edu/~lriek/papers/taylor-icra-2021.pdf) that uses optical flow to determine busy-ness in hospital settings to facilitate robot navigation. Note the velocity parameter on page 3 and the mentions of optical flow.

Now, connect your webcam to your Pi and use **VNC to access to your Pi** and open the terminal. Use the following command lines to try each of the examples we provided:
(***it will not work if you use ssh from your laptop***)

```
pi@ixe00:~$ cd ~/openCV-examples/contours-detection
pi@ixe00:~/openCV-examples/contours-detection $ python contours.py
...
pi@ixe00:~$ cd ~/openCV-examples/face-detection
pi@ixe00:~/openCV-examples/face-detection $ python face-detection.py
...
pi@ixe00:~$ cd ~/openCV-examples/flow-detection
pi@ixe00:~/openCV-examples/flow-detection $ python optical_flow.py 0 window
...
pi@ixe00:~$ cd ~/openCV-examples/object-detection
pi@ixe00:~/openCV-examples/object-detection $ python detect.py
```

**\*\*\*Try each of the following four examples in the `openCV-examples`, include screenshots of your use and write about one design for each example that might work based on the individual benefits to each algorithm.\*\*\***

Countour detection: 

![546350F3-7D1B-4CD3-B468-233C3A38B51F_1_105_c](https://user-images.githubusercontent.com/112049036/197574096-9a05580e-2dd0-43ea-9365-a80375bf46a7.jpeg)

One design that I  believe would be interesting to implement is to make a dog contour detector. Let's say I let my dogs outside of my house and they have a doggy door outside. Based on the distinctive appearances of my two dogs, my device will allow me to control what dog I will allow back in the house. If I am watching my dogs through a camera and I see one of them goes to the bathroom and one of them doesn't, when they are trying to enter the house again the contour of the dog will be detected and I can make the decision of opening the doggy door or not.
![FC3E00DD-94F5-4C44-B9BA-CD8C17E492CB_1_105_c](https://user-images.githubusercontent.com/112049036/197574844-3ba590be-2233-433a-90f2-6bb660021d57.jpeg)

Flow detection:

![77D3C901-5CCE-481F-ACC6-1C48C105C6D8](https://user-images.githubusercontent.com/112049036/197575337-7aa2d622-ffd2-4f2c-bc26-c41bef3a9a05.jpeg)

A cool design that I believe would be useful to implement is an airplane traffic indicator for flow detection. Here, the device would be able to tell which baton was moving in whichever direction the user chose to move it. This is in the effort to direct plane traffic in airports in order to establish a more efficient process. This would also be accompanied by the sound of the traffic officer, screaming the directions that applied to the airplanes.

![99795592-ADFA-4A5A-A273-406CB70A7D2C_1_105_c](https://user-images.githubusercontent.com/112049036/197577312-97a5c0df-e8cb-4b84-a6f3-37abcee45022.jpeg)

Face detection:

<img width="628" alt="BA3DFEE3-E2B1-45A1-B290-782C10C8CCA3" src="https://user-images.githubusercontent.com/112049036/197577620-ed7bc235-61d9-4022-8864-70e73fea76c0.png">


A useful design for face detection would be a cloud detector. I would put this in front of my house, and a person would have to get a facial scan before entering. This would be a useful tool, because I am scared of clowns and no clowns are allowed in my house. The algorithmic model would also be improved by detecting either a regular sounding person, or a clown sound which consists of much laughter.

<img width="524" alt="92060DDD-EBC1-4AD3-9D5E-13E0FA5FF2EA" src="https://user-images.githubusercontent.com/112049036/197577400-81340bc4-1412-40bc-b853-ae642c75302c.png">

Object detection:

<img width="603" alt="209FE838-AC3A-48A4-B36A-72A2B960177F" src="https://user-images.githubusercontent.com/112049036/197577819-25390f33-0bfb-41ae-902c-cbdefdfa663e.png">

<img width="523" alt="715BF509-CEA7-4390-985B-FD60F4AAE8CB" src="https://user-images.githubusercontent.com/112049036/197577829-641c183f-88aa-4d72-91bc-816ae2f16542.png">

Another useful design that would be helpful for daily life would be a gym equipment detection list. This would scan an object to see if it was acceptable to bring to a gym. This is shown by the water bottle, which is an acceptable gym item. This is also shown by a computer, which is not an acceptable gym item.

<img width="427" alt="9518490B-0EEE-4A27-98EA-2111CF46260C" src="https://user-images.githubusercontent.com/112049036/197577878-06764444-6fdb-4df5-b34d-ac9060284de4.png">

#### Filtering, FFTs, and Time Series data. 
Additional filtering and analysis can be done on the sensors that were provided in the kit. For example, running a Fast Fourier Transform over the IMU or Microphone data stream could create a simple activity classifier between walking, running, and standing.

To get the microphone working we need to install two libraries. `PyAudio` to get the data from the microphone, `sciPy` to make data analysis easy, and the `numpy-ringbuffer` to keep track of the last ~1 second of audio. 
Pyaudio needs to be installed with the following comand:
``sudo apt install python3-pyaudio``
SciPy is installed with 
``sudo apt install python3-scipy`` 

Lastly we need numpy-ringbuffer, to make continues data anlysis easier.
``pip install numpy-ringbuffer``

Now try the audio processing example:
* Find what ID the micrpohone has with `python ListAvalibleAudioDevices.py`
    Look for a device name that includes `USB` in the name.
* Adjust the variable `DEVICE_INDEX` in the `ExampleAudioFFT.py` file.
    See if you are getting results printed out from the microphone. Try to understand how the code works.
    Then run the file by typing `python ExampleAudioFFT.py`



Using the microphone, try one of the following:

**1. Set up threshold detection** Can you identify when a signal goes above certain fixed values?

A thershold detection was set up sucsessfully and will be used in the aaplication of this lab experiment.

**2. Set up a running averaging** Can you set up a running average over one of the variables that are being calculated.[moving average](https://en.wikipedia.org/wiki/Moving_average)

**3. Set up peak detection** Can you identify when your signal reaches a peak and then goes down?

For technical references:

* Volume Calculation with [RootMeanSqare](https://en.wikipedia.org/wiki/Root_mean_square)
* [RingBuffer](https://en.wikipedia.org/wiki/Circular_buffer)
* [Frequency Analysis](https://en.wikipedia.org/wiki/Fast_Fourier_transform)

https://github.com/patrickMazza/Interactive-Lab-Hub/blob/Fall2022/Lab%205/thresholdCode

**\*\*\*Include links to your code here, and put the code for these in your repo--they will come in handy later.\*\*\***

### (Optional Reading) Introducing Additional Concepts
The following sections ([MediaPipe](#mediapipe) and [Teachable Machines](#teachable-machines)) are included for your own optional learning. **The associated scripts will not work on Fall 2022's Pi Image, so you can move onto part B.** However, you are welcome to try it on your personal computer. If this functionality is desirable for your lab or final project, we can help you get a different image running the last OS and version of python to make the following code work.

#### MediaPipe

A more recent open source and efficient method of extracting information from video streams comes out of Google's [MediaPipe](https://mediapipe.dev/), which offers state of the art face, face mesh, hand pose, and body pose detection.

![Alt Text](mp.gif)

To get started, create a new virtual environment with special indication this time:

```
pi@ixe00:~ $ virtualenv mpipe --system-site-packages
pi@ixe00:~ $ source mpipe/bin/activate
(mpipe) pi@ixe00:~ $ 
```

and install the following.

```
...
(mpipe) pi@ixe00:~ $ sudo apt install ffmpeg python3-opencv
(mpipe) pi@ixe00:~ $ sudo apt install libxcb-shm0 libcdio-paranoia-dev libsdl2-2.0-0 libxv1  libtheora0 libva-drm2 libva-x11-2 libvdpau1 libharfbuzz0b libbluray2 libatlas-base-dev libhdf5-103 libgtk-3-0 libdc1394-22 libopenexr25
(mpipe) pi@ixe00:~ $ pip3 install mediapipe-rpi3 pyalsaaudio
```

Each of the installs will take a while, please be patient. After successfully installing mediapipe, connect your webcam to your Pi and use **VNC to access to your Pi**, open the terminal, and go to Lab 5 folder and run the hand pose detection script we provide:
(***it will not work if you use ssh from your laptop***)


```
(mpipe) pi@ixe00:~ $ cd Interactive-Lab-Hub/Lab\ 5
(mpipe) pi@ixe00:~ Interactive-Lab-Hub/Lab 5 $ python hand_pose.py
```

Try the two main features of this script: 1) pinching for percentage control, and 2) "[Quiet Coyote](https://www.youtube.com/watch?v=qsKlNVpY7zg)" for instant percentage setting. Notice how this example uses hardcoded positions and relates those positions with a desired set of events, in `hand_pose.py` lines 48-53. 

~~\*\*\*Consider how you might use this position based approach to create an interaction, and write how you might use it on either face, hand or body pose tracking.\*\*\*~~

(You might also consider how this notion of percentage control with hand tracking might be used in some of the physical UI you may have experimented with in the last lab, for instance in controlling a servo or rotary encoder.)



#### Teachable Machines
Google's [TeachableMachines](https://teachablemachine.withgoogle.com/train) might look very simple. However, its simplicity is very useful for experimenting with the capabilities of this technology.

![Alt Text](tm.gif)

To get started, create and activate a new virtual environment for this exercise with special indication:

```
pi@ixe00:~ $ virtualenv tmachine --system-site-packages
pi@ixe00:~ $ source tmachine/bin/activate
(tmachine) pi@ixe00:~ $ 
```

After activating the virtual environment, install the requisite TensorFlow libraries by running the following lines:
```
(tmachine) pi@ixe00:~ $ cd Interactive-Lab-Hub/Lab\ 5
(tmachine) pi@ixe00:~ Interactive-Lab-Hub/Lab 5 $ sudo chmod +x ./teachable_machines.sh
(tmachine) pi@ixe00:~ Interactive-Lab-Hub/Lab 5 $ ./teachable_machines.sh
``` 

This might take a while to get fully installed. After installation, connect your webcam to your Pi and use **VNC to access to your Pi**, open the terminal, and go to Lab 5 folder and run the example script:
(***it will not work if you use ssh from your laptop***)

```
(tmachine) pi@ixe00:~ Interactive-Lab-Hub/Lab 5 $ python tm_ppe_detection.py
```


(**Optionally**: You can train your own model, too. First, visit [TeachableMachines](https://teachablemachine.withgoogle.com/train), select Image Project and Standard model. Second, use the webcam on your computer to train a model. For each class try to have over 50 samples, and consider adding a background class where you have nothing in view so the model is trained to know that this is the background. Then create classes based on what you want the model to classify. Lastly, preview and iterate, or export your model as a 'Tensorflow' model, and select 'Keras'. You will find an '.h5' file and a 'labels.txt' file. These are included in this labs 'teachable_machines' folder, to make the PPE model you used earlier. You can make your own folder or replace these to make your own classifier.)

~~**\*\*\*Whether you make your own model or not, include screenshots of your use of Teachable Machines, and write how you might use this to create your own classifier. Include what different affordances this method brings, compared to the OpenCV or MediaPipe options.\*\*\***~~


*Don't forget to run ```deactivate``` to end the Teachable Machines demo, and to reactivate with ```source tmachine/bin/activate``` when you want to use it again.*


### Part B
### Construct a simple interaction.

* Pick one of the models you have tried, and experiment with prototyping an interaction.
* This can be as simple as the boat detector showen in a previous lecture from Nikolas Matelaro.
* Try out different interaction outputs and inputs.
* Fill out the ``Contextual Interaction Design Tool`` sheet.[Found here.](ThinkingThroughContextandInteraction.png)

**\*\*\*Describe and detail the interaction, as well as your experimentation here.\*\*\***

The interaction that I have thought of is combining object detection with a threshold detection of sound. This interaction would start with putting a kettle on the stove filled with water and heating it up. The camera would be faced towards the kettle as the water heated up. Once the water heats up to a certain temperature, the kettle will start to smoke, and a whistling noise will be emitted. From here, the system would recognize the water was ready and the user would then be notified and take the kettle off of the stove. From here there would be a timer set for two minutes and 15 seconds. The 15 seconds allows the chance for the user to pour the hot water into the French press, while the two minutes was for the coffee beans and hot water to coagulate. From here, you would just press down on the lever on the french press and then you could pour yourself a hot cup of coffee. 

The experimentation I did to prepare for this interaction was to see if my object detection algorithm could identify the kettle. The algorithm was able to identify this as an object. The next step was to see if my threshold code would be able to detect the noise of the whistling. This was also successful.
<img width="442" alt="21527CC8-AFFA-414A-AE3F-9A048F685C68" src="https://user-images.githubusercontent.com/112049036/197601558-23d72bd6-9846-41ba-b947-5aebe67f2943.png">
![DEABB60C-C45E-4583-AA2D-00B70714839D_1_105_c](https://user-images.githubusercontent.com/112049036/197622854-dfa5bc56-43e6-4cb0-af7b-c14fd6fcf4d0.jpeg)

### Part C
### Test the interaction prototype

Now flight test your interactive prototype and **note down your observations**:
For example:
1. When does it what it is supposed to do?
1. When does it fail?
1. When it fails, why does it fail?
1. Based on the behavior you have seen, what other scenarios could cause problems?

**\*\*\*Think about someone using the system. Describe how you think this will work.\*\*\***
1. Are they aware of the uncertainties in the system?
1. How bad would they be impacted by a miss classification?
1. How could change your interactive system to address this?
1. Are there optimizations you can try to do on your sense-making algorithm.

The flight test to see the interaction of my design prototype went well in many areas. The object detector‘s main purpose was to detect the kettle on the stove, in order to listen for the whistling with the threshold marker. The whistling was also internalized by the system, and I was able to detect the whistling. The system did have some faults that led to some concerning conclusions. Sometimes the camera would not pick up the kettle at all, and it would just view the oven as an object. The frame rate is also slow, so observation was therefore inaccurate, and I don’t know how applicable this device would be in real time situations. Based on this behavior, I can see a scenario where other items around the oven that confuse the object detector or the system picking up another noise from a source closer to it.

This also presents a problem to people because they are unaware of all of these uncertainties that are affecting my system. The key to implementing this device for the everyday user would be to have a system that is more detail oriented or embedded into the actual kettle and or stove. Also, I believe I could change the system to address. The problem of random noise would be to work out some sort of de-noising OP AMP filter where the system would have a high cut off frequency, so it would only read the high decibel number that the whistling would give off. I believe an optimization that I can make to the object detection algorithm would be to put weight on the variables that have to do with the color and shape of the cattle in order to detect it more accurately.


### Part D
### Characterize your own Observant system

Now that you have experimented with one or more of these sense-making systems **characterize their behavior**.
During the lecture, we mentioned questions to help characterize a material:
* What can you use X for?
* What is a good environment for X?
* What is a bad environment for X?
* When will X break?
* When it breaks how will X break?
* What are other properties/behaviors of X?
* How does X feel?

https://youtu.be/175A9cmH-q0
**\*\*\*Include a short video demonstrating the answers to these questions.\*\*\***

### Part 2.

Following exploration and reflection from Part 1, finish building your interactive system, and demonstrate it in use with a video.

**\*\*\*Include a short video demonstrating the finished result.\*\*\***

This video is in accordance with the coffee/tea kettle storyboard above. First, water is put into the kettle and then placed on the stove. The system detects the kettle was put on the stove which then prompts the pi to initiate a threshold detection feature. Then, once the water starts boiling and smoke comes out of the kettle, it will make a whistling sound that will break the threshold detection. Once the threshold detection is exceeded, the system will say the water is hot enough and ready. Then, the user will pour the hot water into the French press, and a two minute timer will be set. Finally once the two minute timer is done, you can pour the coffee/tea into the cup and enjoy!

Video:
https://youtu.be/bEfNYMsRd60
