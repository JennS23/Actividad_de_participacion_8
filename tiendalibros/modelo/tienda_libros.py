from libro import Libro
from carro_compra import CarroCompra
from libro_existente_error import LibroExistenteError
from libro_agotado_error import LibroAgotadoError
from existencias_insuficientes_error import ExistenciasInsuficientesError

class TiendaLibros:
    def __init__(self):
        self.catalogo = {}
        self.carrito = CarroCompra()

    def agregar_libro_a_catalogo(self, libro):
        self.catalogo[libro.isbn] = libro

    def buscar_libro_por_isbn(self, isbn):
        return self.catalogo.get(isbn)

    def agregar_libro_al_carrito(self, isbn, cantidad):
        libro = self.buscar_libro_por_isbn(isbn)
        if libro:
            self.carrito.agregar_item(libro, cantidad)
        else:
            print("Libro no encontrado en el catálogo.")

    def adicionar_libro_a_catalogo(self, isbn, titulo, precio, existencias):
        if isbn in self.catalogo:
            raise LibroExistenteError(isbn, titulo)

        nuevo_libro = Libro(isbn, titulo, precio, existencias)
        self.catalogo[isbn] = nuevo_libro
        return nuevo_libro
    
    def agregar_libro_a_carrito(self, libro, cantidad):
        if libro.existencias == 0:
            raise LibroAgotadoError(libro.isbn, libro.titulo)
        elif libro.existencias < cantidad:
            raise ExistenciasInsuficientesError(libro.isbn, libro.titulo, cantidad, libro.existencias)
        else:
            self.carrito[libro.isbn] = self.carrito.get(libro.isbn, 0) + cantidad

    def retirar_item_de_carrito(self, isbn):
        self.carrito.pop(isbn, None)