import sqlite3
conn = sqlite3.connect('filedb.db')
c = conn.cursor()
c.execute('''CREATE TABLE files (fileset text, filename text, filekey text)''')
conn.commit()
conn.close()
