# Crie uma classe e insira nela, no mínimo, dois atributos, os quais devem ter um método acessor (get) e um método
# modificador (set) para cada. Defina um objeto para cada atributo e elabore um construtor para criar alguma regra.
#
# A atividade pode ser realizada em qualquer linguagem de programação ou apenas utilizando algoritmos.
#


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def discount(self, percent):
        self.price = self.price - (self.price * (percent / 100))

    #getter
    @property
    def price(self):
        return self._price

    #setter
    @price.setter
    def price(self, value):
        if isinstance(value, str):
            try:
                value = float(value)
            except:
                return "error"
        self._price = value


produto = Product("qql coisa", "2")
print(produto.price)
