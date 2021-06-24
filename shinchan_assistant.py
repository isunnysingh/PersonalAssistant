import pyttsx3#(text to speech)
import datetime
import speech_recognition as sr#(used for convert speech into text)
import wikipedia
import webbrowser
import os
import random # (used for randomly select some elements)
import sys
import requests #(used to send all kind of HTTP requests)
import json #(the transformation of data into a series of bytes(hence serial) to be transmitted across a network)
import smtplib #() SMTP = simple mail transfer protocol........ used to send e-mail and routing e-mail between mail server.)




engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[2].id)
engine.setProperty('voices', voices[3].id)




def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning!" + name + '.' )

    elif hour>=12 and hour<18:
        speak("good Afternoon" + name + '.')

    else:
        speak("good evening!" + name + '.')

    speak("i am Shinchan , how may i help you?")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening...')
        r.pause_threshold = 1
        r.energy_threshold = 400
        audio = r.listen(source)

    try:
        print('Recognising...')
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("say that again please...")
        return"None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your_email_address', 'your_password')
    server.sendmail('your_email_address', to, content)
    server.close()

if __name__ == "__main__":
    speak("What's your name, Human?")
    name ='Human'
    name = takecommand()
    speak("Hello")

    wishme()
    while True:
        query = takecommand().lower()

        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query,sentences=4)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak('youtube opened')
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak('google opened')
            webbrowser.open("google.com")

        elif 'open facebook' in query:
            speak('facebook opened')
            webbrowser.open("facebook.com")

        elif 'play music' in query:
            speak('music played')
            music_dir = 'F:\\Music'
            Music = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir , random.choice(Music)))

        elif 'the time' in query:
            curtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"its {curtime}")

        elif 'thank you' in query:
            speak("my pleasure")

        elif 'open vs code' in query:
            codepath = "C:\\Users\\sunny singh\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif 'open MS Word' in query:
            path = "C:\\Users\\sunny singh\\Desktop\\New Word Document.docx"
            os.startfile(path)

        elif 'quit' in query:
            speak("good bye")
            sys.exit(0)

        elif 'latest news' in query:
            speak("News for today.. Lets begin")
            url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=4431100cfeb042cc8039348b8c0b4a51"
            news = requests.get(url).text
            news_dict = json.loads(news)
            arts = news_dict['articles']
            for article in arts:
                speak(article['title'])
                print(article['title'])
                speak("Moving on to the next news..Listen Carefully")

            speak("Thanks for listening...")

        elif 'who are you' in query:
            speak("Hey!, I am Shinchan. Your personal Assistant, I am here to make your life easier. You can command me to perform various tasks such as open google,facebook,vs code, play music, and many more. ")

        elif 'who made you' in query:
            speak("i have been created by sunny singh")

        elif 'email' in query:
            try:
                speak("What should I say?")
                content = takecommand()
                to = "receiver_email"
                sendEmail(to, content)
                speak("Email has been sent!")
                print("email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry. I am not able to send this email")

        elif 'what' in query:
            speak('searching...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query,sentences=4)
            speak("I've got this for you...")
            print(results)
            speak(results)

        else:
            speak('i dont know this')
