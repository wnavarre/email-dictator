
boolean_strict = True #Prompt on boolean error? 
boolean_default = None #If boolean fails, what is assumed.  Does nothing if boolean_strict = True

boolean_true = ["y", "yes", "true", "t"]
boolean_true = boolean_true + [x + "." for x in boolean_true]
boolean_false = ["n", "no", "false", "f"]
boolean_false = boolean_false + [x + "." for x in boolean_false]

interface_true = ["t", "true"]
interface_false = ["f", "false"]

def parse_cell(cell):
    return cell.strip()

def get_boolean(cell, t = boolean_true, f = boolean_false):
    cell = cell.lower() #Case Insensitive.  
    if cell in t:
        return True
    if cell in f:
        return False
    if not boolean_strict:
        return boolean_default
    while True:
        user = raw_input("Have value'", cell+"'.  How should this evaluate?  (T/F)?")
        user = user.lower()
        user.strip()
        if user in interface_true:
            return True
        if user in interface_false:
            return False
