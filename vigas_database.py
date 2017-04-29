import sqlite3
from matplotlib import style
style.use('fivethirtyeight')

#se não existir, é criado
conn = sqlite3.connect('beams_data.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS iso_beams(beam_name TEXT,'
              ' height REAL, width REAL, length REAL, load REAL, positive_armor REAL, negative_armor REAL,'
              ' shear_armor REAL)')

def data_entry(name, height, width, length, load, positive_armor, negative_armor, shear_armor):
    c.execute("INSERT INTO stuffToPlot VALUES("
              "%(1)s,%(2)s,%(3)s,%(4)s,%(5)s,%(6)s,%(7)s,%(8)s)"
              % {'1': name, '2': height, '3': width, '4': length, '5': load,
                 '6': positive_armor, '7': negative_armor, '8': shear_armor})
    conn.commit()
    c.close()
    conn.close()
