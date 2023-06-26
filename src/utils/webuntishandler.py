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

    # Get whole lesson plan
    # Args: day (today/tmrw)
    # Returns lesson plan from webuntis

def get_lesson(day, lessonnum):
    #print(lesson_plan.filter(start=datetime.datetime(year=start_date.year,month=start_date.month,day=start_date.day,hour=12,minute=20)))
    #lesson_plan = get_lesson_plan(day)
    #if next_lessons:
        #sorted_lessons = sorted(next_lessons, key=lambda lesson: lesson.start)

        #next_lesson = sorted_lessons[0]

        ##print("Next Lesson:")
        #subjects = ', '.join([subject.name for subject in next_lesson.subjects])
        #rooms = ', '.join([room.name for room in next_lesson.rooms])
        #print(f"Subject: {subjects}")
        #print(f"Room: {rooms}")
        #print(f"Start Time: {next_lesson.start.strftime('%H:%M')}")
        #print(f"End Time: {next_lesson.end.strftime('%H:%M')}")
    #else:
        #print("Keine kommenden Unterrichte gefunden.")
    pass

    # Get single lesson
    # Args: day (today/tmrw), lessonnum (number of the lesson)
    # Returns single lesson