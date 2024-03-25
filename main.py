import eel
from functools import cache
from datetime import datetime
from src.ai_models import models
from src.google.gmail_bot import GoogleGmailManager
from src.google.calendar_bot import GoogleCalendarManager
from src.google.contact_bot import GoogleContactManager

eel.init('UI/web')

@cache
def get_subject_body(text):
    lines = text.split('\n')
    subject_index = next((i for i, line in enumerate(lines) if "Subject:" in line), None)
    body = '\n'.join(lines[subject_index+2:]) if subject_index is not None else text
    subject = next((line.replace("Subject: ", "") for line in lines if "Subject" in line), None)
    return body, subject

@cache
def format_datetime(timestamp: str):
    if "T" not in timestamp:
        timestamp += "T00:00:00+05:30"
    dt = datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S%z")
    return dt.strftime("%H.%M, %d/%m/%Y")

@eel.expose
@cache
def give_response(query):
    try:
        response = models.ask_me(query)
        response = response.replace("\n", "<br>")

        if "task is sending email" in response:
            body, subject = get_subject_body(response)
            gmail = GoogleGmailManager()
            gmail.create_draft(body=body, subject=subject)
            response = f"Subject: {subject}<br><br>{body}<br><br><br>Draft email created for you"

        elif "task is fetching upcoming events from Calendar" in response:
            calendar = GoogleCalendarManager()
            amount = 10
            if "task is fetching upcoming events from Calendar (amount: " in response:
                amount = int(response.split("amount: ", 1)[1].split(")", 1)[0])
            event_list = calendar.give_upcoming_event(amount)
            draft_response = "<br>".join(f"{format_datetime(item[1])} : {item[2]}" for item in event_list)
            response = f"Sure, here are your upcoming events: <br><br>{draft_response}"

        elif "task is fetching today's events from Calendar" in response:
            calendar = GoogleCalendarManager()
            event_list = calendar.give_todays_event()
            draft_response = "<br>".join(f"{format_datetime(item[1])} : {item[2]}" for item in event_list)
            response = f"Sure, here are your upcoming events for today: <br><br>{draft_response}"

        elif "task is fetching contact from Contact" in response:
            name = models.find_name(query)
            contact = GoogleContactManager()
            contact_info = contact.give_phone_number(name)
            print(type(contact_info))
            print(contact_info)
            if isinstance(contact_info[0], list):
                draft_response = "<br>".join(f"{item[0]} : {item[1]}" for item in contact_info)
            else: draft_response = f"<br>{contact_info[0]} : {contact_info[1]}"
            response = f"Sure, here is your contact: <br>{draft_response}"
    
    except TypeError: response = "Unfortunately, the event you are searching for does not appear to be exist"
    except UnboundLocalError: response = "we are unable to locate any contact number you are searching for in Google Contact"
    except: response = "Oops! It seems like you're not connected to the internet. Please check your network connection and try again. If the problem persists, you might want to contact your service provider. We appreciate your patience!"
    return response

eel.start('index.html')


""""
First comment the whole above and run the below code, it will create google token for you.
Then comment below code and run above code for running application.
"""
# activate = GoogleGmailManager()
