from typing import List, Dict
from flask import Flask
import mysql.connector
import json

app = Flask(__name__)


def favorite_colors() -> List[Dict]:
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'token_pooling'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute('SELECT token_name, used_count FROM tokens')
    print(cursor)
    results = [{token_name: used_count} for (token_name, used_count) in cursor]
    cursor.close()
    connection.close()

    return results


@app.route('/')
def index() -> str:
    return json.dumps({'favorite_colors': favorite_colors()})

@app.route('/he')
def hes() -> str:
    return json.dumps({'Hii': "asdasdasdsad"})

if __name__ == '__main__':
    app.run(host='0.0.0.0')
