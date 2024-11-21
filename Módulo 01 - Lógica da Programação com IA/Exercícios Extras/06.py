#Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
# A = pi * r**2

raio = float(input("Por favor, digite o raio do círculo: "))
pi = 3.141592653

area = pi * (raio**2)

print(f'A Área do círculo é de: {area:.2f}')