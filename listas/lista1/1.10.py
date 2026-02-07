hora1 = float (input ('Insira a hora do primeiro horário:'))
min1 = float (input ('Insira os minutos do primeiro horário:'))

hora2 = float (input ('Insira a hora do segundo horário:'))
min2 = float (input ('Insira os minutos do segundo horário:'))

if (hora2 < hora1):
    totaldif24 = abs((((hora2 * 60) + (24*60) + min2) - ((hora1 * 60) + min1)))

    horadif = (totaldif24 // 60)
    mindif = (totaldif24 - (horadif * 60))

else:
    totaldif = abs(((hora2 * 60) + min2) - ((hora1 * 60) + min1))
    
    horadif = (totaldif // 60)
    mindif = (totaldif - (horadif * 60)) # ou então (totaldif % 60)

print (f'O primeiro horário é: {round(hora1):02d}:{round(min1):02d}') #"round()" imprime o valor da variável sem casas decimais.
print (f'O segundo horário é: {round(hora2):02d}:{round(min2):02d}') # Já ":02d" formata o valor da variável para 2 dígitos

print (f'A diferença entre os horários é: {round(horadif):02d}:{round(mindif):02d}')
