import eel
from functools import cache
import dateutil.parser
from src.ai_models import models
from src.google.gmail_bot import GoogleGmailManager
from src.google.calendar_bot import GoogleCalendarManager



eel.init('UI/web')

@cache
def get_subject_body(text):
    
    lines = text.split('\n')
    subject_index = next((i for i, line in enumerate(lines) if "Subject:" in line), None)
    body = '\n'.join(lines[subject_index+2:]) if subject_index is not None else text

    for line in text.splitlines():
        if "Subject" in line:
            sub = line.replace("Subject: ", "")
    return body, sub


@cache
def formate_datetime(time_str: str):
    dt = dateutil.parser.parse(time_str)
    normal_datetime  = dt.strptime(time_str, "%Y-%m-%dT%H:%M:%S%z")
    return normal_datetime


@eel.expose
@cache
def give_response(query):
    response = models.ask_me(query)

    if "task is sending email" in response:
        body, subject = get_subject_body(response)
        gmail = GoogleGmailManager()
        draft = gmail.create_draft(body=body, subject=subject)
        
        body = body.replace("\n", "<br>")
        response = f"Subject: {subject}<br><br>{body}<br><br><br>Email draft created: {draft}"


    elif "task is fetching upcoming events from Google Calendar" in response:
        
        calendar = GoogleCalendarManager()
        if "task is fetching upcoming events from Google Calendar (amount: " in response:
                line = response.splitlines()[0]
                amount = line.replace("task is fetching upcoming events from Google Calendar (amount: ", "").replace(")", "")
                try: event_list = calendar.give_upcoming_event(int(amount))
                except: pass
        else:
            try: event_list = calendar.give_upcoming_event(10)
            except: pass
        try:
            draft_response = ""
            for item in event_list:
                formatted_time = formate_datetime(item[1])
                draft_response += f"{formatted_time} : {item[2]}<br>"
        except:
            draft_response = "Sir, there is no upcoming events for you"

        response = draft_response.replace("\n", "<br>")
        response = f"Sure, here are your's upcoming events: <br><br>{response}"


    elif "task is fetching today's events from Google Calendar" in response:
        calendar = GoogleCalendarManager()
        try:
            event_list = calendar.give_todays_event()
            draft_response = ""
            for item in event_list:
                formatted_time = formate_datetime(item[1])
                draft_response += f"{formatted_time} : {item[2]}<br>"
        except:
            draft_response = "Sir, there is no upcoming events for you"

        response = draft_response.replace("\n", "<br>")
        response = f"Sure, here are your's upcoming events for today: <br><br>{response}"

    response = response.replace("\n", "<br>")
    return response

eel.start('index.html')


""""
First comment the whole above and run the below code, it will create google token for you.
Then comment below code and run above code for running application.
"""
# activate = GoogleGmailManager()
