from time import sleep
import speech_recognition as sr
from gtts import gTTS
import pygame
import webbrowser


def take_commands():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Ouvindo...')
        r.pause_threshold = 0.7
        audio = r.listen(source)
        try:
            print("Reconhecendo...")
            Query = r.recognize_google(audio, language='pt-BR')
            print("a consulta é:'", Query, "'")
        except Exception as e:
            print(e)
            print("Repita por favor")
            return "None"

    return Query


def Speak(audio):
    speech = gTTS(audio, lang='pt')
    speech.save('mp3_fp.mp3')
    pygame.init()
    pygame.mixer.music.load('mp3_fp.mp3')
    pygame.mixer.music.play()


if __name__ == '__main__':
    while True:
        command = take_commands()
        if "sair" in command.lower():
            Speak("Claro senhor! como desejar. Até mais")
            sleep(5)
            break
        if "Muito Obrigado" in command.lower():
            Speak("Eu que agradeço!")
            sleep(5)
            break
        if "abrir navegador" in command:
            Speak("Abrindo navegador")
            webbrowser.open("https://google.com")
        if "hello" in command:
            Speak("Olá, tudo bem")
        if "bem e você" in command:
            Speak("Estou ótima!")
            sleep(1)
            Speak(" Qual função deseja?")
        if "Abrir YouTube" in command:
            Speak("Abrindo youtube")
            webbrowser.open("https://youtube.com")
        if "Música" in command:
            Speak("Executando Música")
            webbrowser.open("https://youtu.be/F64yFFnZfkI")
