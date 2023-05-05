import time as timemod
keywords = ["time"]

def cmdfunction(spktext: str):
    try:
        hour = timemod.strftime("%H", timemod.localtime())
        minute = timemod.strftime("%M", timemod.localtime())

        text = "Es ist " + hour + " Uhr"
        if minute != "00":
            text += " " + minute
        
        return {
            "error": "",
            "value": text
        }
    except:
        return {
            "error": "time-1",
            "value": ""
        }