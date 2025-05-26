import os

lista_restaurantes = []

def exibir_nome_do_programa():
    '''Exibe o nome do sistema de forma estilizada para a interação com o usuário'''
    print("""
            '░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
            ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
            ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
            ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
            ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
            ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
            """)
    
def exibir_opcoes():
    '''
    Exibe funções disponiveis no menu principal do sistema

    - Quais são elas?
    1. Cadastrar Restaurante
    2. Listar Restaurantes
    3. Ativar/Desativar Restaurante
    4. Sair -> Encerra a execução do sistema
    
    '''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar/Desativar restaurante')
    print('4. Sair \n')
    
def limpar_tela():
    '''
    Limpa a tela em multiplataformas Linux/MacOS/WINDOWS
    
    - função usa 'cls' para Windows e 'clear' para as demais plataformas 

    '''
    os.system('cls' if os.name == 'nt' else 'clear')

def voltar_ao_menu_principal():
    '''
    Retorna ao menu principal
    
    - inputs:]
        + Apenas uma trava para exibir outputs anteriores ao uso dessa função

    usa a função 'limpar_tela()' multiplataformas, e, 
    usa a função main para retornar ao inicio do programa
    '''
    input('\nTecle [Enter] para retornar ao Menu Principal: ')
    limpar_tela()
    main()

def opcao_invalida():
    '''
    Função resposavel para alertar entradas de dados invalidos.

    limpa a tela com função 'limpar_tela()',
    exibe mensagem de erro, e, 
    retorna ao menu principal usando a função 'voltar_ao_menu_principal()'
    '''
    limpar_tela()
    print('Opção invalida!')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    '''
    Função estética para apenas informar qual titulo da função selecionada.

    função limpa tela com a função 'limpar_tela()',
    e usando o argumento fornecido na chamada retorna o subtitulo da função que está em execução
    '''
    limpar_tela()
    print(texto)
    print()

def cadastrar_restaurante():
    '''
    Função responsavel por cadastrar restaurante usando inputs abaixo.

    - Inputs:
        * NOME DO RESTAURANTE
        * CATEGORIA DO RESTAURANTE

    - Efeito colateral (OUTPUT):
        Exibe subtitulo,
        Armazena dados na lista de dicionarios 'lista_restaurantes'

    - Essa função não retorna outputs
    
    '''
    exibir_subtitulo('Cadastrar restaurante')
    nome_do_restaurante = input('Insira o nome do restaurante: ')
    categoria_do_restaurante = input(f'Insira a categoria do restaurante "{nome_do_restaurante}": ')
    dados_cadastrados = {'nome': nome_do_restaurante, 'categoria': categoria_do_restaurante, 'ativo': False}
    lista_restaurantes.append(dados_cadastrados)
    voltar_ao_menu_principal()

def listagem_restaurantes():
    '''
    Função responsavel por listar em formato de matriz todos os restaurantes cadastrados.

    - outputs:
        * indice,
        * nome,
        * categoria,
        * condição
        -*linhas divisorias para melhor organização - 'linha_divisoria_listagem_restaurantes'

    - Função usa FOR IN para percorrer dados armazenado durante execução em lista de dicionarios
    '''
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
    '''
    Função responsavel por apenas exibir dados armazenados

    - Funções chamadas: 
        * exibir_subtitulo('Listar restaurantes') - usando argumento
        * listagem_restaurantes()
        * voltar_ao_menu_principal()

    - outputs:
        * Todos restaurantes cadastrados foram listado acima!
        *-Efeitos Colaterais: 
            * exibir_subtitulo('Listar restaurantes') - usando argumento
            * listagem_restaurantes()

    '''
    exibir_subtitulo('Listar restaurantes')
    listagem_restaurantes()
    print('\nTodos restaurantes cadastrados foram listado acima!')
    voltar_ao_menu_principal()

def status_atividade_restaurantes():
    '''
    Exibe a lista de restaurantes e permite ao usuário ativar ou desativar um restaurante.

    - Ações realizadas:
        * Exibe subtítulo "Ativar/Desativar Restaurante"
        * Lista todos os restaurantes cadastrados com seus respectivos IDs
        * Solicita ao usuário a escolha entre:
            - Ativar restaurante
            - Desativar restaurante
            - Voltar ao menu principal
        * Solicita o ID do restaurante desejado
        * Atualiza o status "ativo" do restaurante na lista

    - Inputs:
        * Opção de ação (1: Ativar | 2: Desativar | 3: Menu Principal)
        * ID do restaurante a ser ativado/desativado

    - Efeitos colaterais:
        * Modifica o status do restaurante selecionado dentro da lista global `lista_restaurantes`

    - Saídas visuais (print):
        * Mensagem de confirmação: "Restaurante [nome] ativado/desativado com sucesso"
        * Mensagens de erro em caso de entrada inválida

    - Funções auxiliares utilizadas:
        * exibir_subtitulo(titulo)
        * listagem_restaurantes()
        * voltar_ao_menu_principal()
        * limpar_tela()
    '''   

    while True: 
        exibir_subtitulo('Ativar/Desativar Restaurante')
        listagem_restaurantes()   
        print('\nOpções disponiveis. Use o número que representa a opção!\n')
        print(' 1. Ativar restaurante.')
        print(' 2. Desativar restaurante.')
        print(' 3. Retornar ao Menu Principal.\n')
        try:
            opcao_escolhida = int(input('Insira a opção escolhida: '))
            if opcao_escolhida not in [1, 2, 3]:
                limpar_tela()
                print('\nOpção invalida, tente novamente!\n')
                input('Tecle [Enter] para retornar ao menu.')
                continue
            elif opcao_escolhida in [1, 2]:
                ativar = True if opcao_escolhida == 1 else False
            elif opcao_escolhida == 3:
                voltar_ao_menu_principal()
        except ValueError:
            print('\nEntrada Inválida, digite um número!\n')
            continue

        ativar_desativar = 'ativar' if ativar else 'desativar'

        while True:    
            try:
                limpar_tela()
                listagem_restaurantes()
                print(f'\nVocê escolheu {ativar_desativar} um restaurante!\n')
                id_restaurante = int(input(f'insira o ID do restaurante que deseja {ativar_desativar}: '))
            except ValueError:
                print('\n ID inválido, Tente um ID existente na lista! \n')
                continue

            lista_restaurantes[id_restaurante]['ativo'] = True if ativar else False
            mensagem_formatada_com_sucesso = 'ativado com Sucesso'if lista_restaurantes[id_restaurante]['ativo'] == True else f'desativado com sucesso'
            print(f'\nO restaurante "{lista_restaurantes[id_restaurante]['nome']}" foi {mensagem_formatada_com_sucesso}')

            voltar_ao_menu_principal()
    
def finalizar_app():
    '''Finaliza o app'''
    exibir_subtitulo('Finalizar APP')

def escolher_opcoes():
    '''
    Menu Principal, usuario escolher função que deseja trabalhar
    
    - input: 
        *escolha_usuario
    '''
    try:
        escolha_usuario = int(input('Escolha uma das opções usando (1, 2, 3 ou 4): '))
        limpar_tela()

        if escolha_usuario == 1:
            cadastrar_restaurante()
        elif escolha_usuario == 2:
            listar_restaurante()
        elif escolha_usuario == 3:
            status_atividade_restaurantes()
        elif escolha_usuario == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    '''ordenação e inicialização do sistema'''
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcoes()

if __name__ == '__main__':
    '''Inicializando com verificação'''
    main()