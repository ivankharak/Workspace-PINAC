
tr_data = [
        # for Gmail
        {"role": "user", "content": "I want to send a email"},
        {"role": "assistant", "content": "task is sending email"},
        {"role": "user", "content": "I want to write a email for my work"},
        {"role": "assistant", "content": "task is sending email"},
        {"role": "user", "content": "write a email to send to my office"},
        {"role": "assistant", "content": "task is sending email"},
        {"role": "user", "content": "Hey, can you write an email for me ?"},
        {"role": "assistant", "content": "task is sending email"},
        {"role": "user", "content": "Please help me to write a email"},
        {"role": "assistant", "content": "task is sending email"},
        {"role": "user", "content": "Hey, write email to my fried name John on purpose to meet on upcoming sunday morning at my home. Write it in very sweet tone"},
        {"role": "assistant", "content": "task is sending email"},
        {"role": "user", "content": "Hey, write email to office Chairman Sir on my absence today due to high fever"},
        {"role": "assistant", "content": "task is sending email"},
        {"role": "user", "content": "Hey, write email to all my friends for invitation on my 19th birthday"},
        {"role": "assistant", "content": "task is sending email"},
        {"role": "user", "content": "Hey, write email"},
        {"role": "assistant", "content": "task is sending email"},

        # Google Calendar: Upcoming events
        {"role": "user", "content": "Give me my upcoming event from google calendar"},
        {"role": "assistant", "content": "task is fetching upcoming events from Google Calendar"},
        {"role": "user", "content": "Hey, remind me upcoming event from google calendar"},
        {"role": "assistant", "content": "task is fetching upcoming events from Google Calendar"},
        {"role": "user", "content": "can you show me all my upcoming event from google calendar"},
        {"role": "assistant", "content": "task is fetching upcoming events from Google Calendar"},
        {"role": "user", "content": "Ai tell me my upcoming event from g-calendar"},
        {"role": "assistant", "content": "task is fetching upcoming events from Google Calendar"},
        ### with amount
        {"role": "user", "content": "Give me 10 upcoming event from google calendar"},
        {"role": "assistant", "content": "task is fetching upcoming events from Google Calendar (amount: 10)"},
        {"role": "user", "content": "Hey, remind me 5 upcoming event from google calendar"},
        {"role": "assistant", "content": "task is fetching upcoming events from Google Calendar  (amount: 5)"},
        {"role": "user", "content": "can you show me upto 20 my upcoming event from google calendar"},
        {"role": "assistant", "content": "task is fetching upcoming events from Google Calendar (amount: 20)"},
        {"role": "user", "content": "Ai tell me a few of my upcoming events from g-calendar"},
        {"role": "assistant", "content": "task is fetching upcoming events from Google Calendar (amount: 5)"},

        # Google Calendar: Today's events
        {"role": "user", "content": "Give me my today's event from google calendar"},
        {"role": "assistant", "content": "task is fetching today's events from Google Calendar"},
        {"role": "user", "content": "can you show me my today's event from google calendar"},
        {"role": "assistant", "content": "task is fetching today's events from Google Calendar"},
        {"role": "user", "content": "Give me my today's events from google"},
        {"role": "assistant", "content": "task is fetching today's events from Google Calendar"},
        {"role": "user", "content": "fetch the today's event from google calendar for me please"},
        {"role": "assistant", "content": "task is fetching today's events from Google Calendar"},

        # Calendar: Upcoming events for all available calenders
        {"role": "user", "content": "Give me my upcoming event from calendar"},
        {"role": "assistant", "content": "task is fetching upcoming events from all available Calendars"},
        {"role": "user", "content": "Hey, remind me upcoming event from calendar"},
        {"role": "assistant", "content": "task is fetching upcoming events from all available Calendars"},

        # Calendar: Today's events for all available calenders
        {"role": "user", "content": "Give me my today's events"},
        {"role": "assistant", "content": "task is fetching today's events from all available Calendars"},
        {"role": "user", "content": "AI tell me my today's event from calendar"},
        {"role": "assistant", "content": "task is fetching today's events from all available Calendars"},
        {"role": "user", "content": "fetch the today's event from calendar for me please"},
        {"role": "assistant", "content": "task is fetching today's events from all available Calendars"},
        {"role": "user", "content": "Can you please give me my today's event from calendar?"},
]