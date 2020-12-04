from gtts import gTTS
from playsound import playsound
import subprocess

def textToVoice(texto, lang):
    fileName = "voz.mp3"
    try:
        file = gTTS(text=texto, lang=lang)
        file.save(fileName)
    except:
        print("Error al procesar voz.")
    
    try:
        playsound(fileName)
    except:
        print("Se produjo un error al reproducir voz.")
    
    # luego, borramos el archivo .mp3 creado:
    subprocess.call("rm -r " + fileName, shell=True)   # onlyLinux :D

texto = input("Ingrese texto para convertir a voz: ")

textToVoice(texto, "ES")
