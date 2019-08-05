# Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deverá terminar quando for lido um número negativo.

a, b, c, d = 0, 0, 0, 0
n = 0

while (n > -1):
    n = int(input('Informe um valor de 0-100 ou um número negativo para sair: '))
    
    if (n>-1 and n<26):
        a+=1
    elif (n>25 and n<51):
        b+=1
    elif (n>50 and n<76):
        c+=1
    elif (n>75 and n<101):
        d+=1
    else:
        print('Valor maior que 100. Valor não contabilizado.')

print('[0-25] = {}'.format(a))
print('[26-50] = {}'.format(b))
print('[51-75] = {}'.format(c))
print('[76-100] = {}'.format(d))