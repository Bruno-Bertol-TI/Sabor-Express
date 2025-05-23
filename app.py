import os

lista_restaurantes = [
    {'nome': 'dona brida', 'categoria': 'brasileira', 'ativo': False}, 
    {'nome': 'don juan', 'categoria': 'mexicana', 'ativo': False},
    {'nome': 'teste_1', 'categoria': 'teste_1', 'ativo': False},
    {'nome': 'teste_2', 'categoria': 'teste_2', 'ativo': False},
    {'nome': 'teste_3', 'categoria': 'teste_3', 'ativo': False},
    {'nome': 'teste_4', 'categoria': 'teste_4', 'ativo': False}
    ]

def exibir_nome_do_programa():
    print("""
            '░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
            ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
            ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
            ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
            ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
            ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
            """)
    
def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar restaurante')
    print('4. Sair \n')
    
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu: ')
    limpar_tela()
    main()

def opcao_invalida():
    limpar_tela()
    print('Opção invalida!')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    limpar_tela()
    print(texto)
    print()

def cadastrar_novo_restaurante():

    exibir_subtitulo('Cadastrar novo restaurante')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria_do_restaurante = input(f'Digite a categoria do restaurante {nome_do_restaurante}: ')
    dados_cadastrados = {'nome': nome_do_restaurante, 'categoria': categoria_do_restaurante, 'ativo': False}
    lista_restaurantes.append(dados_cadastrados)
    voltar_ao_menu_principal()

def listagem_restaurantes():
    linha_divisoria_listagem_restaurantes = '|' + 125 * '-' + '|'

    print(linha_divisoria_listagem_restaurantes)
    print(f"|{'ID':^25} | {'Restaurante':^35} | {'Categoria':^30} | {'Condição':^25} |")
    print(linha_divisoria_listagem_restaurantes)
    
    for i, restaurante in enumerate(lista_restaurantes):
        nome = restaurante['nome']
        categoria = restaurante['categoria']
        ativo_inativo = 'Ativo' if restaurante['ativo'] == True else 'Inativo'
        ativo = ativo_inativo
        print(f"|{i:^25} | {nome:<35} | {categoria:<30} | {ativo:<25} |")
        print(linha_divisoria_listagem_restaurantes)

def listar_restaurante():
    exibir_subtitulo('Listar restaurantes')
    listagem_restaurantes()
    print('\nTodos restaurantes cadastrados foram listado acima!')
    voltar_ao_menu_principal()

def ativar_restaurante():
    exibir_subtitulo('Ativar Restaurante')
    listagem_restaurantes()   
    print()
    try:
        ativacao = int(input('Digite o número do restaurante que deseja ativar: '))
        lista_restaurantes[ativacao]['ativo'] = True

        mensagem_ativação = ' ativado com Sucesso'if lista_restaurantes[ativacao]['ativo'] == True else f' não foi ativado'
        print(f'\nRestaurante {lista_restaurantes[ativacao]['nome']} {mensagem_ativação}')
    except:
        opcao_invalida()

    voltar_ao_menu_principal()
    
def finalizar_app():
    exibir_subtitulo('Finalizar APP')

def escolher_opcoes():
    try:
        escolha_usuario = int(input('Digite o número da opção escolhida: '))
        limpar_tela()

        if escolha_usuario == 1:
            cadastrar_novo_restaurante()
        elif escolha_usuario == 2:
            listar_restaurante()
        elif escolha_usuario == 3:
            ativar_restaurante()
        elif escolha_usuario == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcoes()

if __name__ == '__main__':
    main()