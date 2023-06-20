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

    "time-1": {
    "log": "Error time-1: Unkown",
    "speak": "Es gab einen Fehler bei der Bearbeitung deiner Anfrage.",
    "severity": 1},

    "weather-1": {
    "log": "Error weather-1: Internet connection error",
    "speak": "Ich konnte die Wetterdaten nicht abrufen. Bitte überprüfe deine Internetverbindung.",
    "severity": 2},

    "sett-1": {
    "log": "Error sett-1: No env found",
    "speak": "Ich konnte keine Einstellungen finden",
    "severity": 3},
}

# Syntax
# "word": {"typeword": "Topic word to choose cmd", "weight": The weight of the word (how definitive is it)}

# 

keywords = {
    "uhr": {
        "typeword": "time",
        "weight": 5
    },
    "welt": {
        "typeword": "helloworld",
        "weight": 1
    },
    "änderungen": {
        "typeword": "changes",
        "weight": 5
    },
    "wetter": {
        "typeword": "weather",
        "weight": 5
    }
}

def handleerror(errcode: str):
    err = errordef[errcode]
    if not err:
        speak("Ein unbekannter Fehler ist aufgetreten.")
        return
    
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

# API Returncodes from the weather api

weatherapicodes = {
    "1000": {
        "day": "es ist sonnig",
        "night": "es ist klar"
    },
    "1003": {
        "day": "es ist teilweise bewölkt",
        "night": "es ist teilweise bewölkt"
    },
    "1006": {
        "day": "es ist bewölkt",
        "night": "es ist bewölkt"
    },
    "1009": {
        "day": "es ist stark bewölkt",
        "night": "es ist stark bewölkt"
    },
    "1030": {
        "day": "es ist leicht nebelig",
        "night": "es ist leicht nebelig"
    },
    "1063": {
        "day": "es ist lückenhaft Regen möglich",
        "night": "es ist lückenhafter Regen möglich"
    },
    "1066": {
        "day": "es ist lückenhaft Schnee möglich",
        "night": "es ist lückenhafter Schnee möglich"
    },
    "1069": {
        "day": "es ist lückenhaft Schneeregen möglich",
        "night": "es ist lückenhafter Schneeregen möglich"
    },
    "1072": {
        "day": "es ist lückenhaft eisiger Nieselregen möglich",
        "night": "es ist lückenhaft eisiger Nieselregen möglich"
    },
    "1087": {
        "day": "es sind Gewitterausbrüche möglich",
        "night": "es sind Gewitterausbrüche möglich"
    },
    "1114": {
        "day": "es ist Schneetreiben vorhanden",
        "night": "es ist Schneetreiben vorhanden"
    },
    "1117": {
        "day": "es ist ein Schneesturm vorhanden",
        "night": "es ist ein Schneesturm vorhanden"
    },
    "1135": {
        "day": "es ist stark nebelig",
        "night": "es ist stark nebelig"
    },
    "1147": {
        "day": "es ist eisiger Nebel vorhanden",
        "night": "es ist eisiger Nebel vorhanden"
    },
    "1150": {
        "day": "es nieselt lückenhaft",
        "night": "es nieselt lückenhaft"
    },
    "1153": {
        "day": "es nieselt leicht",
        "night": "es nieselt leicht"
    },
    "1168": {
        "day": "es nieselt eisig",
        "night": "es nieselt eisig"
    },
    "1171": {
        "day": "es nieselt stark eisig",
        "night": "es nieselt start eisig"
    },
    "1180": {
        "day": "es regnet lückenhaft leicht",
        "night": "es regnet lückenhaft leicht"
    },
    "1183": {
        "day": "es regnet leicht",
        "night": "es regnet leicht"
    },
    "1186": {
        "day": "es regnet hin und wieder mäßig",
        "night": "es regnet hin und wieder mäßig"
    },
    "1189": {
        "day": "es regnet mäßig stark",
        "night": "es regnet mäßig stark"
    },
    "1192": {
        "day": "es regnet hin und wieder stark",
        "night": "es regnet hin und wieder stark"
    },
    "1195": {
        "day": "es regnet stark",
        "night": "es regnet stark"
    },
    "1198": {
        "day": "es regnet eisig leicht",
        "night": "es regnet eisig leicht"
    },
    "1201": {
        "day": "es regnet eisig mäßig stark bis stark",
        "night": "es regnet eisig mäßig stark bis stark"
    },
    "1204": {
        "day": "es ist leichter Schneeregen vorhanden",
        "night": "es ist leichter Schneeregen vorhanden"
    },
    "1207": {
        "day": "es ist mäßig starker bis starker Schneeregen vorhanden",
        "night": "es ist mäßig starker bis starker Schneeregen vorhanden"
    },
    "1210": {
        "day": "es schneit lückenhaft leicht",
        "night": "es schneit lückenhaft leicht"
    },
    "1213": {
        "day": "es schneit leicht",
        "night": "es schneit leicht"
    },
    "1216": {
        "day": "es schneit lückenhaft mäßig stark",
        "night": "es schneit lückenhaft mäßig stark"
    },
    "1219": {
        "day": "es schneit mäßig stark",
        "night": "es schneit mäßig stark"
    },
    "1222": {
        "day": "es schneit lückenhaft stark",
        "night": "es schneit lückenhaft stark"
    },
    "1225": {
        "day": "es schneit stark",
        "night": "es schneit stark"
    },
    "1237": {
        "day": "es hagelt",
        "night": "es hagelt"
    },
    "1240": {
        "day": "es sind leichte Regenschauer vorhanden",
        "night": "es sind leichte Regenschauer vorhanden"
    },
    "1243": {
        "day": "es sind mäßig starke bis starke Regenschauer vorhanden",
        "night": "es sind mäßig starke bis starke Regenschauer vorhanden"
    },
    "1246": {
        "day": "es sind sintflutartige Regenschauer vorhanden",
        "night": "es sind sintflutartige Regenschauer vorhanden"
    },
    "1249": {
        "day": "es sind leichte Graupelschauer vorhanden",
        "night": "es sind leichte Graupelschauer vorhanden"
    },
    "1252": {
        "day": "es sind mäßig starke bis starke Graupelschauer vorhanden",
        "night": "es sind mäßig starke bis starke Graupelschauer vorhanden"
    },
    "1255": {
        "day": "es sind leichte Schneeschauer vorhanden",
        "night": "es sind leichte Schneeschauer vorhanden"
    },
    "1258": {
        "day": "es sind mäßig starke bis starke Schneeschauer vorhanden",
        "night": "es sind mäßig starke bis starke Schneeschauer vorhanden"
    },
    "1261": {
        "day": "es schauert leicht Hagel",
        "night": "es schauert leicht Hagel"
    },
    "1264": {
        "day": "es schauert mäßig stark bis stark Hagel",
        "night": "es schauert mäßig stark bis stark Hagel"
    },
    "1273": {
        "day": "es regnet lückenhaft leicht mit Donner",
        "night": "es regnet leicht mit Donner"
    },
    "1276": {
        "day": "es regnet mäßig stark bis stark mit Donner",
        "night": "es regnet mäßing stark bis stark mit Donner"
    },
    "1279": {
        "day": "es schneit lückenhaft leicht mit Donner",
        "night": "es schneit lückenhaft leicht mit Donner"
    },
    "1282": {
        "day": "es schneit lückenhaft mäßig stark bis stark mit Donner",
        "night": "es schneit lückenhaft mäßig stark bis stark mit Donner"
    }
}