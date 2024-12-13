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
        print("\033[032m1. Realizar una operación\033[0m")
        print("\033[032m2. Ver historial de operaciones\033[0m")
        print("\033[032m3. Salir\033[0m")
        return input("Seleccione una opción: ")

    @staticmethod
    def mostrar_mensaje(mensaje):
        print(mensaje)