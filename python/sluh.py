import pyttsx3
from fuzzywuzzy import fuzz
import speech_recognition as sr
import pyglet

timer_hour,timer_min=0,0
stop,day2,hour2,min2,clock_chek,timer_chek,repeat_time,time_to_stay=0,0,0,0,0,0,0,0
save1,save2,stay_timer,sit_timer,sit_minet,stay_hour=0,0,0,0,0,0
clockes,music,clock=[],[],[]
command1,command2,voice='','',''

names=['джарвис',"жарвис","дарвис","арвис","дарвин","джанго","джаред","jahres","джара","джанис",'java']
delete=["пожалуйста","плиз","пж","ладно","эй","ой","не мог бы ты","мог бы ты","на","в","утра","дня","вечера",'эй',"хэй","ой",'сколько',"какие"]

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
    'games':["запусти"],
    'planes':["планы"],
    'vk':['vk','вк'],
    'youtube':['youtube','ютуб'],
    'google_drive':['drive','драйв','disk','диск'],
    'google':['google','гугл'],
    'school':['успеваемость','школьный'],
    'find person':['кто','такая']
}

ru_voice_id='HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\TokenEnums\RHVoice\Aleksandr'
rech=sr.Recognizer()
micro=sr.Microphone(device_index=1)

def audio(files):
    media = pyglet.media.load(files)
    media.play()

def Speak(what):
    print(what)
    speak_engine.say(what)
    speak_engine.runAndWait()
    speak_engine.stop()

def sluh(limit):
    global voice, rech, micro, time1,cmd
    print(":)")
    voice=''
    with sr.Microphone() as sourse:
        rech.adjust_for_ambient_noise(sourse)
        audio = rech.listen(sourse, phrase_time_limit=limit)
        try:
            voice = (rech.recognize_google(audio, language="ru-RU")).lower()
        except(sr.UnknownValueError):
            pass
        except(TypeError):
            pass
        print(voice)
        return voice

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
            if k >= 75:
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
    command = ''

def main():
    global voice,rech,micro,time1
    voice= input() #sluh(4)
    cmda=deletes(voice)
    if cmda==False:
        pass
    else:
        cmda=recognize_cmd(cmda)
        execute_cmd(cmda)

print("start")
speak_engine = pyttsx3.init()
speak_engine.setProperty('voice', ru_voice_id)
Speak("слушаю сэр")

while True:
    main()