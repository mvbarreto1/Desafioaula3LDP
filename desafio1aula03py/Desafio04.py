numero = int(input("Digite um numeral para calcular o fatorial: "))

fatorial = 1
contador = 1

while contador <= numero:
    fatorial *= contador
    contador += 1

print(f"O fatorial de {numero} é: {fatorial}")
