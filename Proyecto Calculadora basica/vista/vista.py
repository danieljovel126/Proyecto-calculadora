class Vista:
    @staticmethod
    def pedir_operacion():
        return input("Ingrese la operación (por ejemplo, 2 + 2) y asi con las demaas operaciones: ")

    @staticmethod
    def mostrar_resultado(resultado):
        print(f"Resultado: {resultado}")

    @staticmethod
    def mostrar_historial(historial):
        print("\nHistorial de Operaciones:")
        for entrada in historial:
            descripcion, resultado, fecha = entrada
            print(f"Operacion: {descripcion} | Resultado: {resultado} | Fecha: {fecha}")

    @staticmethod
    def mostrar_menu():
        print("\n Calculadora EJ :")
        print("1. Realizar una operación")
        print("2. Ver historial de operaciones")
        print("3. Salir")
        return input("Seleccione una opción: ")

    @staticmethod
    def mostrar_mensaje(mensaje):
        print(mensaje)