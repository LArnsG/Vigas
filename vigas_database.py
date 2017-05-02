import sqlite3
from matplotlib import style
style.use('fivethirtyeight')

#se não existir, é criado
conn = sqlite3.connect('beams_data.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS iso_beams(beam_name TEXT,'
              ' height REAL, width REAL, length REAL, load REAL, cobrimento REAL'
              ' positive_armor REAL, negative_armor REAL,'
              ' shear_armor REAL)')

def data_entry(name, height, width, length, load, positive_armor, negative_armor, shear_armor):
    c.execute("INSERT INTO iso_beams "
              "(beam_name, height, width, length, load, cobrimento, positive_armor, negative_armor, shear_armor)"
              "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
              (name, height, width, length, load, positive_armor, negative_armor, shear_armor))
    conn.commit()
    c.close()
    conn.close()
