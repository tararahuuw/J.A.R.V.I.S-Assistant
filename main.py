import speech_recognition as sr
import pyttsx3
import webbrowser
import sys
import pywhatkit
import subprocess
import os
from datetime import datetime

def greetMe() :
    currentH = int (datetime.datetime.now(). hour)
    if currentH >= 0 and currentH < 12:
        
        engine2 = pyttsx3.init()
        
        engine2.say("Good Morning, Sir! This is jarvis")
       
        engine2.runAndWait()
    if currentH >=12 and currentH < 18 :
        speak ("Good Afternoon, Sir! This is jarvis")
        print("JARVIS : Good Morning, Sir! This is JARVIS")
    if currentH >=18 and currentH < 0 :
        speak ("Good Evening, Sir! This is jarvis")

def inputvoice():
    r = sr.Recognizer()
    try:
        with sr.Microphone () as source:
            print("JARVIS : Listening..")
            
            audio = r.listen(source)
            voice = r.recognize_google(audio)
            voice = voice.lower()
            if "jarvis" in voice:
                print(voice)
                voice = voice.replace('jarvis', '')
    except:
        engine3 = pyttsx3.init()
        print("JARVIS : I dont know what you mean. Please repeat again or typing the command!")
        engine3.say("Sorry sir, I dont know what you mean. Please repeat again or typing the command!")
        engine3.runAndWait()
        voice = 'dorr'
    
    return voice

def answer (text):
    engine2 = pyttsx3.init()
    engine2.say("Okay sir" + text)
    print("JARVIS : Okay sir" + text)
    engine2.runAndWait()
    
def givecommand ():
    a = 1
    print(a)
    command = inputvoice()
    while (a <= 4 and command == 'dorr'):
        a = a + 1
        command = inputvoice()
        print(a)
    print(a)
    if (a == 3) or command == "type the command" :
        command = str(input ("Command : "))
        
    else :
        print("Your Command :",command)

    if 'google' in command :
        webbrowser.open("https://google.com")
        answer ("Open google")
        print("JARVIS : Okey sir, Opening google")
                
    elif 'rinaldi munir website' in command:
        webbrowser.open('https://informatika.stei.itb.ac.id/~rinaldi.munir/')
        answer  ( "opening rinaldi munir's website")
        print( "JARVIS : Okey sir, Opening rinaldi munir's website")
        
    elif 'goodbye' or "enough" in command:
        answer ("Have a nice day")
        print("JARVIS : Okey sir, Have a nice day")
        sys.exit()
        
    elif "thank you" in command:
        answer ("Your Welcome sir")
        print("JARVIS : Okay sir, your welcome sir")
        
    elif "microsoft teams" in command:
        webbrowser.open("https://teams.microsoft.com/_?culture=en-us&country=US&lm=deeplink&lmsrc=homePageWeb&cmpid=WebSignIn#/school//?ctx=teamsGrid")
        answer  ( "opening microsoft teams")
        print( "JARVIS : Okey sir, Opening microsoft teams")
        
    elif "play" in command:
        pywhatkit.playonyt(command)
        clean = command.replace('play', '')
        answer  ( "Playing" + command)
        print( "JARVIS : Okey sir, Playing" + command)
        
    elif "what is" in command:
        pywhatkit.search(command)
        answer  ( "this is what you are looking for")
        print( "JARVIS : Okey sir, This is what you are looking for ")
        
    elif "who are you" in command:
        answer  ( "I am jarvis, I am a digital assistant who created by Muhammad Fahmi Alamsah")
        print("JARVIS : Okey sir, I am jarvis, I am a digital assistant who created by Muhammad Fahmi Alamsyah")
        
    elif "cmd" in command :
        subprocess.run("start", shell = True)
        answer("Opening cmd")
        print("JARVIS : Okey sir, Opening cmd")
        
    elif "vs code" in command :
        subprocess.call(['C:\Users\M. Fahmi Alamsyah\AppData\Local\Programs\Microsoft VS Code'])
        
    else:
        print("Jarvis : I dont know what you mean sir. Please repeat again or typing the command!")
        engine2 = pyttsx3.init()
        engine2.say("I dont know what you mean sir. Please repeat again or typing the command!")
        engine2.runAndWait()
        
 
greetMe()      
while True:
    givecommand()
    answer("any more command sir?")
    print("JARVIS : Okey sir, Any more command sir?")
    
