import os
from setup import first_run
from utils.stt import listen
from utils.definitions import handleerror
from utils.speak import speak

if (os.getenv('SCHOOLBUDDY_FIRSTRUN') == "yes"):
    first_run()

def activate():
    spkres = listen()
    if spkres["error"] != "":
        handleerror(spkres["error"])
    
    