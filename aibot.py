from speak import *
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import subprocess
import os
import webbrowser
import pyttsx3
import speech_recognition as sr


app = Tk()
app.title('ai_bot')
app.overrideredirect(1)
app.configure(bg = 'white')
app.geometry('700x600+700+250')





def ex(e = ''):
    exit()


l = Label(bg = 'black', fg = 'blue', font = ('chiller', 30), text = 'WELL COME TO MY AI BOT', padx = 165, pady = 20)
b =Button(bg = 'black', border = 5, fg = 'red', font = ('chiller', 20), command = ex, text = 'X', padx = 14, pady = 15)
b.place(x = 640, y = 0)
l.place(x = 0, y = 0)




app.mainloop()



