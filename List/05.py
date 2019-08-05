# Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.

par = []
impar = []
todos = []

for x in range(5):
    valor = int(input('Digite um inteiro: '))
    todos.append(valor)

    if ((valor%2) == 0):
        par.append(valor)
    else:
        impar.append(valor)

print(todos)
print(par)
print(impar)