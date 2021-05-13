class Lote:
    def __init__(self, nombre, cajones, precio):
        self.nombre = nombre
        self.cajones = cajones
        self.precio = precio

    def __repr__(self):
        rep = f"Lote('{self.nombre}', {self.cajones}, {self.precio})"
        return rep

    def costo(self):
        return self.cajones * self.precio

    def vender(self, ncajones):
        self.cajones -= ncajones

# TEST
# peras = Lote('Pera', 100, 490.1)
# print(repr(peras))