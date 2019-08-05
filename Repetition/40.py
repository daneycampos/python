# Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos os seguintes dados:
# Código da cidade;
# Número de veículos de passeio (em 1999);
# Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:
# Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
# Qual a média de veículos nas cinco cidades juntas;
# Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.

menorAcidente = float('inf')
maiorAcidente = float('-inf')
codMenorAcidente = 0
codMaiorAcidente = 0
somaVeiculos = 0
cidadePequena = 0
somaAcidentes = 0
numCidades = 0
mediaVeiculos = 0
mediaAcidenteCidadePeq = 0 
somaAcidentesCidadePequena = 0

while(True):
    cod = input('Digite o codigo da cidade ou "sair" para sair: ')
    if (cod == 'sair'):
        break
    else:
        cod = int(cod)
        numVeiculos = int(input('Digite o numero de veiculos da cidade: '))
        numAcidentes = int(input('Digite o numero de acidades em 1999: '))

        if(numVeiculos < 2000):
            cidadePequena += 1
            somaAcidentesCidadePequena += numAcidentes 

        if(numAcidentes > maiorAcidente):
            maiorAcidente = numAcidentes
            codMaiorAcidente = cod 

        if(numAcidentes < menorAcidente):
            menorAcidente = numAcidentes
            codMenorAcidente = cod
        
        somaVeiculos += numVeiculos
        numCidades += 1

if(numCidades != 0):
    mediaVeiculos = somaVeiculos/numCidades

if(cidadePequena != 0):
    mediaAcidenteCidadePeq = somaAcidentesCidadePequena/cidadePequena

print('Maior índice de acidentes foi da cidade de código {} com {} acidentes.'.format(codMaiorAcidente, maiorAcidente))
print('Menor índice de acidentes foi da cidade de código {} com {} acidentes.'.format(codMenorAcidente, menorAcidente))
print('A média de veículos nas {} cidades é de {:.2f} veículos.'.format(numCidades, mediaVeiculos))
print('A média de acidentes em cidades com até 2000 veículos é de {} acidentes.'.format(mediaAcidenteCidadePeq))


            
