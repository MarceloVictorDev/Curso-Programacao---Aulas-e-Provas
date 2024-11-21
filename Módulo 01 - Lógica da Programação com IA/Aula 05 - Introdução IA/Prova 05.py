#[LPIA-A05]Desenvolva um programa em Python para calcular a média de notas de alunos em uma disciplina. O programa deve solicitar ao usuário o número de alunos
#  e, em seguida, para cada aluno, pedir o nome e três notas. Utilize um loop 'for' para iterar sobre os alunos e suas notas.
# Além disso, implemente uma estrutura condicional para verificar se cada aluno foi aprovado ou reprovado, considerando que a média mínima para aprovação é 7.0. 
# Exiba o nome do aluno, suas notas, média e a indicação de aprovação ou reprovação.
# Ao final, exiba a média geral da turma.

num_alunos = int(input("Por favor, digite o número de alunos da disciplina: "))
soma_turma = 0

for i in range(num_alunos):
    nome_alunos = input(f"Insira o nome do aluno {i+1}: ")
    notas = []
    for m in range(3):
        while True:
                nota = float(input(f"Digite a {m+1}ª nota (0 a 10): "))
                if 0 <= nota <= 10:
                    notas.append(nota)
                    break
                else:
                    print("Nota inválida. Por favor, insira um valor entre 0 e 10.")
    soma_notas = sum(notas)
    soma_turma += soma_notas
    media_aluno = soma_notas / 3
    
    if media_aluno >= 7:
        print(f"\nParabéns {nome_alunos}!")
        print(f"Suas notas foram: {notas}")
        print(f"Sua média foi: {media_aluno:.2f}")
        print("Você está aprovado!\n")
    else:
        print(f"\n{nome_alunos}, suas notas foram: {notas}")
        print(f"Sua média foi: {media_aluno:.2f}")
        print("Infelizmente, você está reprovado.\n")

media_turma = soma_turma / (num_alunos * 3)
print(f"A média geral da turma foi de: {media_turma:.2f}")
