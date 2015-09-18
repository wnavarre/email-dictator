import template
import template
import smtplib
import config
import mess
import csv
CSV_DELIMITER = config.CSV_DELIMITER
def run(TEMPLATE_FILENAME, SPREADSHEET_FILE, RELEVANT = lambda x, y: True, FUNCS = {}):
    with open(TEMPLATE_FILENAME, 'r') as template_file:
        email_template = template.EmailTemplate(template_file)
    with open(SPREADSHEET_FILE, "r") as spreadsheet_file_pointer:
        rows = csv.DictReader(spreadsheet_file_pointer)
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
