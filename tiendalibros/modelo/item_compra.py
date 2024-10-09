class ItemCompra:
    def __init__(self, libro, cantidad):
        self.libro = libro
        self.cantidad = cantidad

    def calcular_subtotal(self):
        """Calcula el subtotal de un item de compra.

        Returns:
            float: El subtotal del item de compra.
        """
        subtotal = self.libro.precio * self.cantidad
        return subtotal
    
