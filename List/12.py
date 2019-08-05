# Foram anotadas as idades e alturas de 5 alunos. Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.

idades = [12,14,15,14,12]
alturas = [130,140,100,140,135]

soma = sum(alturas)

mediaAltura = soma/5
alunos = 0

for x in range(5):
    if (idades[x]>13 and alturas[x]<mediaAltura):
        alunos += 1
    
print(alunos)
print(mediaAltura)