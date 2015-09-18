import config

boolean_strict = config.BOOLEAN_STRICT 
boolean_default = config.BOOLEAN_DEFAULT

boolean_true = ["y", "yes", "true", "t"]
boolean_true = boolean_true + [x + "." for x in boolean_true]
boolean_false = ["n", "no", "false", "f"]
boolean_false = boolean_false + [x + "." for x in boolean_false]

interface_true = ["t", "true"]
interface_false = ["f", "false"]

def parse_cell(cell):
    return cell.strip()

def get_boolean(cell):
    cell = cell.lower() # Case Insensitive.  
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

def starts_with(prefix, string):
    return bool(string[0:len(prefix)] == prefix)
