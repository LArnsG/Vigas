import sqlite3
import math
from matplotlib import style

style.use('fivethirtyeight')


#se não existir, é criado
conn = sqlite3.connect('beams_data.db')
c = conn.cursor()


def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS iso_beams('
              'beam_name TEXT,'
              'height REAL,'
              'width REAL,'
              'length REAL,'
              'load REAL,'
              'fck REAL,'
              'cobrimento REAL,'
              'positive_armor REAL,'
              'negative_armor REAL,'
              'shear_armor REAL)')

    c.execute('CREATE TABLE IF NOT EXISTS steel_area('
              'bitola TEXT,'
              'area REAL)')


def data_entry(name, height, width, length, load, fck, cobrimento, positive_armor, negative_armor, shear_armor):
    c.execute("INSERT INTO iso_beams "
              "(beam_name, height, width, length, load, fck, cobrimento, positive_armor, negative_armor, shear_armor)"
              "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
              (name, height, width, length, load, fck, cobrimento, positive_armor, negative_armor, shear_armor))
    conn.commit()
    c.close()
    conn.close()


def create_steel_area_table():
    bitolas = [5.0, 6.3, 8.0, 10.0, 12.5, 16.0, 20.0, 25.0, 32.0]
    steel_area = {}

    for i in bitolas:
        area = math.pow(i * .5, 2) * 3.14
        steel_area[i] = area
    # print(steel_area)
    for x in steel_area:
        c.execute(' INSERT INTO steel_area('
                  'bitola, area)'
                  'VALUES(?, ?)',
                  (x, steel_area[x]))
        print(x)
        print(steel_area[x])

