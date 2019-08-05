# Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.

numPessoas = int(input('Numero de pessoas: '))
soma = 0

for x in range(numPessoas):
    n = int(input('idade:'))
    soma += n

media = soma/numPessoas

if(media>0 and media<26):
   print('Turma jovem: {}'.format(media))
else:
   if(media>25 and media<61):
      print('Turma adulta: {}'.format(media))
   else:
      print('Turma idosa; {}'.format(media))
