import template as t

def test_template_once(inp, vals, funcs, output):
    actual = t.Template(inp).parse(vals, funcs)
    print (inp, vals, funcs, output, actual)
    assert(actual == output)
    print True

def test_basic_vals_0():
    test_template_once("", {}, {}, "")
    test_template_once("HI", {}, {}, "HI")

def test_basic_vals_1():
    inp = "@@@HI@@@"
    vals = {"HI": "hEllo", "hi": "hoho"}
    funcs = {}
    output = "hEllo"
    test_template_once(inp, vals, funcs, output)

def test_basic_vals_2():
    inp = "My name is @@@name@@@ and I am @@@age@@@."
    vals = {"name": "William", "age": 20}
    funcs = {}
    output = "My name is William and I am 20."
    test_template_once(inp, vals, funcs, output)

def test_basic_func():
    inp = "I am @@@age@@@ so I can @@@\\tooyoung@@@buy alcohol."
    vals1 = {"age": 20}
    vals2 = {"age": 21}
    def f(vals, funcs):
        if vals["age"] < 21:
            return "not "
        else: 
            return ""
    funcs = {"tooyoung": f}
    output1 = "I am 20 so I can not buy alcohol."
    output2 = "I am 21 so I can buy alcohol." 
    test_template_once(inp, vals1, funcs, output1)
    test_template_once(inp, vals2, funcs, output2)
    
def test_compound_func():
    inp = "I am @@@age@@@ again so I can @@@\\notiftooyoung@@@buy alcohol."
    vals1 = {"age": 20}
    vals2 = {"age": 21}
    def too_young(vals, funcs):
        return vals["age"] < 21
    def not_if_too_young(vals, funcs):
        if funcs["too_young"]:
            return "not "
        else:
            return ""
    funcs = {"notiftooyoung": not_if_too_young, 
             "too_young": too_young}
    output1 = "I am 20 again so I can not buy alcohol." 
    output2 = "I am 21 again so I can not buy alcohol."
    test_template_once(inp, vals1, funcs, output1)
    test_template_once(inp, vals2, funcs, output2)

test_basic_vals_0()
test_basic_vals_1()
test_basic_vals_2()
test_basic_func()
test_compound_func()
