import eel
from ai_models import models
from apps.google.gmail_bot import GoogleGmailManager



def remove_first_line(text):
    
    lines = text.split('\n')
    subject_index = next((i for i, line in enumerate(lines) if "Subject:" in line), None)
    body = '\n'.join(lines[subject_index+2:]) if subject_index is not None else text

    for line in text.splitlines():
        if "Subject" in line:
            sub = line.replace("Subject: ", "")

    return body, sub


eel.init('UI/web')

@eel.expose
def give_response(query):
    
    response = models.ask_me(query)
    print(response)

    if "task is sending email" in response:
        body, subject = remove_first_line(response)
        msg = GoogleGmailManager()
        draft = msg.create_draft(body=body, subject=subject)
        
        body = body.replace("\n", "<br>")
        response = f"Subject: {subject}<br><br>{body}<br><br><br>Email draft created: {draft}"

    return response

eel.start('index.html')
