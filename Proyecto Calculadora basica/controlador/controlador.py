class Controlador:
    """
    Clase Controlador que conecta el modelo y la vista,
    y gestiona la lógica de las operaciones.
    """
    def __init__(self, model, view):
        """
        Inicializa el controlador con el modelo y la vista.
        """
        self.model = model
        self.view = view

    def realizar_operacion(self):
        """
        Solicita una operación, la evalúa y guarda el resultado.
        """
        try:
            operacion = self.view.pedir_operacion()
            resultado = eval(operacion)  # ¡No recomendado para producción!
            self.model.guardar_operacion(operacion, resultado)
            self.view.mostrar_resultado(resultado)
        except Exception as e:
            self.view.mostrar_mensaje(f"Error al realizar la operación: {e}")
        #mostar el historial del programa

    def mostrar_historial(self):
        historial = self.model.obtener_historial()
        self.view.mostrar_historial(historial)
        #ejecutar el programa
    def ejecutar(self):
        while True:
            opcion = self.view.mostrar_menu()
            if opcion == "1":
                self.realizar_operacion()
            elif opcion == "2":
                self.mostrar_historial()
            elif opcion == "3":
                self.view.mostrar_mensaje("\033[31mSaliendo del programa...\033[0m")
                break
            else:
                self.view.mostrar_mensaje("Opción no válida.")
