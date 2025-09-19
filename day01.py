#Desafio: Criar um programa que receba do usuário o título de uma tarefa e a exiba na tela.
tarefa = input("Título da tarefa: ")

print(tarefa) #Opção 1 somente o input

print(f"O nome da tarefa é {tarefa}") #Opção 2 input em um texto

#Opção 3 validando se o usuário deixa o titulo vazio
if tarefa != str:  
    print("Titulo invalido")
else:
    print(f"A tarefa {tarefa} é valida")

