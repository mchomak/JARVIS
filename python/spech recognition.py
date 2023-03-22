import speech_recognition as sr
kolvo=int(input())
for i in range(kolvo):
    name=str(i)
    sample_audio = sr.AudioFile('D:\рамиль\PycharmProjects\J.A.R.V.I.S\\audio\\'+name+'.wav')
    print('name:'+ name+'.wav')
    rech=sr.Recognizer()
    print('obraborka')
    with sample_audio as audio_file:
        rech.adjust_for_ambient_noise(audio_file)
        audio_content = rech.record(audio_file)

    voice = (rech.recognize_google(audio_content, language="ru-RU")).lower()
    print('number '+str(i)+': '+voice)