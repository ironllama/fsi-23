from flask import Flask
from sqlalchemy import create_engine

app = Flask(__name__)
app.secret_key = 'ElephantintheRoomLongInTheTooth'

sql = create_engine('mariadb+mariadbconnector://root:@127.0.0.1:3306/fsi-23')

import chat.views
