# Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

soma = 0
v = []
for x in range(4):
    n = float(input('Digite a nota {}: '.format(x)))
    soma += n
    v.append(n)

media = soma/4
print(media)
print(v)
