import sqlite3
import os
import hashlib

HERE = os.path.dirname(__file__)

def get_path(key):
    return os.path.join(HERE, "data", key)

def get_hash(string):
    h = hashlib.new('md5')
    h.update(string)
    return h.hexdigest()

def put(files):
    db_entries = []
    for filename, contents in files.items():
        filekey = get_hash(contents)
        with open(get_path(filekey), 'w') as file_pointer:
            file_pointer.write(contents)
        entry = (filename, filekey)
        db_entries.append(entry)
    conn = sqlite3.connect("filedb.db")
    c = conn.cursor()
    all_hashes = "ZZZ".join(entry[1] for entry in db_entries)
    set_id = get_hash(all_hashes)
    for entry in db_entries:
        c.execute('''
        INSERT INTO files VALUES
        (?, ?, ?)''', (set_id,) + entry)
    conn.commit()
    conn.close()
    return set_id

def get(set_id):
    conn = sqlite3.connect("filedb.db")
    c = conn.cursor()
    key_list = list(c.execute('''SELECT filename, filekey FROM files WHERE fileset=?''', (set_id,)))
    conn.commit()
    conn.close()
    files = {}
    for filename, filekey in key_list:
        with open(get_path(filekey), 'r') as datafile: 
            files[filename] = datafile.read()
    return files
