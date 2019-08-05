# Faça um Programa que leia dois vetores com 5 elementos cada. Gere um terceiro vetor de 10 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.

a = [1,1,1,1,1]
b = [2,2,2,2,2]
c = []

tamanho = len(a)

for x in range(tamanho):
    aux = a[x]
    c.append(aux)
    aux = b[x]
    c.append(aux)

print(c)
