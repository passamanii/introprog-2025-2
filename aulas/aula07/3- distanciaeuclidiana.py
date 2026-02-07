import math as m

X1 = float (input ('Insira a coordenada X do primeiro ponto:'))
Y1 = float (input ('Insira a coordenada Y do primeiro ponto:'))

X2 = float (input ('Insira a coordenada X do segundo ponto:'))
Y2 = float (input ('Insira a coordenada Y do segundo ponto:'))

d =  m.sqrt (m.pow (X2 - X1, 2) + m.pow (Y2 - Y1, 2))

print (f'{d:.02f}')
