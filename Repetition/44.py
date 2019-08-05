# Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de
# código. Os códigos utilizados são:
# 1 , 2, 3, 4  - Votos para os respectivos candidatos 
# (você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
# 5 - Voto Nulo
# 6 - Voto em Branco
# Faça um programa que calcule e mostre:
# O total de votos para cada candidato;
# O total de votos nulos;
# O total de votos em branco;
# A percentagem de votos nulos sobre o total de votos;
# A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto 
# de votos tem-se o valor zero.

print('Opções de voto.')
print('1. Alberto')
print('2. Bianca')
print('3. Carlos')
print('4. Danilo')
print('5. Voto Nulo')
print('6. Voto Branco')

totalVotos = 0
opcaoUm = 0
opcaoDois = 0
opcaoTres = 0
opcaoQuatro = 0
opcaoCinco = 0
opcaoSeis = 0

while (True):
    voto = int(input('Digite o seu voto: '))
    if (voto == 0):
        break
    elif (voto == 1):
        totalVotos += 1
        opcaoUm += 1
    elif (voto == 2):
        totalVotos += 1
        opcaoDois += 1
    elif (voto == 3):
        totalVotos += 1
        opcaoTres += 1
    elif (voto == 4):
        totalVotos += 1
        opcaoQuatro += 1
    elif (voto == 5):
        totalVotos += 1
        opcaoCinco += 1
    elif (voto == 6):
        totalVotos += 1
        opcaoSeis += 1
    else:
        print('Valor inválido.')

print('Primeiro Candidato: {} votos'.format(opcaoUm))
print('Segundo Candidato: {} votos'.format(opcaoDois))
print('Terceiro Candidato: {} votos'.format(opcaoTres))
print('Quarto Candidato: {} votos'.format(opcaoQuatro))
print('Votos nulos: {}'.format(opcaoCinco))
print('Votos em branco: {}'.format(opcaoCinco))

print('Percentual de votos nulos: {:.2f} %'.format((opcaoCinco/totalVotos)*100))
print('Percentual de votos em branco: {:.2f} %'.format((opcaoSeis/totalVotos)*100))

     

        

