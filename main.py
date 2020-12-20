import speech_recognition as sr
import pyttsx3
import webbrowser
import sys
import pywhatkit
import subprocess
import os
import random
from datetime import datetime

def greetMe() :
    currentH = int (datetime.now().hour)
    
    if (currentH) == 33: 
        print("masuk")
    
    if (currentH >= 0) and (currentH < 12):
        engine2 = pyttsx3.init()
        print("JARVIS : Good Morning, Sir! This is JARVIS")
        engine2.say("Good Morning Sir! This is jarvis")
        engine2.runAndWait()
        
    elif (currentH >=12) and (currentH < 18) :
        engine2 = pyttsx3.init()
        print("JARVIS : Good Afternoon, Sir! This is JARVIS")
        engine2.say("Good Afternoon Sir! This is jarvis")
        engine2.runAndWait()
        
    else:
        engine2 = pyttsx3.init()
        print("JARVIS : Good Night, Sir! This is JARVIS")
        engine2.say("Good Night Sir! This is jarvis")
        engine2.runAndWait()
        
    engine2 = pyttsx3.init()
    print("JARVIS : What can I help you, sir?")
    engine2.say("What can I help you sir?")
    engine2.runAndWait()

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
        voice = 'error message'
    
    return voice

def answer (text):
    engine2 = pyttsx3.init()
    engine2.say("Okay sir," + text)
    print("JARVIS : Okay sir, " + text)
    engine2.runAndWait()
def answerW (text):
    engine2 = pyttsx3.init()
    engine2.say(text)
    print("JARVIS : " + text)
    engine2.runAndWait()
    
def givecommand ():
    a = 1
    command = inputvoice()
    while (a < 3 and command == 'error message'):
        a = a + 1
        answerW("Sorry sir, I dont know what you mean. Please repeat again or typing the command!")
        command = inputvoice()
    print()
    if (a == 3) or command == "type the command" :
        command = str(input ("Your Command : "))
        
    else :
        print("Your Command :",command)
    print()
    if 'google' in command :
        webbrowser.open("https://google.com")
        answer ("Opening google")
                
    elif 'rinaldi munir website' in command:
        webbrowser.open('https://informatika.stei.itb.ac.id/~rinaldi.munir/')
        answer  ("Opening rinaldi munir's website")
        
    elif 'goodbye' in command or "enough" in command:
        answer("Have a nice day")
        sys.exit()
        
    elif "thank you" in command:
        answer ("Your Welcome")
        
    elif "microsoft teams" in command:
        webbrowser.open("https://teams.microsoft.com/_?culture=en-us&country=US&lm=deeplink&lmsrc=homePageWeb&cmpid=WebSignIn#/school//?ctx=teamsGrid")
        answer  ( "Opening microsoft teams")
        
    elif "play" in command:
        pywhatkit.playonyt(command)
        clean = command.replace('play', '')
        answer  ("Playing" + clean)
        
    elif "what is" in command:
        pywhatkit.search(command)
        answer  ( "This is what you are looking for")
        
    elif "who are you" in command:
        answer  ( "I am jarvis, I am a digital assistant who created by Muhammad Fahmi Alamsah")
        
    elif "cmd" in command :
        subprocess.run("start", shell = True)
        answer("Opening cmd")
        
    # elif "vs code" in command :
    #     subprocess.call(['C:\Users\M. Fahmi Alamsyah\AppData\Local\Programs\Microsoft VS Code'])
    
    elif "how are you" in command or "what's up" in command :
            stMsgs = [ "Yeah, I'm fine. And you?" , "I'm good. And you?"]
            answerW(random.choice(stMsgs))
            jawab = inputvoice()
            print(jawab)
            if (jawab == "good"):
                answerW("Oh nice sir")
            elif (jawab == "bad"):
                answerW("I hope you get well soon")
            else:
                answerW("hmmm, ignore my question.")
    else:
        print("Jarvis : I dont know what you mean sir. Please repeat again or typing the command!")
        engine2 = pyttsx3.init()
        engine2.say("I dont know what you mean sir. Please repeat again or typing the command!")
        engine2.runAndWait()
        
 
greetMe()      
while True:
    givecommand()
    engine2 = pyttsx3.init()
    print("JARVIS : Any more command sir?")
    engine2.say("any more command sir?")
    engine2.runAndWait()
    
