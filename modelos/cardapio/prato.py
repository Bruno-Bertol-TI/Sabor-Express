from modelos.cardapio.item_cardapio import ItemCardapio

class Prato(ItemCardapio):
    def __init__(self, nome, preco, descricao):
        super().__init__(nome, preco)
        self._descricao = descricao

    @property
    def nome(self):
        return self._nome

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, novo_preco):
        self._preco = novo_preco

    @property
    def descricao(self):
        return self._descricao
    
    def aplicar_desconto(self):
        self.preco -= (self.preco * 0.08)
