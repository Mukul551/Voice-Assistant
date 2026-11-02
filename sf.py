import subprocess
import wolframalpha
import pyttsx3
import pyautogui
import requests
from bs4 import BeautifulSoup
import speedtest
import tkinter
import json
import random
import operator
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import winshell
import pyjokes
import feedparser
import smtplib
import ctypes
import time
import requests
import shutil
from twilio.rest import Client
from clint.textui import progress
from ecapture import ecapture as ec
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen
import urllib.request
import urllib.parse
import re
from engine import app


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

from INTRO import play_gif
play_gif


def speak(audio):
	engine.say(audio)
	engine.runAndWait()

def wishMe():
	hour = int(datetime.datetime.now().hour)
	if hour>= 0 and hour<12:
		speak("Good Morning Sir !")

	elif hour>= 12 and hour<18:
		speak("Good Afternoon Sir !") 

	else:
		speak("Good Evening Sir !") 

	speak("I am your Assistant")
	speak("How can i Help you, Sir ?")

def takeCommand():
	
	r = sr.Recognizer()
	
	with sr.Microphone() as source:
		
		print("Listening...")
		r.pause_threshold = 1
		audio = r.listen(source)

	try:
		print("Recognizing...") 
		query = r.recognize_google(audio, language ='en-in')
		print(f"User said: {query}\n")

	except Exception as e:
		print(e) 
		print("Unable to Recognize your voice.") 
		return "None"
	
	return query

def alarm(query):
    timehere = open("Alarmtext.txt","a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")


if __name__ == '__main__':
    clear = lambda: os.system('cls')
     
    clear()
    wishMe()
     
    while True:
        elif "pause" in query:
            pyautogui.press("k")
            speak("video paused")
        elif "play" in query:
            pyautogui.press("k")
            speak("video played")
        elif "mute" in query:
            pyautogui.press("m")
            speak("video muted")

        elif "volume up" in query:
            from keyboard import volumeup
            speak("Turning volume up,sir")
            volumeup()
        elif "volume down" in query:
            from keyboard import volumedown
            speak("Turning volume down, sir")
            volumedown()

        elif "google" in query:
            from SearchNow import searchGoogle
            searchGoogle(query)
        elif "youtube" in query:
            from SearchNow import searchYoutube
            searchYoutube(query)
        elif "wikipedia" in query:
            from SearchNow import searchWikipedia
            searchWikipedia(query)
        elif "open" in query:
            from Dictapp import openappweb
            openappweb(query)
        elif "remember that" in query:
            rememberMessage = query.replace("remember that","")
            rememberMessage = query.replace("jarvis","")
            speak("You told me "+rememberMessage)
            remember = open("Remember.txt","a")
            remember.write(rememberMessage)
            remember.close()
            
        elif "what do you remember" in query:
            remember = open("Remember.txt","r")
            speak("You told me to remember that" + remember.read())    

        elif "tired" in query:
            speak("Playing your favourite songs, sir")
            a = (1,2,3) # You can choose any number of songs (I have only choosen 3)
            b = random.choice(a)
            if b==1:
                webbrowser.open("https://youtu.be/SEpTl9hlyq8?si=F2nd6SRkOklxMUdm")
            elif b==2:
                webbrowser.open("https://youtu.be/cY4nGCw-JxY?si=Ao17AQV_LWhFQSHS")
            elif b==3:
                 webbrowser.open("https://youtu.be/lDbItmGvzDM?si=iSi7Vl65Ndm2Tc8u")

        elif "news" in query:
            from NewsRead import latestnews
            latestnews()
       elif "internet speed" in query:
            wifi  = speedtest.Speedtest()
            upload_net = wifi.upload()/1048576         #Megabyte = 1024*1024 Bytes
            download_net = wifi.download()/1048576
            print("Wifi Upload Speed is", upload_net)
            print("Wifi download speed is ",download_net)
            speak(f"Wifi download speed is {download_net}")
            speak(f"Wifi Upload speed is {upload_net}")
               elif "game" in query:
            from game import game_play
            game_play()

        elif 'back home' in query or 'go back' in query or 'bye' in query:
            speak("Thanks for giving me your time")
            exit()
