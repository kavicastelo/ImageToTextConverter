#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from tkinter import *
import pywhatkit

f = open('image.txt', 'r')
image = f.read()

pywhatkit.image_to_ascii_art(image, '/home/kavi/Desktop/out/output')

print("\033[1;31m #######    ###    ###     ######    ######    #######     #######     #######\n"
      "###         ###    ###    ###       ###        ###        ###         ###\n"
      " #######    ###    ###   ###       ###         #######     #######     #######\n"
      "      ###   ###    ###    ###       ###        ###              ###         ###\n"
      "#######      ########      ######    ######    #######    #######     #######\n"
      "\n\n\nSuccessfully converted your image to text file.. \n"
      "Check it in your desktop/out folder\n"
      "If output file not in here please select your image path correctly in image.txt file")

def openfile():
    tf = open('/home/kavi/Desktop/out/output.txt', 'r')  # or tf = open(tf, 'r')
    data = tf.read()
    txt_area.insert(END, data)
    tf.close()


ws = Tk()
ws.title("Image")
ws.geometry("1200x600")
ws['bg'] = '#000000'


txt_area = Text(ws, width=120, height=30)
txt_area.pack(pady=20)


Button(
    ws,
    text="Open File",
    command=openfile
    ).pack(side=RIGHT, expand=True, fill=X, padx=20)


ws.mainloop()
