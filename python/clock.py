import openpyxl
import datetime
from fuzzywuzzy import fuzz
from openpyxl.styles import Font,PatternFill
book=openpyxl.reader.excel.load_workbook(filename='clock.xlsx')
now=datetime.datetime.now()
print(now)
book.active=0
list=book.active
g7=list['G1'].value
clock_musik1='D:\рамиль\PycharmProjects\J.A.R.V.I.S\sound\будильник.wav'
verbs=['поставь','включи','запусти']

class Event():
    def __init__(self,name,year,month,day,hour,min,audio,type,opisanie=None):
        self.name = name
        self.year = year
        self.month = month
        self.day=day
        self.hour = hour
        self.min = min
        self.audio = audio
        self.opisanie = opisanie
        self.type = type

    def __str__(self):
        return "Имя: {} \n Описание: {} \n Тип: {} \n Год: {} \n Месяц: {} \n День: {} \n Час: {} \n Минута: {} \n Аудио: {} \n".format(
            self.name, self.opisanie,self.type,self.year,self.month,self.day,self.hour,self.min,self.audio)

    def clock_creater(self,command):
        print(command)
        time=Event.obrabotka('gg',command)
        print(time)
        hour,minet=Event.time_obrabotka('gg',time)
        print(hour,minet)
        now=datetime.datetime.now()
        if now.hour<=24 and now.hour>=12:
            day=int(now.day)+1
        else:
            day=int(now.day)
        print(day)
        Event.creater('gg','clock',int(now.year),int(now.month),day,hour,minet,clock_musik1,'clock','go up')

    def obrabotka(self,command):
        index=0
        for slovo in command:
            for verb in verbs:
                k=fuzz.ratio(slovo,verb)
                if k>=75:
                    command.pop(index)
                    time=command
                    return time
            index=+1

    def time_obrabotka(self,time):
        time = time[0]
        time = time.split(':')
        hour = int(time[0])
        minet = int(time[1])
        return hour,minet


    def creater(self,name,year,month,day,hour,min,audio,type,opisanie=None):
        event1=Event(name,year,month,day,hour,min,audio,type,opisanie)
        print(event1)
        for stolbic in range(1, 101):
            print(stolbic, 0)
            kletka = list[stolbic][0].value
            print(kletka, ':)')
            if kletka == None:
                print("kletka was detected")
                list[stolbic][0].value =event1.name
                list[stolbic][1].value = event1.opisanie
                list[stolbic][2].value = event1.year
                list[stolbic][3].value = event1.month
                list[stolbic][4].value = event1.day
                list[stolbic][5].value = event1.hour
                list[stolbic][6].value = event1.min
                list[stolbic][7].value = event1.audio
                list[stolbic][8].value = event1.type
                break

    def recognition_event(self,command):
        time=command
        name=[]
        index=0
        for slovo in command:
            print(slovo)
            print(command)
            if slovo!='на':
                name.append(slovo)
            else:
                break
        for slovo in command:
            print(slovo)
            print(command)
            if slovo != 'на':
                pass
            else:
                break
        print('')
        print(command)
        print(time)
        print(name)


    def all_events(self):
        for stolbic in range(2, 101):
            for acheka in range(0,8):
                kletka = list[stolbic][acheka].value
                if kletka == None:
                    break
                else:
                    print(kletka)
                if acheka==5:
                    print('\n')

    def cheker(self):
        start_event=[]
        now = datetime.datetime.now()
        for stolbic in range(2, 101):
            kletka = list[stolbic][1].value
            if kletka == None:
                break
            else:
                year = list[stolbic][2].value
                print(year)
                if now.year == int(year):
                    month = list[stolbic][3].value
                    print(month)
                    if now.month == int(month):
                        day = list[stolbic][4].value
                        print(day)
                        if now.day==int(day):
                            hour = list[stolbic][5].value
                            print(hour)
                            if now.hour == int(hour):
                                start_event.append(int(stolbic))
                                print(start_event,":)")
                                # min = list[stolbic][5].value
                                # print(min)
                                # if now.minute == int(min):
                                # name=list[stolbic][0].value
                                # opisanie= list[stolbic][1].value
                                # audio = list[stolbic][6].value
                                # type = list[stolbic][7].value
        print(start_event)
        return start_event

    def starter_events(self,start_event):
        opisanie_events={}
        opisanie_event=[]
        if start_event!=None:
            for stolbic in start_event:
                name = list[stolbic][0].value
                opisanie= list[stolbic][1].value
                audio = list[stolbic][6].value
                type = list[stolbic][7].value
                opisanie_event.append(name)
                opisanie_event.append(opisanie)
                opisanie_event.append(audio)
                opisanie_event.append(type)
                print(opisanie_event)
                opisanie_events[stolbic]=opisanie_event
                opisanie_event=[]
        print(opisanie_events)
        return opisanie_events

# start_event=Event.cheker('gg')
# opisanie_events=Event.starter_events('gg',start_event)
# print(opisanie_events)
Event.recognition_event('gg',['выкинуть',"мусор","на","30.05"])
book.save('clock.xlsx')
book.close()
