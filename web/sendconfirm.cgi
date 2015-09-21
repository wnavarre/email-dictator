#!/usr/bin/env python
import cgi
import run_on
import json

print "Content-type: Application/json"
print ""

try:
    editor = cgi.FieldStorage()['editor_email'].value
    key = cgi.FieldStorage()['msg_key'].value
    run_on.run_on(key, actually_send=False,
                  send_default_confirmation=False,
                  confirmation_email=editor)
    out = json.dumps({"success": "success"})
    print out
except:
    out = json.dumps({"success": "failure"})
    print out
    raise
