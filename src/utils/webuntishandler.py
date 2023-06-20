from utils.sqlhandler import get_settings
import webuntis

sett = get_settings()

s = webuntis.Session(
    server=sett["webuserver"],
    username=sett["webuuser"],
    password=sett["webupwd"],
    school=sett["webuschool"],
    useragent="SchoolBuddy"
)

def get_lesson_plan(day):
    print("l")
    # Get whole lesson plan
    # Args: day (today/tmrw)
    # Returns lesson plan from webuntis

def get_lesson(day, lessonnum):
    print("l")
    # Get single lesson
    # Args: day (today/tmrw), lessonnum (number of the lesson)
    # Returns single lesson

