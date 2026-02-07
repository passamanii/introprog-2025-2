import math

def main():

    r = float(input('Insira o tamanho do raio do círculo:'))

    calc_area(r)

    while(1):

        again = (input('Deseja calcular mais áreas? Sim(S) ou Não(N):')).upper()

        if (again == "S"):

            r = float(input('Insira o tamanho do raio do círculo:'))

            calc_area(r)            

            
        elif (again == "N"):

            print('Programa encerrado. Obrigado pela preferência!')

            break

        else:

            again = (input('Código inválido. Deseja calcular mais áreas? Sim(S) ou Não(N):')).upper()


def calc_area(radius):

    pi = round(math.pi, 10)

    area = pi * (radius**2)

    print(f'A área do círculo de raio {radius} é de: {area}')

main()