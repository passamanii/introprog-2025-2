def main():

    preco, dia, ao_vivo = pede_informacoes()
    preco_final = calcula_entrada(preco, dia, ao_vivo)
    print(f'O preço final é R${preco_final}.')
    
def pede_informacoes():

    base = float(input('Informe o preço base de entrada:'))
    dia = input('S - SEGUNDA\nT - TERÇA\nA - QUARTA\nQ - QUINTA\nE - SEXTA\nB - SÁBADO\nD - DOMINGO\nInforme o dia da semana:').upper()
    ao_vivo = input('É dia de música ao vivo? (S/N):').upper()

    return base, dia, ao_vivo

def calcula_entrada(preco, dia, ao_vivo):

    bonus = 0

    if (dia == 'S' or dia == 'T' or dia == 'Q'):
        bonus -= (0.25)
    if (ao_vivo == 'S'):
        bonus += (0.15)
    
    preco_final = (preco+(preco*bonus))

    return preco_final

main()