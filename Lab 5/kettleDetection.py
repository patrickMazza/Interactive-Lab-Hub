
import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np
import cv2
import sys
import pyaudio
from scipy.fft import rfft, rfftfreq
from scipy.signal.windows import hann
from numpy_ringbuffer import RingBuffer

import queue
import time


# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

img = None
webCam = False
if(len(sys.argv)>1 and not sys.argv[-1]== "noWindow"):
   try:
      print("I'll try to read your image");
      img = cv2.imread(sys.argv[1])
      if img is None:
         print("Failed to load image file:", sys.argv[1])
   except:
      print("Failed to load the image are you sure that:", sys.argv[1],"is a path to an image?")
else:
   try:
      print("Trying to open the Webcam.")
      cap = cv2.VideoCapture(0)
      if cap is None or not cap.isOpened():
         raise("No camera")
      webCam = True
   except:
      print("Unable to access webcam.")


# Load the model
model = tensorflow.keras.models.load_model('keras_model.h5')
# Load Labels:
labels=[]
f = open("labels.txt", "r")
for line in f.readlines():
    if(len(line)<1):
        continue
    labels.append(line.split(' ')[1].strip())


while(True):
    if webCam:
        ret, img = cap.read()

    rows, cols, channels = img.shape
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    size = (224, 224)
    img =  cv2.resize(img, size, interpolation = cv2.INTER_AREA)
    #turn the image into a numpy array
    image_array = np.asarray(img)

    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    # Load the image into the array
    data[0] = normalized_image_array

    # run the inference
    prediction = model.predict(data)
    print("I think its a:",labels[np.argmax(prediction)])

    if webCam:
        if sys.argv[-1] == "noWindow":
           cv2.imwrite('detected_out.jpg',img)
           continue
        cv2.imshow('detected (press q to quit)',img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cap.release()
            break
    else:
        break

cv2.imwrite('detected_out.jpg',img)
cv2.destroyAllWindows()
audioQueue = queue.Queue() #In this queue stores the incoming audio data before processing.
    pyaudio_instance = pyaudio.PyAudio() #This is the AudioDriver that connects to the microphone for us.

    def _callback(in_data, frame_count, time_info, status): # This "callbackfunction" stores the incoming audio data in the `audioQueue`
        audioQueue.put(in_data)
        return None, pyaudio.paContinue

    stream = pyaudio_instance.open(input=True,start=False,format=pyaudio.paFloat32,channels=CHANNELS,rate=SAMPLING_RATE,frames_per_buffer=int(SAMPLING_RATE/2),stream_callback=_callback,input_device_index=DEVICE_INDEX)
    
    
    # One essential way to keep track of variables overtime is with a ringbuffer. 
    # As an example the `AudioBuffer` it stores always the last second of audio data. 
    AudioBuffer = RingBuffer(capacity=SAMPLING_RATE*1, dtype=FORMAT) # 1 second long buffer.
    
    # Another example is the `VolumeHistory` ringbuffer. 
    VolumeHistory = RingBuffer(capacity=int(20/UPDATE_INTERVAL), dtype=FORMAT) ## This is how you can compute a history to record changes over time
    ### Here  is a good spot to extend other buffers  aswell that keeps track of varailbes over a certain period of time. 

    nextTimeStamp = time.time()
    stream.start_stream()
    if True:
        while True:
            frames = audioQueue.get() #Get DataFrom the audioDriver (see _callbackfunction how the data arrives)
            if not frames:
                continue

            framesData = np.frombuffer(frames, dtype=FORMAT) 
            AudioBuffer.extend(framesData[0::CHANNELS]) #Pick one audio channel and fill the ringbuffer. 
            
            if(AudioBuffer.is_full and  # Waiting for the ringbuffer to be full at the beginning.
                audioQueue.qsize()<2 and # Make sure there is not alot more new data that should be used. 
                time.time()>nextTimeStamp): # See `UPDATE_INTERVAL` above.

                buffer  = np.array(AudioBuffer) #Get the last second of audio. 


                volume = np.rint(np.sqrt(np.mean(buffer**2))*10000) # Compute the rms volume
                
                
                VolumeHistory.append(volume)
                volumneSlow = volume
                volumechange = 0.0
                if VolumeHistory.is_full:
                    HalfLength = int(np.round(VolumeHistory.maxlen/2)) 
                    vnew = np.array(VolumeHistory)[HalfLength:].mean()
                    vold = np.array(VolumeHistory)[:VolumeHistory.maxlen-HalfLength].mean()
                    volumechange =vnew-vold
                    volumneSlow = np.array(VolumeHistory).mean()
                
                ## Computes the Frequency Foruier analysis on the Audio Signal.
                N = buffer.shape[0] 
                window = hann(N) 
                amplitudes = np.abs(rfft(buffer*window))[25:] #Contains the volume for the different frequency bin.
                frequencies = (rfftfreq(N, 1/SAMPLING_RATE)[:N//2])[25:] #Contains the Hz frequency values. for the different frequency bin.
                '''
                Combining  the `amplitudes` and `frequencies` varialbes allows you to understand how loud a certain frequency is.

                e.g. If you'd like to know the volume for 500Hz you could do the following. 
                1. Find the frequency bin in which 500Hz belis closest to with:
                FrequencyBin = np.abs(frequencies - 500).argmin()
                
                2. Look up the volume in that bin:
                amplitudes[FrequencyBin]


                The example below does something similar, just in revers.
                It finds the loudest amplitued and its coresponding bin  with `argmax()`. 
                The uses the index to look up the Freqeucny value.
                '''


                LoudestFrequency = frequencies[amplitudes.argmax()]
                
                #print("Loudest Frqeuncy:",LoudestFrequency)
                #print("RMS volume:",volumneSlow)
                #print("Volume Change:",volumechange)
                
               if volumneSlow > 60:

                print("the tea is ready")
                say("tea ready")
                break

            nextTimeStamp = UPDATE_INTERVAL+time.time() # See `UPDATE_INTERVAL` above

    #input("click")
    time.sleep(2*60)

    print("two minute is out")
    say("time over")



                nextTimeStamp = UPDATE_INTERVAL+time.time() # See `UPDATE_INTERVAL` above
