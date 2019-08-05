# Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário, mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial e final devem ser informados também pelo usuário, conforme exemplo abaixo:

num = int(input('Digite o numero: '))
inicio = int(input('digite o inicio: '))
fim = int(input('digite o fim: '))

while (inicio > fim):
    fim = int(input('Inicio maior que fim, digite novamente o fim: '))

print('Montar a tabuada de {}'.format(num))
print('Começar por: {}'.format(inicio))
print('Terminar em: {}'.format(fim))

for x in range(inicio, fim+1):
    print('{} X {} = {}'.format(num, x, num*x))