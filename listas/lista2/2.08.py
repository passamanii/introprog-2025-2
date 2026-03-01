num1 = float (input ('Insira o primeiro valor:'))
num2 = float (input ('Insira o segundo valor:'))
num3 = float (input ('Insira o terceiro valor:'))

if (num1 > num2) and  (num1 > num3):
    print (f'{(num1):.1f} é o maior.')

elif (num2 > num1) and (num2 > num3):
    print (f'{(num2):.2f} é o maior.')

else:
    print (f'{(num3):.2f} é o maior.')

