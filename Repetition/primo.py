def primo(x):
        divisoes = 0
        contador = 0
        for divisor in range(1, x):
                if (x%divisor == 0):
                        contador += 1
                        divisoes += 1
                if contador > 1:
                        break

        if (contador < 2):
                return True, divisoes
        else:
                return False, divisoes


valor = int(input('Valor: '))
primos = []
divisoes = 0

for x in range(1, valor):
        result = primo(x)
        divisoes += result[1]

        if (result[0]):
                primos.append(x)

print(primos)
print(divisoes)
