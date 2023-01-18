import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
import customtkinter as ctk
from ttkthemes import ThemedStyle
import os 

FONT = 'monospace'

window = ctk.CTk()
window.geometry("400x150")
window.title('Font Installer')

# style change from ttk 
style = ThemedStyle(window)
style.set_theme("black")

font = ctk.CTkFont(family='monospace', size=12)

title_label = ctk.CTkLabel(window, text='Please select .zip from your font package')
title_label.pack()

entry = ctk.CTkEntry(window, width=350 )
entry.pack()
zipfile = None
path = ''
name = ''


def install_font():

    os.system(f'cd  {os.getcwd()} && pkexec /home/nahuel/Estudios/MisProyectos/font-installer/install_font.sh {path} {name}')

def select_file():
    global zipfile
    global path
    global name
    zipfile = fd.askopenfilename(title='Open a zip file', initialdir='/home/nahuel')

    name = str(zipfile).split('/')[-1]
    if zipfile != None and str(zipfile) != '()':
        
        send_button.configure(state='enabled')
        path = str(zipfile)
        entry.insert(index=0, string=path)

        path = path.replace(name, '')
                

            
        print('salida', path)
send_button = ctk.CTkButton(window, text='Install', command=install_font, state='disabled')
send_button.pack(pady=5)

open_button = ctk.CTkButton(window, text='Select file', command=select_file)
open_button.pack()




window.mainloop()