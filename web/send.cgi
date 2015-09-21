#!/usr/bin/env python
import cgi
import run_on

key = cgi.FieldStorage()['msg_key'].value
run_on.run_on(key, actually_send=True,
              send_default_confirmation=True)
print "Location: success.html"
print ""
