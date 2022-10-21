from time import strftime, struct_time
import pyttsx3
import datetime
import speech_recognition as sr
#import wikipedia
import webbrowser
import os

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
# print(voices[0])
engine.setProperty("voice", voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning sir")
    elif hour >= 12 and hour < 17:
        speak("Good Afternoon sir")
    elif hour >= 17 and hour < 20:
        speak("Good evenig sir")

    else:
        speak("Good night sir")

def wish_mam():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning mam")
    elif hour >= 12 and hour < 17:
        speak("Good Afternoon mam")
    elif hour >= 17 and hour < 20:
        speak("Good evenig mam")

    else:
        speak("Good night mam")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        r.energy_threshold = 20000
        audio = r.listen(source)

    try:
        print("Recognising...")
        query = r.recognize_google(audio, language="hin-in")
        print(f"user said:{query}\n")

    except Exception as e:
        print(e)
        speak ("Say that again please....")
        return "None"

    return query


if __name__ == "__main__":
    
    wishme()
    speak("can you please tell me the password")
    query = takeCommand().lower()
    if "0.0025" in query:
        wishme()
        speak("How may i help you sir")
    else:
        speak("I am not suppose to assist you")
        speak("Pluto  is Shutting down")
        exit()
    while True:

        query = takeCommand().lower()

        if "wikipedia" in query:
            speak("Searching wikipedia....")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)

        elif "shivam" in query:
            wishme()

        elif "swati" in query:
            wish_mam()

        elif "introduce yourself" in query:
            speak("Hello ,I am pluto , i was developed by Shivam and swati.  ")

        elif "how are you" in query:
            speak("Sir I am fine , What about you?")

        elif "job" in query:
            speak("Thank you sir")

        elif "thank you" in query:
            speak("My pleasure sir")

        elif "library" in query:
            webbrowser.open("https://abesit.in//library//question-paper-bank/")

        elif "krishna college" in query:
            webbrowser.open("www.krishnacollege.ac.in")

        elif "a k t u" in query:
            webbrowser.open("aktu.ac.in")

        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        elif "open google" in query:
            webbrowser.open("google.com")

        elif "open instagram" in query:
            webbrowser.open("instagram.com")

        elif "time" in query:
            struct = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the time is {struct}")

        elif "open vs code" in query:
            vspath ="C:\\Users\\shiva\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs"
            os.startfile(vspath)

        elif "chrome" in query:
            chromePath= "C:\\Program Files\\Google\\Chrome\\Application"
            os.startfile(chromePath)

        elif "media player" in query:
            vlcPath="C:\\Program Files\\VideoLAN\\VLC\\vlc.exe"
            os.startfile(vlcPath)

        elif "play music" in query:
            music_folder = "D:\\Shivam\\backup\phone data\\sd card\\SHAREit\\audios"
            songs = os.listdir(music_folder)
            os.startfile(os.path.join(music_folder , songs[1]))

        elif "shutdown" in query:
            speak("Pluto is shutting down")
            exit()
            
