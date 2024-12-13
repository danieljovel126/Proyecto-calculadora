class Controlador:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def realizar_operacion(self):
        try:
            operacion = self.view.pedir_operacion()
            # Validar la operación antes de evaluarla
            if not self.validar_operacion(operacion):
                raise ValueError("La operación contiene caracteres no permitidos.")

            resultado = eval(operacion)  # Evalúa la operación validada
            self.model.guardar_operacion(operacion, resultado)
            self.view.mostrar_resultado(resultado)
        except SyntaxError:
            self.view.mostrar_mensaje("Error: La operación ingresada es inválida.")
        except ValueError as e:
            self.view.mostrar_mensaje(f"Error: {e}")
        except Exception as e:
            self.view.mostrar_mensaje(f"Error al realizar la operación: {e}")

    def validar_operacion(self, operacion):
        """
        Valida que la operación solo contenga números, operadores válidos y espacios.
        """
        import re
        patron = r'^[\d+\-*/().\s]+$'  # Permitir solo números, operadores, paréntesis y espacios
        return bool(re.match(patron, operacion))

    def mostrar_historial(self):
        historial = self.model.obtener_historial()
        self.view.mostrar_historial(historial)

    def ejecutar(self):
        while True:
            opcion = self.view.mostrar_menu()
            if opcion == "1":
                self.realizar_operacion()
            elif opcion == "2":
                self.mostrar_historial()
            elif opcion == "3":
                self.view.mostrar_mensaje("\033[031mSaliendo del programa...\033[0m")
                break
            else:
                self.view.mostrar_mensaje("Opción no válida.")
                

