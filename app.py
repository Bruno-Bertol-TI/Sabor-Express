import os

lista_restaurantes = [1, 2, 3]

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
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair \n')
    
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu')
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
    limpar_tela()
    lista_restaurantes.append(nome_do_restaurante)
    print(f'o restaurante {lista_restaurantes[-1]} foi cadastrado com sucesso')

    voltar_ao_menu_principal()

def listar_restaurante():
    exibir_subtitulo('Listar restaurantes')
    print(10 * '-')
    for restautante in lista_restaurantes:
        print(restautante)
        print(10 * '-')

    print('\nTodos restaurantes cadastrados foram listado acima!')
    voltar_ao_menu_principal()

def finalizar_app():
    exibir_subtitulo('Finalizar APP')

def escolher_opcoes():
    print(10 * '--')
    print('Exemplo:\nDigite o número da opção escolhida: 1.')
    print('Opção 1 escolhida: Cadastrar restaurante.')
    print(10 * '--')
    try:
        print()
        escolha_usuario = int(input('Digite o número da opção escolhida: '))
        limpar_tela()

        if escolha_usuario == 1:
            cadastrar_novo_restaurante()
        elif escolha_usuario == 2:
            listar_restaurante()
        elif escolha_usuario == 3:
            #ativar_restaurante()
            ...
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