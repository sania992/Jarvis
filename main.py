import speech_recognition as sr
import webbrowser
import pyttsx3
import requests
from openai import OpenAI
from gtts import gTTS
import pygame
import musiclibrary



# pip install pocketsphinx

recognizer = sr.Recognizer()
engine = pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()



def processCommand(c):
   if "open google" in c.lower():
      webbrowser.open("https://google.com")
   elif "open facebook" in c.lower():
      webbrowser.open("https://facebook.com")
   elif "open youtube" in c.lower():
      webbrowser.open("https://youtube.com")
   elif "open spotify" in c.lower():
      webbrowser.open("https://spotify.com")   
   elif "open linkedin" in c.lower():
      webbrowser.open("https://linkedin.com")
   elif "open instagram" in c.lower():
      webbrowser.open("https://instagram.com")
      

   elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]  # Gets the second word
        link = musiclibrary[song]
        webbrowser.open(link)

if __name__ == "__main__":
    speak("Intializing Jarvis..." )
    while True:
    # Listen for the wake word " Jarvis"
       r = sr.Recognizer()


       print("recognizing...")          
       try :
          with sr.Microphone() as source:
           print("Listening ...")
           audio = r.listen(source,timeout=1, phrase_time_limit=1)
          command = r.recognize_google(audio)
          if(command.lower() == "friday"):
             speak("yes")
             #listen for command
             with sr.Microphone() as source:
                print("Jarvis active....")
                audio = r.listen(source)
                command = r.recognize_google(audio)

                processCommand(command)

        
       except Exception as e:
          print("Sphinx error; {0}".format(e))
        
    
        
    