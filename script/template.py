import config
import template
import string
import auxilary_not_fucking_aux_because_windows
import email
import mess
import sys

HEADER_ENDING = config.HEADER_ENDING
SEPARATOR = config.SEPARATOR
LAMBDA = config.LAMBDA

def split_header(data):
    '''
    data: a string of the form "header_name: header_value"
    returns: a tuple of the form (header_name, header_value)
    '''
    colon = string.find(data, ":")
    assert(colon > -1)
    key = data[0 : colon].capitalize()
    val = data[colon +1 : ]
    return (key, val)

class Template():
    def __init__(self, template_string):
        self.template_string = template_string
    def render_all(self, variable_values, function_values, onLookupFail):
        '''
        returns a string where all fields of the template have been resolved according
        to variable_values and function_values.
        
        variable_values: dictionary (variable_name -> variable_value)
        function_values: dictionary (function_name -> function)
        '''
        fragments_in = self.template_string.split(SEPARATOR)
        fragments_out = []
        for i in range(len(fragments_in)):
            if i%2 == 0:
                to_append = fragments_in[i]
            else:
                try:
                    to_append = self.render_one(fragments_in[i], variable_values, function_values)
                except KeyError:
                    caught = onLookupFail(fragments_in[i])
                    if not caught: raise
            fragments_out.append(to_append)
        return "".join(map(str, fragments_out))

    def render_one(self, placeholder, variable_values, function_values):
        if auxilary_not_fucking_aux_because_windows.starts_with(LAMBDA, placeholder):
            function_name = placeholder[len(LAMBDA):]
            return function_values[function_name](variable_values, function_values)
        else:
            # Normal variable case.
            return variable_values[placeholder]

class EmailTemplate():
    def __init__(self, file_reference):
        self.fields = {}
        while True: # get the headers.
            line = file_reference.readline().strip()
            if line.strip() == HEADER_ENDING: break
            k, v = split_header(line)
            self.fields[k] = Template(v)
        self.body = Template("".join(file_reference.readlines()))

    def render(self, variable_values, function_values, onFail=lambda x: False):
        has_failed = False
        def on_fail_local(failure):
            has_failed = True
            out = onFail(failure)
            assert(out)
            return out
        rendered_body = self.body.render_all(variable_values,
                                             function_values,
                                             on_fail_local)
        rendered_fields = {}
        rendered_fields = {field_name: field_value.render_all(variable_values, 
                                                          function_values, 
                                                          on_fail_local)
                           for (field_name, field_value) in self.fields.items()}
        if has_failed:
            return Exception
        else:
            return mess.Message(rendered_fields, rendered_body)
