from modelos.restaurante import Restaurante
from modelos import utils
from modelos.avaliacao import Avaliacao

def cadastrar_restaurante():
    utils.limpar_tela()
    print('Cadastrar Restaurante')
    nome = input('Nome do restaurante: ').strip().title()
    categoria = input('Categoria: ').strip().title()
    Restaurante(nome, categoria)
    print(f'Restaurante "{nome}" cadastrado com sucesso!')
    utils.pausar()

def listar_restaurantes():
    utils.limpar_tela()
    print('Lista de Restaurantes:')
    Restaurante.exibir_restaurantes()
    utils.pausar()

def ativar_desativar_restaurante():
    utils.limpar_tela()
    print('Ativar / Desativar Restaurante')
    Restaurante.exibir_restaurantes()
    if not Restaurante.lista_restaurantes:
        utils.pausar()
        return

    try:
        idx = int(input('Digite o ID do restaurante: '))
        if 0 <= idx < len(Restaurante.lista_restaurantes):
            restaurante = Restaurante.lista_restaurantes[idx]
            novo_status = not restaurante.is_ativo
            restaurante.set_ativo(novo_status)
            status_str = 'Ativado' if novo_status else 'Desativado'
            print(f'Restaurante "{restaurante.nome}" {status_str} com sucesso!')
        else:
            print('ID inválido.')
    except ValueError:
        print('Entrada inválida.')
    utils.pausar()

def main():
    utils.limpar_tela()
    utils.exibir_titulo()
    while True:
        utils.exibir_menu()
        opcao = input('Escolha uma opção: ').strip()
        if opcao == '1':
            cadastrar_restaurante()
        elif opcao == '2':
            listar_restaurantes()
        elif opcao == '3':
            ativar_desativar_restaurante()
        elif opcao == '4':
            print('Saindo do sistema...')
            break
        else:
            print('Opção inválida, tente novamente.')
            utils.pausar()

if __name__ == '__main__':
    main()
