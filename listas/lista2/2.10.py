num1 = float (input ('Insira o primeiro valor:'))
num2 = float (input ('Insira o segundo valor:'))

if ((num1 ** 2) < (num2 ** 2)):
    print (f'O número inserido que elevado ao quadrado resulta no menor valor, é: {(num1):.1f}')

elif ((num1 ** 2) == (num2 ** 2)):
    print ('Os dois números inseridos elevados ao quadrado resultam no mesmo valor.')

else:
    print (f'O número inserido que elevado ao quadrado resulta no menor valor, é: {(num2):.1f}')
