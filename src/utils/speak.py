from TTS.api import TTS
import sounddevice as sd

def speak(text):
    tts = TTS("tts_models/de/thorsten/tacotron2-DDC")
    wav = tts.tts(text=text)
    sd.play(wav, 23000)
    return {
        "error": "",
        "value": ""
    }

def cancel():
    try:
        sd.stop()
        return {
            "error": "",
            "value": ""
        }
    except:
        return {
            "error": "tts-1",
            "value": ""
        }