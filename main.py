import eel
import datetime, os
from functools import cache
from email_validator import validate_email
from src.ai_models import ChatGPT
from src.google.__init__ import createService
from src.google.gmail_bot import GoogleGmailManager
from src.google.calendar_bot import GoogleCalendarManager
from src.google.contact_bot import GoogleContactManager
from src.google.task_bot import GoogleTaskManager
from langchain.schema import HumanMessage, AIMessage

eel.init('UI')

@eel.expose
def signUp():
    createService('gmail', 'v1')

@eel.expose
def logIn():
    if os.path.exists("src/configs/google_token.json"):
        return True
    else:
        return False

@cache
def decodeEmail(text):
    lines = text.split('\n')
    subject_index = next((i for i, line in enumerate(lines) if "Subject:" in line), None)
    body = '\n'.join(lines[subject_index+2:]) if subject_index is not None else text
    subject = next((line.replace("Subject: ", "") for line in lines if "Subject" in line), None)
    return body, subject

@cache
def get_ordinal_suffix(day):  # This function helps determine the ordinal suffix for a day number.
  if 4 <= day % 100 <= 20: suffix = "th"
  else: suffix = ("st", "nd", "rd")[day % 10 if day % 10 < 4 else 0]
  return suffix

@cache
def formatDatetime(timestamp: str):
    timestamp= timestamp[:16]
    if "T" not in timestamp: 
        parsed_date = datetime.datetime.strptime(timestamp, "%Y-%m-%d")
        formatted_time = "whole day"
    
    elif "T" in timestamp:
        parsed_date = datetime.datetime.strptime(timestamp, "%Y-%m-%dT%H:%M")
        formatted_time = parsed_date.strftime("%I:%M %p")  # %I for 12-hour format, %p for AM/PM
        timestamp = timestamp.split("T")[0]
        parsed_date = datetime.datetime.strptime(timestamp, "%Y-%m-%d")

    try:
        # Get the day, month name, and day name
        day = parsed_date.day
        day_with_suffix = f"{day}{get_ordinal_suffix(day)}"
        month_name = parsed_date.strftime("%b")
        day_name = parsed_date.strftime("%A")  # Full day name (Monday, Tuesday, etc.)

        # Format the date with all desired components
        formatted_date = f"{day_name}, {month_name} {day_with_suffix}, {parsed_date.year}"

    except: formatted_date, formatted_time = "...", "..."
    return formatted_date, formatted_time

@eel.expose
def validateEmail(emailId):
    try:
        validate_email(emailId)
        return True
    except ValueError as e:
        print(f"Invalid email address: {e}")
        return False

@eel.expose
def sendInstEmail(recipient_email, subject, body):
    gmail = GoogleGmailManager()
    gmail.sendEmail(recipient_email, subject, body)

@eel.expose
def createDraftEmail(subject, body, recipient_email=None):
    print("called")
    gmail = GoogleGmailManager()
    if recipient_email != None:
        gmail.createDraft(body=body, recipient_email=recipient_email, subject=subject)
    else:
        gmail.createDraft(body=body, subject=subject)

@eel.expose
def clearMemory():
    chatHistory = []

chatHistory = []

@eel.expose
@cache
def giveResponseArray(query: str):
        # try:
        # print(chatHistory)
        chatHistory.append(HumanMessage(content=query))
        raw_response = ChatGPT.askAI(query, chatHistory)

        if "order is composing email" in raw_response:
            body, subject = decodeEmail(raw_response)
            response = ["email", subject, body]
            chatHistory.append(AIMessage(content=raw_response))

        elif "order is to fetch upcoming events from Calendar" in raw_response:
            calendar = GoogleCalendarManager()
            amount = 10
            chatHistory.append(AIMessage(content="order is to fetch upcoming events from Calendar"))
            if "order is to fetch upcoming events from Calendar (amount: " in raw_response:
                amount = int(raw_response.split("amount: ", 1)[1].split(")", 1)[0])
            event_list = calendar.upcomingEvent(amount)
            if event_list:
                text = "Sure, here are your upcoming events: \n\n" + "\n".join(f"{formatDatetime(item[1])[0]}, {formatDatetime(item[1])[1]} : {item[2]}" for item in event_list)
            else:
                text = "Unfortunately, the event you are searching for does not appear to be exist"
            response = ["calendar event", text]
            chatHistory.append(AIMessage(content=text))

        elif "order is to fetch today's events from Calendar" in raw_response:
            calendar = GoogleCalendarManager()
            event_list = calendar.todaysEvent()
            chatHistory.append(AIMessage(content="order is to fetch today's events from Calendar"))
            if event_list:
                text = "Sure, here are your upcoming events for today: \n\n" + "\n".join(f"{formatDatetime(item[1])[0]}, {formatDatetime(item[1])[1]} - {item[2]}" for item in event_list)
            else:
                text = "I am unable to locate any event for today in Google Calendar"
            response = ["calendar today's events", text]
            chatHistory.append(AIMessage(content=text))

        elif "order is fetching contact from Contact" in raw_response:
            name = ChatGPT.findName(query)
            contact = GoogleContactManager()
            contact_info = contact.phoneNumber(name)
            chatHistory.append(AIMessage(content="order is fetching contact from Contact"))
            if contact_info:
                text = "Sure, here is your contact: \n\n" + "\n".join(f"{item[0]} : {item[1]}" for item in contact_info)
            else:
                text = "I am unable to locate any contact number you are searching for in Google Contact"
            response = ["contact", text]
            chatHistory.append(AIMessage(content=text))

        elif "order is to fetch task from Calendar" in raw_response:
            task = GoogleTaskManager()
            task_list = task.dueTask()
            chatHistory.append(AIMessage(content="order is to fetch task from Calendar"))
            if task_list:
                text = "Sure, here are your due tasks: \n\n" + "\n".join(f"{formatDatetime(item[1])[0]}, {formatDatetime(item[1])[1]} - {item[0]}" for item in task_list)
            else:
                text = "Hooray! 🎉 you don't have any due tasks !"
            response = ["calendar task", text]
            chatHistory.append(AIMessage(content=text))

        elif "order is fetching today's event and task from Calendar" in raw_response:
            text = "Sorry, this feature is still not available, waiting for the next update"
            response = ["calendar all", text]
            chatHistory.append(AIMessage(content="order is fetching today's event and task from Calendar"))
        
        else:
            response = ["others", raw_response]
            chatHistory.append(AIMessage(content=raw_response))

        # except:
        #     response = "Sorry something went wrong, please try again"
        return response

eel.start('index.html')
