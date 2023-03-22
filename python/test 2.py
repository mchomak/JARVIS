import json
import tkinter as tk
from tkinter import *
import os
import os.path

font='Times 15'
bg='white'
directory = str(os.getcwd())
box_commands_d=directory+'//data//box_commands.json'
commands_on_d=directory+'//data//commands_on.txt'

class Command_app(tk.Tk):
    def __init__(self):
        super().__init__()
        self.window_geometry = '400x550'
        self.geometry(self.window_geometry)
        self.minsize(400, 550)
        self.title('Commands')
        self.otrisovka()


    def otrisovka(self):
        self.entry_text = Entry(self, text='enter request ')
        self.entry_text.pack()

if __name__ == '__main__':
    command_app = Command_app()
    command_app.mainloop()
