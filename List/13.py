# Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).

temps = []

for i in range(12):
    temp = float(input('Digite a temperatura do mês {}: '.format(i+1)))
    temps.append(temp)

somaTemp = sum(temps)
mediaTemp = somaTemp/12

for i in range(1, 13):
    if temps[i-1] > mediaTemp:
        if i==1:
            print('1 - Janeiro')
        elif i == 2:
            print('2 - Fevereiro')
        elif i == 3:
            print('3 - Março')
        elif i == 4:
            print('4 - Abril')
        elif i == 5:
            print('5 - Maio')
        elif i == 6:
            print('6 - Junho')
        elif i == 7:
            print('7 - Julho')
        elif i == 8:
            print('8 - Agosto')
        elif i == 9:
            print('9 - Setembro')
        elif i == 10:
            print('10 - Outubro')
        elif i == 11:
            print('11 - Novembro')
        elif i == 12:
            print('12 - Dezembro')

print('\n {}'.format(mediaTemp))