#Prova 02:[PYIA-A02] Crie um dicionário que irá armazenar informações de um contato, incluindo o nome, o telefone e o email. Peça ao usuário para fornecer esses dados, solicitando que ele insira o nome do contato, o número de telefone e o endereço de email. Após coletar todas as informações necessárias, exiba o conteúdo do dicionário, mostrando todas as informações do contato inserido pelo usuário.
nome_contato = " "
telefone_contato = 0
email_contato = " "

contato = {
    "nome" : nome_contato,
    "telefone" : telefone_contato,
    "email" : email_contato
}
print("\nPara seguir com sua solicitação, iremos precisar de alguns dados pessoais para cadastro no nosso sistema. Por favor, siga as informaçãoes a seguir.\n")
contato["nome"] = input("Digite seu nome: ")
contato["telefone"] = int(input("Digite seu telefone para contato com DDD: "))
contato["email"] = input("Digite seu email: ")

print("-" * 40)
print(f"Suas informações para contato são:")
for chave, valor in contato.items():
    print(f"{chave} -> {valor}")
print("-" * 40)