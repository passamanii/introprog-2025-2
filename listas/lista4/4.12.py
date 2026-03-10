import math as m

def main():
    
    diametro = float(input('Informe o diâmetro do círculo:'))
    raio = (diametro/2)
    area = CALCULA_AREA_DO_CIRCULO(raio)

    print(f'A área da circunferência de diâmetro {diametro} é: {(area):.3f} U.A.')

def CALCULA_AREA_DO_CIRCULO(r):

    area = (m.pi*(r**2))
    return area

main()