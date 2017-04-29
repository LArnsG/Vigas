import sqlite3
import time, datetime, random
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import style
style.use('fivethirtyeight')

#se não existir, é criado
conn = sqlite3.connect('beams_data.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS iso_beams(unix REAL,'
              ' datestamp TEXT, keyword TEXT, value REAL)')
