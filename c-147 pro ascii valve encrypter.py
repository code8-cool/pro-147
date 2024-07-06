# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 16:25:20 2024

@author: occup
"""

from tkinter import * 
root = Tk()
root.title("Ascii value converter")
root.geometry("605x550")

input_word = Entry(root)
label_output = Label(root)
label_encrypt = Label(root) 

def convert_ascii():
   input_text = input_word.get()
   label_output ["text"] = ""
   
   for i in input_text:
       label_output ["text"] += str(ord(i)) + " "
       label_encrypt ["text"] += int(ord(i)) - 1 + " " 
       label_encrypt ["text"] +=  str(chr(i)) + " "
       






btn = Button(root, text = "Show Ascii value of word", command = convert_ascii)




input_word.place(relx = 0.5,  rely = 0.2, anchor = CENTER)
btn.place(relx = 0.5,  rely = 0.3, anchor = CENTER)
label_output.place(relx = 0.5,  rely = 0.4, anchor = CENTER)
label_encrypt.place(relx = 0.5,  rely = 0.5, anchor = CENTER)


root.mainloop()
