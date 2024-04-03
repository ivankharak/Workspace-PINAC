import eel
from functools import cache
from datetime import datetime
from src.ai_models import models
from src.google.__init__ import create_service
from src.google.gmail_bot import GoogleGmailManager
from src.google.calendar_bot import GoogleCalendarManager
from src.google.contact_bot import GoogleContactManager
from src.google.task_bot import GoogleTaskManager
from src.ai_models.model_utils import save_history, clear_history

clear_history()
eel.init('UI')


@eel.expose
def sign_up():
    create_service('gmail', 'v1')

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
def clear_memory():
    clear_history()

@eel.expose
@cache
def give_response(query):
        # try:
        response = models.ask_me(query)

        if "order is sending email" in response:
            body, subject = get_subject_body(response)
            gmail = GoogleGmailManager()
            gmail.create_draft(body=body, subject=subject)
            response = f"Subject: {subject}\n\n{body}\n\n\nDraft email created for you"

        elif "order is fetching upcoming events from Calendar" in response:
            calendar = GoogleCalendarManager()
            amount = 10
            if "order is fetching upcoming events from Calendar (amount: " in response:
                amount = int(response.split("amount: ", 1)[1].split(")", 1)[0])
            event_list = calendar.give_upcoming_event(amount)
            if event_list:
                response = "Sure, here are your upcoming events: \n\n" + "\n".join(f"{format_datetime(item[1])} : {item[2]}" for item in event_list)
            else:
                response = "Unfortunately, the event you are searching for does not appear to be exist"

        elif "order is fetching today's events from Calendar" in response:
            calendar = GoogleCalendarManager()
            event_list = calendar.give_todays_event()
            if event_list:
                response = "Sure, here are your upcoming events for today: \n\n" + "\n".join(f"{format_datetime(item[1])} : {item[2]}" for item in event_list)
            else:
                response = "I am unable to locate any event for today in Google Calendar"

        elif "order is fetching contact from Contact" in response:
            name = models.find_name(query)
            contact = GoogleContactManager()
            contact_info = contact.give_phone_number(name)
            if contact_info:
                response = "Sure, here is your contact: \n\n" + "\n".join(f"{item[0]} : {item[1]}" for item in contact_info)
            else:
                response = "I am unable to locate any contact number you are searching for in Google Contact"    

        elif "order is fetching task from Calendar" in response:
            task = GoogleTaskManager()
            task_list = task.get_due_tasks()
            if task_list:
                response = "Sure, here are your due tasks: \n\n" + "\n".join(f"{item[1]} : {item[0]}" for item in task_list)
            else:
                response = "Hooray! 🎉 you don't have any due tasks !"

        elif "order is fetching event and task from Calendar" in response:
            response = "Sorry, this feature is still not available, waiting for the next update"

        elif "order is fetching today's event and task from Calendar" in response:
            response = "Sorry, this feature is still not available, waiting for the next update"

        save_history(query, response)

        # except:
        #     response = "Sorry something went wrong, please try again"
        return response

eel.start('index.html')
