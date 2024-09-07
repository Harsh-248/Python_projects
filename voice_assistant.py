import pyttsx3 
import speech_recognition as sr #speech recognizer
import webbrowser
import datetime
import pyjokes
import os
import time

def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:  
        print("Say something...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source) 
        try :
           print("recognizing...")
           data = recognizer.recognize_google(audio)
           print(data)
           return data
        except sr.UnknownValueError:
            print("Not recognized")
def speechtx(x):
    engine = pyttsx3.init() 
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[3].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate',150)
    engine.say(x)  
    engine.runAndWait()

if __name__ == '__main__':
 
 if "hey jarvis" in sptext().lower():

  while True:
    
     data1 = sptext().lower()
    
     if "Your name" in data1:
        name = "my name is raand"
        speechtx(name) 
    
     elif "how old are you" in data1:
        age = "i am two years old"
        speechtx(age) 
    
     elif 'time' in data1:
        time = datetime.datetime.now().strftime("%I%M%p")
        speechtx(time)

     elif 'youtube' in data1:
        webbrowser.open('http://www.youtube.com/')
        
     elif 'github' in data1:
        webbrowser.open('https://github.com/Harsh-248')

     elif 'joke' in data1:
       joke_1 = pyjokes.get_joke(language="en",category="neutral")
       print (joke_1)
       speechtx(joke_1)
    
     elif 'play song'in data1:
       add = "/home/hash"
       listsong = os.listdir(add)
       print (listsong)
       os.startfile(os.path.join(add,listsong[0]))

     elif "exit" in data1:
        speechtx("thank you")
        break

     time.sleep(10)


    
else:
     print("thanks")
