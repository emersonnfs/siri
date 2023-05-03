import os

import speech_recognition as sr
from gtts import gTTS
from playsound import playsound

microfone= sr.Microphone()
reconhecedor = sr.Recognizer()

with microfone as mic:
    reconhecedor.adjust_for_ambient_noise(mic)
    audio = gTTS("Quer ouvir Take 5?", lang='pt')
    audio.save('msg.mp3')
    playsound('msg.mp3')
    print("Quer ouvir Take 5?")
    audio= reconhecedor.listen(mic)
    print("Loading")
    texto = reconhecedor.recognize_google(audio ,language='pt')
    print(texto)
    lista=['OK', 'PODE SER','SIM','TUDO BEM','QUERO','BORA']
    if texto.upper() in lista:
        audio= gTTS("ok, abrindo a música...", lang='pt')
        audio.save('msg2.mp3')
        playsound('msg2.mp3')
        print("ok, abrindo a música...")
        os.system('musica.mp3')
    else:
        audio= gTTS("Tudo bem, ate")
        audio.save('msg3.mp3')
        playsound('msg3.mp3')
        print("Tudo bem, ate")