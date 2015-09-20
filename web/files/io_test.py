import io

def execute_test(input_dict):
    dict_expected = input_dict.copy()
    set_id = io.put(input_dict)
    received = io.get(set_id)
    print set_id, received
    assert (dict_expected == received)

dicts = []

dicts.append({})
dicts.append({'file1': 'contents1'})
dicts.append({'file2': '\n\ncontents2', 'file3':'contents3\n\n'})

for d in dicts:
    execute_test(d)
