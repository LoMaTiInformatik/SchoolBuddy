import time as timemod
keywords = ["time"]

def cmdfunction(spktext: str):
    hour = timemod.strftime("%H", timemod.localtime())
    minute = timemod.strftime("%M", timemod.localtime())
    pass