def main():

    feet = float(input('Informe um valor em pés:'))
    inch = float(input('Informe um valor em polegadas:'))
    feet_to_m, inch_to_m = TRANSFORMA_MEDIDAS(feet, inch)

    print(f'FEET --> CM: {feet_to_m}cm\n'
         f'INCH --> CM: {inch_to_m}cm ')

def TRANSFORMA_MEDIDAS(pes, polegadas):

    pes_metros = (pes*30.48)
    pol_metros = (polegadas*2.54)

    return pes_metros, pol_metros

main()