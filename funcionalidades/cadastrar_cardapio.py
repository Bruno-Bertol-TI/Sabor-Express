from modelos import utils
from modelos.restaurante import  Restaurante

def cadastrar_cardapio():
    utils.limpar_tela()
    print('cadastrar cardapio')
    Restaurante.exibir_restaurantes()

    try:
        restaurante_id = int(input('Digite o ID do restaurante: '))
    except ValueError:
        print('ID inválido!')
        utils.pausar()
        return
    
    utils.limpar_tela()
    print('Cadastar:\n[1] Pratos.\n[2] Bebidas.')

    try:
        cadastrar = int(input('Escolha uma opção: '))
    except ValueError:
        print('Opção inválida!')
        utils.pausar()
        return
    
    nome = input('Digite o nome: ')

    try:
        preco = float(input('Digite o preco: '))
    except ValueError:
        print('Preço inválido!')
        utils.pausar()
        return
    
    item = None

    if cadastrar == 1:
        descricao = input('Descricao...: ')
        item = Restaurante.cardapio_prato(nome, preco, descricao, restaurante_id)
    elif cadastrar == 2:
        tamanho = input('Especifique o tamanho: ')
        item = Restaurante.cardapio_prato(nome, preco, tamanho, restaurante_id)
    else:
        print('Opção inválida')
        utils.pausar()
        return

    if not item:
        print('Erro ao cadastrar produto.')
        utils.pausar()
        return
    
    if deseja_aplicar_desconto():
        item.aplicar_desconto()

    print('Item salvo no cardapio!')
    utils.pausar()
    utils.limpar_tela()

def deseja_aplicar_desconto():
    print('Deseja aplicar desconto?\n[1] Sim\n[2] Não')
    try:
        opcao = int(input('Escolha uma opção: '))
        return opcao == 1
    except ValueError:
        return False