from gtts import gTTS
from playsound import playsound

audio= gTTS("Bom dia, seu danado",lang='pt')
audio.save('amigo.mp3')
playsound('amigo.mp3')