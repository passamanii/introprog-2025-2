def main():
    
    dia, mes, ano = input('Informe a data no formato (XX/XX/XXXX):').split('/')
    nome_mes = NOME_MES(mes)
    print(f'DATA FORMATADA: {dia} de {nome_mes} de {ano}.')
    

def NOME_MES(num):

    num = str(num)

    nome_mes = {
        '1': 'Janeiro',
        '2': 'Fevereiro',
        '3': 'Março',
        '4': 'Abril',
        '5': 'Maio',
        '6': 'Junho',
        '7': 'Julho',
        '8': 'Agosto',
        '9': 'Setembro',
        '10': 'Outubro',
        '11': 'Novembro',
        '12': 'Dezembro'
    }

    return nome_mes[num]

main()