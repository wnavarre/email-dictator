import script

TEMPLATE_FILE = "INP/template.txt"
SPREADSHEET_FILE = "INP/spreadsheet.csv"

template_file = open(TEMPLATE_FILE)
spreadsheet_file = open(SPREADSHEET_FILE)
script.run_script(template_file, spreadsheet_file)
