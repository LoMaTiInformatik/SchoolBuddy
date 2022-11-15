# LessonBuddy
This is Lesson Buddy. A voice assistant that sits on your shoulder, that's going to help you in your school life.
## Structures
### Folder structure
```mermaid graph RL;
"/audio/" --> ger["german/"];
ger --> gerwebu["webuntis/"];
ger --> gernum["numbers/"];
ger --> gerdate["date/"];
ger --> gerweather["weather/"];
ger --> gercore["core/"];
gerwebu --> gerwebuteach["teachers/"];
gerwebu --> gerwebusubj["subjects/"];
gerwebu --> gerweburoom["rooms/"];
gerwebu --> gerwebgener["generic/"];
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

## Ideas
### Aesthetic
- "Buddy" round?
- Cable to connect "Buddy" to Case in black heatshrink
- LED in "Buddy" to indicate listening or errors
- Fabric on "Buddy" (maybe like the one on an Alexa)
- Case see-through
- One cable to connect (maybe with USB-Hub)
- Strap to right or left shoulder-strap on school bag

### Functional
- Accelerometer to detect tapping
- Powerbank in Case

## ToDo
### Record audio
- [X] Intro
- [ ] Time numbers (0 - 60)
- [ ] Date numbers (1st - 31st)
- [ ] Date months (January - December)
- [ ] Date years ?
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
