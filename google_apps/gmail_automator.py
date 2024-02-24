# importing
from __init__ import create_service

import os
import base64
import mimetypes
from email.mime.multipart import MIMEMultipart
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.text import MIMEText


class Gmail:

    def __init__(self):
        self.sender_email = "your@gmail.com"
        try:
            self.service = create_service('gmail', 'v1')
        except:
            print("Oops..\nSomething went wrong")

    #  (PART 1)---> FOR CREATING AND SENDING EMAILS

    # for creating msg without attachment
    def create_message(self, receiver_email: str, subject: str, email_body: str):

        # Create a multipart message
        message = MIMEMultipart('alternative')

        # Set the sender, receiver, and subject of the message
        message['from'] = self.sender_email
        message['to'] = receiver_email
        message['subject'] = subject

        # Attach the email body as plain text to the message
        message.attach(MIMEText(email_body, 'plain'))
        # Return the raw message in dictionary format
        return {'raw': base64.urlsafe_b64encode(message.as_string().encode('utf-8')).decode()}

    # for creating msg with attachment
    def create_message_with_attachment(self, receiver_email: str, subject: str, email_body: str, file: str):

        # Create a MIMEMultipart message object.
        message = MIMEMultipart()

        # Set the recipient email, sender email and subject fields of the message.
        message['to'] = receiver_email
        message['from'] = self.sender_email
        message['subject'] = subject

        # Create a MIMEText object and attach it to the message.
        msg = MIMEText(email_body)
        message.attach(msg)

        # Guess the content type of the file to be attached.
        content_type, encoding = mimetypes.guess_type(file)

        # If the content type is not known or the file is encoded, set the content type to 'application/octet-stream'.
        main_type, sub_type = None, None
        if content_type is None or encoding is not None:
            content_type = 'application/octet-stream'
            main_type, sub_type = content_type.split('/', 1)

        # Depending on the content type, create the appropriate MIME object and attach it to the message.
        if main_type == 'text':
            fp = open(file, 'rb')
            msg = MIMEText(fp.read().decode("utf-8"), _subtype=sub_type)
            fp.close()

        elif main_type == 'image':
            fp = open(file, 'rb')
            msg = MIMEImage(fp.read(), _subtype=sub_type)
            fp.close()

        elif main_type == 'audio':
            fp = open(file, 'rb')
            msg = MIMEAudio(fp.read(), _subtype=sub_type)
            fp.close()

        else:
            fp = open(file, 'rb')
            msg = MIMEBase(main_type, sub_type)
            msg.set_payload(fp.read())
            fp.close()

        # Set the filename and content disposition of the attachment.
        filename = os.path.basename(file)
        msg.add_header('Content-Disposition', 'attachment', filename=filename)

        # Attach the MIME object to the message.
        message.attach(msg)

        # Encode the message in base64 and return the raw message in a dictionary.
        raw_message = base64.urlsafe_b64encode(message.as_string().encode("utf-8"))
        return {'raw': raw_message.decode("utf-8")}

    # for creating draft
    def create_draft(self, email_body: str):
        try:
            # Create message object
            message = {'message': email_body}

            # Create draft message
            draft = self.service.users().drafts().create(userId=self.sender_email, body=message).execute()
            # Print draft information
            print("Draft id: %s\nDraft message: %s" % (draft['id'], draft['message']))
            # Return draft message
            return draft

        except:
            # Handle exception
            print("Sir, something went wrong.")
            return None

    # for sending email with above created msg
    def send_message(self, message):
        try:
            message = self.service.users().messages().send(userId=self.sender_email, body=message).execute()
            return message
        except:
            # In case of an error, return None.
            print("Sir, something went wrong.")
            return None

    #  (PART 2)---> FOR FETCHING EMAILS AND EMAILS DATA
