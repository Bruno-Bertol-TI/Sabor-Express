import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_titulo():
    print("""
    === Sistema de Gestão de Restaurantes ===
    """)

def exibir_menu():
    print("""
    1. Cadastrar restaurante
    2. Listar restaurantes
    3. Listar avaliações
    4. Ativar / Desativar restaurante
    5. Avaliar restaurantes
    6. Sair
    """)

def pausar():
    input("\nPressione ENTER para voltar ao menu...")
    limpar_tela()

def em_massa():
    print('[1] Em massa.')
    print('[2] Unitário.')
    opcao = int(input('Digite a opção 1 ou 2: '))
    limpar_tela()
    return opcao

def quantidade_funcao_em_massa():
    print('Opção em massa')
    repeticoes = int(input('Quantas repetições deseja: '))
    limpar_tela()
    return repeticoes