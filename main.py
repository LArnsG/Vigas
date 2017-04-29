import vigas_database as data

beam_name = input('Nome da viga:')
height = 40
width = 20
length = 250

load = 500

data.create_table()
data.data_entry(beam_name, height, width, length, load)




