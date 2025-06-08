from modelos import utils
from modelos.restaurante import  Restaurante

def cadastrar_cardapio():
    utils.limpar_tela()
    print('cadastrar cardapio')
    Restaurante.exibir_restaurantes()
    restaurante_id = int(input('Digite o ID do restaurante: '))
    utils.limpar_tela()
    print('Cadastar:\n[1] Pratos.\n[2] Bebidas.')
    cadastrar = int(input('Escolha uma opção: '))
    nome = input('Digite o nome: ')
    preco = float(input('Digite o preco: '))
    if cadastrar == 1:
        descricao = input('Descricao...: ')
        Restaurante.cardapio_prato(nome, preco, descricao, restaurante_id)
    elif cadastrar == 2:
        tamanho = input('Especifique o tamanho: ')
        Restaurante.cardapio_bebida(nome, preco, tamanho, restaurante_id)
    else:
        print('Opção inválida')
        utils.pausar()

    print('Item salvo no cardapio!')
    utils.pausar()
    utils.limpar_tela()