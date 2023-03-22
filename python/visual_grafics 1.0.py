import tkinter as tk
from tkinter import *
from tkinter import messagebox
import tkinter.filedialog as fd
import os
import os.path
from os import path

window=Tk()
window_g='400x550'
window.title('J.A.R.V.I.S')
window.geometry(window_g)
window.minsize(400,550)
directory=str(os.getcwd())
work_data_d=directory+r'\data\work_data.txt'
box_commands_d=directory+r'\data\box_commands.json'
jarvis_d=directory+r'\J.A.R.V.I.S_vol_3.py'
otchet_for_work_d=directory+r'\data\otchet_for_work.txt'
inp=''
version='1.0'
sluh='___________________'
command='___________________'
start=0

button_cord=[2,20]

def voice_input():
    global inp,inp_title
    inp=1
    inp_title['text']='input means \n'+'voice'
def text_input():
    global inp,inp_title
    inp = 0
    inp_title['text'] = 'input means \n' +'text'
    entry_text.grid(pady=2.5, row=2, column=1)

def Start():
    global inp,work_data,inp_title,start
    if start==0:
        sluh_button.grid(pady=2.5, row=1, column=2)
        text_button.grid(pady=2.5, row=3, column=2)
        start=1
    elif start==1:
        with open(work_data_d, 'w', encoding="utf-8") as work_data:
            if inp==1:
                work_data.write('1\n')
                work_data.write('1\n')
                inp=2
                print('voice input')
                inp_title['text'] = 'input means \n'
                os.startfile(jarvis_d)
            elif inp==0:
                work_data.write('0\n')
                work_data.write('1\n')
                inp = 2
                print('text input')
                start=2
            else:
                messagebox.showwarning(title='warning', message='Выберите средство ввода')

    elif start==2:
        start=0
        text=entry_text.get()
        with open(work_data_d, 'a', encoding="utf-8") as work_data:
            work_data.write(f'{text}\n')
            print(text)
        entry_text.delete(first=0,last=END)
        inp_title['text'] = 'input means \n'
        hear_text['text'] = 'I thing: '+text
        sluh_button.grid_remove()
        text_button.grid_remove()
        entry_text.grid_remove()
        os.startfile(jarvis_d)

def Settings():
    pass

def Commands():
    pass

def open_report():
    os.startfile(otchet_for_work_d)

def Exit():
    window.destroy()

# настраиваем все виджеты
def otrisovka():
    global canvas,frame1,sluh,inp_title,inp,entry_text,hear_text,sluh_button,text_button

    frame1 = tk.Frame(window,height=200, width=400)
    frame2 = tk.Frame(window, height=270, width=400)
    frame3 = tk.Frame(window, height=80, width=400)

    start_button = Button(frame1, text='Start', bg='white', command=Start,font=1,
                          height=button_cord[0],width=button_cord[1])
    settings_button = Button(frame1, text='Settings', bg='white', command=Settings, font=1,
                          height=button_cord[0], width=button_cord[1])
    comands_button = Button(frame1, text='Comands', bg='white', command=Commands, font=1,
                           height=button_cord[0], width=button_cord[1])
    sluh_button = Button(frame1, text='voice\ninput ', bg='white', command=voice_input, font=1)
    text_button = Button(frame1, text='text\ninput ', bg='white', command=text_input, font=1)
    entry_text=Entry(frame1,text='enter request ', font=1, bg='white')

    hear_text = Label(frame2, text='I thing:', font=1, bg='white',
                         width=500, anchor='w')
    hear_text2 = Label(frame2, text=sluh, font=1, bg='white',
                       width=500, anchor='w')
    Recognized_text = Label(frame2, text='Recognized command: ', font=1, bg='white',
                      width=500, anchor='w')
    Recognized_text2= Label(frame2, text=command, font=1, bg='white',
                      width=500, anchor='w')
    open_report_butoon= Button(frame2, text='Open work report', bg='white', command=open_report, font=1,
                           height=button_cord[0], width=button_cord[1])
    inp_title =Label(frame1, text='input means:\n'+inp, font=1, bg='white',
                    relief=tk.RAISED, width=20,height=2)


    Exit_button = Button(frame3, text='Close', bg='white', command=Exit, font=1)
    program_version = Label(frame3, text=version, font=1)

    frame1.pack()
    start_button.grid(pady=2.5,row=1,column=1)
    settings_button.grid(row=3,column=1)
    comands_button.grid(pady=2.5,row=4,column=1)
    inp_title.grid(pady=2.5,row=5,column=1)
    frame1.grid_columnconfigure(0,minsize=60)
    frame1.grid_columnconfigure(1,minsize=280)
    frame1.grid_columnconfigure(2,minsize=60)



    frame2.pack()
    hear_text.place(x=0, y=30)
    hear_text2.place(x=0, y=56)
    Recognized_text.place(x=0, y=80)
    Recognized_text2.place(x=0, y=106)
    open_report_butoon.place(x=100, y=135)

    frame3.pack()
    Exit_button.place(x=0, y=0)
    program_version.place(x=370, y=10)

def main():
    otrisovka()
    window.mainloop()

main()


