# # Estrutura do FOR

# for variavel in range(1 , 11, 1):
# # FOR ; Variável ; IN ; Range (Primeiro número que vai iniciar, último número + 1 , De quantos em quantos ele vai percorrer)
# # Range é usado para sequência de números inteiros.

#Atividade 01:Faça um programa que solicite um número ao usuário e use um laço for para exibir a tabuada desse número (de 1 a 10).

num = int(input("Por favor, digite um número entre 1 e 10: "))

print(f"Tabuada de {num}")
for i in range(1, 11):
    print(f"{num} * {i} = {num * i}")

#Atividade 02: Crie um programa que use um laço for para somar todos os números de 1 a 100 e exiba o resultado.
resultado = 0
for i in range(1, 101):
    resultado += i
print(resultado)

#Atividade 03: Escreva um programa que solicite uma palavra ao usuário e use um laço for para exibir cada caractere da palavra em uma linha separada.
palavra = input("Insira uma palavra: ")
for i in palavra:
    print(i)

#Atividade 04: Desenvolva um programa que use um laço for para fazer uma contagem regressiva de 10 até 1 e, em seguida, exiba "Feliz Ano Novo!".
for i in range(10, 0, -1):
    print(i)
print("Feliz Ano Novo!")

#Atividade 05: Escreva um programa que solicite ao usuário 10 números e use um laço for com uma condicional para contar quantos são positivos e quantos são negativos.
contador_positivo = 0
contador_negativo = 0
nulo = 0 

for i in range(10):
    num = int(input("Digite um número: "))
    if num > 0:
        contador_positivo += 1
    elif num < 0:
        contador_negativo += 1
    else:
        nulo += 1
print(f"Positivos: {contador_positivo}")
print(f"Negativos: {contador_negativo}")
print(f"Nulos: {nulo}")

#Atividade 06: Escreva um programa que use um laço for para somar todos os números pares de 1 a 50 e exiba o resultado final.
contador = 0
for i in range(1, 51):
    if i % 2 == 0:
        contador += i
print(contador)

#Atividade 07: Crie um programa que solicite uma palavra ao usuário e use um laço for com uma condicional para contar quantas vogais (a, e, i, o, u) a palavra contém.
palavra = input("Digite uma palavra: ")
contador = 0

for i in palavra:
    if i.lower() in 'aeiou':
        contador +=1
print(f"A palavra '{palavra}' contém {contador} vogais.")

#Atividade 08: Escreva um programa que solicite 5 notas de alunos. Use um laço for para somar as notas e uma condicional para exibir a média e a
# classificação ("Aprovado" para média >= 6, "Reprovado" para média < 6).
soma = 0
for i in range(5): 
    notas = float(input("Digite suas notas: "))
    soma += notas

media = soma / 5
if media >= 6:
    print("Aprovado!")
else:
    print("Reprovado!")