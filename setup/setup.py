#####################
#
#
#
#####################


import sqlite3

from tradingapp.sql.script import read

db = sqlite3.connect('app.db')
cursor = db.cursor()

setup = read('setup.sql')
cursor.executescript(setup)

populate = read('populate.sql')
cursor.executescript(populate)

db.commit()
db.close()
