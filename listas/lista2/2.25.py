def main():

    w, h = map(int, input('Informe a largura e altura da imagem(L, A):').split(','))
    x, y = map(int, input('Informe as coordenadas do ponto(X, Y):').split(','))

    vef_pertencimento(w, h, x, y)

def vef_pertencimento(width, height, coordx, coordy):

    if ((coordx <= width) and (coordy <= height)):
        print(f'O ponto ({coordx}, {coordy}) corresponde às coordenadas de um pixel pertencente à imagem de dimensões ({width}, {height}).')
    else:
        print(f'O ponto({coordx}, {coordy}) não corresponde à um pixel da imagem de dimensões ({width}, {height}).')
        
main()