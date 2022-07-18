import json
import logging
import os
import sys

import requests

from flask import Flask
from mysql.connector import connect
from time import sleep

# Creating and Configuring Logger

Log_Format = "%(levelname)s %(asctime)s - %(message)s"

logging.basicConfig(stream=sys.stdout,
                    format=Log_Format,
                    level=logging.DEBUG)
logger = logging.getLogger()


def log(record):
    logger.debug(record)


def get_weather(use_db=True):

    api_key = os.environ['WEATHER_API_KEY']
    api = f'https://api.openweathermap.org/data/2.5/weather?units=metric&lat=55.7609&lon=37.6703&appid={api_key}'
    # api = f'https://api.openweathermap.org/data/2.5/forecast?units=metric&lat=55.7609&lon=37.6703&appid={api_key}'
    db_host = 'database'
    db_user = os.environ['MYSQL_USER']
    db_pass = os.environ['MYSQL_PASS']
    db_db = os.environ['MYSQL_DATABASE']

    try:
        r = requests.get(api).json()
        result = json.dumps(r)
        log(r)

        if use_db:
            conn = connect(host=db_host, user=db_user, password=db_pass)
            cursor = conn.cursor()
            query = f'INSERT INTO {db_db}.weather (`data`) VALUES (\'{result}\');'
            cursor.execute(query)
            conn.commit()

        return result

    except Exception as e:
        log(f'Something went wrong "{e}"')
        if result:
            return result


app = Flask(__name__)


@app.route('/')
def root():
    return 'The root'


@app.route('/test')
def test():
    return 'The test\n'


@app.route('/greet<name>')
def greet(name):
    return f"Hello, {name}"


@app.route('/weather')
def weather():
    weather_response = get_weather()
    return f"{weather_response}"


if __name__ == '__main__':
    sleep(int(os.environ['BOOT_DELAY']))
    app.debug = True
    app.run(host='0.0.0.0')
