# Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.
a = [1,1,1,1,1]
b = [2,2,2,2,2]
c = [3,3,3,3,3]
d = []
tamanho = len(a)

for x in range(tamanho):
    aux = a[x]
    d.append(aux)
    aux = b[x]
    d.append(aux)
    aux = c[x]
    d.append(aux)

print(d)