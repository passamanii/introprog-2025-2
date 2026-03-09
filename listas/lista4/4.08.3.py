def main():

    hr1, min1, sec1 = map(int, input(f'Insira o 1º horário no formato (XX:XX:XX):').split(':'))
    hr2, min2, sec2 = map(int, input(f'Insira o 2º horário no formato (XX:XX:XX):').split(':'))

    total_sec1 = SEG(hr1, min1, sec1)
    total_sec2 = SEG(hr2, min2, sec2)
    maior, hrdif, mindif, secdif = COMPARA_SEGUNDOS(total_sec1, total_sec2)
    PRINTA_DIFERENÇA(maior, hrdif, mindif, secdif, hr1, min1, sec1, hr2, min2, sec2)

def SEG(hour, minute, seconds):
    
    seg = ((hour*3600)+(minute*60)+seconds)
    return seg

def HMS(seconds):
    
    hr = (seconds//3600)
    min = ((seconds%3600)//60)
    sec = ((seconds%3600)%60)
    return hr, min, sec

def COMPARA_SEGUNDOS(x, y):

    dif = (x-y)
    
    if (dif > 0):
        maior = 0
    else:
        maior = 1
        dif = abs(dif)
    
    hrdif, mindif, secdif = HMS(dif)
    return maior, hrdif, mindif, secdif

def PRINTA_DIFERENÇA(maior, hrdif, mindif, secdif, hr1, min1, sec1, hr2, min2, sec2):

    if (maior == 0):
        print(f'A diferença entre {(hr1):02d}:{(min1):02d}:{(sec1):02d} e {(hr2):02d}:{(min2):02d}:{(sec2):02d} é: {(hrdif):02d}:{(mindif):02d}:{(secdif):02d}.')
    elif (maior == 1):
        print(f'A diferença entre {(hr2):02d}:{(min2):02d}:{(sec2):02d} e {(hr1):02d}:{(min1):02d}:{(sec1):02d} é: {(hrdif):02d}:{(mindif):02d}:{(secdif):02d}.')
    else: 
        print('Erro.')

main()