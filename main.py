from modelos.restaurante import Restaurante
from modelos import utils
from funcionalidades.cadastrar_cardapio import cadastrar_cardapio
from funcionalidades.listar_cardapio import listar_cardapio
import random

def cadastrar_restaurante():
    utils.limpar_tela()
    print('Cadastrar Restaurante')
    opcao = utils.em_massa()
    if opcao == 1:
        restaurantes = []
        repeticoes = utils.quantidade_funcao_em_massa()
        i = 1
        while i <= repeticoes:
            print(15*'-')
            print(f'cadastro {i}:')
            nome = input('Nome do restaurante: ').strip().title()
            categoria = input('Categoria: ').strip().title()
            restaurantes.append((nome, categoria))
            print(restaurantes[i-1], '- Cadastrado')
            i += 1

        for nome, categoria in restaurantes:
            Restaurante(nome, categoria)

        print('\nCadastro em massa concluido com sucesso!\n')
        utils.pausar()
    elif opcao == 2:
        nome = input('Nome do restaurante: ').strip().title()
        categoria = input('Categoria: ').strip().title()
        Restaurante(nome, categoria)
        print(f'Restaurante "{nome}" cadastrado com sucesso!')
        utils.pausar()
    else:
        print('Opção inválida, retornar ao menu principal!')
        utils.pausar()

def listar_restaurantes():
    utils.limpar_tela()
    print('Lista de Restaurantes:')
    Restaurante.exibir_restaurantes()
    utils.pausar()

def listar_avaliacoes():
    utils.limpar_tela()
    print('Lista de avaliações:')
    Restaurante.exibir_avaliacoes()
    utils.pausar()

def ativar_desativar_restaurante():
    utils.limpar_tela()
    print('Ativar / Desativar Restaurante')
    opcao = utils.em_massa()
    Restaurante.exibir_restaurantes()
    if not Restaurante.lista_restaurantes:
        utils.pausar()
        return

    if opcao == 1 :
        executar_ativar_desativar = int(input('[1] Ativar\n[2] Desativar: '))
        novo_status = True if executar_ativar_desativar == 1 else False
        for r in Restaurante.lista_restaurantes:
            r.set_ativo(novo_status)
    elif opcao == 2:
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

def avaliacoes_em_massa():
    nomes_teste = ['Bruno', 'Ana', 'Carlos', 'Fernanda', 'João', 'Marina', 'Luiz', 'Paula', 'Roberta', 'Felipe']

    if not Restaurante.lista_restaurantes:
        print('Nenhum restaurante cadastrado para avaliar.')
        return
    
    for restaurante in Restaurante.lista_restaurantes:
        for _ in range(5):
            cliente = random.choice(nomes_teste)
            nota = random.randint(0, 5)
            restaurante.receber_avaliacao(cliente, nota)
        print(f'Avaliações cadastradas para o restaurante: {restaurante.nome}')

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
        nota = int(input('Digite uma nota de 0 até 5: '))

        if 0 > nota > 5:
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
            cadastrar_restaurante()
        elif opcao == 2:
            listar_restaurantes()
        elif opcao == 3:
            listar_avaliacoes()
        elif opcao == 4:
            ativar_desativar_restaurante()
        elif opcao == 5:
            print('Avaliações em massa apenas para testes.\n')
            opcao = utils.em_massa()
            if opcao == 1:
                avaliacoes_em_massa()
            elif opcao == 2:    
                avaliar_restaurantes()
        elif opcao == 6:
            cadastrar_cardapio()
            pass
        elif opcao == 7:
            listar_cardapio()
        elif opcao == 0:
            print('Saindo do sistema...')
            break
        else:
            print('Opção inválida, tente novamente.')
            utils.pausar()

if __name__ == '__main__':
    main()
