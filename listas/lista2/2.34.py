def main():

    indice = float(input('Informe o índice de poluição da empresa:'))
    
    if (indice < 0.05):
        acao = 'TÁ DE PARABÉNS'
    elif (0.05 <= indice < 0.3):
        acao = 'ACEITÁVEL'
    elif (indice < 0.4):
        acao = 'SUSPENDER GRUPO 1'
    elif (indice < 0.5):
        acao = 'SUSPENDER GRUPOS 1 E 2'
    else:
        acao = 'SUSPENDER TODOS OS GRUPOS'

    print(f'Ação à ser tomada: {acao}.')

main()