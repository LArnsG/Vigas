import vigas_database as data

beam_name = input('Nome da viga:')
height = int(input('Altura da viga [cm]:'))
width = int(input('Largura da viga [cm]:'))
length = int(input('Vão da viga [cm]:'))
load = int(input('Carga atuante [kgf/cm]:'))

data.create_table()
data.data_entry(beam_name, height, width, length, load, 0, 0, 0)




