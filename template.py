import string
import email
import mess

SEPARATOR = "@@@"
LAMBDA = "\\"

class SimpleTemplate:
    def __init__(self, inp):
        self.render = self.template(inp)

    def _parseField(self, inp):
        def out(vals, funcs):
            assert(type(vals)==dict)
            if inp[0] == LAMBDA:
                name = inp[1:]
                return funcs[name](vals, funcs)
            else:
                return vals[inp]
        return out

    def _parse(self, (inp, isfield), vals, funcs):
        if isfield:
            return str(self._parseField(inp)(vals, funcs))
        else:
            return str(inp)

    def template(self, st):
        is_field = False
        pieces = [([], not is_field)] + string.split(st, SEPARATOR)
        def helper((out_list, was_field), elem, vs, fs):
            new_list = out_list + [self._parse((elem, not was_field), vs, fs)]
            return (new_list, not was_field)
        def out(vals, funcs = {}):
            return "".join(reduce(lambda x, y: helper(x, y, vals, funcs), pieces)[0])
        return out

class EmailTemplate:
    def __init__(self, fields):
        assert(type(fields)==dict)
        #mess.validateFields(fields)
        self.templates = {k : SimpleTemplate(v) for (k, v) in fields.items()}

    def render(self, vals, funcs):
        assert(type(vals)==dict)
        out = {k : v.render(vals, funcs) for (k, v) in self.templates.items()}
        return mess.Message(out)
