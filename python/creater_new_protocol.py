import json
import tkinter as tk
from tkinter import *
import os
import os.path

font='Times 17'
bg='white'
directory = str(os.getcwd())
box_commands_d=directory+'//data//box_commands.json'
commands_on_d=directory+'//data//commands_on.txt'
new_box_commands_d=directory+'//data//new_box_commands.json'
protocol_com_on=0

class Command_app(tk.Toplevel):
    def __init__(self,parent):
        super().__init__(parent)
        self.window_geometry = '700x550'
        self.geometry(self.window_geometry)
        self.title('J.A.R.V.I.S')
        self.minsize(650, 550)
        self.otrisovka()

    def otrisovka(self):

        self.all_commands=All_commads(self)
        self.protocol_command=Protocol_command(self)
        self.button_frame=Button_frame(self)

        self.all_commands.grid(row=0,column=0,rowspan=2)
        self.button_frame.grid(row=0,column=1)
        self.protocol_command.grid(row=1,column=1)

    def file_reader(self):
        with open(box_commands_d, encoding="utf-8") as box_commands:
            commands = json.load(box_commands)
            return commands

    def get_value(self):
        self.command_on,self.commands=All_commads.get_value(self.all_commands)
        self.protocol_commands={}
        i=0
        for key in self.commands:
            if self.command_on[i]=='1':
                self.protocol_commands[key]=self.commands[key]
            i=i+1
        print(self.protocol_commands)
        Protocol_command.add_commands(self.protocol_command,self.protocol_commands)

    def Exit(self):
        window.quit()

class Button_frame(tk.Frame):
    def __init__(self,parent):
        super().__init__(parent)
        self.button_cord2=[1,20]
        self.add_widgets()

    def add_widgets(self):
        self.entry_name = Entry(self, font=font, bg=bg, width=30)
        self.enrty_keys = Entry(self, font=font, bg=bg, width=30)

        self.name_title = Label(self, text='Entry protocol name:',font=font, bg=bg, width=25)
        self.keys_title = Label(self, text='Entry protocol keys:',font=font, bg=bg, width=25)
        self.show_command_button = Button(self, text='show_command', bg=bg,
                                  command=lambda: Command_app.get_value(app), font=font,
                                  height=self.button_cord2[0], width=self.button_cord2[1])

        self.name_title.pack()
        self.entry_name.pack()
        self.keys_title.pack()
        self.enrty_keys.pack()
        self.show_command_button.pack()

class Protocol_command(tk.Frame):
    def __init__(self,parent):
        super().__init__(parent)
        self.commands_titles = []
        self.commands = self.file_reader()
        self.add_widgets()

    def add_widgets(self):
        self.scroll_x = tk.Scrollbar(self, orient=tk.HORIZONTAL)
        self.scroll_y = tk.Scrollbar(self, orient=tk.VERTICAL)
        self.canvas = tk.Canvas(self, width=330, height=330,
                                xscrollcommand=self.scroll_x.set,
                                yscrollcommand=self.scroll_y.set)
        self.scroll_x.config(command=self.canvas.xview)
        self.scroll_y.config(command=self.canvas.yview)

        self.frame = tk.Frame(self.canvas)
        self.frame.pack()
        self.canvas.create_window((0, 0), window=self.frame,
                                  anchor=tk.N + tk.W)
        self.canvas.grid(row=0, column=0, sticky="nswe")
        self.scroll_x.grid(row=1, column=0, sticky="we")
        self.scroll_y.grid(row=0, column=1, sticky="ns")

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.bind("<Configure>", self.resize)
        self.update_idletasks()

        self.start_button = Button(self, text='close', bg=bg, command=lambda: print(2), font='Times 13')
        self.start_button.grid(row=2,column=0, sticky="e")

    def add_commands(self, protocol_commands):
        number = 0

        for cmd in self.commands_titles:
            cmd.grid_remove()

        self.commands_titles=[]
        for keys in protocol_commands:
            massive = protocol_commands[keys]
            self.command_title = Label(self.frame, text=f"{keys}:\n{massive}", font=font, bg=bg, anchor='w',
                                             width=25, justify='left')
            print(keys)

            self.command_title.grid(row=number, column=0)
            self.commands_titles.append(self.command_title)
            number = number + 1

    def resize(self, event):
        region = self.canvas.bbox(tk.ALL)
        self.canvas.configure(scrollregion=region)

    def file_reader(self):
        with open(box_commands_d, encoding="utf-8") as box_commands:
            commands = json.load(box_commands)
            return commands

class All_commads(tk.Frame):
    def __init__(self,parent):
        super().__init__(parent)
        self.commands = self.file_reader()
        self.add_widgets()

    def add_widgets(self):
        self.scroll_x = tk.Scrollbar(self, orient=tk.HORIZONTAL)
        self.scroll_y = tk.Scrollbar(self, orient=tk.VERTICAL)
        self.canvas = tk.Canvas(self, width=320, height=530,
                                xscrollcommand=self.scroll_x.set,
                                yscrollcommand=self.scroll_y.set)
        self.scroll_x.config(command=self.canvas.xview)
        self.scroll_y.config(command=self.canvas.yview)

        self.frame = tk.Frame(self.canvas)
        self.frame.pack()
        self.canvas.create_window((0, 0), window=self.frame,
                                  anchor=tk.N + tk.W)
        self.canvas.grid(row=0, column=0, sticky="nswe")
        self.scroll_x.grid(row=1, column=0, sticky="we")
        self.scroll_y.grid(row=0, column=1, sticky="ns")

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.bind("<Configure>", self.resize)
        self.update_idletasks()

        number = 0
        self.list_cb = []

        for j in range(len(self.commands)):
            self.list_cb.append(IntVar())

        for keys in self.commands:
            massive = self.commands[keys]
            self.command_title = Checkbutton(self.frame, text=f"{keys}:\n{massive}", font=font, bg=bg, anchor='w',
                                             width=25, justify='left',variable=self.list_cb[number])

            self.command_title.grid(row=number, column=0)
            number=number+1

    def resize(self, event):
        region = self.canvas.bbox(tk.ALL)
        self.canvas.configure(scrollregion=region)

    def file_reader(self):
        with open(box_commands_d, encoding="utf-8") as box_commands:
            commands = json.load(box_commands)
            return commands

    def get_value(self):
        new_com_on=''
        for number in range(len(self.commands)):
            com_state=self.list_cb[number].get()
            new_com_on=new_com_on+str(com_state)
        return new_com_on,self.commands

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.window_geometry='400x550'
        self.geometry(self.window_geometry)
        self.title('J.A.R.V.I.S')
        self.minsize(400,550)

if __name__ == '__main__':
    window=App()
    app = Command_app(window)
    window.mainloop()