def main():
    
    num = int(input('Informe um número inteiro qualquer:'))
    bits = CALCULA_BITS_RECURSAO(num)
    print(f'O número {num} em binário equivale à {bits}.\n'
          f'Ele contém {len(bits)} bits.')

def  CALCULA_BITS_RECURSAO(x):

    bits = ''

    if (x == 0):
        bits += str('0')
    else:
        resto = (x%2)
        bits += CALCULA_BITS_RECURSAO(x//2)+str(resto) 
  
    return bits #Complexo. Consegui fazer mas ainda tá nebuloso na minha mente.

#Número 4
#4%2 = 0
#2%2 = 0
#1%2 = 1
#Usar bits = bits + str(resto) faz com que a recursão construa os bits na ordenação correta.
#A função retornar bits significa retornar o valor total, não a sua parcela individual, essa sendo str(resto).
# bits = 1 --> bits = 10 --> bits = 100.

#Fiz a função usando loop em uns 7 minutos. Já usando recursividade levei facilmente uns 40.

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
