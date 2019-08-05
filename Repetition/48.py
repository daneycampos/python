# Faça um programa que peça um numero inteiro positivo e em seguida mostre este numero 
# invertido.

def inverter(palavra):
    return palavra[::-1]

word = (input('Digite um valor inteiro: '))
invertida = inverter(word)

print(invertida)
