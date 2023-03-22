import time
day,hour,minet,sekond=0,0,0,0

def sekundomer():
    global day,hour,minet,sekond
    while True:
        if sekond>=60:
            sekond=0
            minet=minet+1
        if minet>=60:
            minet=0
            hour=hour+1
        if hour>=24:
            hour=0
            day=day+1
        print(day,hour,minet,sekond)
        sekond = sekond+1
        time.sleep(1)

def main():
    sekundomer()
main()