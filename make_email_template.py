HEADER_ENDING = "###"

import template
import string

def split_header(data):
    colon = string.find(data, ":")
    assert(colon > -1)
    key = data[0 : colon].capitalize()
    val = data[colon +1 : ]
    return (key, val)

def get_template(filename):
    fp = open(filename, 'r')
    header_mode = True
    body = ""
    fields = {}
    while True:
        data = fp.readline()
        if data.strip() == "###":
            break
        key, value = split_header(data)
        key = key.strip()
        value = value.strip()
        fields[key] = value
    body = "".join(fp.readlines())
    fields["Body"] = body
    return fields
