# O cardápio de uma lanchonete é o seguinte:
# Especificação   Código  Preço
# Cachorro Quente 100     R$ 1,20
# Bauru Simples   101     R$ 1,30
# Bauru com ovo   102     R$ 1,50
# Hambúrguer      103     R$ 1,20
# Cheeseburguer   104     R$ 1,30
# Refrigerante    105     R$ 1,00
# Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. 
# Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido. 
# Considere que o cliente deve informar quando o pedido deve ser encerrado.

qtdCachorroQuente = 0 
qtdBauruSimples = 0
qtdBauruOvo = 0
qtdHamburguer = 0
qtdCheesburguer = 0
qtdRefri = 0

precoCachorroQuente = 1.2
precoBauruSimples = 1.3
precoBauruOvo = 1.5
precoHamburguer = 1.2
precoCheesburguer = 1.3
precoRefri = 1

titulo1 = 'Cod'
titulo2 = 'Qtd'
titulo3 = 'Valor'

conta = 0

while (True):
    cod = int(input('Informe o codigo do produto ou "000" para sair: '))

    if (cod == 000):
        break

    elif (cod<100 and cod>105):
        print('Código Inválido.')

    else:
        qtd = int(input('Informe a quantidade: '))

        if cod == 100:
            qtdCachorroQuente += qtd
        
        elif cod == 101:
            qtdBauruSimples += qtd 

        elif cod == 102:
            qtdBauruOvo += qtd

        elif cod == 103:
            qtdHamburguer += qtd 

        elif cod == 104:
            qtdCheesburguer += qtd

        elif cod == 105:
            qtdRefri += qtd

totalCachorroQuente = qtdCachorroQuente*precoCachorroQuente
totalBauruSimples = qtdBauruSimples*precoBauruSimples
totalBauruOvo = qtdBauruOvo*precoBauruOvo
totalHamburguer = qtdHamburguer*precoHamburguer
totalCheesburguer = qtdCheesburguer*precoCheesburguer
totalRefri = qtdRefri*precoRefri

conta = totalBauruOvo + totalBauruSimples + totalCachorroQuente + totalCheesburguer + totalHamburguer + totalRefri

linha = '-' * 31

print(linha)
print('{:<}'.format(titulo1), end='')
print('{:>13}'.format(titulo2), end='')
print('{:>15}'.format(titulo3))
print(linha)

if (totalCachorroQuente != 0):
    print('100', end='')
    print('{:>13}'.format(qtdCachorroQuente), end='')
    print('{:>12.2f} R$'.format(totalCachorroQuente))

if (totalBauruSimples != 0):
    print('101', end='')
    print('{:>13}'.format(qtdBauruSimples), end='')
    print('{:>12.2f} R$'.format(totalBauruSimples))

if (totalBauruOvo != 0):
    print('102', end='')
    print('{:>13}'.format(qtdBauruOvo), end='')
    print('{:>12.2f} R$'.format(totalBauruOvo))

if (totalHamburguer != 0):
    print('103', end='')
    print('{:>13}'.format(qtdHamburguer), end='')
    print('{:>12.2f} R$'.format(totalHamburguer))

if (totalCheesburguer != 0):
    print('104', end='')
    print('{:>13}'.format(qtdCheesburguer), end='')
    print('{:>12.2f} R$'.format(totalCheesburguer))

if (totalRefri != 0):
    print('105', end='')
    print('{:>13}'.format(qtdRefri), end='')
    print('{:>12.2f} R$'.format(totalRefri))

print(linha)

print('Total', end='')
print('{:>23.2f} R$'.format(conta))