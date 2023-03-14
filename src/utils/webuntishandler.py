import webuntis

server = ""
school = ""
user = ""
pwd = ""

s = webuntis.Session(
    server=server,
    username=user,
    password=pwd,
    school=school,
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

