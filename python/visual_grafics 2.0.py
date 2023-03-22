import tkinter as tk
from tkinter import *
from tkinter import messagebox
import tkinter.filedialog as fd
import os
import os.path
from os import path
import json

inp=''
version='1.0'
sluh='___________________'
command='___________________'
start=0
button_cord=[2,20]

font='Times 15'
bg='white'
directory = str(os.getcwd())
box_commands_d=directory+'//data//box_commands.json'
commands_on_d=directory+'//data//commands_on.txt'
new_box_commands_d=directory+'//data//new_box_commands.json'

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.window_geometry='400x550'
        self.geometry(self.window_geometry)
        self.title('J.A.R.V.I.S')
        self.minsize(400,550)
        self.create_frames()

    def create_frames(self):
        self.button_frame=Button_frame(self)
        self.info_frame=Info_frame(self)
        self.last_frame=Last_frame(self)

        self.button_frame.grid(column=0)
        self.info_frame.grid(column=0,columnspan =6)
        self.last_frame.grid(column=0)

    def del_frames(self):
        self.button_frame.grid_forget()
        self.info_frame.grid_forget()
        self.last_frame.grid_forget()

        self.command_frame=Command_app(self)
        self.command_frame.grid()

    def add_frames(self):
        self.command_frame.grid_forget()
        self.button_frame.grid()
        self.info_frame.grid()
        self.last_frame.grid()

class Button_frame(tk.Frame):
    def __init__(self,parent):
        super().__init__(parent)
        self.add_widgets()

    def add_widgets(self):
        self.start_button = Button(self, text='Start', bg=bg, command=Button_model.Start(self), font=font,
                              height=button_cord[0], width=button_cord[1])
        self.settings_button = Button(self, text='Settings', bg=bg, command=Button_model.Settings(self), font=font,
                                 height=button_cord[0], width=button_cord[1])
        self.comands_button = Button(self, text='Comands', bg=bg, command=lambda: Button_model.Commands(self), font=font,
                                height=button_cord[0], width=button_cord[1])
        self.sluh_button = Button(self, text='voice\ninput ', bg=bg, command=Button_model.voice_input(self), font=font)
        self.text_button = Button(self, text='text\ninput ', bg=bg, command=Button_model.text_input(self), font=font)
        self.entry_text = Entry(self, text='enter request ', font=font, bg=bg)
        self.inp_title = Label(self, text='input means:\n' + inp, font=font, bg=bg,
                          relief=tk.RAISED, width=20, height=2)


        self.start_button.grid(pady=2.5, row=1, column=1)
        self.settings_button.grid(row=2, column=1)
        self.comands_button.grid(pady=2.5, row=3, column=1)

        self.grid_columnconfigure(0, minsize=60)
        self.grid_columnconfigure(1, minsize=280)
        self.grid_columnconfigure(2, minsize=60)

class Info_frame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.add_widgets()

    def add_widgets(self):
        self.hear_text = Label(self, text='I thing:\n'+sluh, font=font, bg=bg,
                      width=35, anchor='w',justify='left')
        self.Recognized_text = Label(self, text='Recognized command:\n'+command, font=font, bg=bg,
                               width=35, anchor='w',justify='left')
        self.open_report_butoon = Button(self, text='Open work report', bg=bg, command=Button_model.open_report(self), font=font,
                                    height=button_cord[0], width=button_cord[1])

        self.hear_text.grid(row=4, column=1)
        self.Recognized_text.grid(row=5, column=1)
        self.open_report_butoon.grid(row=6, column=1)

        self.grid_rowconfigure(4, minsize=50)
        self.grid_rowconfigure(5, minsize=50)
        self.grid_rowconfigure(6, minsize=70)

class Last_frame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.add_widgets()

    def add_widgets(self):

        self.Exit_button = Button(self, text='Close', bg=bg, command=lambda: Button_model.Exit(self), font=font)
        self.program_version = Label(self, text=version, font=font)

        self.grid_columnconfigure(1, minsize=300)
        self.grid_rowconfigure(0, minsize=140)

        self.Exit_button.grid(row=1,column=0)
        self.program_version.grid(row=1,column=2)

class Command_app(tk.Frame):
    def __init__(self,parent):
        super().__init__(parent)
        self.width=430
        self.commands = self.file_reader()
        self.cmd_on = self.command_reader(self.commands)
        self.list_cb = self.otrisovka()
        self.set_value()

    def otrisovka(self):
        self.scroll_x = tk.Scrollbar(self, orient=tk.HORIZONTAL)
        self.scroll_y = tk.Scrollbar(self, orient=tk.VERTICAL)
        self.canvas = tk.Canvas(self, width=380, height=530,
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

        self.Exit_button = Button(self.frame, text='Close', bg=bg,
                                  command=lambda: self.Exit(), font=font)
        self.set_on_button=Button(self.frame, text='seet on', bg=bg,
                                  command=lambda: self.set_on(), font=font)
        self.set_off_button = Button(self.frame, text='seet off', bg=bg,
                                    command=lambda: self.set_off(), font=font)
        self.create_new_cmd_button = Button(self.frame, text='new cmd', bg=bg,
                                     command=lambda: self.create_new_command(), font=font)

        self.set_on_button.grid(row=0, column=1)
        self.set_off_button.grid(row=1, column=1)
        self.create_new_cmd_button.grid(row=2, column=1)
        self.Exit_button.grid(row=3, column=1)

        for keys in self.commands:
            massive = self.commands[keys]
            self.command_title = Checkbutton(self.frame, text=f"{keys}:\n{massive}", font=font, bg=bg, anchor='w',
                                             width=25, justify='left',variable=self.list_cb[number])

            self.command_title.grid(row=number, column=0)
            number=number+1

        return self.list_cb

    def set_value(self):
        for number in range(len(self.commands)):
            self.cmd_on=str(self.cmd_on)
            cmd_on_off=int(self.cmd_on[number])
            self.list_cb[number].set(cmd_on_off)
            print(cmd_on_off)

    def get_value(self):
        new_com_on=''
        for number in range(len(self.commands)):
            com_state=self.list_cb[number].get()
            new_com_on=new_com_on+str(com_state)
        return new_com_on

    def set_on(self):
        for number in range(len(self.commands)):
            self.list_cb[number].set(1)

    def set_off(self):
        for number in range(len(self.commands)):
            self.list_cb[number].set(0)

    def create_new_command(self):
        pass

    def resize(self, event):
        region = self.canvas.bbox(tk.ALL)
        self.canvas.configure(scrollregion=region)

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

    def create_new_cmd(self):
        with open(box_commands_d, 'r', encoding="utf-8") as box_commands:
            box_cmd = json.load(box_commands)
            new_box_cmd = {}
            with open(commands_on_d, encoding="utf-8") as commands_on:
                cmd_on = commands_on.read()
                i = 0
                for key in box_cmd:
                    if cmd_on[i] == '1':
                        new_box_cmd[key] = box_cmd[key]
                    else:
                        pass
                    i = i + 1
                with open(new_box_commands_d, 'w', encoding="utf-8") as new_box_commands:
                    json.dump(new_box_cmd, new_box_commands, indent=4, ensure_ascii=False)

    def Exit(self):
        self.new_com_on=self.get_value()
        with open(commands_on_d,'w', encoding="utf-8") as commands_on:
            commands_on.write(str(self.new_com_on))
            print(self.new_com_on)
        Command_app.create_new_cmd(self)
        App.add_frames(window)

class Button_model():
    def __init__(self):
        self.work_data_d= directory+r'\data\work_data.txt'
        self.box_commands_d =  directory + r'\data\box_commands.json'
        self.jarvis_d =  directory + r'\J.A.R.V.I.S_vol_3.py'
        self.otchet_for_work_d =  directory + r'\data\otchet_for_work.txt'
        self.inp=0
        self.start=1
        self.text=''

    def Start(self):
        pass

    def Settings(self):
        pass

    def Commands(self):
        App.del_frames(window)
        print(1)

    def voice_input(self):
        pass

    def text_input(self):
        pass

    def open_report(self):
        pass

    def Exit(self):
        window.quit()

window=App()
window.mainloop()
