# Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela.
# Os juros e a quantidade de parcelas seguem a tabela abaixo:
# Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
# 1       0
# 3       10
# 6       15
# 9       20
# 12      25

divida = float(input('Digite o valor da divida: '))
parcelas = 1
juros = 0

titdivida = 'Divida'
titjuros = 'Juros'
titparcelas = 'Número de Parcelas'
titvalor = 'Valor da Parcela'

print('\n')
print('-'*98)
print('{:<15} {:>16} {:>35} {:>29}'.format(titdivida, titjuros, titparcelas, titvalor))
print('-'*98)

for x in range(5):
    if (x == 0): 
        print('R$ {:<15.2f} {:>12}% {:>35} {:>26.2f} R$'.format(divida, juros, parcelas, divida))

    elif (x == 1):
        parcelas +=2
        juros += 10
        divida += divida*(juros/100)
        valorParcela = divida/parcelas

        print('R$ {:<15.2f} {:>12}% {:>35} {:>26.2f} R$'.format(divida, juros, parcelas, valorParcela))
    else:
        parcelas +=3
        juros += 5
        divida += divida*(juros/100)
        valorParcela = divida/parcelas

        print('R$ {:<15.2f} {:>12}% {:>35} {:>26.2f} R$'.format(divida, juros, parcelas, valorParcela))

print('-'*98)
print('\n')





