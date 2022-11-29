# LessonBuddy
This is Lesson Buddy. A voice assistant that sits on your shoulder, that's going to help you in your school life.
## Structures
### Folder structure
<details>
<summary>Click me</summary>
```mermaid
flowchart LR;
  audio["/audio/"] --> ger["german/"];
  ger --> gerwebu["webuntis/"];
  ger --> gernum["numbers/"];
  ger --> gerdate["date/"];
  ger --> gerweather["weather/"];
  ger --> gercore["core/"];
  gerwebu --> gerwebuteach["teachers/"];
  gerwebu --> gerwebusubj["subjects/"];
  gerwebu --> gerweburoom["rooms/"];
  gerwebu --> gerwebugener["generic/"];
  gerwebuteach --> gerteachval["[name].wav"];
  gerwebusubj --> gersubjval["[subject].wav"];
  gerweburoom --> gerroomval["[rooms].wav"];
  gerwebugener --> gerandval["and.wav"];
  gerwebugener --> gercanceval["cancelled.wav"];
  gerwebugener --> gerinroomval["inroom.wav"];
  gerwebugener --> gerwithwebval["with.wav"];
  gerwebugener --> gerfromwebval["from.wav"];
  gerwebugener --> geruntilwebval["until.wav"];
  gernum --> gernumval["[0-100].wav"];
  gerdate --> germonth["months/"];
  gerdate --> gerday["days/"];
  gerdate --> geryear["years/"];
  gerdate --> geritstheval["itsthe.wav"];
  germonth --> germonthval["[Jan.-Dec.].wav"];
  gerday --> gerdayval["[1st-31st].wav"];
  geryear --> geryearval["[2022-2035].wav"];
  gerweather --> gerwstatus["wstatus/"];
  gerweather --> gerrainperval["rainper.wav"];
  gerweather --> gerdegreescval["degreesc.wav"];
  gerweather --> gerdegreesfval["degreesf.wav"];
  gerwstatus --> gerwstatusval["[wstatuses].wav"];
  gercore --> gersetup["setup/"];
  gercore --> gershortans["shortans/"];
  gercore --> gererror["error/"];
  gercore --> gerstartup["startup/"];
  gersetup --> gersetupval["TBD"];
  gershortans --> gershortansval["TBD"];
  gererror --> gererrcodes["codes/"];
  gererror --> gererrfix["fixes/"];
  gererrcodes --> gererrcodeval["[errcode].wav"];
  gererrfix --> gererrfixval["[possiblefix].wav"];
  gerstartup --> gerstartupval["TBD"];
```
</details>
### Speech structure
- Lesson plan start
  > "Hier ist der Stundenplan von [heute/morgen]"
- Lesson info
  > "Du hast [Lesson name] bei [Teacher name] in Raum [Room name] von [Time begin] bis [Time end]"
- Lesson cancelled
  > "[Lesson name] bei [Teacher name] von [Time begin] bis [Time end] fällt aus"
- Time
  > "Es ist [Hour] Uhr"

  > "Es ist [Hour] Uhr [Minute]"
- Date
  > "Heute ist der [Day] [Month] [Year]"

  > "Es ist [Weekday] der [Day] [Month] [Year]"
- Weather
  > "[Heute/Morgen] wird es [Weather status] mit einer Regenwahrscheinlichkeit von [Rain percent]"

  > "[Heute/Morgen] wird es [Weather status]
- Error
  > "Es ist ein Fehler aufgetreten. Fehlercode [Error code]. [Possible fix]"

## Ideas
### Aesthetic
- "Buddy" round?
- Cable to connect "Buddy" to Case in black heatshrink
- LED in "Buddy" to indicate listening or errors
- Fabric on "Buddy" (maybe like the one on an Alexa)
- Case see-through
- One cable to connect (maybe with USB-Hub)
- Strap to right or left shoulder-strap on school bag

### Hardware
- Accelerometer to detect tapping
- Powerbank in Case

### Functions
- Give whole lesson plan
- Give infos about specific lesson
- Give infos about weather, date and time
- More general infos (maybe)
- Reminders for exams (maybe)

## ToDo
### Record audio
- [X] Intro
- [ ] Time numbers (0 - 60)
- [ ] Date numbers (1st - 31st)
- [ ] Date months (January - December)
- [ ] Date years (2022 - 2035)
- [ ] Weather
- [ ] Setup
- [ ] General answers

### 3D Print
- [ ] "Buddy"
- [ ] Case

### Program
- [ ] Speech recongnition (Google)
- [ ] Setup
- [ ] WebUntis API
- [ ] Config website
- [ ] Command handling
