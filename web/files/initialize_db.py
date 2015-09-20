import sqlite3
import constants
conn = sqlite3.connect(constants.DBFILE)
c = conn.cursor()
c.execute('''CREATE TABLE files (fileset text, filename text, filekey text)''')
conn.commit()
conn.close()
