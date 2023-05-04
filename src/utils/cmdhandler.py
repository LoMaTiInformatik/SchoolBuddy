import logging
from definitions import keywords

# Commands

import commands
from commands import *

cmdkeywords = {}

for x in dir(commands):
    if x.startswith("__"):
        continue

    mod = getattr(commands, x)
    cmdkeywords[x] = {"keywords": mod.keywords}

    logging.debug(str.format("Cmdhandler: Command module {} sucessfully added.", x))



def handlecmd(spktext: str):
    typewords = {
        1: {"word": None,
            "weight": 0},
        2: {"word": None,
            "weight": 0},
        3: {"word": None,
            "weight": 0},
        4: {"word": None,
            "weight": 0},
        5: {"word": None,
            "weight": 0}
    }

    for x in spktext.split(" "):
        if x not in keywords:
            continue

        key = keywords[x]
        succ = False

        for y in typewords:
            if typewords[y]["weight"] >= key["weight"]:
                continue

            typewords[y] = {"word": key["typeword"], "weight": key["weight"]}
            succ = True
            break

        else:
            if not succ:
                logging.debug(str.format("CmdHandler: Word {} did not match a keyword.",x))
    else:
        if typewords[1]["word"] == None:
            return {
                "error": "cmdh-1",
                "value": ""
            }
    cmdlist = {}

    for x in cmdkeywords:
        cmdlist[x] = {"times": 0, "weight": 0}
        for y in typewords:
            if not typewords[y]["word"] in cmdkeywords[x]["keywords"]:
                continue

            cmdlist[x]["times"] += 1
            cmdlist[x]["weight"] += typewords[y]["weight"]
        
        else:
            logging.debug(str.format("Cmdhandler: Cmd {} had {} matches with the collective weight of {}.", x, cmdlist[x]["times"], cmdlist[x]["weight"]))
    else:
        if not cmdlist:
            return {
                "error": "cmdh-2",
                "value": ""
            }

    chosencmd = {}

    for x in cmdlist:
        if cmdlist[x]["times"] < chosencmd["times"]:
            continue
        elif cmdlist[x]["times"] == chosencmd["times"]:
            if cmdlist[x]["weight"] < chosencmd["weight"]:
                continue
        
        chosencmd["name"] = x
        chosencmd["weight"] = cmdlist[x]["weight"]
        chosencmd["times"] = cmdlist[x]["times"]
    
    else:
        if not chosencmd:
            return {
                "error": "cmdh-3",
                "value": ""
            }

    mod = getattr(commands, chosencmd["name"])

    res = mod.cmdfunction(spktext)

    return res
