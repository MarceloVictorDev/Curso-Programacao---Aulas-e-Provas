#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

altura = float(input("Digite sua altura: "))
sexo = input("Digite 'h' para homem, ou 'm' para mulher: ")

if sexo == "h":
    ideal = (72.7 * altura) - 58
    print(f"Seu peso ideal é de: {ideal:.2f}")
else:
    ideal = (62.1 * altura) - 44.7
    print(f"Seu peso ideal é de: {ideal:.2f}")