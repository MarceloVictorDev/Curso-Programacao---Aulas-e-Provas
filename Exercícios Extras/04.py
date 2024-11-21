# #Faça um Programa que peça as 4 notas bimestrais e mostre a média.
# num1 = float(input("Digite sua nota 01: "))
# num2 = float(input("Digite sua nota 02: "))
# num3 = float(input("Digite sua nota 03: "))
# num4 = float(input("Digite sua nota 04: "))

# media = (num1 + num2 + num3 + num4) / 4

# print(f"Sua média foi: {media}")

lista = []

while True:
    print("Menu\n")
    print("1: Contar de 1 até 5")
    print("2: Criar uma lista de números")
    print("3: Verificar quantos números da lista são pares, ímpares, negativos ou positivos")
    print("4: Sair do programa")
    opcao = input("Digite uma opção de 1 a 4 ")

    if opcao == "1":
        for i in range(6):
            print(i)
    elif opcao == 2:
        insercao = int(input(""))
        lista.append(insercao)
        print(lista)
    elif opcao == 3:
        pos = 0
        neg = 0
        impar = 0
        par = 0
        for i in lista:
            if i > 0:
                pos += 1
            elif i < 0:
                neg += 1
            elif i % 2 == 0:
                par += 1
            elif i % 2 == 1:
                impar += 1
        print(f"Temos {pos} positivos, {neg} negativos, {par} pares e {impar} impares\n")
    elif opcao == 4:
        print ("Saindo do programa")
        break
    else:
        print("Opção inválida")