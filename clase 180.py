from tkinter import *
import speech_recognition as sr
import webbrowser
import pyttsx3
from datetime import datetime
import subprocess


root = Tk()
root.geometry("500x500")
root.configure(background="Light Blue")

label=Label(root,text="Bienvenido a tu asistente de escritorio personal",bg="Light Blue",font=("Bahnschrift Light",15,"bold"))
label.place(relx=0.5,rely=0.1,anchor=CENTER)

text_to_speech=pyttsx3.init()
    
def speak(audio):
    text_to_speech.say(audio)
    text_to_speech.runAndWait()
    
def r_audio():
    speech_recognisor= sr.Recognizer()
    speak("¿Cómo puedo ayudarte?")   
    with sr.Microphone() as source:
        audio=  speech_recognisor.listen(source) 
        voice_data=''
        try:
            voice_data=  speech_recognisor.recognize_google(audio, language='es-mx')
        except sr.UnknownValueError:
            print('Por favor, repite. No entendí tu solicitud')
            speak('Por favor, repite. No entendí tu solicitud')
            r_audio()
        respond(voice_data)
       
        
def respond(voice_data):
    print(voice_data)
    if "nombre" in voice_data:
        speak("Mi nombre es Jarvis")
        print('Mi nombre es Jarvis')
            
    if "hora" in voice_data:
        speak("La hora actual es")
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        speak(current_time)
        print(current_time)
            
    if "buscar" in voice_data:
        speak("Abriendo Google")
        print("Abriendo Google")
        webbrowser.get().open("https://google.com/")
            
    if "videos" in voice_data:
        speak("Abriendo YouTube")
        print("Abriendo YouTube")
        webbrowser.get().open("https://youtube.com/")
            
    if "editor de texto" in voice_data:
        speak("Abriendo la app")
        print("Abriendo la app")
        subprocess.Popen(["notepad.exe"])
        #Para Mac
        #subprocess.call(["/usr/bin/open", "/Applications/TextEdit.app"])        
        
btn= Button(root, text="Iniciar", command=r_audio,bg="red3", fg="white", padx=10, pady=1,  font=("Arial",11, "bold"), relief=FLAT)
btn.place(relx=0.5,rely=0.5,anchor=CENTER)

root.mainloop()