from modelos.restaurante import Restaurante
from modelos import utils

def listar_cardapio():
    utils.limpar_tela()
    print('Listar Cardapio')
    Restaurante.exibir_restaurantes()
    id = int(input('Digite o Id:'))
    Restaurante.exibir_cardapio_completo(id)
    input()