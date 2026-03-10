def main():

    while (True):
        try:
            dia1, mes1, ano1 = map(int, input('Insira a data no formato (XX/XX/XXXX):').split('/'))
            if (DATA_VALIDA(dia1, mes1, ano1) == False):
                raise ValueError('Insira uma data válida.')
            dia2, mes2, ano2 = map(int, input('Insira a data no formato (XX/XX/XXXX):').split('/'))
            if (DATA_VALIDA(dia2, mes2, ano2) == False):
                raise ValueError('Insira uma data válida')
            break
        except ValueError as error:
            print(f'Erro: {error}.')
            continue
    
    dias1 = DIAS_ANO(dia1, mes1, ano1)
    dias2 = DIAS_ANO(dia2, mes2, ano2)
    maior, dif = COMPARA_DIAS(dias1, dias2)
    PRINTA_DIFERENCA(maior, dif, dia1, mes1, ano1, dia2, mes2, ano2)

def DIAS_ANO(dia, mes, ano):

    dias = ((mes*30)+dia)

    return dias

def DATA_VALIDA(dia, mes, ano):

    if (dia > 30):
        return False
    elif (mes > 12):
        return False
    
    if (((ano%400) == 0) and ((ano%100) == 0)):
        if ((dia > 29) and (mes == 2)):
            return False
    elif (((ano%4) == 0) and (ano%100) != 0):
        if ((dia > 29) and (mes == 2)):
            return False
    else:
        if ((dia > 28) and (mes == 2)):
            return False
        
    return True

def COMPARA_DIAS(x, y):

    dif = (x-y)

    if (dif > 0):
        maior = 0
    elif (dif < 0):
        maior = 1
        dif = abs(dif)
    
    return maior, dif

def PRINTA_DIFERENCA(maior, dif, dia1, mes1, ano1, dia2, mes2, ano2):

    if (maior == 0):
        print(f'A diferença entre as datas {dia1}/{mes1}/{ano1} e {dia2}/{mes2}/{ano2} é de {dif} dias.')
    elif (maior == 1):
        print(f'A diferença entre as datas {dia2}/{mes2}/{ano2} e {dia1}/{mes1}/{ano1} é de {dif} dias.')

main()