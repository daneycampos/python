# Em uma competição de salto em distância cada atleta tem direito a cinco saltos. O resultado do atleta será determinado pela média dos cinco valores restantes. Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe o nome, os saltos e a média dos saltos. O programa deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:
# Atleta: Rodrigo Curvêllo
 
# Primeiro Salto: 6.5 m
# Segundo Salto: 6.1 m
# Terceiro Salto: 6.2 m
# Quarto Salto: 5.4 m
# Quinto Salto: 5.3 m

# Resultado final:
# Atleta: Rodrigo Curvêllo
# Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
# Média dos saltos: 5.9 m

flag = False


while (flag == False):
    saltos = []
    soma = 0
    
    atleta = input('Digite o nome do atleta: ')
    
    if atleta == '':
        flag = True

    else: 
        for x in range(5):
            salto = float(input('Digite o valor do salto {}: '.format(x+1)))
            soma += salto
            saltos.append(salto)

        print('\nAtleta: {}'.format(atleta))
        print('\nPrimeiro Salto: {} m'.format(saltos[0]))
        print('Segundo Salto: {} m'.format(saltos[1]))
        print('Terceiro Salto: {} m'.format(saltos[2]))
        print('Quarto Salto: {} m'.format(saltos[3]))
        print('Quinto Salto: {} m'.format(saltos[4]))

        print('\nResultado Final: ')
        print('Atleta: {}'.format(atleta))
        print('Saltos: ', end='')
        for i in range(5):
            if i < 4:
                print('{:.1f}'.format(saltos[i]), end=' - ')
            else:
                print('{:.1f}'.format(saltos[i]))

        print('Média dos Saltos: {:.1f}m\n'.format(soma/5))
        


            


