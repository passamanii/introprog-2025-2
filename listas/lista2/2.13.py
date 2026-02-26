nasc = input ('Insira sua data de nascimento no formado dd/mm/aaaa:')
ndia, nmes, nano = nasc.split('/') ## .split('/') segmenta as informações inseridas de acordo com o separador especificado dentro do (), que é '/'.

ndia = int(ndia) ## definindo cada variável em um número inteiro
nmes = int(nmes)
nano = int(nano)

atual = input ('Insira a data atual no formado dd/mm/aaaa:')
adia, ames, aano = atual .split ('/')

adia = int(adia)
ames = int(ames)
aano = int(aano)

ntotal = ((nano * 365) + (nmes * 30.416666667) + ndia)
atotal = ((aano * 365) + (ames * 30.416666667) + adia)

dif = atotal - ntotal

iano = dif / 365
imes = (dif % 365) / 30.416666667
idia = (dif % 365) % 30.416666667

iano = int (iano)
imes = int (imes)
idia = int (idia)

print (f'A idade da pessoa é de: {(iano)} anos, {(imes)} meses e {(idia)} dias.')

if (iano >= 18):
    print ('A pessoa tem idade suficiente para tirar carteira de habilitação e votar.')

elif (18 > iano >= 16):
    print ('A pessoa tem idade para votar.')

elif (16 > iano):
    print ('A pessoa não tem idade suficiente para votar nem tirar carteira de habilitação.')
