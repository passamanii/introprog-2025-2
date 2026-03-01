def main():

    num1, gols1, presencas1, penalidades1, altura1, peso1, idade1 = pedir_informacoes()
    num2, gols2, presencas2, penalidades2, altura2, peso2, idade2 = pedir_informacoes()
    num3, gols3, presencas3, penalidades3, altura3, peso3, idade3 = pedir_informacoes()

    avaliacao1 = avaliar_jogador(gols1, presencas1, penalidades1, altura1, peso1, idade1)
    avaliacao2 = avaliar_jogador(gols2, presencas2, penalidades2, altura2, peso2, idade2)
    avaliacao3 = avaliar_jogador(gols3, presencas3, penalidades3, altura3, peso3, idade3)

    comparar_avaliacoes(avaliacao1, num1, avaliacao2, num2, avaliacao3, num3)

def pedir_informacoes():
    
    numero = int(input('\nInforme o número do jogador:'))
    gols = int(input('Informe a quantidade de gols feitos pelo jogador:'))
    presenca = int(input('Informe a quantidade de presenças do jogador:'))
    penalidades = int(input('Informe o tempo das penalidades sofridas pelo jogador em minutos:'))
    altura = int(input('Informe a altura do jogador em cm:'))
    peso = float(input('Informe o peso do jogador em kg:'))
    idade = int(input('Informe a idade do jogador:'))

    return numero, gols, presenca, penalidades, altura, peso, idade

def avaliar_jogador(gols, presencas, penalidades, altura, peso, idade):
    
    avaliacao = ((gols+presencas+(penalidades/4)+((altura+peso)/5)-idade)*0.8)

    return avaliacao

def comparar_avaliacoes(av1, num1, av2, num2, av3, num3):
    
    if ((av1 > av2) and (av1 > av3)):
        maior_num = num1
        maior_av = av1
    elif ((av2 > av1) and (av2 > av3)):
        maior_num = num2
        maior_av = av2
    elif ((av3 > av1) and (av3 > av2)):
        maior_num = num3
        maior_av = av3
    if ((av1 < av2) and (av1 < av3)):
        menor_num = num1
        menor_av = av1
    elif ((av2 < av1) and (av2 < av3)):
        menor_num = num2
        menor_av = av2
    elif ((av3 < av1) and (av3 < av2)):
        menor_num = num3
        menor_av = av3
    
    print(f'MELHOR AVALIAÇÃO: JOGADOR {maior_num}. AVALIAÇÃO: {maior_av}.')
    print(f'PIOR AVALIAÇÃO: JOGADOR {menor_num}. AVALIAÇÃO: {menor_av}.')

main()