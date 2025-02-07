import sys

from tiendalibros.modelo.tienda_libros import TiendaLibros
from tiendalibros.modelo.libro_existente_error import LibroExistenteError
from tiendalibros.modelo.libro_agotado_error import LibroAgotadoError
from tiendalibros.modelo.existencias_insuficientes_error import ExistenciasInsuficientesError

class UIConsola:

    def __init__(self):
        self.tienda_libros: TiendaLibros = TiendaLibros()
        self.opciones = {
            "1": self.adicionar_un_libro_a_catalogo,
            "2": self.agregar_libro_a_carrito_de_compras,
            "3": self.retirar_libro_de_carrito_de_compras,
            "4": self.salir
        }

    @staticmethod
    def salir():
        print("\nGRACIAS POR VISITAR NUESTRA TIENDA DE LIBROS. VUELVA PRONTO")
        sys.exit(0)

    @staticmethod
    def mostrar_menu():
        titulo = "¡Tienda Libros!"
        print(f"\n{titulo:_^30}")
        print("1. Adicionar un libro al catálogo")
        print("2. Agregar libro a carrito de compras")
        print("3. Retirar libro de carrito de compras")
        print(f"{'_':_^30}")

    def ejecutar_app(self):
        while True:
            self.mostrar_menu()
            opcion = input("Seleccione una opción: ")
            accion = self.opciones.get(opcion)
            if accion:
                accion()
            else:
                print(f"{opcion} no es una opción válida")
    
    def retirar_libro_de_carrito_de_compras(self):
        isbn = input("Ingrese el ISBN del libro a retirar: ")
        self.tienda_libros.retirar_item_de_carrito(isbn)
        print("Libro retirado del carrito con éxito.")

    def agregar_libro_a_carrito_de_compras(self):
        isbn = input("Ingrese el ISBN del libro: ")
        cantidad = int(input("Ingrese la cantidad: "))
        try:
            self.tienda_libros.agregar_libro_al_carrito(isbn, cantidad)
            print("Libro agregado al carrito con éxito.")
        except LibroAgotadoError as e:
            print(f"Error: {e}")
        except ExistenciasInsuficientesError as e:
            print(f"Error: {e}")
        except ValueError:
            print("Error: La cantidad debe ser un número entero positivo.")

    def adicionar_un_libro_a_catalogo(self):
        isbn = input("Ingrese el ISBN: ")
        titulo = input("Ingrese el título: ")
        precio = float(input("Ingrese el precio: "))
        existencias = int(input("Ingrese las existencias: "))
        try:
            self.tienda_libros.adicionar_libro_a_catalogo(isbn, titulo, precio, existencias)
            print("Libro agregado al catálogo con éxito.")
        except LibroExistenteError as e:
            print(f"Error: {e}")
        except ValueError:
            print("Error: Los valores ingresados no son válidos.")
