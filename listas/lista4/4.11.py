def main():
    
    num = int(input('Informe um número inteiro qualquer:'))
    bits = CALCULA_BITS_RECURSAO(num)
    print(f'O número {num} em binário equivale à {bits}.\n'
          f'Ele contém {len(bits)} bits.')

def  CALCULA_BITS_RECURSAO(x):

    bits = ''

    if (x == 1):
        bits += str('1')
    else:
        resto = (x%2)
        bits += CALCULA_BITS_RECURSAO(x//2)+str(resto) 
  
    return bits #Complexo. Consegui fazer mas ainda tá nebuloso na minha mente.

def CALCULA_BITS_LOOP(x):

    bits = ''

    while (True):
        if (x == 0):
            break
        resto = (x%2)
        x//= 2
        bits = str(resto) + bits
    
    tamanho_bits = len(bits)
    return bits, tamanho_bits

main()
