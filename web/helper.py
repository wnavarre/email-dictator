import string
import sys

def web_template(path):
    with open(path, 'r') as f:
        template_string = f.read()
    return string.Template(template_string)

def headers(target=sys.stdout):
    target.write("Content-type:text/html\n")
    target.write("\n")
