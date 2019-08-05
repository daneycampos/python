voto = -1
jogadores = []
count = 0

for x in range(23):
    jogadores.append(0)

while(True):
    voto = int(input('Numero do jogador (0 para sair): '))
    
    if (voto == 0):
        break
    elif (voto<0 or voto>23):
        print('Numero inválido.')
    else: 
        jogadores[voto] += 1
        count += 1

print('\nResultado:')
print('\nForam computados {} votos'.format(count))
print('\nJogador', end='')
print(linha, end='')
print('Votos')

# for x in range(23):
#     if (jogadores[x] != 0):
        # print('{}')
