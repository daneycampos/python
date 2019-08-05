# Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.

vetor = [1,2]
mult = 1
soma = 0

for x in vetor:
    soma += x
    mult *= x

print(mult)
print(soma)