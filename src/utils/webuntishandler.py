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