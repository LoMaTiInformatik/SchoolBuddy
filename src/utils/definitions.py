import logging
from utils.speak import speak

# Syntax 
# "error-code": {"log": "Text to log in errorlog", "speak": "text to speak", "severity": 0(Debug),1(Warn),2(Non-Fatal Error),3(Fatal Error)}
errordef = {
    "stt-1": {
    "log": "Error stt-1: No Text",
    "speak": "Ich habe dich leider nicht verstanden.",
    "severity": 1},

    "stt-2": {
    "log": "Error stt-2: No Wifi/Connection",
    "speak": "Fehler s t t 2. Es gab einen Fehler bei der Bearbeitung deiner Anfrage. Bist du mit dem Internet verbunden?",
    "severity": 2},

    "tts-1": {
    "log": "Error tts-1: Speech fault",
    "speak": "Fehler t t s 1. Es gab einen Fehler bei der Ausgabe der Sprache.",
    "severity": 2},

    "mysql-1": {
    "log": "Error mysql-1: Database failure",
    "speak": "Fehler mai s q l 1. Es gab einen Fehler mit der Datenbank.",
    "severity": 3},

    "cmdh-1": {
    "log": "Error cmdh-1: No keyword found in input",
    "speak": "Ich konnte keinen passenden Befehl für deine Anfrage finden. Bitte versuche es erneut.",
    "severity": 1},

    "cmdh-2": {
    "log": "Error cmdh-2: No command matching keywords found",
    "speak": "Ich konnte keinen passenden Befehl für deine Anfrage finden. Bitte versuche es erneut.",
    "severity": 1},

    "cmdh-3": {
    "log": "Error cmdh-3: No chosencmd. How did this even happen?",
    "speak": "Ich konnte keinen passenden Befehl für deine Anfrage finden. Bitte versuche es erneut.",
    "severity": 1},
}

# Syntax
# "word": {"typeword": "Topic word to choose cmd", "weight": The weight of the word (how definitive is it)}

# 

keywords = {
    "uhr": {
        "typeword": "time",
        "weight": 5
    }
}

cmdkeywords = {
    
}

def handleerror(errcode: str):
    err = errordef[errcode]
    if err["severity"] == 0:
        logging.debug(err["log"])
    elif err["severity"] == 1:
        logging.warn(err["log"])
    elif err["severity"] == 2:
        logging.error(err["log"])
    else:
        logging.critical(err["log"])
    
    speak(err["speak"])

    return 