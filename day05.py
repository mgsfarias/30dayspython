#Desafio: Organizar o código criando funções para adicionar e listar tarefas.

#lista vazia que vai armazenar as tarefas.
tarefas = []

#função para adicionar novas tarefas
def adicionar_tarefa():
    tarefa = input("\nDigite uma tarefa: ").strip()
    #se estiver vazia ou somente numeros retorna com erro
    while tarefa == "" or tarefa.isdigit():
        print("Tarefa inválida. Digite um texto válido")
        tarefa = input("\nDigite uma tarefa: ").strip()
    tarefas.append(tarefa)
    print("Tarefa adicionada com sucesso!")

#função para listar tarefas
def listar_tarefas():
    #se estiver vazia informa que não existe cadastros
    if not tarefas:
        print("\nNenhuma tarefa cadastrada ainda.")
    else:
        print("\nLista de tarefas:")
        for i, t in enumerate(tarefas, start=1):
            print(f"{i}. {t}")

while True:
    #exibe as opções do menu para o usuário
    print("""\n Menu:
    1 - Adicionar tarefa
    2 - Listar tarefas
    3 - Sair""")

    #pede a escolha do usuário
    opcao = input("\nEscolha uma opção: ")

    #verifica se a opção escolhida foi "1"
    if opcao == "1":
        adicionar_tarefa()
    elif opcao == "2":
        listar_tarefas()
    elif opcao == "3":
        print("Saindo do programa...")
        break
    else:
        print("Opção invalida, tente novamente.")