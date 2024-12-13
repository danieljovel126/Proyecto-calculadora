# modulo principal
from modelo.modelo import Database
from vista.vista import Vista
from controlador.controlador import Controlador


def main():
    # Configurar la conexión con MySQL
    modelo = Database(host="localhost", user="root", password="")
    modelo.crear_tablas()  # Cambiado a "crear_tablas"

    # Inicializar vista y controlador
    vista = Vista()
    controlador = Controlador(modelo, vista)

    # Ejecutar aplicación
    controlador.ejecutar()

    # Cerrar conexión a la base de datos
    modelo.cerrar()

if __name__ == "__main__":
    main()
