import pyttsx3     #pip install pyttxs3
import datetime
import speech_recognition as sr  #using pip
import pyaudio
import wikipedia      #using pip
import webbrowser
import os

# r = sr.Recognizer()
# with sr.Microphone() as source:
#      print("Listening...")
engine = pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
rate = engine.getProperty('rate')   # getting details of current speaking rate
engine.setProperty('rate', 150)
engine.runAndWait()
def Speak(audio):
    engine.say(audio)
    engine.runAndWait()
def intro():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        Speak("Good Morning ")
    elif hour>=12 and hour<18:
        Speak("Good Afternoon")
    else:
        Speak("Good Evening ")
    Speak("Amy here,your assistant,How may i help you?")
def take_command():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print("Recognizing...")
        instructions= r.recognize_google(audio,language='en-in')
        print("Paritosh said :",instructions)
    except Exception as error:
        # print(error)
        print(".......~")
        return "Nothing"
    return instructions
if __name__=="__main__":
    intro()
    while(True):
        instructions=take_command().lower()
        if 'tell me what to do now' in instructions:
            Speak("you have so many things, to do just open your google keep,    do i need to do tell u any thing more ")
        elif 'i am feeling bored' in instructions:
            Speak("shut the fuck up and start hustling")
        elif 'hello' in instructions:
            Speak("hello sir")
        elif 'wikipedia' in instructions:
            Speak('Searching,please wait')
            instructions=instructions.replace("wikipedia","")
            result=wikipedia.summary(instructions,sentences=1)
            Speak('Answer is ')
            print(result)
            Speak(result)
        elif 'open youtube' in instructions:
            code_target2 = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome_proxy.exe"
            os.startfile(code_target2)
        elif 'play linkin park' in instructions:
            mus_dir='F:\\Linkin Park'
            songs=os.listdir(mus_dir)
            print(songs)
            os.startfile(os.path.join(mus_dir,songs[0]))
        elif'open adobe acrobat' in instructions:
            code_target="C:\\Program Files (x86)\\Adobe\\Acrobat Reader DC\\Reader\\AcroRd32.exe"
            os.startfile(code_target)
        elif 'the time' in instructions:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            Speak(f"Sir, the time is {strTime}")
        elif 'open chrome' in instructions:
            code_target2 = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(code_target2)

        elif 'thank you' in instructions:
            Speak("its my pleasure sir ,Have a nice day")