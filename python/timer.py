import datetime
import pyglet
import time
from fuzzywuzzy import fuzz
file=open('D:\рамиль\PycharmProjects\J.A.R.V.I.S\\timer.txt','r')
hours=["час","часы","часов"]
minets=["минута","минуту","минуты"]
sekonds=["секунд","сек","секунда","секунды","секунду"]
letters=['й', 'ц', 'у', 'к', 'е', 'н', 'г', 'ш', 'щ', 'з', 'х', 'ъ', 'ф', 'ы', 'в', 'а', 'п', 'р', 'о', 'л', 'д', 'ж', 'э', 'я', 'ч', 'с', 'м', 'и', 'т', 'ь', 'б', 'ю', 'ё']
integer={"один":1,"два":2,"три":3,"четыре":4,"пять":5,
        "шесть":6,"семь":7,"восемь":8,"девать":9,"десять":10,"ноль":0}

voice=file.readline()
timer_hour,timer_min,timer_sek=0,0,0

def poisk_slov(text,slova):
    global index_slova
    text = voice.split(' ')
    print(text)
    for slov_text in text:
        for slovo in slova:
            k=fuzz.ratio(slovo, slov_text)
            if (k >= 75):
                index_slova=voice.find(slov_text)
                print(slov_text)
                return True

def audio(files):
    media = pyglet.media.load(files)
    media.play()

def delete():
    global timer_clock
    buf=False
    text = voice.split(' ')
    for slov_text in text:
        for inter in integer:
            k = fuzz.ratio(slov_text, inter)
            if k>=65:
                timer_clock=integer[inter]
                buf=True
                break
    if buf == False:
        print(index_slova)
        timer_clock = voice[(index_slova - 5): (index_slova)]
        print(timer_clock)
        timer_clock = timer_clock.replace(' ', '')
        print(timer_clock)
        for i in letters:
            timer_clock = timer_clock.replace(i, '')
        timer_clock = int(timer_clock)
        print(timer_clock)

def timer():
    global timer_hour, timer_min, ost_sek, timer_sek,index_slova,timer_clock
    now = datetime.datetime.today()

    if poisk_slov(voice,hours)==True:
        delete()
        timer_hour=timer_clock
        timer_hour = now.hour + timer_hour
        print("hour")
    else:
        timer_hour=now.hour

    if poisk_slov(voice,minets)==True:
        delete()
        timer_min=timer_clock
        timer_min = now.minute + timer_min
        print("minet")
    else:
        timer_min = now.minute

    if poisk_slov(voice,sekonds)==True:
        delete()
        timer_sek=timer_clock
        print(timer_sek)
        timer_sek = now.second + timer_sek
        print(timer_sek)
        print("sekond")
    else:
        timer_sek=now.second
    timer_cheker(timer_hour,timer_min,timer_sek)

def timer_cheker(timer_hour,timer_min,timer_sek):
    while True:
        file = open('D:\рамиль\PycharmProjects\J.A.R.V.I.S\\timer.txt', 'r')
        stop = file.readline()
        if stop == '1':
            break
        now = datetime.datetime.today()
        print(timer_hour,timer_min,timer_sek)
        print(now.hour, now.minute, now.second)
        print(' ')
        if now.hour==timer_hour:
            if now.minute==timer_min:
                if now.second==timer_sek:
                    audio('D:\рамиль\PycharmProjects\J.A.R.V.I.S\sound\будильник.wav')
                    while True:
                        file = open('D:\рамиль\PycharmProjects\J.A.R.V.I.S\\timer.txt', 'r')
                        stop=file.readline()
                        time.sleep(1)
                        if stop=='1':
                            break
                    break
        time.sleep(1)

def main():
    timer()
main()