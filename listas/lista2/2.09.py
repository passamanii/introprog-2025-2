num1 = float (input ('Insira o primeiro número:'))
num2 = float (input ('Insira o segundo número:'))
num3 = float (input ('Insira o terceiro número:'))

if (num1 > num2 > num3):
    print (f'{(num3)}, {(num2)}, {(num1)}')

elif (num1 > num3 > num2):
    print (f'{(num2)}, {(num3)}, {(num1)}')

elif (num2 > num1 > num3):
    print (f'{(num3)}, {(num1)}, {(num2)}')

elif (num2 > num3 > num1):
    print (f'{(num1)}, {(num3)}, {(num2)}')

elif (num3 > num1 > num2):
    print (f'{(num2)}, {(num1)}, {(num3)}')

elif (num3 > num2 > num1):
    print (f'{(num1)}, {(num2)}, {(num3)}')
    