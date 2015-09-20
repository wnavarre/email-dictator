import io

def execute_test(input_dict):
    dict_expected = input_dict.copy()
    set_id = io.put(input_dict)
    received = io.get(set_id)
    print set_id, received
    assert (dict_expected == received)

dicts = []

dicts.append({})
dicts.append({'spreadsheet': 'contents1'})
dicts.append({'template': '\n\ncontents2', 'spreadsheet':'contents3\n\n'})

for d in dicts:
    execute_test(d)
