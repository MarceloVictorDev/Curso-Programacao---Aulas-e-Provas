#[LPIA-A06]  Crie um programa em Python que simule um sistema de login. O programa deve permitir ao usuário três tentativas para acertar o nome de usuário e a senha corretos. Caso o usuário erre as credenciais, o programa deve fornecer uma mensagem informando quantas tentativas restam. Se o usuário acertar, uma mensagem de boas-vindas deve ser exibida, e o programa deve terminar imediatamente.
#Se todas as três tentativas falharem, o programa deve usar um loop for para exibir uma mensagem de "Acesso bloqueado" repetida três vezes.
nome_login = "infinity"
senha_login = "dev1234"

tentativas = 1
def linhas():
    print("-" * 30)

while tentativas <= 3:
    nome_usuario = input("Digite seu nome de usuário: ")
    senha_usuario = input("Digite sua senha de usuário: ")
    if nome_usuario == nome_login and senha_usuario == senha_login:
        linhas()
        print(f"Boas Vindas {nome_usuario}!")
        linhas()
        break
    else:
        print(f"Nome de usuário ou senha incorreta. Restam {3 - tentativas} tentativas.")
        tentativas += 1
if tentativas == 4:
    for i in range(3):
        linhas()
        print("Acesso Bloqueado!")
        linhas()