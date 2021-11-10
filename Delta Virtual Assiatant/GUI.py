"""virtual assistant delta """
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import pyjokes
import ctypes
from tkinter import *

assistantName = "Delta Virtual Assistant v0.1.0"

class commands:
    
    def speak(self,audio):
        self.engine = pyttsx3.init('sapi5')
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice',self.voices[0].id)
        self.engine.say(audio)
        self.engine.runAndWait()

    def wishme(self):
        hour = int(datetime.datetime.now().hour)
        if hour>=0 and hour<12:
            self.speak("Good Morning!")
        elif hour>=12 and hour<18:
            self.speak("Good Afternoon!")
        else:
            self.speak("Good Evening!")
        self.speak("I am delta Sir. Please tell me how may I help you")
        
    def takeCommand(self):
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
    

class GUI(commands):

    def __init__(self):
        self.window = Tk()
        self.window.title(assistantName)
        self.window.geometry("600x400")
        self.window.configure(bg="black")
        self.window.iconbitmap("E:\Programming\Py\Projects\Delta Virtual Assiatant\_resources\main.ico")
        self.window.resizable(0,0)
        
        # self.window.iconbitmap('app_icon.ico')       # solve doubt here
        
    def guiLayout(self):
        self.name_label = Label(text = assistantName,width = 300, bg = "blue", fg="white", font = ("Calibri", 13))
        self.name_label.pack()
        
        self.canvas = Canvas(self.window,width = 398, height = 400,bg='black')
        self.canvas.pack(side= RIGHT)
        self.img = PhotoImage(file="E:\Programming\Py\Projects\Delta Virtual Assiatant\_resources\myassist.png")
        self.canvas.create_image(201,218,image=self.img)
    
    def instructions(self):
        self.insWindow = Toplevel(self.window)
        self.insWindow.title("Instructions Page")
        self.insWindow.geometry("690x760")
        self.insWindow.iconbitmap("E:\Programming\Py\Projects\Delta Virtual Assiatant\_resources\main2.ico")
        self.canvas = Canvas(self.insWindow,width = 680, height = 710,bg='white')
        self.canvas.pack(expand= TRUE, fill=BOTH)
        self.inst_photo = PhotoImage(file = "E:\Programming\Py\Projects\Delta Virtual Assiatant\_resources\instructions.png")
        self.canvas.create_image(345,380,image=self.inst_photo)
     
    def allButtons(self):
        self.microphone_photo = PhotoImage(file = "E:\Programming\Py\Projects\Delta Virtual Assiatant\_resources\logo.png")
        self.microphone_button = Button(image=self.microphone_photo, command = self.Run, bg= 'black', borderwidth=0)
        self.microphone_button.place(x=39,y=100)

        self.exitbtn_photo = PhotoImage(file = "E:\Programming\Py\Projects\Delta Virtual Assiatant\_resources\exit_button.png")
        self.exitbtn = Button(image=self.exitbtn_photo, command = self.stop_exit,bg= 'black',borderwidth=0)
        self.exitbtn.place(x=68,y=270)

        self.insbtn_photo = PhotoImage(file = "E:\Programming\Py\Projects\Delta Virtual Assiatant\_resources\ins.png")
        self.insbtn = Button(image=self.insbtn_photo, command = self.instructions,borderwidth=0)
        self.insbtn.place(x=567,y=27)
    
    def Run(self):
        
        self.wishme()
        while True:
            query = self.takeCommand().lower()

            if 'wikipedia' in query:
                try:
                    self.speak('Searching Wikipedia...')
                    query = query.replace("wikipedia", "")
                    results = wikipedia.summary(query, sentences=3)
                    self.speak("According to wikipedia")
                    print(results)
                    self.speak(results)
                
                except Exception as e:
                    print("Unable to process your request!!!")

            elif 'open youtube' in query:
                webbrowser.open("youtube.com")
            
            elif 'open google' in query:
                webbrowser.open("google.com")

            elif 'open stackoverflow' in query:
                webbrowser.open("stackoverflow.com")

            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                self.speak(f"Sir, the time is {strTime}") 
                    
            elif 'hi delta'in query or 'hello delta' in query:
                self.speak("Hi Buddy!!")
            
            elif 'what are you doing'in query:
                self.speak("Chatting with you bud")
            
            elif 'Do you know alexa'in query or 'Do you know siri'in query:
                self.speak("why do you bother")
            
            elif 'creator'in query or 'who is your creator'in query:
                self.speak("i was created by masood akhtar vaheed")

            elif 'joke' in query or 'tell a joke' in query:
                
                self.speak(pyjokes.get_joke())
            
            elif 'write a memo' in query:
                self.speak("what should i write sir")
                note = self.takeCommand()
                memo = open("memo.txt",'w')
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                memo.write(strTime)
                memo.write(" :- ")
                memo.write(note)
            
            elif 'read memo' in query:
                with open("memo.txt","r") as f:
                    print(f.read())
                    self.speak(f.read())
            
            elif 'lock windows' in query:
                try:
                    self.speak("locking windows")
                    ctypes.windll.user32.LockWorkStation()
                except Exception:
                    print("Could not process the request")
            
            elif 'shutdown' in query:
                self.speak("shutting down delta")
                self.stop_exit() 

    def stop_exit(self):
        exit()

    def main_window(self):
        self.guiLayout()
        self.allButtons()
        self.window.mainloop()

if __name__ == "__main__":
    start = GUI()
    start.main_window()
    