import os

class GestaoRestaurantes:
    lista_restaurantes = []
    
    def __init__(self, nome, categoria):
        self._nome = nome
        self._categoria = categoria
        self._ativo = False
        GestaoRestaurantes.lista_restaurantes.append(self)

    def __str__(self):
        return self._nome, self._categoria, self._ativo

    @property
    def is_ativo(self):
        return self._ativo
    
    def set_ativo(self, novo_valor: bool):
        self._ativo = novo_valor
    
    @property
    def nome(self):
        return self._nome
        
    @property
    def categoria(self):
        return self._categoria
    
    @property
    def ativo(self):
        return 'Ativo' if self._ativo else 'Inativo'
    
    @classmethod
    def exibir_restaurantes(cls):
        if not cls.lista_restaurantes:
            print('Atenção!! Nenhum cadastro registrado.')
        for id, restaurante in enumerate(cls.lista_restaurantes):
                print(f'| {id} | {restaurante.nome} | {restaurante.categoria} | {restaurante.ativo} |')
    
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

def cadastrar_restaurantes_em_massa():
    dados_teste = [
        ('Pizza do Zé', 'Pizzaria'),
        ('Sushi Yama', 'Japonesa'),
        ('Churras Top', 'Churrascaria'),
        ('Veg Delícia', 'Vegano'),
        ('Pastel do João', 'Lanchonete')
    ]

    for nome, categoria in dados_teste:
        GestaoRestaurantes(nome, categoria)

def cadastrar_restaurante():
    cadastrar_restaurantes_em_massa()
    # exibir_subtitulo('Cadastrar restaurante')
    # restaurante = input('Digite o nome do restaurante: ').title()
    # categoria = input('Digite a categoria do restaurante: ').title()
    # GestaoRestaurantes(restaurante, categoria)
    voltar_ao_menu_principal()

def listagem_restaurantes():
    print(GestaoRestaurantes.exibir_restaurantes())

def listar_restaurante():
    exibir_subtitulo('Listar restaurantes')
    listagem_restaurantes()
    print('\nTodos restaurantes cadastrados foram listado acima!')
    voltar_ao_menu_principal()

def status_atividade_restaurantes():

    while True: 
        exibir_subtitulo('Ativar/Desativar Restaurante')
        listagem_restaurantes()   
        print('\nOpções disponiveis. Use o número que representa a opção!\n')
        print(' 1. Ativar restaurante.')
        print(' 2. Desativar restaurante.')
        print(' 3. Retornar ao Menu Principal.\n')
        try:
            menu_ativar_desativar_escolha = int(input('Digite a opção escolhida: '))
            limpar_tela()
            if menu_ativar_desativar_escolha == 3:
                voltar_ao_menu_principal()
            elif menu_ativar_desativar_escolha == 1:
                ativar = True
                todos_ativos = all(r.is_ativo() for r in GestaoRestaurantes.lista_restaurantes)
                if todos_ativos:
                    print('Todos restaurantes estão ativos!')
                    voltar_ao_menu_principal()
            elif menu_ativar_desativar_escolha == 2:
                ativar = False
                todos_inativos = all(not r.is_ativo() for r in GestaoRestaurantes.lista_restaurantes)
                if todos_inativos:
                    print('Todos restaurantes estão inativos!')
                    voltar_ao_menu_principal()
            else:
                print('Opção invalida!')
                continue
        except ValueError:
            print('\nEntrada Inválida, digite um número!\n')
            continue

        ativar_desativar = 'ativar' if ativar else 'desativar'

        while True:    
            try:
                listagem_restaurantes()
                alterar_status = int(input(f'Digite o ID do restaurante que deseja {ativar_desativar}: '))
                if 0 <= alterar_status <= len(GestaoRestaurantes.lista_restaurantes):
                    GestaoRestaurantes.lista_restaurantes[alterar_status].set_ativo(ativar)
                    print(f'Restaurante: {GestaoRestaurantes.lista_restaurantes[alterar_status].nome}, foi {'Ativado' if GestaoRestaurantes.lista_restaurantes[alterar_status].is_ativo else 'Destativado'} com sucesso')
                else:
                    print('ID inválido, tente um que está na lista')
                    continue
            except ValueError:
                print('\n ID inválido, Tente um ID existente na lista! \n')
                continue

            voltar_ao_menu_principal()
    
def finalizar_app():
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
            print('função em correção!')
            status_atividade_restaurantes()
            voltar_ao_menu_principal()
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
