numero = int(input("Digite um número: "))

while numero >= 10:
    soma = 0
    while numero > 0:
        soma += numero % 10
        numero //= 10
    numero = soma

print("Soma final é:", numero)

