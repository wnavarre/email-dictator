import template
import template
import smtplib
import config
import mess
import csv
import sys

CSV_DELIMITER = config.CSV_DELIMITER

def run_script(template_file, spreadsheet_file, RELEVANT = lambda x, y: True, funcs = {}, output=sys.stdout, actually_send=config.CONFIRMATION_EMAIL):
    email_template = template.EmailTemplate(template_file)
    rows = csv.DictReader(spreadsheet_file)
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

    return
    connection = smtplib.SMTP(config.SERVER)
            
    for i in emails:
        output.write(str(i)+"\n")

    if config.SEND:
        for email in emails:
            email.send(connection)
    if config.CONFIRMATION_EMAIL:
        email_str = [str(email) for email in emails]
        confirm = "EMAILS SET TO SEND? "+str(config.SEND)+"\n"+"\n".join(email_str)    
        email_dict = {"Body": confirm, "Subject": "Confirmation", "From": config.CONFIRMATION_EMAIL, "To": config.CONFIRMATION_EMAIL}
        mess.Message(email_dict).send(connection)

    connection.quit()
    return True
