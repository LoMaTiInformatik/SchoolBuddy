from TTS.api import TTS
import sounddevice as sd

def speak(text):

    """
        Speaks the given text

        Arguments:
        text: Text to speak (str)

        Returns:
        error: Error-Code if any (str)
        value: None (str)
    """

    tts = TTS("tts_models/de/thorsten/tacotron2-DDC")
    wav = tts.tts(text=text)
    sd.play(wav, 23000)
    return {
        "error": "",
        "value": ""
    }

def question(text):

    """
        Asks a question with the given text

        Arguments:
        text: Question to ask (str)

        Returns:
        error: Error-Code if any (str)
        value: Answertext (str)
    """
    
    pass 

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