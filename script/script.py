import template
import template
import smtplib
import config
import mess
import csv
import sys

CSV_DELIMITER = config.CSV_DELIMITER

def run_script(template_file, spreadsheet_file, RELEVANT=lambda x, y: True, funcs = {}, output=sys.stdout, actually_send=config.SEND, send_confirmation_to=config.CONFIRMATION_EMAIL):
    email_template = template.EmailTemplate(template_file)
    rows = csv.DictReader(spreadsheet_file, delimiter="\t")
    emails = []
    missing_fields = set([])
    def lookupFail(key):
        missing_fields.add(key)
        return True
    #MAKE ALL THE EMAILS.
    for row in rows:
        if RELEVANT(row, funcs):
            email = email_template.render(row, funcs, onFail=lookupFail)
            emails.append(email)

    if missing_fields:
        output.write("ERROR!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
        output.write("THE SYSTEM CANNOT RESOLVE THESE FIELDS:\n")
        for field in sorted(list(missing_fields)):
            output.write("-> " + field + "\n")
        return False
    connection = smtplib.SMTP(config.SERVER)

    if actually_send:
        for email in emails:
            email.send(connection)

    email_str = [str(email) for email in emails]
    confirm = "EMAILS SET TO SEND? "+str(actually_send)+"\n"+"\n".join(email_str)    
    if send_confirmation_to:
        email_dict = {"Subject": "Confirmation", "From": send_confirmation_to, "To": send_confirmation_to}
        mess.Message(email_dict, confirm).send(connection)
    connection.quit()
    output.write(confirm)
    return True

def get_mailserver_connection():
    return smtplib.SMTP(config.SERVER)
