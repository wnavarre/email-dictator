import sys
import os
import files.io
from StringIO import StringIO
from constants import *

added_path = os.path.join(os.path.dirname(os.path.abspath(os.path.dirname(__file__))), "script")
sys.path.append(added_path)
import script
import mess
sys.path.pop()

def full_file(pointer):
    pointer.seek(0)
    return pointer.read()

def send_confirmation_email(recipient, contents):
    connection = script.get_mailserver_connection()
    email_headers = {
        "Subject": CONFIRMATION_EMAIL_SUBJECT,
        "To": recipient,
        "From": CONFIRMATION_EMAIL_FROM
    }
    mess.Message(email_headers, contents).send(connection)
    connection.quit()

def run_on(key, actually_send=False, confirmation_email=CONFIRMATION_EMAIL_FROM, confirmation_email_on_success=True, confirmation_email_on_fail=True, special_text="", send_default_confirmation=False):
    input_files = files.io.get(key)
    assert "template" in input_files, "Need to submit non-empty template"
    assert "spreadsheet" in input_files, "Need to submit non-empty spreadsheet"
    output_location = StringIO()
    kwargs = {}
    if send_default_confirmation:
        pass
    else:
        kwargs["send_confirmation_to"] = None
    if "constants" in input_files:
        kwargs["constants"] = StringIO(input_files["constants"])
    success = script.run_script(
        StringIO(input_files["template"]),
        StringIO(input_files["spreadsheet"]),
        output=output_location,
        actually_send=actually_send,
        **kwargs
    )
    script_results = special_text + full_file(output_location)
    if confirmation_email and ((confirmation_email_on_success and success) or (confirmation_email_on_fail and not success)):
        send_confirmation_email(confirmation_email, script_results)
    return script_results, success
