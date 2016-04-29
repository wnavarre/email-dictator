#!/usr/bin/env python
import cgi
import constants
import files.io
import os
import web_helper as helper
import run_on

helper.headers()
HERE = os.path.dirname(__file__)

key = cgi.FieldStorage()['msg_key'].value
special_string = "This is msg id " + key + "\n" + "####################################################\n\n"
result, success = run_on.run_on(
    key,
    actually_send=False,
    confirmation_email=None,
    special_text = special_string)
button = '<button type="submit" >SEND ALL THE EMAILS!</button>' if success else ""
template = helper.web_template(os.path.join(HERE, "templates", "review.html"))
print template.substitute(key=key, stdout=result, button=button)