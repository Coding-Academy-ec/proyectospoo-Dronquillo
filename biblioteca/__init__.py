# Archivo: biblioteca/__init__.py

# Importar las clases necesarias desde los submódulos
from .libros import Libro
from .usuarios import Usuario
from .transacciones import Transaccion

# Punto de entrada del programa
def main():
    # Crear algunos libros
    libro1 = Libro("ISBN-04-11", "Python El Viaje", "Dario Ronquillo")
    libro2 = Libro("ISBN-06-01", "Codigo Alfa", "Dj Ron")

    # Crear algunos usuarios
    usuario1 = Usuario("1001", "Geo")
    usuario2 = Usuario("1002", "Dan")

    # Realizar algunas transacciones
    transaccion1 = Transaccion(usuario1, libro1)
    transaccion1.prestar()
    transaccion2 = Transaccion(usuario2, libro2)
    transaccion2.prestar()

    # Mostrar detalles de las transacciones
    print("Transacciones realizadas:")
    for transaccion in [transaccion1, transaccion2]:
        print(transaccion)

if __name__ == "__main__":
    main()

