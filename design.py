import math
import vigas_database as data
import strutural_analysis as analysis


def minimum_steel_area(height, width):
    concrete_area = height * width
    as_minimum = 0.0015 * concrete_area
    as_maximum = 0.04 * concrete_area
    return {'min': as_minimum, 'max': as_maximum}


def set_domains(d):
    # global x_2_lim, x_3_lim
    x_2_lim = 0.26 * d
    x_3_lim = 0.63 * d
    x_lim = 0.45 * d
    return {'x_23': x_2_lim, 'x_34': x_3_lim, 'x_lim': x_lim}


def beam_design(fck, fyd, height, width, beam_length, load, cobrimento):
    # global fck, fyd, height, width, beam_length, load, cobrimento
    stresses = analysis.isostatic_stress(beam_length, load)
    minimum_steel = minimum_steel_area(height, width)
    b = width
    d = height - cobrimento
    d_line = cobrimento
    x_domains = set_domains(d)
    m_d = stresses['positive_moment'] * 1.4
    print('Momento de projeto = {a:.2f} kN/cm²'.format(a=m_d))

    fcd = fck / 1.4
    e_yd = 0.00207 # fyd/Es = 43.48/21000
    raiz = (1 - m_d / (0.425 * b * math.pow(d, 2) * fcd))

    x = 1.25 * d * (1 - math.sqrt(raiz))

    print('x: {a:.2f} cm'.format(a=x))

    if x < x_domains['x_34']:
        as_simple = m_d / (fyd * (d - 0.4 * x))
        if x_domains['x_34'] > x > x_domains['x_23']:
            print('Dominio 3')
        else:
            print('Dominio 2')

        print("Armadura necessária: {a:.2f} cm2".format(a=as_simple))

    else: # x > x_domains['x_lim']:
        print('Dominio 4')
        # lembrar que => y = 0.8 * x
        x_4 = x_domains['x_lim']

        as_line = (m_d - 0.85 * fcd * b * (0.8 * x_4) * (d - 0.4 * x_4)) / (fyd * (d - d_line))
        as_simple = (0.85 * fcd * b * (0.8 * x_4) + as_line * fyd) / fyd

        print("Armaduras necessárias:")
        print("As = {a:.2f} cm2".format(a=as_simple))
        print("As' = {a:.2f} cm2".format(a=as_line))


def beam_reinforcement():
    # pegar todas bitolas, realizar comparativo com areas
    data.get_steel_area(8.0)

