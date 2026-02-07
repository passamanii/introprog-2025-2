def main():

    grades = []
    name = str(input('Insira o nome do aluno:'))
    tests = int(input('Insira a quantidade de provas realizadas:'))

    for i in range(tests):

        grades.append(float(input(f'Digite a nota da prova {i+1} aqui:')))

    process(grades, name, tests)


def process(list, name, tests):

    media = sum(list) / tests

    print (f'A média das notas do aluno {name} é: {media}')


main()