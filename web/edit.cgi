#!/usr/bin/env python
import cgi
import os
import web_helper as helper

helper.headers()

HERE = os.path.dirname(__file__)

fields = cgi.FieldStorage()
template_dict = helper.get_main_files_from_FieldStorage(fields)
template_path = os.path.join(HERE, "templates", "edit.html")
if template_dict["template"] == "":
    template_dict["template"] = (
            "To: [recipients]\n"
            "From: [sender]\n"
            "Subject: [subject]\n"
            "Cc: [optional cc]\n"
            "Bcc: [optional bcc]\n"
            "###\n"
            "Hello:\n"
            "\n"
            "Your body goes here! You can use @@@variables@@@ which go in the "
            "spreadsheet below if you wish.\n"
            "\n"
            "When you're done, press submit below to preview. Have fun!\n"
    )
if "constants" not in template_dict:
    template_dict["constants"] = ""
print helper.web_template(template_path).substitute(**template_dict)
