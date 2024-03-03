# importing
from __init__ import create_service
import datetime


class GoogleCalendarManager:
    """
    Manages calendar using Google Calendar API and provides user-friendly functions.
    """

    def __init__(self):
        """
        Initializes the CalendarManager and creates a Google API service object.

        Raises:
            Exception: If an error occurs during Google API service creation.
        """
        try:
            self.service = create_service('calendar', 'v3')
        except Exception as e:
            return e
    

    def give_upcoming_event(self, amount: int):
        """
        Retrieve upcoming events from the calendar.

        Args:
            amount (int): The number of upcoming events to retrieve.

        Returns:
            dict: A dictionary containing the upcoming event IDs as keys and their start time and summary as values.
            Returns None if no events are found.
        """
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
        """
        Retrieve today's events from the calendar and return a dictionary containing 
        event IDs as keys and their start time and summary as values.
        """
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
        
        
    def give_holidays(self, country_name="usa"):
        """
        Get holiday of any country. But all countries are not tested yet.
        enter the name according to google calendar

        Args:
            country_name (str): Country code. Defaults to "usa".
            tested options are:
                - usa
                - indian
                - japanese
                - uk
                - french
                - italian
                - spain
                - swedish
                - german
                - austrian
                - danish
                - dutch
        
        Returns:
            event_list (list): List of upcoming events.
        """
        try:
            now = datetime.datetime.utcnow().isoformat() + "Z"
            events_result = self.service.events().list(calendarId=f"en.{str(country_name)}#holiday@group.v.calendar.google.com", timeMin=now, maxResults=10, singleEvents=True, orderBy='startTime').execute()
            events = events_result.get('items', [])

            if not events:
                return None

            event_list = []
            for event in events:
                start = event['start'].get('dateTime', event['start'].get('date'))
                event_list.append([start, event["summary"]])
            return event_list
        except Exception as e:
            return e