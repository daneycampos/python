# O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas.

maior = float('-inf')
menor = float('inf')
soma = 0
count = 0


while (True):
    entrada = input('Digite um valor ou "sair" para sair: ')
    entrada.lower()

    if(entrada == 'sair'):
        break
    else:
        temp = float(entrada)
    
        if (temp > maior):
            maior = temp
        if (temp < menor):
            menor = temp
    
        soma += temp
        count += 1

media = soma/count

print(media, maior, menor)

