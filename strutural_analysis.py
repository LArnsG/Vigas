import math

global fck, fyd, height, width, beam_length, load, cobrimento


def isostatic_stress(beam_length, beam_load):
    shear_stress = beam_length * beam_load / 2
    positive_moment = (beam_load * math.pow(beam_length, 2)) / 8

    print('Esforços, cortante: {a:.2f} kN, momento: {b:.2f} kN.cm'.format(a=shear_stress, b=positive_moment))
    return {'shear': shear_stress, 'positive_moment': positive_moment}

