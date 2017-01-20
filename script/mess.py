import smtplib
import config

from email.mime.text import MIMEText
from time import sleep

SLEEP_TIME = config.SLEEP_TIME
VALID_MESSAGE_HEADERS = ["To", "From", "Subject", "Cc"]
VALID_MESSAGE_FIELDS = VALID_MESSAGE_HEADERS + ["Bcc", "Body"]

def validateFields(fields):
    '''Require that all fields used are legitimate.
    return dictionary where all fields used.
    '''
    for i in fields:
        assert i in VALID_MESSAGE_FIELDS,
            "Message field {} is invalid".format(i)
    out = {}
    for i in VALID_MESSAGE_FIELDS:
        if i in fields:
            out[i] = fields[i]
        else:
            out[i] = ""
    return out

def addressList(st):
    '''Accepts a string of comma-
    separated items.  
    Returns a list of the
    items.'''
    entries = st.split(",")
    out = []
    for i in entries: 
        entry = i.strip()
        if entry == "":
            continue
        else: 
            out.append(entry)
    return out

class Message:
    def __init__(self, headers, body):
        fields = validateFields(headers)
        self.to_envelope = addressList(fields["To"])+addressList(fields["Bcc"])+addressList(fields["Cc"])
        self.from_envelope = fields["From"]
        msg = MIMEText(body)
        for f in VALID_MESSAGE_HEADERS:
            msg[f] = fields[f]
        self.msg_string = msg.as_string()

    def __str__(self):
        return str("\nMESSAGE##############\nRECIPIENTS: "+ str(self.to_envelope) + "\nENV_FROM: "+ self.from_envelope + "\n" + self.msg_string + "\n")

    def __repr__(self):
        return str(self)

    def send(self, connection):
        connection.sendmail(self.from_envelope, self.to_envelope, self.msg_string)
        sleep(SLEEP_TIME)
    
