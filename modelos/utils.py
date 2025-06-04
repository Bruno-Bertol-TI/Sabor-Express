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
    3. Ativar / Desativar restaurante
    4. Avaliar restaurantes
    5. Sair
    """)

def pausar():
    input("\nPressione ENTER para voltar ao menu...")
    limpar_tela()