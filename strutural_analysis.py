import math

def def_isostatic_stress(beam_length, beam_load):
    shear_stress = beam_length * beam_load / 2
    positive_moment = (beam_load * math.pow(beam_length, 2)) / 8

    return {'shear': shear_stress, 'positive_moment': positive_moment}


