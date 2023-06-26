<!--Written by Max Leon Guwa (OrangePurgatory; https://github.com/OrangePurgatory)-->


<head>
<h1 align="center">Schoolbuddy - Projekttagebuch</h1> 
</head>
<h3 align="center"> Ein Projekt von Lois und Max 11p </h3>
</br>


<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://user-images.githubusercontent.com/105984356/186677878-5eddbf06-304d-4ea7-90db-5ddba9e40dbf.png">
  <source media="(prefers-color-scheme: light)" srcset="https://user-images.githubusercontent.com/105984356/186676647-16dacef0-4117-4750-afc1-1d4d6409e6d3.png">
  <img alt="" src="">
</picture>


<h3 align="left">Stormarnschule Ahrensburg <br/> Informatik, Buhl <br/> Schuljahr 2022/23, 2. Halbjahr </br> </h3> </div>
<h3 align="left"> &#10132; <a href="https://github.com/LoMaTiInformatik/SchoolBuddy/blob/main/README.md"> Projektseite</a> </h3> 
</br>


## Inhalt
<p><a href="#kapitell">1. Einleitung</a></p>
<p style="margin-bottom: 5px;">
<details style="margin: 0px !important;">
<summary>2. Stundenprotokolle</summary>
<ul>
  <li><a href="#protokoll-zum-06022023">Protokoll zum 06.02.2023</a></li>
  <li><a href="#protokoll-zum-08022023">Protokoll zum 08.02.2023</a></li>
  <li><a href="#protokoll-zum-10022023">Protokoll zum 10.02.2023</a></li>
  <li><a href="#protokoll-zum-13022023">Protokoll zum 13.02.2023</a></li>
  <li><a href="#protokoll-zum-14032023">Protokoll zum 14.03.2023</a></li>
  <li><a href="#protokoll-zum-15032023">Protokoll zum 15.03.2023</a></li>
  <li><a href="#protokoll-zum-17032023">Protokoll zum 17.03.2023</a></li>
  <li><a href="#protokoll-zum-20032023">Protokoll zum 20.03.2023</a></li>
  <li><a href="#protokoll-zum-05042023">Protokoll zum 05.04.2023</a></li>
  <li><a href="#protokoll-zum-04052023">Protokoll zum 04.05.2023</a></li>
  <li><a href="#protokoll-zum-05052023">Protokoll zum 05.05.2023</a></li>
  <li><a href="#zeitraum-vom-06052023-bis-zum-13062023">Zeitraum vom 06.05.2023 bis zum 13.06.2023</a></li>
  <li><a href="#protokoll-zum-14062023">Protokoll zum 14.06.2023</a></li>
  <li><a href="#protokoll-zum-15062023">Protokoll zum 15.06.2023</a></li>
  <li><a href="#protokoll-zum-20062023">Protokoll zum 20.06.2023</a></li>
  <li><a href="#protokoll-zum-21062023">Protokoll zum 21.06.2023</a></li>
  <li><a href="#protokoll-zum-26062023">Protokoll zum 26.06.2023</a></li>
</ul></details></p>
<p style="margin-top: 5px;"><a href="#kapitel3">3. Materialien</a></p>
<p><a href="#kapitel4">4. Quellen</a></p>


<h2 id="kapitell">1. Einleitung</h2>
<p>Hallo und herzlich Wilkommen zu unserem Projekttagebuch. Hier protokollieren wir unseren Arbeitsprozess, um später wieder zurückgucken zu können und sehen, was wir an welchem Tag genau gemacht haben. Einige Protokolle enthalten Beispielcodes, um unseren Arbeitsprozess zu visualisieren.</p>

Der Großteil des Codes ist in dem Unterordner /src/ hier auf GitHub zu finden oder unter dem folgenden Link:
<a href="https://github.com/LoMaTiInformatik/SchoolBuddy/tree/main/src">Die Codes</a>


<h2 id="kapitel2">2. Protokolle</h2>

### Protokoll zum 06.02.2023
Wir haben heute die "speak()" und die "listen()" Funktionen vollendet. Dadurch kann das Programm bereits uns verstehen und auch reden.
```py
def speak(text):

    tts = TTS("tts_models/de/thorsten/tacotron2-DDC")
    wav = tts.tts(text=text)
    sd.play(wav, 23000)
    sd.wait()
    return {
        "error": "",
        "value": ""
    }
```
```py
def listen():
    r = sr.Recognizer()

    mic = sr.Microphone()

    logging.warn("Listening")
    with mic as source:
        audio = r.listen(source)

    try:
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
```

### Protokoll zum 08.02.2023
Heute haben wir mit dem Installations- und Konfigurationsskript angefangen.
```sh
if [ "$act" == 1 ]; then
    echo $'\nPlease wait while we install the required packages.\n'

    apt-get update
    apt-get install software-properties-common -y
    ln -s /usr/lib/python3/dist-packages/gi/_gi.cpython-{36m,37m}-x86_64-linux-gnu.so
    ln -s /usr/lib/python3/dist-packages/apt_pkg.cpython-{36m,37m}-x86_64-linux-gnu.so
    add-apt-repository -y ppa:deadsnakes/ppa
    apt-get update
    apt-get install "python3.7" python3-pip "python3.7-dev" "python3-pyaudio" "portaudio19-dev" mysql-server ffmpeg apache2 espeak-ng -y
    update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.7 1
    update-alternatives --set python3 /usr/bin/python3.7

    cp schoolbuddy.service /etc/systemd/system/schoolbuddy.service
    systemctl daemon-reload
    useradd -m schoolbuddy
    cp -r . /home/schoolbuddy/
    chmod -R 777 /home/schoolbuddy
    cd /home/schoolbuddy/ || exit 2

    su schoolbuddy -c "pip3 install pipenv==2022.4.8"
    su schoolbuddy -c "pipenv --python 3.7"
    su schoolbuddy -c "pipenv run pip install torch==1.13.1 --no-cache-dir"
    su schoolbuddy -c "pipenv install"

    echo $'\nInstallation complete.'

    configure "init"
```

### Protokoll zum 10.02.2023
Das Konfigurationsskript ist fertig. Das Installationsskript können wir erst vollenden, wenn wir mit dem allgemeinen Programm fertig sind.
```sh
renderconfigdisplay () {
    clear
    if [ "$1" == "main" ]; then
        local missstr
        missstr="$(getmissing)"

        echo $'\nSchoolBuddy Configuration'
        echo $'\nPlease choose one of the following options: '
        echo $'\n1 - SchoolBuddy Admin Password'
        echo $'\n2 - MySQL Database Password'
        echo $'\n3 - Wifi Settings'
        echo $'\n4 - WebUntis Settings'
        echo $'\n'
        echo $'\nC - Complete Configuration'

        if [ "$missstr" != "none" ]; then
            echo " (Cannot proceed. You're missing settings in sections"
            echo "$missstr"
            echo ".)"
        fi
    elif [ "$1" == "wifi" ]; then
        echo $'\nWifi Configuration'
        echo $'\nPlease choose one of the following options: '
        echo $'\n'
        echo $'\n1 - SSID (SSID of the wifi network SchoolBuddy will host.)'
        echo $'\n2 - Password (Password of the wifi network SchoolBuddy will host.)'
        echo $'\n'
        echo $'\nB - Go Back'
    elif [ "$1" == "webu" ]; then
        echo $'\n WebUntis Configuration'
        echo $'\nPlease choose one of the following options: '
        echo $'\n'
        echo $'\n1 - Server (URL of the WebUntis server)'
        echo $'\n2 - School (Name of your school in WebUntis format [See configuration page in repository])'
        echo $'\n3 - Username (Usename you use to login to WebUntis)'
        echo $'\n4 - Password (Password you use to login to WebUntis)'
        echo $'\n5 - Class (Initial class to get info for. Don\'t worry you can change it later.)'
        echo $'\n'
        echo $'\nB - Go Back'
    fi
    configure "$1"
}
```

### Protokoll zum 13.02.2023
Die bereits aufgetretenen Fehler des Installationsskripes wurden behoben. Während der Installation schlug das Modul "torch" fehl, woraufhin das gesammte Programm nicht funktionierte. Dies wurde behoben, indem man das Modul manuell installiert, anstatt es automatisch mit allen Anderen zu installieren.

### Protokoll zum 14.03.2023
setup.py angefangen zu schreiben. Nun führt es sqlhandler.py aus um die Datenbank zu populieren.
```py
import os
from utils.sqlhandler import set_init_settings

def first_run():
    res = set_init_settings()
    if (res["error"] != ""):
        return res
    
    return {
        "error": "",
        "value": "true"
    }
```

### Protokoll zum 15.03.2023
Minimale Veränderungen am Installationsskript getätigt. Neue benötigte Module hinzugefügt.

### Protokoll zum 17.03.2023
sqlhandler.py kann nun die Funktion set_init_settings(). Mit Hilfe dieser wird nun die Datenbank mit den Werten aus dem Konfigurationsskript gefüllt.
```py
def set_init_settings():
    try:
        cursor = db.cursor()
    
        settings = {}
        settings['adm_pwd']=os.getenv('SCHOOLBUDDY_ADMPWD')
        settings['default_wifi_ssid']=os.getenv('SCHOOLBUDDY_WIFISSID')
        settings['default_wifi_pwd']=os.getenv('SCHOOLBUDDY_WIFIPWD')
        settings['webu_server']=os.getenv('SCHOOLBUDDY_WEBUSERVER')
        settings['webu_user']=os.getenv('SCHOOLBUDDY_WEBUUSER')
        settings['webu_pwd']=os.getenv('SCHOOLBUDDY_WEBUPWD')
        settings['webu_school']=os.getenv('SCHOOLBUDDY_WEBUSCHOOL')
        settings['webu_class']=os.getenv('SCHOOLBUDDY_WEBUCLASS')

        sql = "UPDATE settings SET value = %s WHERE setting_name = %s;"
        data = []
        for x in settings:
            val = (settings[x],x)
            data.append(val)

        cursor.executemany(sql,data)
        db.commit()
    except:
        return {
            "error": "mysql-1",
            "value": ""
        }

    return {
        "error": "",
        "value": "true"
    }
```

### Protokoll zum 20.03.2023
sqlhandler.py kann nun Einträge aus den Datenbanken abrufen. Hierfür benutzen wir eine MySQL Datenbank, womit der unten stehende Code die eingetragenen Daten auslesen kann.
```py
def get_settings(valueonly: bool = True):
    try:
        cursor = db.cursor()

        sql = "SELECT "
        if (valueonly):
            sql += "setting_name, value, type"
        else:
            sql += "*"
        sql += " FROM settings;"

        cursor.execute(sql)

        sqlres = cursor.fetchall()

        result = {}

        for x in sqlres:
            val = {
                "value": x[1],
                "type": x[2]
            }
            result[x[0]] = val

        ret = {
            "error": "",
            "value": result
        }
        return ret
```

### Protokoll zum 05.04.2023
Heute haben wir beim Projekttag weiter an der Formartierung und der Vervollständigung der Projektseite, sowohl als auch dem Projekttagebuch gearbeitet.<br>
Außerdem haben gegen Ende des Tages versucht das Circuit-Building Programm "Fritzing" mit Hilfe von Qt eigenständig zu builden. Grund hierfür ist die kostenpflichtige Version von Fritzing, die durch eigenes Builden des Programmes umgangen werden kann.

### Protokoll zum 04.05.2023
Mit der Arbeit am cmdhandler.py begonnen. Zurzeit können wir das geschriebene noch nicht testen, deswegen hoffe ich einfach, dass das Programm soweit in dieser Form funktioniert.
```py
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
        x = x.lower()
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
```

### Protokoll zum 05.05.2023
Der cmdhandler.py ist nun vollständig funktionsfähig. Außerdem haben wir zum testen den timecmd.py Code geschrieben, der einem einfach mitteilt, wie viel Uhr es ist.

Der Code im Command-Handler (cmdhandler.py):
```py
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
        if not chosencmd or chosencmd["name"] == "":
            return {
                "error": "cmdh-3",
                "value": ""
            }

    mod = getattr(commands, chosencmd["name"])

    res = mod.cmdfunction(spktext)

    return res
```
<br>
Der Code als Command in timecmd.py:

```py
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
```
<br>

### Zeitraum vom 06.05.2023 bis zum 13.06.2023
Wir hatten uns ein paar Mal in diesem Zeitraum getroffen und uns überlegt, welche weiteren Möglichkeiten für unser Projekt bestehen. Außerdem haben wir außerhalb dieser und jeglicher Repository, Tests an verschiedenen Programmen durchgeführt.<br>
Da wir auch am letzten Projekttag bereits angefangen hatten Fritzing mit Hilfe von Qt zu builden, hatten wir in diesem Zeitraum auch mehrere Versuche angestrebt, dies fertigzustellen. Bisher verbleibt dies allerdings weiterhin bei einem Misserfolg, denn es treten immer noch verschiedene Fehler auf.

### Protokoll zum 14.06.2023
Heute haben wir weitere Dateien für die Commands erstellt und haben bereits angefangen diese zu schreiben. Ebenfalls haben wir ein paar Korrekturen an bereits vorhandenen Code vorgenommen. Mit der Finalisierung dieser Commands, erwarten wir bald eine Vervollständigung des Projektes. Es fehlen nur noch einige Details und Bugfixes.

### Protokoll zum 15.06.2023
Heute stand ein weiterer Projekttag nach etwa einem Monat an. Wir hatten uns für heute vorgenommen, dass wir heute ein paar Commands fertigstellen und eine Art ausarbeiten, wie wir das Projekt präsentieren wollen.<br>
Schlussendlich haben wir den Wetter Command fertigstellen können, welcher mithilfe einer API das aktuelle Wetter von deinem Standort ausgeben kann.

### Protokoll zum 20.06.2023
Heute wurde der Wetter Befehl in das Programm integriert und eine neue Funktion hinzugefügt, welche Einstellungen aus einer .env Datei lesen kann.

### Protokoll zum 21.06.2023
Wir haben heute einen Ansatz für den webuntishandler entwickelt. Bisher gibt es die Option entweder sich den Stundenplan des gesamten nächsten Tages oder sich die nächste Stunde vorlesen zu lassen. Dies beinhaltet sowohl die Stunde selbst als auch der Raum, die Start- und die Endzeit.

```py
from utils.sqlhandler import get_settings
import webuntis
import datetime

sett = get_settings()

s = webuntis.Session(
    server=sett["webuserver"],
    username=sett["webuuser"],
    password=sett["webupwd"],
    school=sett["webuschool"],
    useragent="SchoolBuddy"
)

s.login()

now = datetime.datetime.now()

start_date = now.strftime("%Y%m%d")
end_date = (now + datetime.timedelta(days=1)).strftime("%Y%m%d")

classes = s.klassen()
klasse = None

# 11p has the ID 893
for c in classes:
    if c.id == 893:
        klasse = c
        break

if klasse:
    next_lessons = s.timetable(klasse=klasse, start=start_date, end=end_date)
else:
    print("Klasse mit der ID 893 wurde nicht gefunden.")

def get_lesson_plan(day):
    if next_lessons:
        sorted_lessons = sorted(next_lessons, key=lambda lesson: lesson.start)

        print("Next Lessons:")
        for next_lesson in sorted_lessons:
            subjects = ', '.join([subject.name for subject in next_lesson.subjects])
            rooms = ', '.join([room.name for room in next_lesson.rooms])

            print(f"Subject: {subjects}")
            print(f"Room: {rooms}")
            print(f"Start Time: {next_lesson.start.strftime('%H:%M')}")
            print(f"End Time: {next_lesson.end.strftime('%H:%M')}")
            print()
    else:
        print("Keine kommenden Unterrichte gefunden.")

    # Get whole lesson plan
    # Args: day (today/tmrw)
    # Returns lesson plan from webuntis

def get_lesson(day, lessonnum):
    if next_lessons:
        sorted_lessons = sorted(next_lessons, key=lambda lesson: lesson.start)

        next_lesson = sorted_lessons[0]

        print("Next Lesson:")
        subjects = ', '.join([subject.name for subject in next_lesson.subjects])
        rooms = ', '.join([room.name for room in next_lesson.rooms])
        print(f"Subject: {subjects}")
        print(f"Room: {rooms}")
        print(f"Start Time: {next_lesson.start.strftime('%H:%M')}")
        print(f"End Time: {next_lesson.end.strftime('%H:%M')}")
    else:
        print("Keine kommenden Unterrichte gefunden.")

    # Get single lesson
    # Args: day (today/tmrw), lessonnum (number of the lesson)
    # Returns single lesson

s.logout
```

### Protokoll zum 26.06.2023
Heute haben wir noch letzte Vorkehrungen getroffen, wie unter anderem den webuntishandler fertiggestellt, sowie den lessonplantoday Command. Außerdem haben wir noch Kommentare zu den Codes hinzugefügt, damit der Code für einen Dritten besser und einfacher zu verstehen ist.<br>
Der Code für den webuntishandler ist hier zu finden:
```py
from utils.sqlhandler import get_settings
import webuntis
import datetime

sett = get_settings()["value"]

s = webuntis.Session(
    server=sett["webuserver"],
    username=sett["webuuser"],
    password=sett["webupwd"],
    school=sett["webuschool"],
    useragent="SchoolBuddy"
)

def get_lesson_plan(day,sort:bool=True):

    s.login()

    klasse = s.klassen().filter(name=sett["webuclass"])[0]

    start_date = None
    end_date = None
    if (day == "tmrw"):
        curday = datetime.datetime.now() + datetime.timedelta(days=2)
        start_date = datetime.datetime(year=curday.year,month=curday.month,day=curday.day)
        end_date = start_date + datetime.timedelta(hours=23)
    else:
        curday = datetime.datetime.now()
        start_date = datetime.datetime(year=curday.year,month=curday.month,day=curday.day)
        end_date = start_date + datetime.timedelta(hours=23)

    lesson_plan = s.timetable(klasse=klasse, start=start_date, end=end_date)


    if lesson_plan:
        if sort:
            sorted_lessons = sorted(lesson_plan, key=lambda lesson: lesson.start.strftime("%H:%M"))
            print("Next Lessons:")
            for next_lesson in sorted_lessons:
                subjects = ', '.join([subject.name for subject in next_lesson.subjects])
                rooms = ', '.join([room.name for room in next_lesson.rooms])

                print(f"Subject: {subjects}")
                print(f"Room: {rooms}")
                print(f"Start Time: {next_lesson.start.strftime('%H:%M')}")
                print(f"End Time: {next_lesson.end.strftime('%H:%M')}")
                print()
            
            return {
                "error": "",
                "value": sorted_lessons
            }
        else:
            return {
                "error": "",
                "value": lesson_plan
            }
    else:
        print("Keine kommenden Unterrichte gefunden.")

    s.logout()
```
<br>
Und der Code für den lessonplantoday Command ist hier zu finden:

```py
from utils.webuntishandler import get_lesson_plan

keywords = ["lessonplan"]

def cmdfunction(spktext: str):
    try:
        lesson_plan = get_lesson_plan("today")

        text = "Du hast heute "
        for next_lesson in lesson_plan:
            subjects = ', '.join([subject.long_name for subject in next_lesson.subjects])
            start_time = next_lesson.start.strftime("%H:%M")
            end_time = next_lesson.end.strftime("%H:%M")
            next_text = f"{subjects} von {start_time} bis {end_time}."
            text += next_text + " "

        return {
            "error": "",
            "value": text
        }
    except:
        return {
            "error": "sst-2",
            "value": ""
        }
```

<h2 id="kapitel4">4. Materialien</h2>
- Raspberry Pi<br>
- Lautsprecher


<h2 id="kapitel5">5. Quellen</a></h2>
<a href="https://github.com/espeak-ng/espeak-ng">ESpeak-ng</a><br>
<a href="https://github.com/thorstenMueller/Thorsten-Voice">Thorsten Voice</a><br>
<a href="https://www.mysql.com/">MySQL</a><br>
Alle weiteren Quellen sind in der Pipfile.lock Datei zu finden.