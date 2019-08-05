# Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
# Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
# Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
# A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior. Faça um programa que determine o salário atual desse funcionário. Após concluir isto, altere o programa permitindo que o usuário digite o salário inicial do funcionário.

salario = float(input('Digite o salario inicial: '))
from datetime import date

anoAtual = date.today().year
anos = anoAtual - 2009

for x in range(1, anos+1):
    salario += salario*(x*0.015)

print('Salario atual: R$ {:.2f}'.format(salario))