from utils.webuntishandler import get_lesson_plan

keywords = ["lessonplan"]

def cmdfunction(spktext: str):

    lesson_plan = get_lesson_plan("today")

    text = "Du hast heute "
    for next_lesson in lesson_plan:
        nexttext = ""
        

    return {
        "error": "",
        "value": ""
    }