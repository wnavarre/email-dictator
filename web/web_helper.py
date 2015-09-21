import string
import sys
import files.io
import constants

def web_template(path):
    with open(path, 'r') as f:
        template_string = f.read()
    return string.Template(template_string)

def headers(target=sys.stdout):
    target.write("Content-type:text/html\n")
    target.write("\n")

def get_main_files_from_FieldStorage(fields):
    try:
        key = fields['msg_key'].value
    except KeyError:
        key = ""
    vals = files.io.get(key)
    files_dict = {}
    for filename in constants.MAIN_SCRIPT_INPUTS:
        files_dict[filename] = vals.get(filename, "")
    return files_dict
