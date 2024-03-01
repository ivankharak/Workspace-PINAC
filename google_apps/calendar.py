# importing
from __init__ import create_service
import datetime


class CalendarManager:
    """
    Manages calendar using Google Calendar API and provides user-friendly functions.
    """

    def __init__(self):
        """
        Initializes the ContactManager and creates a Google People API service object.

        Raises:
            Exception: If an error occurs during Google People API service creation.
        """
        try:
            self.service = create_service('calendar', 'v3')
        except Exception as e:
            return e
    
    # Fetching events

    def give_upcoming_event(self, amount: int):
        now = datetime.datetime.utcnow().isoformat() + "Z"
        events_result = (
            self.service.events()
            .list(
                calendarId="primary",
                timeMin=now,
                maxResults=amount,
                singleEvents=True,
                orderBy="startTime",
            ).execute())
        events = events_result.get("items", [])
        
        if not events:
            return None
        
        event_list = {}
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            event_list[str(event["id"])] = [start, event["summary"]]
        return event_list


    def give_todays_event(self):
        now = datetime.datetime.utcnow().isoformat() + "Z"
        end = str(now).split("T")[0] + "T23:59:59.00" + "Z"
        events_result = (
            self.service.events()
            .list(
                calendarId="primary",
                timeMin=now,
                maxResults=10,
                timeMax=end,
                singleEvents=True,
                orderBy="startTime",
            ).execute())
        events = events_result.get("items", [])

        if not events:
            return None
        
        event_list = {}
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            event_list[str(event["id"])] = [start, event["summary"]]

        return event_list
        
        
