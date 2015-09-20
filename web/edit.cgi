#!/usr/bin/env python
import cgi
import constants
import files.io
import os
import helper

helper.headers()

HERE = os.path.dirname(__file__)

fields = cgi.FieldStorage()
try:
    key = fields['msg_key'].value
except KeyError:
    key = ""
vals = files.io.get(key)

template_dict = {}
for placeholder in constants.MAIN_SCRIPT_INPUTS:
    template_dict[placeholder] = vals.get(placeholder, "")

template_path = os.path.join(HERE, "templates", "edit.html")
print helper.web_template(template_path).substitute(**template_dict)
