# Nome: Pedro Henrique do Nascimento Urbano | Turma: 2190 | Exercício 03

# Dicionário Vazio [{}] - "Tarefas":
tarefas = {}

# Funções [def] - Uma para cada Opção (choice):
def cadastrar(titulo,tarefa):
    tarefas[titulo] = tarefa

def alterar(titulo):
    tarefas[novo_titulo] = tarefas.pop(titulo)

def alterar_2(titulo):
    tarefas[titulo] = nova_tarefa

def excluir(titulo):
    if titulo in tarefas.keys():
        tarefas.pop(titulo)
        print('Tarefa excluída com sucesso!')
    else:
        print('Título não encontrado!')
def pesquisar():
    for titulo,tarefa in tarefas.items():
        print(f'{titulo}: {tarefa}')
    print(f'Títulos das tarefas em ordem alfabética: {sorted(tarefas.values())}')

while True:
    print('''
             |------------------------|
             |     Menu de Opções     |
             |------------------------|
             | C | Cadastrar;         |
             | A | Alterar;           |
             | E | Excluir;           |
             | P | Pesquisar tarefas; |
             | S | Sair.              |
             |------------------------|
                                       ''')
    choice = input('Digite a opção desejada:').capitalize()

    if choice == 'C':
        titulo = input('Defina um título para a tarefa:')
        tarefa = input('Digite a tarefa a ser registrada:')
        cadastrar(titulo,tarefa)

    elif choice == 'A':
        for titulo,tarefa in tarefas.items():
            print(f'{titulo}: {tarefa}')
        print('O que deseja alterar?\n 1 - Título\n 2 - Tarefa')
        choice = int(input('Digite o número da opção desejada:'))
        if choice == 1:
            titulo = input('Digite o nome do titulo que deseja alterar:').capitalize()
            if titulo in tarefas.keys():
                novo_titulo = input(f'Digite o novo título para {titulo}:').capitalize()
                alterar(titulo)
                print(f'Listagem atual de títulos: {tarefas.keys()}')
        elif choice == 2:
            titulo = input('Digite o título da tarefa que deseja alterar:').capitalize()
            if titulo in tarefas.keys():
                nova_tarefa = input(f'Digite a nova tarefa a ser registrada:').capitalize()
                alterar_2(titulo)
                print(f'Listagem atual de tarefas: {tarefas.values()}')
        else:
            print('Opção inválida, tente novamente!')
            continue

    elif choice == 'E':
        for titulo,tarefa in tarefas.items():
            print(f'{titulo}: {tarefa}')
        titulo = input('Digite o nome do título ao qual deseja excluir:')
        excluir(titulo)

    elif choice == 'P':
        pesquisar()

    elif choice == 'S':
        print('Saindo do programa...')
        break

    else:
        print('Opção inválida, tente novamente!')
        continue