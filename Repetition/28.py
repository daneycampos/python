# Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.

numCds = int(input('Numero de CDs: '))
valorTotal = 0

for x in range(numCds):
    valorCd = float(input('Valor do CD {}: '.format(x+1)))

    valorTotal += valorCd

media = valorTotal/numCds

print("Valor total investido: R$ {:.2f}".format(valorTotal))
print('Valor medio por CD: R$ {:.2f}'.format(media))