a = float (input ('Insira o primeiro número:'))
b = float (input ('Insira o segundo número:'))
c = float (input ('Insira o terceiro número:'))

if (a > b):

    if (b > c):
        print (f'{a}, {b}, {c}')
    
    else:
        if (a > c):
            print (f'{a}, {c}, {b}')
    
        else:
            print (f'{c}, {a}, {b}')

else:

    if (a > c):
        print (f'{b}, {a}, {c}')
    
    else:
        if (b > c):
            print (f'{b}, {c}, {a}')
        
        else:
            print (f'{c}, {b}, {a}')