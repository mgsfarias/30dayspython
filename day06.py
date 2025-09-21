# Desafio: Cada tarefa deve ter título e status (pendente/concluída)

# cria uma lista vazia que irá armazenar várias tarefas
# cada tarefa será representada por um dicionário: {"titulo": "...", "status": "..."}
tarefas = []

# função para adicionar uma nova tarefa
def adicionar_tarefa():
    # inicia um loop para garantir que só saímos quando tivermos um título válido
    while True:
        # pede ao usuário o título da tarefa e remove espaços no início/fim
        titulo = input("\nDigite o título da tarefa: ").strip()
        
        # verifica se o título está vazio ("" após strip) ou é composto só por números
        if titulo == "" or titulo.isdigit():
            # avisa o usuário sobre a entrada inválida e repete o loop
            print("Tarefa inválida. Não pode estar vazia nem ser apenas números.")
            continue  # volta ao começo do while para pedir novamente
        
        # cria um dicionário representando a tarefa com status padrão "pendente"
        tarefa = {"titulo": titulo, "status": "pendente"}
        
        # adiciona o dicionário na lista 'tarefas' no final dela
        tarefas.append(tarefa)
        
        # confirma para o usuário que a tarefa foi adicionada
        print("\nTarefa adicionada com sucesso!")
        # sai do loop while pois já adicionamos a tarefa com sucesso
        break

# função para listar todas as tarefas (com numeração e status)
def listar_tarefas():
    # se a lista estiver vazia, avisa o usuário e retorna ao menu (return)
    if not tarefas:
        print("\nNenhuma tarefa foi cadastrada ainda.")
        return
    
    # imprime um cabeçalho antes da listagem
    print("\n Lista de tarefas:")
    # percorre cada tarefa com índice (enumerate) começando em 1 para exibirmos "1., 2., ..."
    for i, tarefa in enumerate(tarefas, start=1):
        # para cada dicionário 'tarefa', mostra o título e o status entre colchetes
        print(f"{i}. {tarefa['titulo']} - [{tarefa['status']}]")

# função para marcar uma tarefa como concluída
def concluir_tarefa():
    # se não houver tarefas, avisa e retorna ao menu
    if not tarefas:
        print("\nNenhuma tarefa foi cadastrada para concluir ainda.")
        return
    
    # mostra a lista atual para o usuário escolher o número correspondente
    listar_tarefas()
    
    # loop para garantir entrada válida (número dentro do intervalo ou cancelar)
    while True:
        # pede ao usuário para digitar o número da tarefa ou 'c' para cancelar
        escolha = input("\nDigite o número da tarefa a marcar como concluída (ou 'c' para cancelar): ").strip()
        
        # se o usuário optar por cancelar, sai da função
        if escolha.lower() == "c":
            print("Operação cancelada.")
            return
        
        # valida se a escolha é um número
        if not escolha.isdigit():
            print("Por favor, digite um número válido ou 'c' para cancelar.")
            continue
        
        # converte para índice da lista (0-based)
        indice = int(escolha) - 1
        
        # verifica se o índice está dentro do intervalo da lista
        if indice < 0 or indice >= len(tarefas):
            print("Número fora do intervalo. Tente novamente.")
            continue
        
        # se a tarefa já estiver concluída, informa e retorna (ou poderia permitir desmarcar)
        if tarefas[indice]["status"] == "concluída":
            print("Essa tarefa já está marcada como concluída.")
            return
        
        # altera o status da tarefa selecionada para 'concluída'
        tarefas[indice]["status"] = "concluída"
        
        # confirma para o usuário qual tarefa foi marcada
        print(f" Tarefa '{tarefas[indice]['titulo']}' marcada como concluída!")
        return  # sai da função após marcar

# loop principal do menu — continua até o usuário escolher sair
while True:
    # exibe o menu com opções
    print("""
 Menu:
1 - Adicionar tarefa
2 - Listar tarefas
3 - Concluir tarefa
4 - Sair
""")
    # lê a opção do usuário (texto)
    opcao = input("Escolha uma opção: ").strip()
    
    # verifica cada opção e chama a função correspondente
    if opcao == "1":
        adicionar_tarefa()   # adiciona nova tarefa
    elif opcao == "2":
        listar_tarefas()     # lista as tarefas atuais
    elif opcao == "3":
        concluir_tarefa()    # marca uma tarefa como concluída
    elif opcao == "4":
        print("Saindo do programa. Até logo!")
        break                # encerra o loop principal e finaliza o programa
    else:
        # caso digite algo inválido, informa e o menu reaparece
        print("Opção inválida, tente novamente.")
