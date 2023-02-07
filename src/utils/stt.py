import speech_recognition as sr


def listen():

    r = sr.Recognizer()

    mic = sr.Microphone()

    with mic as source:
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio, language="de-DE", show_all=False)
        return {
            "error": "",
            "text": text
        }
    except sr.UnknownValueError:
        return {
            "error": "stt-1",
            "text": ""
        }
    except:
        return {
            "error": "stt-2",
            "text": ""
        }