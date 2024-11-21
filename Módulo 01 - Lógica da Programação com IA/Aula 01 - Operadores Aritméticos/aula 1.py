saudacao = str("hello world")
print(saudacao)

nome = str()
idade = int()
altura = float()

nome = str(input("Olá, insira seu nome:"))
idade = int(input("Digite sua idade:"))
altura = float(input("Insira sua altura"))
    
print(f"seu nome é: {nome} ,Sua idade é: {idade},Sua altura é: {altura}")
print(f"{nome} = type(nome)")
print(f"{idade}type(idade)")
print(f"{idade}type(altura)")

#Atividade 04 notas bimestrais
nota1 = float(input("Por favor, digite a nota do PRIMEIRO bimestre: "))
nota2 = float(input("Por favor, digite a nota do SEGUNDO bimestre: "))
nota3 = float(input("Por favor, digite a nota do TERCEIRO bimestre: "))
nota4 = float(input("Por favor, digite a nota do QUARTO bimestre: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

print(f"A média dos seus 04 bimestres foi: {media}")

#Atividade salário hora
dias = 20

salario_mensal = float(input("Qual seu salário mensal?"))
horas_semana = float(input("Quantas horas você trabalha na semana?"))

n_horasmes = horas_semana * 4
salario_hora = salario_mensal / n_horasmes

print(f"Seu salário por hora é: {salario_hora}")

#Atividade Cidade natal
nome = input("Qual é o seu nome? ")
idade = int(input("Qual sua idade?"))
cidade = input("Qual sua cidade natal?")

print(f"Seu nome é {nome}, sua idade é {idade}, Sua cidade natal é: {cidade}")
