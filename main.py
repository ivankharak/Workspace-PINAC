import eel
from ai_models import models
from apps.google.gmail_bot import GoogleGmailManager



def remove_first_line(x):
    body = '\n'.join(x.splitlines()[4:])

    for line in x.splitlines():
        if "Subject" in line:
            sub = line.replace("Subject: ", "")
    return body, sub


eel.init('UI/web')

@eel.expose
def give_response(query):
    print("Received Query")
    response = models.ask_me(query)

    if "task is sending email" in response:
        body, subject = remove_first_line(response)
        msg = GoogleGmailManager()
        draft = msg.create_draft(body=body, subject=subject)
        print(subject, "\n-------------------------------", body,)
        return subject, body, draft

    else: return response

eel.start('index.html')



