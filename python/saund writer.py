from fuzzywuzzy import fuzz
import speech_recognition as sr

for audio in range(23,26):
    sample_audio = sr.AudioFile('D:\рамиль\PycharmProjects\J.A.R.V.I.S\\audio\\'+str(audio)+'.wav')
    print(audio)
    rech=sr.Recognizer()

    with sample_audio as audio_file:
        rech.adjust_for_ambient_noise(audio_file)
        audio_content = rech.record(audio_file)

    voice = (rech.recognize_google(audio_content, language="ru-RU")).lower()

    voice=voice.strip()
    voice=voice.capitalize()
    print(voice)