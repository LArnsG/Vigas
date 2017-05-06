import vigas_database as data
import strutural_analysis as structural

beam_name = 'v1' #input('Nome da viga:')
height = 40 #int(input('Altura da viga [cm]:'))
width = 20 #int(input('Largura da viga [cm]:'))
beam_length = 200 #int(input('Vão da viga [cm]:'))
load = 5 #int(input('Carga atuante [kgf/cm]:'))
fck = 2.5 #float(input('Concreto (padrão C25): [MPa]'))/10 #kN/cm²
cobrimento = 2 #int(input('Cobrimento da armadura (padrão = 2 cm): [cm]'))
fyd = 50 / 1.4

data.create_table()
# data.data_entry(beam_name, height, width, beam_length, load, fck, cobrimento, 0, 0, 0)

structural.beam_design(fck, fyd, height, width, beam_length, load, cobrimento)

