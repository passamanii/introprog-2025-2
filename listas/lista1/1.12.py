valor = float (input ('Insira um valor qualquer:'))

cinq = int(valor / 50) 
vint = int((valor - (cinq * 50)) / 20)
dez = int((valor - ((cinq * 50) + (vint * 20))) / 10)
resto = float(valor - ((cinq * 50) + (vint * 20) + (dez * 10)))

print ('Notas de R$50:', cinq)
print('Notas de R$20:', vint)
print('Notas de R$10:', dez)

print(f'Resto: R${(resto):.2f}')