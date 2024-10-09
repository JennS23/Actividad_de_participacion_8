
from item_compra import ItemCompra

class CarroCompra:
    def __init__(self):
        self.items = []

    def agregar_item(self, libro, cantidad):
        nuevo_item = ItemCompra(libro, cantidad)
        self.items.append(nuevo_item)
        return nuevo_item

    def calcular_total(self):
        total = sum(item.calcular_subtotal() for item in self.items)
        return total

    def quitar_item(self, isbn):
        self.items = [item for item in self.items if item.libro.isbn != isbn]