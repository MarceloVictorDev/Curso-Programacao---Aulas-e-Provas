#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
valor_hora = float(input("Quanto você ganha por hora ?"))
num_horas_mes = float(input("Quantas horas você trabalha no mês? "))
salario = valor_hora * num_horas_mes
print(f"O valor do seu salário no mês será de: {salario:.2f}")
