"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-cgrqh5g2qv2dcb95mgf0-a",
        database="todo_zimo",
        user="root",
        password="pnKeawhROCEEQiFLEZToIvN8FTp0vDMp")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
