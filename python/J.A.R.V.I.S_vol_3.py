# voice-о что он услышал или записал
# command1- весь текст в массиве без имени
# command2-весь текст без лишних слов
# command3- ключ команды которую надо исполнить
#  Джарвис сколько время
import pyttsx3
from clock import Event
from any_module import Moduls
import speech_recognition as sr
import os
import os.path
from os import path
import json
from any_module import cmd,speaking_verbs,info,micro

names=info['names']
delete=info['delete']
delete_toka=info['delete_toka']
Yes=info['Yes']
No=info['No']
epic_game=info['epic_game']

directory=str(os.getcwd())
jarvis_d=directory+r'\data\J.A.R.V.I.S_vol_3.exe'
otchet_for_work_d=directory+r'\data\otchet_for_work.txt'
work_data_d=directory+r'\data\work_data.txt'
box_commands_d=directory+r'\data\box_commands.json'
# hours=["час","часы","часов","минута","минуту","минуты","секунд","сек","секунда","секунды","секунду"]

websites={
    'vk':'https://vk.com/feed',
    'youtube':'https://www.youtube.com',
    'school':'https://schools.school.mosreg.ru/marks.aspx?school=48734&index=5&tab=week&year=2021&month=3&day=25&homebasededucation=False',
    'google':'https://www.google.ru',
    'google_drive':'https://drive.google.com/drive/my-drive'
}
# проверяем есть ли файл в директории
def make_data_file():
    if path.exists(work_data_d)==False:
        with open(work_data_d, 'w') as work_data:
            work_data.write('')
            work_data.close()

    if path.exists(otchet_for_work_d) == False:
        with open(otchet_for_work_d, 'w') as otchet_for_work:
            otchet_for_work.write('')
            otchet_for_work.close()


    with open(work_data_d, 'r',encoding="utf-8") as work_data:
        inp = work_data.readline()
        start = work_data.readline()
        text = work_data.readline()

    with open(box_commands_d,'w',encoding="utf-8") as box_commands:
        json.dump(cmd, box_commands, indent=4, ensure_ascii=False)

def execute_cmd(command):
    print("execute_cmd")
    print(command)
    if command == 'times': # сказать текущее время
        jarvis.Cmd_time()
    elif command=='poisk': # найди что-то
        jarvis.Cmd_poisk()
    elif command=='translete': # переведи сто-то
        jarvis.Cmd_translate()
    elif command == 'websites':  # открывает вк
        jarvis.open_website(command1)
    elif command=='saund_write': #  голосовой ввод
        jarvis.Cmd_saund_write()
    elif command=='games': #  запускает приложения
        jarvis.Cmd_games()
    elif command=='planes': #  планы на сегодня
        jarvis.Cmd_games()
    command = ''

def Exit_save():
    pass

def after_work(inp,text,command):
    with open(work_data_d, 'w', encoding="utf-8") as work_data:
        work_data.write(str(inp)+'\n')
        work_data.write('1\n')
        work_data.write('\n')
        work_data.write(str(command) + '\n')

    if text!='':
        with open(otchet_for_work_d, 'a', encoding="utf-8") as otchet_for_work:
            otchet_for_work.write(str(text) + '\n')
            otchet_for_work.write(str(command) + '\n')

def proverki():
    global work_data_d
    with open(work_data_d, 'r',encoding="utf-8") as work_data:
        inp = work_data.readline()
        start = work_data.readline()
        text = work_data.readline()
        if start==1:
            pass
        else:
            Exit_save()
    return inp,start,text

# предворительная подготовка
def fist_main():
    global speak_engine,start,jarvis
    jarvis = Moduls()
    # создаем необхадимые файлы
    make_data_file()
    # Moduls.checker('gg')
    jarvis.Speak( "слушаю сэр")
    inp, start, text = proverki()
    inp = inp.replace(' ', '')
    inp = inp.replace('\n', '')
    if inp.isdigit():
        inp = int(inp)
    print("start")
    return inp, start, text

# начало работы
def main(inp, start, text):
    global rech,micro,time1,last_day
    global voice,command1,command2,command3
    if inp==1:
        voice=jarvis.sluh(limit=4)
    elif inp==0:
        voice = text
        voice=voice.replace('\n','')
    if voice!='':
        command2,command1=jarvis.deletes(command=voice)
        if command2==False:
            command3='None'
            after_work(inp, voice,command3)
        else:
            command3=jarvis.recognize_cmd(command=command2)
            execute_cmd(command3)
            after_work(inp, voice,command3)
        # Moduls.checker_timer('gg')
    else:
        pass
    return start

# начало
inp, start, text=fist_main()
while True:
    start=main(inp, start, text)
    if start==0:
        break

