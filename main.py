from modelos.restaurante import Restaurante
from modelos import utils

def cadastro_em_massa():
    restaurantes = [
    ("Sabor Express", "Comida Brasileira"),
    ("La Pasta", "Culinária Italiana"),
    ("Tokyo Sushibar", "Culinária Japonesa"),
    ("Burger House", "Lanches"),
    ("Casa do Norte", "Comida Nordestina"),
    ("Green Veggie", "Comida Vegetariana"),
    ("Doce Delícia", "Confeitaria"),
    ("El Mexicano", "Culinária Mexicana"),
    ("Le Bistrô", "Culinária Francesa"),
    ("Wok To Go", "Comida Asiática Rápida")
]
    
    for nome, categoria in restaurantes:
        Restaurante(nome, categoria)

    print('cadastro em massa concluido...')
    utils.pausar()


# função principal subistituida apenas para testes
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

def avaliar_restaurantes():
    while True:
        utils.limpar_tela()
        print('Avaliação de restaurantes')
        Restaurante.exibir_restaurantes()
        idx_restaurante = int(input('Digite o ID do restaurante: '))
        if 0 < idx_restaurante > len(Restaurante.lista_restaurantes):
            print('Restaurante não encontrado!')
            continue

        cliente = input('Digite seu nome: ')
        nota = int(input('Digite uma nota de 0 até 10: '))

        if 0 > nota > 10:
            continue
        
        restaurante_avaliado = Restaurante.lista_restaurantes[idx_restaurante]
        restaurante_avaliado.receber_avaliacao(cliente, nota)
        utils.limpar_tela()
        print('Avaliação salva com sucesso.')
        print(restaurante_avaliado)
        utils.pausar()
        break
    

def main():
    while True:
        utils.limpar_tela()
        utils.exibir_titulo()
        utils.exibir_menu()
        opcao = int(input('Escolha uma opção: ').strip())
        if opcao == 1:
            cadastro_em_massa()
            # cadastrar_restaurante()
        elif opcao == 2:
            listar_restaurantes()
        elif opcao == 3:
            ativar_desativar_restaurante()
        elif opcao == 4:
            avaliar_restaurantes()
        elif opcao == 5:
            print('Saindo do sistema...')
            break
        else:
            print('Opção inválida, tente novamente.')
            utils.pausar()

if __name__ == '__main__':
    main()
