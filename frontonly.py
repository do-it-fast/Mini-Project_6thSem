from tkinter import *
import tkinter.font as font
gui = Tk()
gui.geometry('1000x800')
'''
widgets are added here
'''
def helloCallBack():
   tkMessageBox.showinfo( "Hello Python", "Hello World")
title = Label(gui, text = "Sign Language Prediction Using LSTM",font=font.Font(family='Helvetica',size=30,weight='bold')).place(x = 150,y = 80)
btnStartCapture = Button(gui, text ="Start Capture", command = helloCallBack,height=5,width=30,fg='white', bg='blue',font=font.Font(family='Helvetica',size=15,weight='bold')).place(x=300,y=480)


gui.mainloop()