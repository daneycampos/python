# Faça um programa que mostre os n termos da Série a seguir:
# S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m. 
# Imprima no final a soma da série.

n = int(input('Digite o valor de N: '))
soma = 0
divisor = -1
for x in range(1, n+1):
    divisor += 2
    soma += x/divisor
    print('{}/{}'.format(x, divisor))

print(soma)

