import math
import random
from tkinter import *
from PIL import ImageTk, Image

def clicked(): 
    startButton.configure(text = "I just got clicked!")
    

if __name__ == '__main__':
    #creating Tk window
    main = Tk()
    
    #window name
    main.title("first tkinter program!")
    
    #setting geometry of tk window
    main.geometry("1000x1000")
        
    #title screen
    label = Label(main, text = "Hello world !")
    label.place(relx = .5, rely = .1, anchor = CENTER)
    
    #splash text
    splashText = Label(main, text = "splashText")
    splashText.grid()
    
    #background 
    main.configure(background = "light pink")
    
    #start button widget 
    startButton = Button(main, text = "Test start game button", fg = "blue", background = "light pink", command = clicked)
    startButton.place(relx = .5, rely = .5, anchor = CENTER)
    
    frame = LabelFrame(main, text = "this is my frame", padx = 5, pady = 5)
    frame.pack(padx = 10, pady = 10)
    
    #exit button widget
    exitButton = Button(main, text = "click me! im the exit button", fg = "red", command = clicked)
    exitButton.place(relx = 1, x =- 2, y = 2, anchor = NE)
    
    
main.mainloop()
    