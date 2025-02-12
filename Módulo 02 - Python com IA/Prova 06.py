tarefas = []

def menu():
    print("-"*50)
    print("Menu do organizador\n")
    print("1 - Adicionar nova tarefa.")
    print("2 - Listar tarefas: ")
    print("3 - Marcar Tarefa como concluída.")
    print("4 - Exibir tarefas por prioridade")
    print("5 - Sair")
    print("-"*50)

def adicionar_tarefa():
    nome_tarefa = input("Digite aqui o nome da tarefa: ")
    descricao = input("Digite aqui a descrição dessa tarefa: ")
    prioridade = int(input("Digite aqui a prioridade: (onde 0 é a prioridade máxima e 5 é baixa prioridade) "))
    categoria = int(input("Digite aqui a categoria dessa tarefa:\n 1-Casa\n 2-Pessoal\n 3-Finanças\n 4-Trabalho\n 5-Estudos\n 6-Outros\n"))

    nova_tarefa = {
    "nome" : nome_tarefa,
     "descricao" : descricao,
     "prioridade" : prioridade,
     "categoria" : categoria
    }
    
    tarefas.append(nova_tarefa)
    print("\n Tarefa Adicionada com sucesso!\n")

def listar_tarefas():
    print("\nLista de Tarefas:")
    for i, tarefa in enumerate(tarefas, 1):
        print(f"{i}. Nome: {tarefa['nome']}, Descrição: {tarefa['descricao']}, Prioridade: {tarefa['prioridade']}, Categoria: {tarefa['categoria']}\n")
    

def concluir_tarefa():
    global tarefas

    print("\nLista de Tarefas Pendentes:")
    for i, tarefa in enumerate(tarefas, 1):
        print(f"{i}. Nome: {tarefa['nome']} -  Descrição: {tarefa['descricao']} - Prioridade: {tarefa['prioridade']} - Categoria: {tarefa['categoria']}")
    nome_tarefa_concluida = input("Digite aqui o nome da tarefa que você quer remover:  ")
    for tarefa in tarefas:
        if tarefa["nome"].lower() == nome_tarefa_concluida.lower():
            tarefas.remove(tarefa)
            print(f"A tarefa {nome_tarefa_concluida} foi concluída com sucesso.")
            return
        else: 
            print("Tarefa não encontrada.")

def prioridades():
    global tarefas
    tarefas = sorted(tarefas, chave=lambda tarefa: tarefa["prioridade"])  
    print("\nTarefas organizadas por prioridade!\n")
    


while True:
    menu()
    opcao = int(input("Digite aqui a opção: "))

    if opcao == 1:
        adicionar_tarefa()
    elif opcao == 2:
        listar_tarefas()
    elif opcao == 3:
        concluir_tarefa()
    elif opcao == 4:
        prioridades()
        listar_tarefas()
    elif opcao == 5:
        break
    else:
        print("Opção inválida, tente novamente!")



        

