
import configparser

import sqlite3
import alpaca_trade_api as tradeapi

# from sql.script import read





if __name__ == '__main__':
    db = sqlite3.connect('data/app.db')
    
    config = configparser.ConfigParser()
    config.read('../config.ini')
    print(config.get('alpaca','key_public'))
    
    api = tradeapi.REST()