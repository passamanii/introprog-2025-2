#import os [linux]

def adicionar_nota():
    nome = input ('Insira o nome do aluno:')
    n1 = float (input ('Insira a primeira nota:'))
    n2 = float (input ('Insira a segunda nota:'))
    n3 = float (input ('Insira a terceira nota:'))
    
    return n1, n2, n3, nome

def calcular_media(x, y, z):
    
    mediadef = round ((x + y + z) / 3, 2)

    return mediadef

def verificar_media(nome, var):

    if (var >= 7):

        return f"{nome} - Media: {var} **Aprovado** \n"

    elif (7 > var >= 5):

        return f"{nome} - Media: {var} **Recuperação** \n"

    elif (5 < var):

        return f"{nome} - Media: {var} **Reprovado** \n"

def exibir_resultado(str):
    
        print (str)

def main():
    resultado = "" 
    r = "1"

    while (r != 'N'):
        
        x,y,z,n = adicionar_nota()
        media = calcular_media(x,y,z)
        resultado += verificar_media(n, media)

        r = input ('Deseja inserir notas de outro aluno? (S/N) ').upper()
    #os.system('clear') [linux]
    exibir_resultado(resultado)

main()