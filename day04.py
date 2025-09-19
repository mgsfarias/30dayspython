# Desafio: Criar um menu que permita ao usuário adicionar e listar tarefas até decidir sair

tarefas = [] #lista vazia para armazenar tarefas

#loop principal do menu, que só vai parar quando o usuário escolher a opção "sair"
while True:
    #exibe as opções do menu para o usuário
    print("\n Menu:")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Sair")

    #pede a escolha do usuário
    opcao = input("Escolha uma opção: ")

    #verifica se a opção escolhida foi "1"
    if opcao == "1":
        #pede a descrição da tarefa e remove espaços extras
        tarefa = input("Digite a nova tarefa: ").strip()

        #validação: não aceitar vazio ou números
        while tarefa == "" or tarefa.isdigit():
            print("Tarefa inválida! Digite um texto válido.")
            tarefa = input("Digite a nova tarefa: ").strip()

        #adiciona a tarefa à lista
        tarefas.append(tarefa)
        print("Tarefa adicionada com sucesso!")
    
    #verifica se a opção escolhida foi "2"
    elif opcao == "2":
        #se a lista estiver vazia, avisa ao usuário
        if not tarefas:
            print("Nenhuma tarefa foi cadastrada ainda.")
        else:
            print("\n Lista de tarefas:")
            #percorre a lista e mostra cada tarefa numerada
            for i, t in enumerate(tarefas, start=1):
                print(f"{i}. {t}")

    #verifica se a opção escolhida foi "3"
    elif opcao == "3":
        print("Saindo do programa. Até logo!")
        break #interrompe o while e encerra o programa

    #se a opção não for nenhuma das válidas
    else:
        print("Opção inválida, tente novamente.")

    