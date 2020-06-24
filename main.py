import sqlite3
from sqlite3 import Error

def create_conntcrion(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
    except Error as e:
        print(f'The error "{e}" occurred')

    return connection

create_conntcrion('first_db')