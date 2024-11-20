inicio = int(input("Digite o início do intervalo: "))
fim = int(input("Digite o fim do intervalo: "))

if inicio % 2 != 0:
    inicio += 1

while inicio <= fim:
    print(inicio)
    inicio += 2