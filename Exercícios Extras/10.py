#Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit. C = 5 * ((F-32) / 9).
temp_c = float(input("Qual a temperatura em Celsius ?"))
temp_f = (temp_c * 1.8 ) + 32

print(f"A temperatura em Fahrenheit será de: {temp_f:.2f} graus")