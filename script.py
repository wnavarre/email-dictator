import make_email_template
import spreadsheet
import template
import smtplib
import config
import mess

def run(TEMPLATE_FILE, SPREADSHEET_FILE, RELEVANT = lambda x, y: True, FUNCS = {}):
    template_data = make_email_template.get_template(TEMPLATE_FILE)
    rows = spreadsheet.import_spreadsheet(SPREADSHEET_FILE)

    ourTemplate = template.EmailTemplate(template_data)

    emails = []
    for row in rows:
        if RELEVANT(row, FUNCS):
            emails.append(ourTemplate.render(row, FUNCS))

    connection = smtplib.SMTP(config.SERVER)

    [print i for i in emails]

    if config.SEND:
        for email in emails:
            email.send(connection)

    if config.CONFIRMATION_EMAIL:
        email_str = [str(email) for email in emails]
        confirm = "EMAILS SET TO SEND? "+str(config.SEND)+"\n"+"\n".join(email_str)    
        email_dict = {"Body": confirm, "Subject": "Confirmation", "From": config.CONFIRMATION_EMAIL, "To": config.CONFIRMATION_EMAIL}
        mess.Message(email_dict).send(connection)

    connection.quit()
