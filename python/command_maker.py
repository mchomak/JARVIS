import json
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import tkinter.filedialog as fd
import os

window=Tk()
window_g='400x550'
window.title('command_maker')
window.geometry(window_g)
window.minsize(400,550)
font='Times 15'
bg='white'

box_commands_d='C://Users//admin//PycharmProjects//J.A.R.V.I.S//data//box_commands.json'

def file_reader():
    with open(box_commands_d, encoding="utf-8") as box_commands:
        commands=json.load(box_commands)
        return commands

def otrisovka(commands):
    frame0 = tk.Frame(window,bg=bg)
    frame0.pack()
    row=0
    for keys in commands:
        massive=commands[keys]
        print(keys,massive)
        command_title = Checkbutton(frame0, text=f"{keys}:\n{massive}", font=font, bg=bg,anchor='w',
                              width=100)

        command_title.grid(stick='w',row=row,column=0)
        row=row+1




def main():
    commands=file_reader()
    otrisovka(commands)
    window.mainloop()

main()