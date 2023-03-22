import pyttsx3
from clock import Event
import datetime
import openpyxl
from openpyxl.styles import Font,PatternFill
from fuzzywuzzy import fuzz
import speech_recognition as sr
import time
import os
import cv2
import random
import webbrowser
import pyglet

start_time=datetime.datetime.now()
last_day=start_time.day
last_hour=start_time.hour
timer_hour,timer_min=0,0
stop,day2,hour2,min2,clock_chek,timer_chek,repeat_time,time_to_stay=0,0,0,0,0,0,0,0
save1,save2,stay_timer,sit_timer,sit_minet,stay_hour=0,0,0,0,0,0
clockes,music,clock=[],[],[]
command1,command2,voice='','',''

time1 = datetime.datetime.today()
book=openpyxl.reader.excel.load_workbook(filename='clock.xlsx')
clock_musik1='D:\рамиль\PycharmProjects\J.A.R.V.I.S\sound\будильник.wav'
book.active=0
list=book.active
g7=list['G1'].value
face_cascade_db = cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_eye.xml")
cap = cv2.VideoCapture(0)

# names=['пятница']
names=['джарвис',"жарвис","дарвис","арвис","дарвин","джанго","джаред","jahres","джара","джанис",'java','жанна']
delete=["пожалуйста","плиз","пж","ладно","эй","ой","мог", "бы", "ты","на","в","утра","дня","вечера",'эй',"хэй","ой",'сколько',"какие"]
Yes=["да","давай","ладно","одобряю","окей"]
No=['нет',"не","против","отказ"]
epic_game=['epic games','fortnite',"hitman","tabs","gta","arc",'арк']
# hours=["час","часы","часов","минута","минуту","минуты","секунд","сек","секунда","секунды","секунду"]
cmd={
    'times':['покажи','текущее', "время"," час","времени"],
    'clock':['будильник'],
    'timer':["таймер"],
    'sekundomer':["секундомер"],
    'information':["запомни","запиши"],
    'poisk':["найди","загугли","поищи"],
    'translete':['переведи',"переводиться"],
    'reminder':['добавь',"событие"],
    'saund_write':["голосовой","ввод"],
    'event':['событие'],
    'games':["запусти"],
    'planes':["планы"],
    'vk':['vk','вк'],
    'youtube':['youtube','ютуб'],
    'google_drive':['drive','драйв','disk','диск'],
    'google':['google','гугл'],
    'school':['успеваемость','школьный'],
    'find person':['кто','такая']
}

speaking_verbs={
    'poka':['пока'],
    'privet': ["привет", "доброе", "утро", "вечер", "день"],
    'spasibo': ['спасибо', "спс", "благодарю"]

}
ru_voice_id='HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\TokenEnums\RHVoice\Aleksandr'
rech=sr.Recognizer()
micro=sr.Microphone(device_index=0)


def Cmd_time():
    now = datetime.datetime.now()
    Speak("Сейчас " + str(now.hour) + ":" + str(now.minute))

def Cmd_poisk():
    global command1,voice
    print("save_information")
    print(command1)
    poisk=' '.join(command1)
    print(poisk)
    webbrowser.open('https://yandex.ru/search/?clid=2358536&text='+poisk+'&l10n=ru&lr=213')
    Speak("я нашел " + poisk)

def Cmd_translate():
    global command1, voice
    print("save_information")
    translate=' '.join(command1)
    webbrowser.open('https://translate.google.ru/?sl=en&tl=ru&text='+translate+'&op=translate')
    Speak("я перевел " + translate)

def Cmd_vk():
    Speak('я открыл вк')
    print('vk')
    webbrowser.open('https://vk.com/feed')

def Cmd_youtube():
    Speak('я открыл ютуб')
    print('youtube')
    webbrowser.open('https://www.youtube.com')

def Cmd_school():
    Speak('я открыл школьный портал')
    print('school')
    webbrowser.open('https://schools.school.mosreg.ru/marks.aspx?school=48734&index=5&tab=week&year=2021&month=3&day=25&homebasededucation=False')

def Cmd_google():
    Speak('я открыл гугл')
    print('google')
    webbrowser.open('https://www.google.ru')

def Cmd_google_drive():
    Speak('я открыл гугл диск')
    print('google_drive')
    webbrowser.open('https://drive.google.com/drive/my-drive')

def Cmd_saund_write():
    saund_write=''
    Speak('голосовой ввод активирован')
    while True:
        Speak('слушаю')
        voice=sluh(180)
        saund_write=saund_write+str(voice)+". "
        k=fuzz.ratio(voice,'стоп')
        if k>=80:
            Speak('голосовой ввод завершен')
            break
    while True:
        Speak('мне запомнить этот текст?')
        voice=sluh(3)
        otvet=NO_or_Yes(voice)
        if otvet==True:
            file=open('D:\рамиль\PycharmProjects\J.A.R.V.I.S\\txt_documents\\saund_write.txt','w')
            file.write(saund_write)
            Speak('я сохранил текст')
            break
        elif otvet==False:
            Speak('текст не сохранен')
            break
        else:
            pass
        print(saund_write)
        time.sleep(1)

def Cmd_games():
    game=command2
    print(game)
    game1=''
    for slovo in game:
        game1=game1+slovo+' '
    print(game1,":)")
    if game1=='':
        pass
    elif fuzz.ratio(game1,'overwatch')>=80 or fuzz.ratio(game1,'овервотч')>=80:
        os.startfile('C:\Program Files (x86)\Overwatch\\Overwatch Launcher.exe')
    elif game1=='майнкрафт' or game1=='minecraft':
        os.startfile('C:\\Users\Ramil\AppData\Roaming\.minecraft\\TLauncher.exe')
    elif game1=='браузер':
        os.startfile('C:\\Users\Ramil\AppData\Local\Programs\Opera GX\\launcher.exe')
    elif game1=='валорант' or game1=='valorant':
        os.startfile('C:\Riot Games\Riot Client\\RiotClientServices.exe')
    elif game1=='стим' or game1=='steam':
        os.startfile('C:\Program Files (x86)\Steam\\steam.exe')
    for game2 in epic_game:
        k=fuzz.ratio(game1,game2)
        if k>=80:
            os.startfile('C:\Program Files (x86)\Epic Games\Launcher\Portal\Binaries\Win32\\EpicGamesLauncher.exe')
            break

def Cmd_new_event():
    print(command2)
    Speak('какое событие на этот раз ?')
    voise=sluh(7)
    buf_command=voise.strip()
    buf_command1=delete1(buf_command)
    
    
def checker():
    print('')
    start_event=Event.cheker('gg')
    if start_event!=[]:
        print('')
        print(start_event,":)")
        opisanie_events=Event.starter_events('gg',start_event)
        print('')
        for key in opisanie_events:
            all_event = opisanie_events[key]
            event_name=all_event[0]
            event_opisanie = all_event[1]
            event_audio=all_event[2]
            event_type = all_event[3]

            for event in opisanie_events[key]:
                print(event)
            if event_type == 'event':
                Speak('напоминаю, что время для события: '+event_name+', пришло')
                Speak(event_audio)
            elif event_type == 'clock':
                audio(clock_musik1)
                time.sleep(5)

def checker_timer():
    global last_day,last_hour
    now=datetime.datetime.now()
    if int(now.day)-int(last_day)==1:
        if int(now.hour) - int(last_hour) == 1:
            last_day=now.day
            last_hour=now.hour
            checker()

def audio(files):
    media = pyglet.media.load(files)
    media.play()

def Speak(what):
    print(what)
    speak_engine.say(what)
    speak_engine.runAndWait()
    speak_engine.stop()

def NO_or_Yes(predlog):
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

def sluh(limit):
    global voice, rech, micro, time1,cmd
    print(":)")
    voice=''
    with sr.Microphone() as sourse:
        rech.adjust_for_ambient_noise(sourse)
        audio = rech.listen(sourse)
        try:
            voice = (rech.recognize_google(audio, language="ru-RU")).lower()
        except(sr.UnknownValueError):
            pass
        except(TypeError):
            pass
        print(voice)
        return voice

def poisk_in_slovar(text,slovar):
    for slovo in text:
        for key in slovar:
            for sl in slovar[key]:
                k=fuzz.ratio(slovo,sl)
                if k>=75:
                    cmda=key
                    return cmda

def deletes(command):
    global command1,command2,voice
    print("deletes")
    command1 = command.split(' ')
    print(command1)
    command1=delete1(command1)
    if command1==None:
        print("это не мне")
        return False
    else:
        command2 = delete2(command1)
        if len(command2)<=0:
            Speak("что сэр")
            return False
        else:
            return command2

def delete1(command):
    index=0
    for slovo in command:
        for name in names:
            k = fuzz.ratio(slovo, name)
            if k >= 50:
                print(index)
                command.pop(index)
                return command
        index = index + 1
    return None

def delete2(command):
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

def recognize_cmd(command):
    print("recognize_cmd")
    print(command)
    kolvo_poisk = 0
    index = 0
    for slovo in command:
        for y in cmd:
            for slovo_cmd in cmd[y]:
                k = fuzz.ratio(slovo, slovo_cmd)
                if k >= 75:
                    kolvo_poisk = kolvo_poisk + 1
                    print(slovo_cmd, index,':)')
                    print(command)
                    command.pop(index)
                    print(command)
                    commanda = y
        index = index + 1
    if kolvo_poisk >= 1:
        print(slovo,slovo_cmd)
        print(command)
        return commanda

def execute_cmd(command):
    print("execute_cmd")
    print(command)
    if command == 'times': # сказать текущее время
        Cmd_time()
    elif command=='poisk': # найди что-то
        Cmd_poisk()
    elif command=='translete': # переведи сто-то
        Cmd_translate()
    elif command == 'vk':  # открывает вк
        Cmd_vk()
    elif command == 'youtube':  # открывает ютуб
        Cmd_youtube()
    elif command == 'google':  # открывает гугл
        Cmd_google()
    elif command == 'school':  # открывает школьный портал
        Cmd_school()
    elif command == 'google_drive':  # открывает диск
        Cmd_google_drive()
    elif command=='saund_write': #  голосовой ввод
        Cmd_saund_write()
    elif command=='games': #  запускает приложения
        Cmd_games()
    elif command=='planes': #  планы на сегодня
        Cmd_games()
    elif command == 'event':  # новые события
        Cmd_new_event()

    command = ''

def main():
    global voice,rech,micro,time1,last_day
    sluh(4) #voice= input()
    cmda=deletes(voice)
    if cmda==False:
        pass
    else:
        cmda=recognize_cmd(cmda)
        execute_cmd(cmda)
    checker_timer()

print("start")
speak_engine = pyttsx3.init()
speak_engine.setProperty('voice', ru_voice_id)
checker()
Speak("слушаю сэр")

while True:
    main()
