# Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos.

numTurmas = int(input('Numero de turmas: '))
totalAlunos = 0

for x in range(numTurmas):
    numAlunos = int(input('Numeros de alunos da turma {}: '.format(x+1)))

    while numAlunos > 40:
        numAlunos = int(input('Valor inválido. Digite novamente: '))
    
    totalAlunos += numAlunos

media = totalAlunos/numTurmas

print(media)
