numero = int(input("Digite um número: "))

while numero != 1:
    print(numero)
    if numero % 2 == 0:
        numero //= 2
    else:
        numero = 3 * numero + 1
print(numero)

