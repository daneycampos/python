# Faça um Programa que peça as 2 notas de 3 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.

soma = 0
notas = []
aprovados = 0

for aluno in range(3):
    for nota in range(2):
        nota = float(input('Digite a nota {} do aluno {}: '.format(nota, aluno)))
        soma += nota
    print('\n')
    media = soma/2
    notas.append(media)

for x in notas:
    if x >= 7:
        aprovados += 1

print(aprovados)