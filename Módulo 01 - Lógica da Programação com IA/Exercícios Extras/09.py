#Faça um Programa que peça a temperatura em graus Fahrenheit,transforme e mostre a temperatura em graus Celsius. C = 5 * ((F-32) / 9).
temp_f = float(input("Qual a temperatura em Fahrenheit ?"))
celsius = 5 * ((temp_f - 32) / 9)

print(f"A temperatura em Celsius será de: {celsius:.2f} graus")