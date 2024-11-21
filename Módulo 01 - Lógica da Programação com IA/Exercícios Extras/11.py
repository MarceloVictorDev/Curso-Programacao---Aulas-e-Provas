#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#     o produto do dobro do primeiro com metade do segundo.
#     a soma do triplo do primeiro com o terceiro.
#     o terceiro elevado ao cubo.

num1_int = int(input("Por favor, digite um número inteiro: "))
num2_int = int(input("Por favor, digite outro número inteiro: "))
num_real = float(input("Por favor, digite mais um número: "))

op_01 = (num1_int * 2) * (num2_int / 2)
op_02 = (num1_int * 3) + num_real
op_03 = num_real**3

print(f"O resultado da primeira operação foi de: {op_01:.2f}")
print(f"O resultado da segunda operação foi de: {op_02:.2f}")
print(f"O resultado da terceira operação foi de: {op_03:.2f}")