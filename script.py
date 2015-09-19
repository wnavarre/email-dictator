import template
import template
import smtplib
import config
import mess
import csv
CSV_DELIMITER = config.CSV_DELIMITER
def run_script(template_file, spreadsheet_file, RELEVANT = lambda x, y: True, FUNCS = {}):
    email_template = template.EmailTemplate(template_file)
    rows = csv.DictReader(spreadsheet_file)
    emails = []
    for row in rows:
        print row
        if RELEVANT(row, FUNCS):
            emails.append(email_template.render(row, FUNCS))
    connection = smtplib.SMTP(config.SERVER)

    for i in emails:
        print i

    if config.SEND:
        for email in emails:
            email.send(connection)

    if config.CONFIRMATION_EMAIL:
        email_str = [str(email) for email in emails]
        confirm = "EMAILS SET TO SEND? "+str(config.SEND)+"\n"+"\n".join(email_str)    
        email_dict = {"Body": confirm, "Subject": "Confirmation", "From": config.CONFIRMATION_EMAIL, "To": config.CONFIRMATION_EMAIL}
        mess.Message(email_dict).send(connection)
    connection.quit()

