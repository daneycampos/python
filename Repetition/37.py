# Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e o mais magro, para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu código, sua altura e seu peso. O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código. Ao encerrar o programa também deve ser informados os códigos e valores do clente mais alto, do mais baixo, do mais gordo e do mais magro, além da média das alturas e dos pesos dos clientes

fatter = float('-inf')
tallest = float('-inf')

thinner = float('inf')
smallest = float('inf')

idFatter = 0
idTallest = 0 
idThinner = 0
idSmallest = 0

while (True):
    cod = int(input('Digite o codigo do cliente: '))
        if (cod == 0):
            break
    weight = float(input('Digite o peso do cliente: '))
    height = float(input('Digite a altura do cliente: '))

    if (weight > fatter):
        fatter = weight
        idFatter = cod
    if (weight < thinner):
        thinner = weight
        idThinner = cod
    if (height > tallest):
        tallest = height
        idTallest = cod
    if (height < smallest):
        smallest = height
        idSmallest = height
