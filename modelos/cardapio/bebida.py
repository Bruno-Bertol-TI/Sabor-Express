from modelos.cardapio.item_cardapio import ItemCardapio

class Bebida(ItemCardapio):
    def __init__(self, nome, preco, tamanho):
        super().__init__(nome, preco)
        self._tamanho = tamanho

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
    def tamaho(self):
        return self._tamaho
    
    def aplicar_desconto(self):
        self.preco -= (self.preco * 0.05)
      