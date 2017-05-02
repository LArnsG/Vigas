import math


def isostatic_stress(beam_length, beam_load):
    shear_stress = beam_length * beam_load / 2
    positive_moment = (beam_load * math.pow(beam_length, 2)) / 8

    return {'shear': shear_stress, 'positive_moment': positive_moment}


def minimum_steel_area(height, width):
    concrete_area = height * width
    as_minimum = 0.0015 * concrete_area
    as_maximum = 0.04 * concrete_area
    return {'min': as_minimum, 'max': as_maximum}


def dominios_y(height, cobrimento):
    d = height - cobrimento
    global x_2_lim, x_3_lim
    x_2_lim = 0.26 * d
    x_3_lim = 0.63 * d


def beam_design():
    global fck, fyd, height, width, length, load, cobrimento
    # globals(fck, fyd, height, width, length, load, cobrimento)
    stresses = isostatic_stress(length, load)
    minimum_steel = minimum_steel_area(height, width)

    b = width
    d = height - cobrimento
    md = stresses['positive_moment'] * 1.4
    fcd = fck / 1.4
    x = 1.25 * d * (1 - math.sqrt(1 - md / (0.425 * b * math.pow(d, 2) * fcd)))
    

