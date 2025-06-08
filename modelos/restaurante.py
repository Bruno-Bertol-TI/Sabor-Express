from modelos.avaliacao import Avaliacao
from modelos.cardapio.prato import Prato
from modelos.cardapio.bebida import Bebida 

class Restaurante:
    lista_restaurantes = []
    
    def __init__(self, nome, categoria):
        self._nome = nome
        self._categoria = categoria
        self._ativo = False
        self._avaliacao = []
        self._cardapio = [[],[]]
        Restaurante.lista_restaurantes.append(self)

    def __str__(self):
        return f"{self._nome} | {self._categoria} | {'Ativo' if self._ativo else 'Inativo'}"

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
    
    @property
    def avaliacao(self):
        return self._avaliacao
    
    @property
    def cardapio(self):
        return self._cardapio

    @property
    def media(self):
        if not self._avaliacao:
            return 'Não avaliado'
        notas = [a.nota for a in self._avaliacao]
        self._media = round(sum(notas) / len(notas), 2)
        return self._media
        
    @classmethod
    def exibir_restaurantes(cls):
        linha_divisoria_exibir_restaurantes = f'+ {1 * '---'} + {10 * '---'} + {10 * '---'} + {4 * '--'} + {7 * '--'} + {7 * '--'} +'
        if not cls.lista_restaurantes:
            print('Nenhum restaurante cadastrado.')
            return 0
        print(f"| {'ID':<3} | {'Nome':<30} | {'Categoria':<30} | {'Status':<8} | {'Nota média':^14} | {'Cardapio':^14} |")
        print(linha_divisoria_exibir_restaurantes)
        for id, r in enumerate(cls.lista_restaurantes):
            print(f"| {id:^3} | {r.nome:<30} | {r.categoria:<30} | {r.ativo:^8} | {r.media:^14} | {'Disponivel' if r.cardapio[0] or r.cardapio[1] else 'Indisponivel':^14} |")
            print(linha_divisoria_exibir_restaurantes)

    @classmethod
    def exibir_avaliacoes(cls):
        linha_divisoria_exibir_avaliacoes = f'+ {1 * '---'} + {10 * '---'} + {10 * '---'} + {4 * '--'} + {10 * '--'} + {5 * '-'} +'
        print(f"| {'ID':<3} | {'Nome':<30} | {'Categoria':<30} | {'Status':<8} | {'Cliente':<20} | {'Nota':^5} |")
        print(linha_divisoria_exibir_avaliacoes)
        for id, r in enumerate(cls.lista_restaurantes):
            if r.avaliacao:
                for a in r.avaliacao:
                    print(f'| {id:^3} | {r.nome:<30} | {r.categoria:<30} | {r.ativo:^8} | {a.cliente:<20} | {a.nota:^5} |')
                    print(linha_divisoria_exibir_avaliacoes)
        
    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)

    def cardapio_bebida(cls, nome, preco, tamanho, id):
        restaurante = cls.lista_restaurantes[id]
        cadastro_bebida = Bebida(nome, preco, tamanho)
        restaurante.cardapio[1].append(cadastro_bebida)
    
    @classmethod
    def cardapio_prato(cls, nome, preco, descricao, id):
        restaurante = cls.lista_restaurantes[id]
        cadastro_prato = Prato(nome, preco, descricao)
        restaurante.cardapio[0].append(cadastro_prato)

    @classmethod
    def exibir_cardapio_completo(cls, id):
        restaurante = cls.lista_restaurantes[id]
        for cardapio in restaurante.cardapio:
            if cardapio == restaurante.cardapio[0]:
                print('Pratos')
            elif cardapio == restaurante.cardapio[1]:
                print('Bebidas')
            for item in cardapio:
                print(f'Prato: {item.nome} - Preço: {item.preco} - ' + (f'Descrição: {item.descricao}' if cardapio == restaurante.cardapio[0] else f'Tamanho: {item.tamanho}'))