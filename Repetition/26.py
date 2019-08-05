# Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.

eleitores = int(input('Numero total de eleitors: '))

print('Candidadtos')
print('1. Alberto')
print('2. Baiano')
print('3. Caio')

a = 0
b = 0
c = 0

for x in range(eleitores):
    voto = int(input('Voto: '))

    if (voto == 1):
        a += 1
    elif (voto == 2):
        b += 1
    elif (voto == 3):
        c += 1
    else:
        print('voto nulo')

vencedor = max(a,b,c)

if (vencedor == 1):
    print('Vencedor é Alberto')
elif vencedor == 2:
    print('vencedor é Baiano')
else: 
    print('Vencedor é Caio')