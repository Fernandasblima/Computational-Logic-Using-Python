# Lista para armazenar os produtos
produtos = []

# Funcao para o menu principal
def exibir_menu():
    while True:
        print('#######  Menu #######')
        print('----------------------')
        print('1 - Adicionar Produto')
        print('2 - Visualizar Estoque')
        print('3 - Atualizar Produto')
        print('0 - Sair do Sistema')
        print()
        opcao = input('Escolha uma opcao: ')
        print()
        selecionar_menu(opcao) 
        if opcao == '0':
            exit()

# Funcao para chamar a opcao selecionada pelo usuario
def selecionar_menu(opcao):
    if opcao == '1':
        adicionar_produto()
    elif opcao == '2':
        visualizar_estoque()
    elif opcao == '3':
        atualizar_produto()
    elif opcao == '0':
        print('Saindo do sistema!!!')
    else:
        print('Opcao invalida!')
        print()

# Funcao para adicionar novo produto
def adicionar_produto():
    produto = input('Digite o nome do produto: ')
    while True:
        try:
            preco = float(input('Digite o preco do produto: '))
            break
        except ValueError:
            print(f'Erro: o preco deve ser um numero valido!\n')
    while True:
        try:    
            quantidade = int(input('Digite a quantidade em estoque: '))
            break
        except ValueError:
            print(f'Erro: A quantidade deve ser um numero inteiro valido!\n')
    novo_produto = {'produto': produto, 'preco': preco, 'quantidade': quantidade}
    produtos.append(novo_produto)
    print(f'Produto {produto} adicionado com sucesso!\n')

# Funcao para visualizar os produtos no estoque
def visualizar_estoque():
    if not produtos:
        print('O estoque esta vazio!\n')
    else:
        for index, produto in enumerate(produtos):
            print(f'{index + 1} - Produto: {produto["produto"]}, Preço: R${produto["preco"]:.2f}, Quantidade: {produto["quantidade"]}')
        print()

# Funcao para atualizar um produto
def atualizar_produto():
    if not produtos:
        print('O estoque esta vazio! Nao e possivel atualizar.\n')
        return
    visualizar_estoque()
    nome_produto = input('Escolha o produto que deseja atualizar: ')
    for produto in produtos:
        if produto['produto'].lower() == nome_produto.lower():
            while True:
                try:
                    preco = float(input('Digite o novo preco do produto: '))
                    break
                except ValueError:
                    print(f'Erro: o preco deve ser um numero valido!\n')
            while True:
                try:    
                    quantidade = int(input('Digite a quantidade em estoque: '))
                    break
                except ValueError:
                    print(f'Erro: A quantidade deve ser um numero inteiro valido!\n')     
            produto['preco'] = preco
            produto['quantidade'] = quantidade
            print(f'Produto {nome_produto} atualizado com sucesso!\n')
            return
    print(f'Produto {nome_produto} nao encontrado no estoque!\n')
    atualizar_produto()

# Chama a funcao do menu principal
exibir_menu()