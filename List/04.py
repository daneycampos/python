# Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

v = []
con= 0

for x in range(10):
    char = input('Digite uma letra: ')
    char = char.lower()
    v.append(char)

lista = ['a','e','i','o','u']

for i in range(10):
    if (v[i] not in lista):
        con += 1
        print(v[i])

print(con)