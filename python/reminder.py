import datetime
from fuzzywuzzy import fuzz
import time
events=[]
number=0
week_days=['понедельник','вторник','среда','четверг','суббота','воскресенье']

week={
    'понедельник':[],
    'вторник':[],
    'среда':[],
    'четверг':[],
    'пятница':[],
    'суббота':[],
    'воскресенье':[]
}
delete=['добвавь',"объект","событие","на"]
class Event:
    def __init__(self, name, day, hour, number):
        self.name = name
        self.day = day
        self.hour = hour
        self.number = number

    def create_event(self, name, day, hour):
        global number
        for days in week:
            k=fuzz.ratio(days,day)
            if k>=80:
                week[days].append(Event(name,day,hour,number))
        number = number + 1
        Event.sorting('event')

    def sorting(self):
        print(week)
        buf=[]
        for days in week:
            for event in week[days]:
                buf.append(event.hour)
            week[days]=sorted(week[days],key=lambda event: event.hour)

    def checer(self):
        file = open('D:\рамиль\PycharmProjects\J.A.R.V.I.S\\events.txt', 'w')
        for day in week:
            for event in week[day]:
                file.write(str(event.name)+' '+str(event.day)+' '+str(event.hour)+' '+str(event.number))
                file.write('\n')
                print(str(event.name)+' '+str(event.day)+' '+str(event.hour)+' '+str(event.number))


        while True:
            file = open('D:\рамиль\PycharmProjects\J.A.R.V.I.S\\команда.txt','r')
            now = datetime.datetime.now()
            x = datetime.datetime(now.year, now.month, now.day)
            filey = open('D:\рамиль\PycharmProjects\J.A.R.V.I.S\\start events.txt', 'w')
            if x.strftime("%w")=='1':
                for event in week['понедельник']:
                    if event.hour==now.hour:
                        text = 'сэр, у вас на '+str(event.hour)+' часов заплонированно событие, '+ str(event.name)
                        filey.write(text)
                        print(event.name)
            elif x.strftime("%w")=='2':
                for event in week['вторник']:
                    if int(event.hour)==int(now.hour):
                        text = 'сэр, у вас на '+str(event.hour)+' часов заплонированно событие, '+ str(event.name)
                        filey.write(text)
                        filey.write('\n')
                        print(event.name)
            elif x.strftime("%w")=='3':
                for event in week['среда']:
                    if event.hour==now.hour:
                        text = 'сэр, у вас на '+str(event.hour)+' часов заплонированно событие, '+ str(event.name)
                        filey.write(text)
                        print(event.name)
            elif x.strftime("%w")=='4':
                for event in week['четверг']:
                    if event.hour==now.hour:
                        text = 'сэр, у вас на '+str(event.hour)+' часов заплонированно событие, '+ str(event.name)
                        filey.write(text)
                        print(event.name)
            elif x.strftime("%w")=='5':
                for event in week['пятница']:
                    if event.hour==now.hour:
                        text = 'сэр, у вас на '+str(event.hour)+' часов заплонированно событие, '+ str(event.name)
                        filey.write(text)
                        print(event.name)
            elif x.strftime("%w")=='6':
                for event in week['суббота']:
                    if event.hour==now.hour:
                        text = 'сэр, у вас на '+str(event.hour)+' часов заплонированно событие, '+ str(event.name)
                        filey.write(text)
                        print(event.name)
            elif x.strftime("%w")=='7':
                for event in week['воскресенье']:
                    if event.hour==now.hour:
                        text = 'сэр, у вас на '+str(event.hour)+' часов заплонированно событие, '+ str(event.name)
                        filey.write(text)
                        print(event.name)
            time.sleep(10)

    def create_object(self,cmd):
        global day, hour, name, number
        cmd = cmd.split(' ')
        print(cmd)
        index2 = 0
        for x in delete:
            for slovo in cmd:
                k = fuzz.ratio(slovo, x)
                if k >= 80:
                    cmd.pop(index2)
                index2 = index2 + 1
            index2 = 0

        index2 = 0
        for slovo in cmd:
            for x in week_days:
                k = fuzz.ratio(slovo, x)
                if k >= 80:
                    day = x
                    cmd.pop(index2)
            index2 = index2 + 1

        x=len(cmd)
        x=int(x)-1
        y=cmd[x]
        if y=='':
            x=int(x)-1
            y = cmd[x]
        cmd.pop(x)
        y=y.split(':')
        y.pop(1)
        x=''
        for i in y:
            x=x+i
        hour=int(x)

        names = []
        name = ''
        for slovo in cmd:
            names.append(slovo)
        for slovo in names:
            name = name + str(slovo) + ' '
        print(name, day, hour, number)
        Event.create_event('event',name,day,hour)

def main():
    file = open('D:\рамиль\PycharmProjects\J.A.R.V.I.S\\команда.txt', 'r')
    voice=file.readline()
    print('voice')
    Event.create_object('event',voice)
    print('event')
    print(week)
    for event in events:
        print(event.name, event.day, event.hour, event.number)
    print('events')
    Event.checer('event')

main()
