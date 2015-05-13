import script
import data

TEMPLATE_FILE = "INP/template.txt"
SPREADSHEET_FILE = "INP/spreadsheet.csv"

def RELEVANT(vals, funcs):
    return True

FUNCS = {}

script.run(TEMPLATE_FILE, SPREADSHEET_FILE, RELEVANT, FUNCS)
