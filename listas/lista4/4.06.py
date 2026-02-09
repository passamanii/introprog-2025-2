def main():

    while (1):

        mat = int(input('Informe a matrícula do funcionário:'))

        if (mat < 0):

            print('Programa encerrado.')
            break

        name = input('Informe o nome do funcionário:')
        sal = float(input(f'Informe o salário do funcionário {mat}:'))
        k = float(input('Insira a porcentagem k% de aumento desejada:'))

        newsal = AUMENTO(sal, k)

        print(f'O novo salário do funcionário {name} é: R${(newsal):.2f}!')

def AUMENTO(salario, percentual):

    raised_salary = salario * ((percentual / 100) + 1)

    return raised_salary


main()