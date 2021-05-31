#####################
# Set up the app from scratch
#
#
#####################

from configparser import ConfigParser

import sqlite3

from sql.script import read


########################################
#  Part 1 - Create/Populate Config file
########################################
config = ConfigParser()

config['alpaca'] = {}
config['alpaca']['key_public'] = 'PKQ2FWHNVLVPQGVIWNW5'
config['alpaca']['key_private'] = 'nQ4MQkD3nn5SvCnYK3tVsOFhp0h2T4vhfviLuRct'
config['alpaca']['endpoint_paper'] = 'https://paper-api.alpaca.markets'

with open('../config.ini', 'w') as conf:
    config.write(conf)


########################################
#  Part 2 - Create the database and tables
########################################
db = sqlite3.connect('data/app.db')
cursor = db.cursor()

setup = read('setup.sql')
cursor.executescript(setup)

populate = read('populate.sql')
cursor.executescript(populate)

db.commit()
db.close()
