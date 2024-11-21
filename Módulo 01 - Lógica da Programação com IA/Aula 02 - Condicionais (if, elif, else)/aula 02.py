#Atividade 01 
idade1 = int(input("Digite sua idade 1: "))
idade2 = int(input("Digite sua idade 2"))

print(f"maior {idade1 >= idade2}")
print(f"menor {idade1 <= idade2}")
print(f"igual {idade1 == idade2}")

#Atividade 02
palavra1 = input("Digite uma palavra")
palavra2 = input("Digite uma palavra")

print(f"Palavras são iguais? {palavra1 == palavra2}")

#Atividade 03
idade = int(input("Digite sua idade: "))
habilitacao = input("Tem habilitação: 'S'para Sim , 'N'para não.")

print(f'Maior de idade e possui habilitação? {idade >= 18 and habilitacao =="S"}')

#Atividade 04
nota1 = float(input("Digite sua nota1: "))
nota2 = float(input("Digite sua nota2: "))

print(f"As duas notas são maiores ou iguais a 06? {nota1 >= 6 and nota2 >= 6}")

#Atividade 05
preco = float(input("Digite o preço do produto: "))

desconto = (preco * 5) / 100
preco = preco - desconto
#Ou pode-se usar o preco -= preco * 0.05
print(f"O preço com desconto é: {preco}")

#Atividade 06
num1 = float(input("digite um número: "))

num1 *= 2

print(f"O dobro do número digitado é: {num1}")

#Atividade 07
frase = input("Digite uma frase")
letra = input("Digite uma letra ")

print(f"A letra digitada está presente na frase ? {letra in frase}")

#Atividade 08
frase = input("Digite uma frase")
palavra= input("Digite uma palavra ")

print(f"A palavra digitada está presente na frase ? {palavra in frase}")

#Atividade 09
num1 = int(input("Digite um número inteiro: "))

if num1 % 2 == 0:
    print(f'O número {num1} é par')
else:
    print(f'O número {num1} é ímpar')

#Atividade 10
nota = float(input('Por favor, digite sua nota: '))

if nota >= 6:
    print("Parábens, você foi aprovado.")
else:
    print("Infelizmente você foi reprovado.")

#Atividade 11
num1 = int(input("Por favor, digite um número inteiro."))

if num1 % 2 == 0 and num1 >= 0:
    print(f"O número {num1} é par e positivo.")

elif num1 % 2 != 0 and num1 >= 0:
    print(f"O número {num1} é ímpar e positivo.")

elif num1 % 2 == 0 and num1 < 0:
    print(f"O número {num1} é par e negativo.")

else: 
    print(f"O número {num1} é ímpar e negativo.")

#Atividade 12
peso = float(input("Por favor, digite seu peso:"))
altura = float(input("Por favor, digite sua altura: "))

imc = peso/ (altura * altura)
# Abaixo do peso
# < 18,50
# Peso normal
# 18,50–24,99
# Sobrepeso
# 25,00–29,99
# Obesidade 
# 30,00–34,99

if imc < 18.5:
    print("Você está abaixo do peso.")
elif imc >= 18.50 and imc <= 24.99:
    print("Você está com o peso normal.")
elif imc >= 25.00 and imc <= 29.99:
    print("Você está com sobrepeso.")
else:
    print("Você está obeso.")

#Atividade 13
usuario = input("Por favor, digite seu usuário: ")
senha = input("Por favor, digite sua senha: ")

if usuario == "admin" and senha == "1234":
    print("usuario e senha não permitidos")
else:
    print("logando...")

#Atividade 14
preco = float(input("Por favor, digite o preco do produto."))
qntd = float(input("Por favor, digite a quantidade comprada."))
total = preco * qntd

if qntd > 10:
    desconto = (preco * qntd) * 0.10
    total = total - desconto
    print("Parabéns, você obteve um desconto de 10%.")
    print(f"O valor total da sua compra era {preco * qntd} e, com desconto de 10% ficou {total}")
else:
    print(f"Você não obteve desconto. Sua compra ficou {total}")



