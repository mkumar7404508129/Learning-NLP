import pyaudio
import wave
import time
import os
from pynput import keyboard


# WAVE_OUTPUT_FILENAME = "output.wav"
break_program =True
class SaveAudio:
    def __init__(self):
        self.LISTOFWORDS=["Nripender","Daimler","Basvaraj","Gopal","BMW","Maruti","Rotary","Machine","MontelOpere","Lucabrasi"]
        self.CHUNK = 1024
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 1
        self.RATE = 44100
        self.RECORD_SECONDS = 5
        self.p=pyaudio.PyAudio()
        self.stream=self.p.open(format=self.FORMAT,
                    channels=self.CHANNELS,
                    rate=self.RATE,
                    input=True,
                    frames_per_buffer=self.CHUNK)

    def createFolder(self,name):
        path='./Dataset/'+name
        length=0
        if os.path.isdir(path):
            length=len(os.listdir(path=path))
        else:
            os.mkdir(path)
        return (length,path)


    def audioRecord(self,CHUNK,FORMAT,CHANNELS,RATE,WAVE_OUTPUT_FILENAME):
       
        print("* recording---")
        print("Press space to Stop recording")


        frames = []
        listner=keyboard.Listener(on_press=self.on_keypress)
        listner.start()
        while break_program:
            data = self.stream.read(CHUNK)
            frames.append(data)
        listner.stop()
    
        print("* done recording")
        wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(self.p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()

    def stop(self):
        self.stream.stop_stream()
        self.p.terminate()
    def on_keypress(self,key):
        global break_program
        if key==keyboard.Key.space and break_program:
            break_program=False
    def start(self):
        while True:
            input("Please press Enter")
            for x in self.LISTOFWORDS:
                print('\033c')
                print("Please Speek This Word\n",x)
                val=self.createFolder(x)
                fileName=val[1]+"/"+x+"_"+str(val[0])+".wav"
                print("Total file :",val[0])
                self.audioRecord(self.CHUNK,self.FORMAT, self.CHANNELS, self.RATE, fileName)
                global break_program
                break_program=True
            print("One Round Complete")
        self.stop()
if __name__=="__main__":
    obj=SaveAudio()
    obj.start()



    
        
