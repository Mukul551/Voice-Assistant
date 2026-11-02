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
from newsapi import NewsApiClient


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

from INTRO import play_gif
play_gif

NEWS_API="8076252ceaea465bb778ede1367109c5"
news_client = NewsApiClient(api_key=NEWS_API)
OPENWEATHERMAP_API="aa8980078f2b8b15756a7fa389c3d717"

def speak(audio):
	engine.say(audio)
	engine.runAndWait()

def wishMe():
	hour = int(datetime.datetime.now().hour)
	if hour>= 0 and hour<12:
		speak("Good Morning friends !")

	elif hour>= 12 and hour<18:
		speak("Good Afternoon friends !") 

	else:
		speak("Good Evening friends !") 

	speak("I am your Assistant")
	speak("How can i Help you ?")

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

def get_news():
    try:
        top_news = ""
        top_headlines = news_client.get_top_headlines(language="en", country="in")
        for i in range(5):
            top_news += re.sub(r'[|-] [A-Za-z0-9 |:.]*', '', top_headlines['articles'][i]['title']).replace("’",
                                                                                                            "'") + '\n'
        return top_news
    except requests.exceptions.RequestException:
        return None

def get_weather(city=''):
    try:
        if city:
            response = requests.get(
                f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHERMAP_API}&units=metric').json()
        else:
            response = requests.get(
                f'https://api.openweathermap.org/data/2.5/weather?q={get_ip(True)["city"]}&appid={OPENWEATHERMAP_API}&units=metric').json()
        weather = f'It\'s {response["main"]["temp"]}° Celsius and {response["weather"][0]["main"]}\n' \
                  f'But feels like {response["main"]["feels_like"]}° Celsius\n' \
                  f'Wind is blowing at {round(response["wind"]["speed"] * 3.6, 2)} km/h\n' \
                  f'Visibility is {int(response["visibility"] / 1000)} km'
        return weather
    except requests.exceptions.RequestException:
        return None
    
def get_ip(_return=False):
    try:
        response = requests.get('http://ip-api.com/json/').json()
        if _return:
            return response
        else:
            return f'Your IP address is {response["query"]}'
    except requests.exceptions.RequestException:
        return None    

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
         
        query = takeCommand().lower()
         

        if 'joke' in query:
            speak(pyjokes.get_joke())

        elif 'lock window' in query:
                speak("locking the device")
                ctypes.windll.user32.LockWorkStation()
        
 
        elif 'shutdown system' in query:
                speak("Hold On a Sec ! Your system is on its way to shut down")
                subprocess.call('shutdown / p /f')
                 
        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            speak("Recycle Bin Recycled")
        
        elif 'news' in query:
            news = get_news()
            speak(news)
            print(news)

        elif 'weather' in query:
            city = query.replace('weather', '').strip()
            weather = get_weather(city)
            speak(weather)
            print(weather)   

        elif 'ip address' in query:
            ip = get_ip()
            speak(ip)
            print(ip)     

        elif 'open' in query:
             query = query.replace("open","")
             query = query.replace("jarvis 1 point 0","")
             pyautogui.press("super")
             pyautogui.typewrite(query)
             pyautogui.sleep(2)
             pyautogui.press("enter")

        elif "temperature" in query:
            search = "temperature in shamli"
            url = f"https://www.google.com/search?q={search}"
            r  = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div", class_ = "BNeawe").text
            speak(f"current{search} is {temp}")

        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M")    
            speak(f"Sir, the time is {strTime}")

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

        elif "camera" in query or "take a photo" in query:
            ec.capture(0, "Jarvis Camera ", "img.jpg")

        elif "open" in query:
            from Dictapp import openappweb
            openappweb(query)
        elif "close" in query:
            from Dictapp import closeappweb
            closeappweb(query)

        elif "set alarm" in query:
            print("input time example:- 10 and 10 and 10")
            speak("Set the time")
            a = input("Please tell the time :- ")
            alarm(a)
            speak("Done,sir")

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
            a = (1,2,3) 
            b = random.choice(a)
            if b==1:
                webbrowser.open("https://youtu.be/SEpTl9hlyq8?si=F2nd6SRkOklxMUdm")
            elif b==2:
                webbrowser.open("https://youtu.be/cY4nGCw-JxY?si=Ao17AQV_LWhFQSHS")
            elif b==3:
                 webbrowser.open("https://youtu.be/lDbItmGvzDM?si=iSi7Vl65Ndm2Tc8u")

        elif "whatsapp" in query:
            from Whatsapp import sendMessage
            sendMessage()

        elif "internet speed" in query:
            wifi  = speedtest.Speedtest()
            upload_net = wifi.upload()/1048576         
            download_net = wifi.download()/1048576
            print("Wifi Upload Speed is", upload_net)
            print("Wifi download speed is ",download_net)
            speak(f"Wifi download speed is {download_net}")
            speak(f"Wifi Upload speed is {upload_net}")    

        elif "screenshot" in query:
            import pyautogui 
            im = pyautogui.screenshot()
            im.save("screenshot.jpg")

        elif "game" in query:
            from game import game_play
            game_play()    

        elif 'back home' in query or 'go back' in query or 'bye' in query:
            speak("Thanks for giving me your time")
            exit()
           