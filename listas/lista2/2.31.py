def main():

    consumo_mes_agua = pedir_volumes()
    conta_agua = calcula_conta(consumo_mes_agua)
    print(f'A conta de água totalizou R${(conta_agua):.2f}.')

def pedir_volumes():

    vol_anterior = float(input('Insira o consumo de água do mês anterior:'))
    vol_atual = float(input('Insira o consumo de água do mês atual:'))

    volume = vol_atual - vol_anterior

    return volume

def calcula_conta(volume):
    
    if (volume <= 10):
        taxa = 0.69
    elif (volume <= 15):
        taxa = 1.17
    elif (volume <= 25):
        taxa = 1.48
    else:
        taxa = 1.6

    conta_inicial = volume * taxa
    tarifa_esgoto = 0.025 * conta_inicial
    taxa_hidrometro = 5
    conta_com_imposto = conta_inicial + tarifa_esgoto + taxa_hidrometro

    return conta_com_imposto

main()