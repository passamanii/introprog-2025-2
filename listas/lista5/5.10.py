def main():
    
    gabarito = []
    alunos = [[], [], [], [], [], []]

    for i in range(5):

        g = input(f'Insira o gabarito da {i + 1}ª questão:')
        gabarito.append(g)

    for i in range(2):
        
        alunos[0].append(input(f'Informe o nome do {i + 1}º aluno:'))
        alunos[1].append(input(f'Informe a primeira resposta:'))
        alunos[2].append(input(f'Informe a segunda resposta:'))
        alunos[3].append(input(f'Informe a terceira resposta:'))
        alunos[4].append(input(f'Informe a quarta resposta:'))
        alunos[5].append(input(f'Informe a quinta resposta:'))

    
    for i in range(len(alunos[0])):
        
        nota = 0

        for j in range(1, 6):

            if (alunos[j][i] == gabarito[j - 1]):

                nota += 2

        quest = nota / 2        
        print(f'O aluno {alunos[0][i]} acertou {quest} questão(ões), ficando com a nota parcial de: {nota} pontos.')


main()