#!/usr/bin/env python
import cgi
import constants
import files.io
import files.constants
import web_helper as helper
import sys

fields = cgi.FieldStorage()

to_save = {}
for field_name in constants.MAIN_SCRIPT_INPUTS:
    try:
        to_save[field_name] = fields[field_name].value
    except KeyError:
        pass
key = files.io.put(to_save)
print "Location: review.cgi?msg_key="+str(key)
print ""
