import pyttsx3
from clock import Event
import datetime
import openpyxl
from openpyxl.styles import Font,PatternFill
from fuzzywuzzy import fuzz
import speech_recognition as sr
import time
import os
import webbrowser
import pyglet
import json
# cmd={
#     'times':['покажи','текущее', "время"," час","времени"],
#     'clock':['будильник'],
#     'timer':["таймер"],
#     'sekundomer':["секундомер"],
#     'information':["запомни","запиши"],
#     'poisk':["найди","загугли","поищи"],
#     'translete':['переведи',"переводиться"],
#     'reminder':['добавь',"событие"],
#     'saund_write':["голосовой","ввод"],
#     'event':['событие'],
#     'games':["запусти"],
#     'planes':["планы"],
#     'websites':['сайт'],
#     'find person':['кто','такая']
# }
start_time=datetime.datetime.now()
last_day=start_time.day
last_hour=start_time.hour

directory = str(os.getcwd())
clock_musik1='D:\рамиль\PycharmProjects\J.A.R.V.I.S\sound\будильник.wav'
new_box_commands_d=directory+'//data//new_box_commands.json'

info={
    'names':['джарвис',"жарвис","дарвис","арвис","дарвин","джанго","джаред","jahres","джара","джанис",'java','жанна'],
    'delete':["пожалуйста","плиз","пж","ладно","эй","ой","мог", "бы", "ты","на","в","утра","дня","вечера",'эй',"хэй","ой",'сколько',"какие"],
    'delete_toka':['"',"''",'?','!','.',','],
    'Yes':["да","давай","ладно","одобряю","окей"],
    'No':['нет',"не","против","отказ"],
    'epic_game':['epic games','fortnite',"hitman","tabs","gta","arc",'арк'],
}
# hours=["час","часы","часов","минута","минуту","минуты","секунд","сек","секунда","секунды","секунду"]

speaking_verbs={
    'poka':['пока'],
    'privet': ["привет", "доброе", "утро", "вечер", "день"],
    'spasibo': ['спасибо', "спс", "благодарю"]
}

names=info['names']
delete=info['delete']
delete_toka=info['delete_toka']
Yes=info['Yes']
No=info['No']
epic_game=info['epic_game']

ru_voice_id='HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\TokenEnums\RHVoice\Aleksandr'
micro = sr.Microphone(device_index=0)
rech=sr.Recognizer()
speak_engine = pyttsx3.init()
speak_engine.setProperty('voice', ru_voice_id)

with open(new_box_commands_d, 'r',encoding="utf-8") as new_box_commands:
    cmd = json.load(new_box_commands)

class Moduls():
    def __init__(self,command1='',command2='',command3='',voice=''):
        self.command1=command1
        self.command2=command2
        self.command3=command3
        self.voice=voice

    # открытие сайтов
    def open_website(self,name):
        Moduls.Speak(self, 'я открыл вк')
        print('open_application')
        webbrowser.open(name)

    # сохранение информации
    def Cmd_poisk(self):
        print("save_information")
        print(self.command1)
        poisk = ' '.join(self.command1)
        print(poisk)
        webbrowser.open('https://yandex.ru/search/?clid=2358536&text=' + poisk + '&l10n=ru&lr=213')
        Moduls.Speak(self,"я нашел " + poisk)

    # время
    def Cmd_time(self):
        now = datetime.datetime.now()
        Moduls.Speak(self,"Сейчас " + str(now.hour) + ":" + str(now.minute))

    # перевод с английского
    def Cmd_translate(self):
        print("save_information")
        translate = ' '.join(self.command1)
        webbrowser.open('https://translate.google.ru/?sl=en&tl=ru&text=' + translate + '&op=translate')
        Moduls.Speak(self,"я перевел " + translate)

    # проверка событий 1
    def checker_timer(self):
        global last_day, last_hour
        now = datetime.datetime.now()
        if int(now.day) - int(last_day) == 1:
            if int(now.hour) - int(last_hour) == 1:
                last_day = now.day
                last_hour = now.hour
                Moduls.checker(self)

    # проверка событий 2
    def checker(self):
        print('')
        start_event = Event.cheker('gg')
        if start_event != []:
            print('')
            print(start_event, ":)")
            opisanie_events = Event.starter_events('gg', start_event)
            print('')
            for key in opisanie_events:
                all_event = opisanie_events[key]
                event_name = all_event[0]
                event_opisanie = all_event[1]
                event_audio = all_event[2]
                event_type = all_event[3]
                for event in opisanie_events[key]:
                    print(event)
                Moduls.events_deystvie(self,event_name,event_opisanie,event_audio,event_type)

    # напоминалка событий
    def events_deystvie(self,event_name,event_opisanie,event_audio,event_type):
        if event_type == 'event':
            Moduls.Speak(self,'напоминаю, что время для события: ' + event_name + ', пришло')
            Moduls.Speak(self,event_audio)
        elif event_type == 'clock':
            Moduls.audio(self,clock_musik1)
            time.sleep(5)

    # олоссовой ввод
    def Cmd_saund_write(self):
        saund_write = ''
        Moduls.Speak(self,'голосовой ввод активирован')
        while True:
            Moduls.Speak(self,'слушаю')
            voice = Moduls.sluh(self,180)
            saund_write = saund_write + str(voice) + ". "
            k = fuzz.ratio(voice, 'стоп')
            if k >= 80:
                Moduls.Speak(self,'голосовой ввод завершен')
                break
        while True:
            Moduls.Speak(self,'мне запомнить этот текст?')
            voice = Moduls.sluh(self,3)
            otvet = Moduls.NO_or_Yes(self,voice)
            if otvet == True:
                file = open('D:\рамиль\PycharmProjects\J.A.R.V.I.S\\txt_documents\\saund_write.txt', 'w')
                file.write(saund_write)
                Moduls.Speak(self,'я сохранил текст')
                break
            elif otvet == False:
                Moduls.Speak(self,'текст не сохранен')
                break
            else:
                pass
            print(saund_write)
            time.sleep(1)

    # открытие игр
    def Cmd_games(self):
        game = self.command2
        print(game)
        game1 = ''
        for slovo in game:
            game1 = game1 + slovo + ' '
        print(game1, ":)")
        if game1 == '':
            pass
        elif fuzz.ratio(game1, 'overwatch') >= 80 or fuzz.ratio(game1, 'овервотч') >= 80:
            os.startfile('C:\Program Files (x86)\Overwatch\\Overwatch Launcher.exe')
        elif game1 == 'майнкрафт' or game1 == 'minecraft':
            os.startfile('C:\\Users\Ramil\AppData\Roaming\.minecraft\\TLauncher.exe')
        elif game1 == 'браузер':
            os.startfile('C:\\Users\Ramil\AppData\Local\Programs\Opera GX\\launcher.exe')
        elif game1 == 'валорант' or game1 == 'valorant':
            os.startfile('C:\Riot Games\Riot Client\\RiotClientServices.exe')
        elif game1 == 'стим' or game1 == 'steam':
            os.startfile('C:\Program Files (x86)\Steam\\steam.exe')
        for game2 in epic_game:
            k = fuzz.ratio(game1, game2)
            if k >= 80:
                os.startfile('C:\Program Files (x86)\Epic Games\Launcher\Portal\Binaries\Win32\\EpicGamesLauncher.exe')
                break

    # ет или да?
    def NO_or_Yes(self,predlog):
        predlog = predlog.split(' ')
        for slovo in predlog:
            for da in Yes:
                k = fuzz.ratio(slovo, da)
                if k >= 80:
                    return True
        for slovo in predlog:
            for no in No:
                k = fuzz.ratio(slovo, no)
                if k >= 80:
                    return False
        return None

    # слух
    def sluh(self,limit):
        print('sluh')
        self.voice = ''
        with sr.Microphone() as sourse:
            rech.adjust_for_ambient_noise(sourse)
            audio = rech.listen(sourse, phrase_time_limit=limit)
            try:
                self.voice = (rech.recognize_google(audio, language="ru-RU")).lower()
            except(sr.UnknownValueError):
                pass
            except(TypeError):
                pass
            print('вы сказали: '+self.voice)
            return self.voice

    # очистка 1
    def delete1(self,command):
        index = 0
        for slovo in command:
            for name in names:
                k = fuzz.ratio(slovo, name)
                if k >= 50:
                    print(index)
                    command.pop(index)
                    return command
            index = index + 1
        return None

    # очистка 2
    def delete2(self,command):
        index = 0
        for slovo in command:
            for dell in delete:
                k = fuzz.ratio(slovo, dell)
                if k >= 75:
                    command.pop(index)
                    break
            index = index + 1
        index = 0

        return command

    # очистка 3
    def deletes(self,command):
        print("deletes")
        self.command1 = command.split(' ')
        print(self.command1)
        self.command1 = Moduls.delete1(self,self.command1)
        if self.command1 == None:
            print("это не мне")
            return False,False
        else:
            self.command2 = Moduls.delete2(self,self.command1)
            if len(self.command2) <= 0:
                Moduls.Speak(self,"что сэр")
                return False,False
            else:
                return self.command2,self.command1

    # говорить
    def Speak(self,what):
        print(what)
        speak_engine.say(what)
        speak_engine.runAndWait()
        speak_engine.stop()

    # воспроизводить аудио
    def audio(self,files):
        media = pyglet.media.load(files)
        media.play()

    # пределние команды
    def recognize_cmd(self,command):
        print("recognize_cmd")
        print(command)
        kolvo_poisk = 0
        index = 0
        commanda=''
        for slovo in command:
            for y in cmd:
                for slovo_cmd in cmd[y]:
                    k = fuzz.ratio(slovo, slovo_cmd)
                    if k >= 75:
                        kolvo_poisk = kolvo_poisk + 1
                        print(slovo_cmd, index, ':)')
                        command.pop(index)
                        commanda = y
            index = index + 1
            if kolvo_poisk >= 1:
                return commanda

















