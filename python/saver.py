import  datetime
file=open('D:\рамиль\PycharmProjects\J.A.R.V.I.S\\txt_documents\\users time.txt','w')
for i in range(2):
    now=datetime.datetime.now()
    file.write('the user got up from the computer '+str(now.year)+'.'+str(now.month)+'.'+str(now.day)+'.'+str(now.hour)+'.'+str(now.minute)+'\n')
file.close()