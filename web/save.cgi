#!/usr/bin/env python
import cgi
import constants
import files.io

fields = cgi.FieldStorage()

to_save = {}
for fieldname in constants.MAIN_SCRIPT_INPUTS:
    try:
        to_save[field_name] = fields[fieldname]
    except KeyError:
        pass

files.io.put(to_save)
