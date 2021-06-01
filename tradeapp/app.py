
import configparser

import sqlite3
import alpaca_trade_api as tradeapi

from tradeapp.sql.script import read

from tradeapp.sql import *


if __name__ == '__main__':
    db = sqlite3.connect('data/app.db')
    
    config = configparser.ConfigParser()
    config.read('config.ini')
    api = tradeapi.REST(config.get('alpaca','key_public'),
                        config.get('alpaca','key_secret'),
                        config.get('alpaca','endpoint_paper'))

    assets = api.list_assets()
    
    for asset in assets:
        try:
            db.execute

    db.commit()
    db.close()
    