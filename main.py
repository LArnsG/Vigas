import vigas_database as data

beam_name = input('Nome da viga:')
height = int(input('Altura da viga:'))
width = int(input('Largura da viga:'))
length = int(input('Vão da viga:'))
load = int(input('Carga atuante:'))

data.create_table()
data.data_entry(beam_name, height, width, length, load, 0, 0, 0)




