import math

global fck, fyd, height, width, beam_length, load, cobrimento


def isostatic_stress(beam_length, beam_load):
    shear_stress = beam_length * beam_load / 2
    positive_moment = (beam_load * math.pow(beam_length, 2)) / 8

    return {'shear': shear_stress, 'positive_moment': positive_moment}


def minimum_steel_area(height, width):
    concrete_area = height * width
    as_minimum = 0.0015 * concrete_area
    as_maximum = 0.04 * concrete_area
    return {'min': as_minimum, 'max': as_maximum}


def dominios_y(d):
    # global x_2_lim, x_3_lim
    x_2_lim = 0.26 * d
    x_3_lim = 0.63 * d
    return {'x23': x_2_lim, 'x34': x_3_lim}


def beam_design(fck, fyd, height, width, beam_length, load, cobrimento):
    # global fck, fyd, height, width, beam_length, load, cobrimento
    stresses = isostatic_stress(beam_length, load)
    minimum_steel = minimum_steel_area(height, width)
    b = width
    d = height - cobrimento
    dominios = dominios_y(d)
    md = stresses['positive_moment'] * 1.4
    fcd = fck / 1.4
    x = 1.25 * d * (1 - math.sqrt(1 - md / (0.425 * b * math.pow(d, 2) * fcd)))

    if x < dominios['x23']:
        print('Dominio 2')

    elif x < dominios['x34']:
        print('Dominio 3')
    as_simple = md / (fyd * (d - 0.4 * x))
    print("Armadura necesária: {a:.2f} cm2".format(a=as_simple))
