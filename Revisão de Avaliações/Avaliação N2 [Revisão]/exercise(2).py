funcionarios = {}

while True:
    print('''
             |--------------------|
             |   Menu de Opções   |
             |--------------------|
             | C | Cadastrar;     |
             | A | Alterar;       |
             | E | Excluir;       |
             | P | Pesquisar;     |
             | S | Sair.          |
             |--------------------|
                                   ''')
    choice = input('Digite a opção desejada:').capitalize()

    if choice == 'C':
        nome = input('Digite o nome do funcionário:').capitalize()
        cargo = input(f'Digite o nome do cargo de {nome}:').capitalize()
        funcionarios[nome] = cargo # Resultado --> {'Pedro': 'Financeiro'}
        print(f'Listagem atual de funcionários: {funcionarios}')

    elif choice == 'A':
        print('O que deseja alterar?\n 1 - Funcionário\n 2 - Cargo')
        choice = int(input('Digite o número da opção desejada:'))
        if choice == 1:
            print(f'Listagem atual de funcionários (nomes): {funcionarios.keys()}')
            nome = input('Digite o nome do funcionário que deseja alterar:').capitalize()
            if nome in funcionarios.keys():
                novo_nome = input(f'Digite o novo nome para {nome}:').capitalize()
                funcionarios[novo_nome] = funcionarios.pop(nome) # Resultado --> {'Pedro': 'Advogado'} SERÁ {'Augusto': 'Advogado'}
                print(f'Listagem atual de funcionários: {funcionarios}')
        elif choice == 2:
            print(f'Listagem atual de funcionários (cargos): {funcionarios}')
            nome = input('Digite o nome do funcionário que deseja alterar o cargo:').capitalize()
            if nome in funcionarios.keys():
                novo_cargo = input(f'Digite o novo cargo para alterar "{cargo}":').capitalize()
                funcionarios[nome] = novo_cargo # Resultado --> {'Pedro': 'Advogado'} SERÁ {'Augusto': 'Promotor'}
                print(f'Listagem atual de funcionários: {funcionarios}')
        else:
            print('Opção inválida, tente novamente!')
            continue

    elif choice == 'E':
        print(f'Listagem atual de funcionários: {funcionarios}')
        nome = input('Digite o nome do funcionário a ser removido:').capitalize()
        if nome in funcionarios.keys():
            funcionarios.pop(nome)
            print('Funcionário removido com sucesso!')
        else:
            print('Nome não encontrado, tente novamente!')
            continue

    elif choice == 'P':
        for nome,cargo in funcionarios.items():
            print(f'{nome}: {cargo}')
        print(f'Listagem em ordem Alfabética: {sorted(funcionarios.values())}')
        print(f'Número total de funcionários cadastrados: {len(funcionarios)}')
        
    elif choice == 'S':
        print('Saindo do programa...')
        break
    else:
        print('Opção inválida, tente novamente!')
        continue