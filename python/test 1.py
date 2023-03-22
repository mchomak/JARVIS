import json
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import tkinter.filedialog as fd
import os
import os.path
from os import path

font='Times 15'
bg='white'
directory = str(os.getcwd())
box_commands_d=directory+'//data//box_commands.json'
commands_on_d=directory+'//data//commands_on.txt'

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.window_geometry = '400x550'
        self.geometry(self.window_geometry)
        self.minsize(400, 550)
        self.title('Commands')

        self.scroll_x = tk.Scrollbar(self, orient=tk.HORIZONTAL)
        self.scroll_y = tk.Scrollbar(self, orient=tk.VERTICAL)
        self.canvas = tk.Canvas(self, width=100, height=100,
                                xscrollcommand=self.scroll_x.set,
                                yscrollcommand=self.scroll_y.set)
        self.scroll_x.config(command=self.canvas.xview)
        self.scroll_y.config(command=self.canvas.yview)
        commands=App.file_reader(self)
        cmd_on=App.command_reader(self,commands)
        list_cb=App.otrisovka(self,commands)
        App.set_value(self,commands,cmd_on,list_cb)

    def otrisovka(self,commands):
        self.frame = tk.Frame(self.canvas)
        number = 0
        command_titles=[]
        list_cb = []
        # self.Exit_button = Button(self.frame, text='Close', bg='white', command=App.Exit(self,list_cb), font=1)

        print(len(commands))
        for j in range(10):
            list_cb.append(IntVar())

        for keys in commands:
            massive = commands[keys]
            print(keys, massive)
            self.command_title = Checkbutton(self.frame, text=f"{keys}:\n{massive}", font=font, bg=bg, anchor='w',
                                             width=27, justify='left',variable=list_cb[number])
            command_titles.append(self.command_title)

            self.command_title.grid(row=number, column=0)
            number=number+1

        self.canvas.create_window((0, 0), window=self.frame,
                                  anchor=tk.N + tk.W)

        # self.Exit_button.grid(row=0, column=1, sticky="e")
        self.canvas.grid(row=0, column=0, sticky="nswe")
        self.scroll_x.grid(row=1, column=0, sticky="we")
        self.scroll_y.grid(row=0, column=1, sticky="ns")

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.bind("<Configure>", self.resize)
        self.update_idletasks()
        self.minsize(self.winfo_width(), self.winfo_height())

        return list_cb

    def set_value(self,commands,cmd_on,list_cb):
        for number in range(10):
            print(cmd_on,number)
            cmd_on=str(cmd_on)
            cmd_on_off=int(cmd_on[number])
            print(cmd_on_off)
            list_cb[number].set(1)


    def resize(self, event):
        region = self.canvas.bbox(tk.ALL)
        self.canvas.configure(scrollregion=region)

    def Exit(self,list_cb):
        list_of_cb_values = []
        for i in range(10):
            list_of_cb_values.append(list_cb[i].get())
        print(list_of_cb_values)

    def add_command(self):
        pass

    def file_reader(self):
        with open(box_commands_d, encoding="utf-8") as box_commands:
            commands = json.load(box_commands)
            return commands

    def command_reader(self,commands):
        if os.path.exists(commands_on_d)==False:
            with open(commands_on_d,'w', encoding="utf-8") as commands_on:
                text=''
                for command in commands:
                    text=text+'1'
                commands_on.write(text)
                print(text)

        else:
            with open(commands_on_d, encoding="utf-8") as commands_on:
                cmd_on=commands_on.read()
                return cmd_on

    def new_keys(self,keys,com_on):
        print(keys,com_on)

app = App()
app.mainloop()