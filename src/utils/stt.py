import speech_recognition as sr
import logging


def listen():

    """Returns the spoken text."""

    r = sr.Recognizer()

    mic = sr.Microphone()

    logging.warn("Listening")
    with mic as source:
        audio = r.listen(source)

    try:
        # Give audio to google to get text
        text = r.recognize_google(audio, language="de-DE", show_all=False)
        return {
            "error": "",
            "value": text
        }
    except sr.UnknownValueError:
        return {
            "error": "stt-1",
            "value": ""
        }
    except:
        return {
            "error": "stt-2",
            "value": ""
        }