#!/usr/bin/env python
import cgi
import constants
import files.io
import os
import web_helper as helper

helper.headers()

HERE = os.path.dirname(__file__)

fields = cgi.FieldStorage()
template_dict = helper.get_main_files_from_FieldStorage(fields)
template_path = os.path.join(HERE, "templates", "edit.html")
print helper.web_template(template_path).substitute(**template_dict)
