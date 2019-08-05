# Faça um Programa que peça a idade e a altura de 2 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.

altura = []
idade = []

def inversor(vetor):
    return vetor[::-1]

for x in range(2):
    height = float(input('Digite a algura do pessoa {}: '.format(x)))
    altura.append(height)

    year = int(input('Digite a idade da pessoa {}: '.format(x)))
    idade.append(year)


print(inversor(altura))
print(inversor(idade))
