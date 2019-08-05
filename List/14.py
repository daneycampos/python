# Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

resp = []

r1 = input('Telefonou para a vitima? \n')
r2 = input('Esteve no local do crime: \n')
r3 = input('Mora perto da vítima? \n')
r4 = input('Devia para a vítima? \n')
r5 = input('Já trabalhou com a vítima? \n')

resp.append(r1.lower())
resp.append(r2.lower())
resp.append(r3.lower())
resp.append(r4.lower())
resp.append(r5.lower())

s = 0

for x in resp:
    if x == 'sim':
        s += 1

if s == 2:
    print('Suspeita')
elif s==3 or s==4:
    print('Cúmplice')
elif s == 5:
    print('Assassino')
else: 
    print('Inocente')