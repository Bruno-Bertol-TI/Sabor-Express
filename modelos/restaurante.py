from modelos.avaliacao import Avaliacao

class Restaurante:
    lista_restaurantes = []
    
    def __init__(self, nome, categoria):
        self._nome = nome
        self._categoria = categoria
        self._ativo = False
        self._avaliacao = []
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
    
    @classmethod
    def exibir_restaurantes(cls):
        if not cls.lista_restaurantes:
            print('Nenhum restaurante cadastrado.')
            return
        print(f"| {'ID':<3} | {'Nome':<30} | {'Categoria':<30} | {'Status':<8} |")
        for id, r in enumerate(cls.lista_restaurantes):
            print(f"| {id:^3} | {r.nome:<30} | {r.categoria:<30} | {r.ativo:^8} |")

    @classmethod
    def exibir_avaliacoes(cls):
        print(f"| {'ID':<3} | {'Nome':<30} | {'Categoria':<30} | {'Status':<8} | | {'Cliente':<20} - {'Nota':^5} |")
        for id, r in enumerate(cls.lista_restaurantes):
            if r.avaliacao:
                print(f'| Avaliações: |')
                for a in r.avaliacao:
                    print(f'| {id:^3} | {r.nome:<30} | {r.categoria:<30} | {r.ativo:^8} |  {a.cliente:<20} -  {a.nota:^5} |')
        print('Não há avaliações a serem exibidas')

    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)