from tiendalibros.modelo.libro_error import LibroError

class ExistenciasInsuficientesError(LibroError):
    def __init__(self, isbn, titulo, cantidad_a_comprar, existencias, message=None):
        if not message:
            message = f"El libro con título {titulo} y isbn {isbn} no tiene suficientes existencias para realizar la compra: cantidad a comprar: {cantidad_a_comprar}, existencias: {existencias}."
        super().__init__(message)
        self.isbn = isbn
        self.titulo = titulo
        self.cantidad_a_comprar = cantidad_a_comprar
        self.existencias = existencias

    def __str__(self):
        return f"ExistenciasInsuficientesError: {self.message}"