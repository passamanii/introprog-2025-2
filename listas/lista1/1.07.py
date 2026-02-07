x1 = float (input ('Insira a coordenada x do ponto 1:'))
y1 = float (input ('Insira a coordenada y do ponto 1:'))

x2 =  float (input ('Insira a coordenada x do ponto 2:')) 
y2 = float (input ('Insira a coordenada y do ponto 2:'))

dman = abs((x1 - x2) + (y1 - y2))

print ('A distância Manhattan dos dois pontos é:', dman)
