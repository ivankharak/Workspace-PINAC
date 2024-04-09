import eel
from functools import cache
from datetime import datetime
from src.ai_models import models
from src.google.__init__ import createService
from src.google.gmail_bot import GoogleGmailManager
from src.google.calendar_bot import GoogleCalendarManager
from src.google.contact_bot import GoogleContactManager
from src.google.task_bot import GoogleTaskManager
from src.ai_models.model_utils import saveHistory, clearHistory

clearHistory()
eel.init('UI')


@eel.expose
def signUp():
    createService('gmail', 'v1')

@cache
def decodeEmail(text):
    lines = text.split('\n')
    subject_index = next((i for i, line in enumerate(lines) if "Subject:" in line), None)
    body = '\n'.join(lines[subject_index+2:]) if subject_index is not None else text
    subject = next((line.replace("Subject: ", "") for line in lines if "Subject" in line), None)
    return body, subject

@cache
def formatDatetime(timestamp: str):
    if "T" not in timestamp:
        timestamp += "T00:00:00+05:30"
    dt = datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S%z")
    return dt.strftime("%H.%M, %d/%m/%Y")

@eel.expose
def clearMemory():
    clearHistory()

@eel.expose
@cache
def giveResponse(query):
        # try:
        response = models.askAI(query)

        if "order is composing email" in response:
            body, subject = decodeEmail(response)
            gmail = GoogleGmailManager()
            gmail.createDraft(body=body, subject=subject)
            response = f"Subject: {subject}\n\n{body}\n\n\nDraft email created for you"

        elif "order is to fetch upcoming events from Calendar" in response:
            calendar = GoogleCalendarManager()
            amount = 10
            if "order is to fetch upcoming events from Calendar (amount: " in response:
                amount = int(response.split("amount: ", 1)[1].split(")", 1)[0])
            event_list = calendar.upcomingEvent(amount)
            if event_list:
                response = "Sure, here are your upcoming events: \n\n" + "\n".join(f"{formatDatetime(item[1])} : {item[2]}" for item in event_list)
            else:
                response = "Unfortunately, the event you are searching for does not appear to be exist"

        elif "order is to fetch today's events from Calendar" in response:
            calendar = GoogleCalendarManager()
            event_list = calendar.todaysEvent()
            if event_list:
                response = "Sure, here are your upcoming events for today: \n\n" + "\n".join(f"{formatDatetime(item[1])} : {item[2]}" for item in event_list)
            else:
                response = "I am unable to locate any event for today in Google Calendar"

        elif "order is fetching contact from Contact" in response:
            name = models.findName(query)
            contact = GoogleContactManager()
            contact_info = contact.phoneNumber(name)
            if contact_info:
                response = "Sure, here is your contact: \n\n" + "\n".join(f"{item[0]} : {item[1]}" for item in contact_info)
            else:
                response = "I am unable to locate any contact number you are searching for in Google Contact"    

        elif "order is to fetch task from Calendar" in response:
            task = GoogleTaskManager()
            task_list = task.dueTasks()
            if task_list:
                response = "Sure, here are your due tasks: \n\n" + "\n".join(f"{item[1]} : {item[0]}" for item in task_list)
            else:
                response = "Hooray! 🎉 you don't have any due tasks !"

        elif "order is fetching today's event and task from Calendar" in response:
            response = "Sorry, this feature is still not available, waiting for the next update"

        saveHistory(query, response)

        # except:
        #     response = "Sorry something went wrong, please try again"
        return response

eel.start('index.html')
