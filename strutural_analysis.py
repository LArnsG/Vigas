import math

def def_isostatic_stress(beam_length, beam_load):
    shear_stress = beam_length * beam_load / 2
    positive_moment = (beam_load * math.pow(beam_length, 2)) / 8

    return {'shear': shear_stress, 'positive_moment': positive_moment}


def minimum_steel_area(height, width):
    concrete_area = height * width
    as_minimum = 0.0015 * concrete_area
    as_maximum = 0.04 * concrete_area
    return {'min': as_minimum, 'max': as_maximum}




