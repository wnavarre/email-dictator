import script
import data

TEMPLATE_FILE = "INP/template.txt"
SPREADSHEET_FILE = "INP/spreadsheet.csv"

def RELEVANT(vals, funcs):
    return True
    
def care(vals, funcs):
    if data.get_boolean(vals["should I care?"]):
        return "The spreadsheet says I should care."
    else:
        return "The spreadsheet says I ought not care too much."
FUNCS = {"care": care}

script.run(TEMPLATE_FILE, SPREADSHEET_FILE, RELEVANT, FUNCS)
