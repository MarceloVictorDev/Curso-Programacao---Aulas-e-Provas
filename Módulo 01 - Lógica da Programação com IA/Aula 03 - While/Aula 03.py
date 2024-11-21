# #Atividade 01: Crie um programa que use um laço while para contar de 1 a 10 e exibir cada número.
contador = 1

while contador <= 10:
    print(contador)
    contador += 1

# #Atividade 02: Escreva um programa que use um laço while para somar os números de 1 a 100 e exiba o resultado.
contador = 1
soma = 0

while contador <= 100:
    soma += contador
    contador += 1
print(soma)

# #Atividade 03: Faça um programa que solicite um número ao usuário e use um laço while para exibir a tabuada desse número (de 1 a 10).
numero = int(input("Por favor, digite um número inteiro: "))
tabuada = 0

print(f"Tabuada de {numero}")
while tabuada <= 10:
    print(f"{numero} * {tabuada} = {numero * tabuada}")
    tabuada += 1

#Atividade 04:
numero = 10

while numero >= 1:
    print(numero)
    numero -= 1
print("Feliz ano novo!")

# #Atividade 05: Crie um programa que solicite um número ao usuário e use um laço while para contar de 1 até o número inserido, exibindo apenas os números ímpares.

numero = int(input("Digite um número inteiro: "))
contador = 1

while contador <= numero:
    if contador % 2 != 0:
        print(contador)
    contador += 1

# #Atividade 06: Escreva um programa que solicite números ao usuário até que ele digite um número negativo, somando apenas os números positivos inseridos.

numero = int(input("Insira um número: "))
soma = 0

while numero >= 0:
    soma += numero
    numero = int(input("Insira um número: "))
print(soma)

#Atividade 07: Faça um programa que solicite um número ao usuário e use um laço while para exibir a tabuada desse número (de 1 a 10), 
# mas apenas para os resultados que forem múltiplos de 3.

numero = int(input("Por favor, insira um número inteiro: "))
contador = 1
mult3 = 1

print(f"Tabuada de {numero}, resultador apenas multiplos de 03.")
while contador <= 10:
    mult3 = numero * contador 
    if mult3 % 3 == 0:
        print(f"{numero} * {contador} = {numero * contador}")
    contador += 1

#Atividade 08: Média de Notas: Desenvolva um programa que solicite as notas dos alunos até que o usuário digite -1. Calcule e exiba a média das notas inseridas.

notas = float(input("Digite suas notas: (para sair, digite -1)"))
contador = 0
media = 0

while notas >= 0: 
    media += notas
    contador += 1
    notas = float(input("Digite suas notas: (para sair, digite -1)"))
print(f"Sua média foi: {media / contador}")

#Atividade 09: Crie um programa que use um laço while para contar de 1 a 10 e termine quando atingir 10.

numero = 1
while numero <= 10:
    print(numero)
    numero += 1

#Atividade 10: Escreva um programa que use um laço while para somar números consecutivos começando de 1 e termine quando a soma atingir ou ultrapassar 50.
numero = 1
soma = 0

while soma <= 50:
    soma += numero
    numero += 1
print(soma)

#Atividade 11: Crie um programa que solicite ao usuário um número entre 1 e 10. Continue pedindo até que o usuário forneça um valor válido.
numero = 11

while numero >= 11 or numero < 0: 
    numero = int(input("Insira um número entre 1 e 10: "))

print("Número Válido.")

#Atividade 12: Desenvolva um programa que peça ao usuário para digitar uma senha e continue pedindo até que a senha correta (previamente definida) seja inserida.
senha = "6789"
digitado = ""

while digitado != senha:
    digitado = input("Tende adivinhar a senha composta de 04 números seguidos: ")

print("Parabéns, você adivinhou a senha.")



