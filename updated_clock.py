from tkinter import *
from time import strftime
from plyer import notification
import pyttsx3
from playsound import playsound

engine = pyttsx3.init()
title_font = ('Helvetica',20,'bold')
digital_clock = Tk()
digital_clock.geometry("720x150")
digital_clock.title('Digital Clock')

def say(text):
    engine.say(text)
    engine.runAndWait()

def time():
    global string
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)
    
    if string == '15:50:15 PM':
        say("its time to wake up")
        notification.notify(
            title='bhoomi',
            message='KB AYEGI LIGHT',
            timeout=10,
        )
title_font = ('Helvetica',20,'bold')
label = Label(digital_clock, font=('algerian', 90, 'bold'), background='#ffffff', foreground='black')
label.grid(row=0,column=0,columnspan=4)

time()
mainloop()