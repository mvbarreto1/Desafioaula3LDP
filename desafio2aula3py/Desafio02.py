numero = int(input("Digite um número para iniciar a contagem regressiva: "))

while numero >= 0:
    print(numero)
    
    if numero % 2 == 0:
        print("Número par")
    
    numero -= 1