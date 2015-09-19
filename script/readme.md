Mailmerge program by William Navarre.

Run with "python run.py"

Template: 
   Stored as specified in run.py
   First lines are email headers (see mess.py for allowed headers.  Do not use "Body").  The format is as here: "To:navarre@mit.edu"
   Next line is "###"
   The rest of the line are messages.  
   @@@varname@@@ maps to the value of varname.  varname may NOT begin with a backslash.  
   @@@\funname@@@ maps to the value of funname.  The first argument is a dictinary of variable mappings, the second argument is a dictionary function mappings. 
   The string "@@@" may not appear in any message output.  
   @@@varname@@@ and @@@\funname@@@ can be used in any VALUE, including the body and headings.  They may *not* be used in heading names.  

Spreadsheet:
   Stored as specified in run.py
   Tab delineated.  
   Entries in first row act as headers (field names).  
   Each additional row corresponds to one email.  

run.py:
   Run run.py to run the script.  
   This is the declaration for the run function: 
   	 run(TEMPLATE_FILE, SPREADSHEET_FILE, RELEVANT = lambda x, y: True, FUNCS = {})
   TEMPLATE_FILE is a string for the path to that file.  
   SPREADSHEET_FILE is a string for the path to that file. 
   RELEVANT is a boolean function over the values dictionary and the funcs dictionary.  An email is sent only if RELEVANT returns a True value.  Otherwise, the row that generated that value dictionary is omitted from output.  
   FUNCS define functions in a dictionary (key: string, val: dict -> dict -> string).  Each function takes the values dictionary, the funcs dictionary, and returns a string.  

debugging and confirmations: 
   Add yourself to esp-email@mit.edu to receive debugging/confirmation information.  If you're using this for something not ESP, or to not send debugging emails or confirmations, change CONFIRMATION_EMAIL to an empty string in config.py
