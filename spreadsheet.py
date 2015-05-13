import data

DELIMITER = "\t"

def onerow(cells, keys):
    out = {}
    i = 0
    for key in keys:
        out[key] = cells[i].strip()
        i += 1
    return out

def import_spreadsheet(filename):
    fp = open(filename, 'r')
    keys = fp.readline().split(DELIMITER)
    keys = [data.parse_cell(key) for key in keys]
    out = []
    for line in fp.readlines():
        line.strip()
        cells = line.split(DELIMITER)
        if len(keys) > len(cells):
            continue
        out.append(onerow(cells, keys))
    return out
