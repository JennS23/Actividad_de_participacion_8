from tiendalibros.modelo.libro_error import LibroError

class LibroAgotadoError(LibroError):
    def __init__(self, isbn, titulo, message=None):
        if not message:
            message = f"El libro con título {titulo} y isbn {isbn} está agotado."
        super().__init__(message)
        self.isbn = isbn
        self.titulo = titulo

    def __str__(self):
        return f"LibroAgotadoError: {self.message}"