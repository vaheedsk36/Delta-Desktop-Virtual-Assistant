"""virtual assistant delta """
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import pyjokes
import ctypes

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
# print(voices[0].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am delta Sir. Please tell me how may I help you")
    
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    
    except Exception as e:
        print("Say that again please...")
        return "None"             """ Solve doubt here"""
    return query


if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}") 
                   
        elif 'hi delta'in query or 'hello delta' in query:
            speak("Hi Buddy!!")
        
        elif 'what are you doing'in query:
            speak("Chatting with you bud")
        
        elif 'creator'in query or 'who is your creator'in query:
            speak("i was created by masood akhtar vaheed")

        elif 'joke' in query or 'tell a joke' in query:
            
            speak(pyjokes.get_joke())
        
        elif 'write a memo' in query:
            speak("what should i write sir")
            note = takeCommand()
            memo = open("memo.txt",'w')
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            memo.write(strTime)
            memo.write(" :- ")
            memo.write(note)
        
        elif 'memo' in query:
            with open("memo.txt","r") as f:
                print(f.read())
                speak(f.read())
        
        elif 'lock windows' in query:
            try:
                speak("locking windows")
                ctypes.windll.user32.LockWorkStation()
            except Exception:
                print("Could not process the request")
        
        elif 'shutdown' in query:
            speak("shutting down delta")
            exit() 
