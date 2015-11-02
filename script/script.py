import template
import template
import smtplib
import config
import mess
import csv
import sys

CSV_DELIMITER = config.CSV_DELIMITER

def run_script(template_file, spreadsheet_file, RELEVANT=lambda x, y: True, funcs = {}, constants=None, output=sys.stdout, actually_send=config.SEND, send_confirmation_to=config.CONFIRMATION_EMAIL):
    email_template = template.EmailTemplate(template_file)
    rows = csv.DictReader(spreadsheet_file)
    constant_mappings = {}
    if constant_mappings is not None:
        constant_rows = csv.DictReader(spreadsheet_file, fieldnames=("key", "val"))
        for contant_row in constant_rows:
            if constant_row["key"] in constant_mappings:
                output.write("ERROR!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
                output.write("A REPEAT CONSTANT IS PROVIDED!\n")
                return false
            constant_mappings[constant_row["key"]] = constant_row["val"]

    emails = []
    missing_fields = set([])
    def lookupFail(key):
        missing_fields.add(key)
        return True
    #MAKE ALL THE EMAILS.
    for row in rows:
        if RELEVANT(row, funcs):
            rows_with_constants = row.copy()
            rows_with_constants.update(constant_mappings)
            if not len(row.keys()) + len(constant_mappings.keys()) == len(rows_with_constants):
                output.write("ERROR!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
                output.write("A FIELD IS PROVIDED EXPLICITLY AS BOTH A CONSTANT AND A COLUMN");
                return false
            rows_with_constants_and_builtins = config.DEFAULT_CONSTANTS()
            rows_with_constants_and_builtins.update(rows_with_constants)
            email = email_template.render(rows_with_constants_and_builtins, funcs, onFail=lookupFail)
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
