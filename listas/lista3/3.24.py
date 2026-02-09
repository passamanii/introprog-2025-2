def main():

    k = 0

    while (1):

        status = ''
        aluno = int(input('Informe o código do aluno:'))

        if (aluno < 0):

            print('\nProgama encerrado.\n')
            break

        n1 = float(input('Insira a primeira nota do aluno:'))
        maior = n1

        n2 = float(input('Insira a segunda nota do aluno:'))

        if (n2 > maior):

            maior = n2

        n3 = float(input('Insira a terceira nota do aluno:'))

        k += 1

        if (n3 > maior):

            maior = n3

        if (maior == n1):

            media = ((n1 * 4) + (n2 * 3) + (n3 * 3)) / (4 + 3 + 3)

        elif (maior == n2):

            media = ((n1 * 3) + (n2 * 4) + (n3 * 3)) / (4 + 3 + 3)

        elif (maior == n3):
            media = ((n1 * 3) + (n2 * 3) + (n3 * 4)) / (4 + 3 + 3)

        if (media >= 5):

            status = 'APROVADO'

        else:

            status = 'REPROVADO'

        print(f'\n---Ficha do Aluno {aluno}---\nNotas: {n1}, {n2}, {n3}.\nMédia: {media}.\nO aluno está {status}!\n')

main()