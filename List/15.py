# Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:
# Mostre a quantidade de valores que foram lidos;
# Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
# Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
# Calcule e mostre a soma dos valores;
# Calcule e mostre a média dos valores;
# Calcule e mostre a quantidade de valores acima da média calculada;
# Calcule e mostre a quantidade de valores abaixo de sete;
# Encerre o programa com uma mensagem;

vNotas = []
soma, count, flag, maiores, menores = 0,0,0,0,0 

while (flag != -1):
    nota = float(input('Digite o valor da nota ou -1 para sair: '))
    
    if nota == -1: 
        flag = -1
    else:
        vNotas.append(nota)
        soma += nota
        count += 1

media = soma/count

for nota in vNotas:
    if nota > media:
        maiores += 1
    elif nota < media:
        menores += 1

print(soma)
print(media)
print(maiores)
print(menores)
print('Tchau.')
