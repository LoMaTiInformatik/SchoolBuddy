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