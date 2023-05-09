import os
import logging
#from setup import first_run
from utils.stt import listen
from utils.definitions import handleerror
from utils.speak import speak
from utils.cmdhandler import handlecmd

#if (os.getenv('SCHOOLBUDDY_FIRSTRUN') == "yes"):
 #   first_run()

def activate():
    logging.basicConfig(level=logging.DEBUG, filename="log.txt")
    spkres = listen()
    if spkres["error"] != "":
        handleerror(spkres["error"])
        return

    cmdres = handlecmd(spkres["value"])
    if cmdres["error"] != "":
        handleerror(cmdres["error"])
        return
    
    speak(cmdres["value"])
    
if __name__ == "__main__":
    activate()
    
    
    