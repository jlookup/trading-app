#####################
#
#
#
#####################


import sqlite3

from sql.script import read

db = sqlite3.connect('app.db')
cursor = db.cursor()

setup = read('setup.sql')
cursor.executescript(setup)

db.commit()
db.close()