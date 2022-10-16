import subprocess
from gtts import gTTS
from playsound import playsound


def delete_file(filename: str):
    """delete file by name"""
    subprocess.call(f"rm -r {filename}", shell=True)


def text_to_voice(text: str, lang: str):
    """
    convert text to voice
    """
    filename = "voz.mp3"
    try:
        file = gTTS(text=text, lang=lang)
        file.save(filename)
    except:
        print("Error al procesar voz")
        raise

    try:
        playsound(filename)
    except:
        print("Se produjo un error al reproducir voz.")
        raise

    delete_file(filename)


def main():
    """main method"""
    text = input("Ingrese texto para convertir a voz: ")

    if text:
        text_to_voice(text, "ES")


if __name__ == "__main__":
    main()
