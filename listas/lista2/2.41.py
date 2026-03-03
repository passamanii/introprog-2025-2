def main():
    
    preco1 = float(input('Insira o preço do 1º produto:'))
    preco2 = float(input('Insira o preço do 2º produto:'))
    preco3 = float(input('Insira o preço do 3º produto:'))

    lucro1 = calcula_lucro(preco1)
    lucro2 = calcula_lucro(preco2)
    lucro3 = calcula_lucro(preco3)

    revenda1 = (preco1*lucro1)
    revenda2 = (preco2*lucro2)
    revenda3 = (preco3*lucro3)

    print(f'O valor de revenda do 1º produto é: R${revenda1}.')
    print(f'O valor de revenda do 2º produto é: R${revenda2}.')
    print(f'O valor de revenda do 3º produto é: R${revenda3}.')

def calcula_lucro(preco):

    if (preco < 10):
        lucro = 1.7
    elif (preco < 30):
        lucro = 1.5
    elif (preco < 50):
        lucro = 1.4
    else:
        lucro = 1.3
    
    return lucro

main()