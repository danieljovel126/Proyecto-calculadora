from datetime import datetime
import mysql.connector


class Database:
    def __init__(self, host="localhost", user="root", password="", database="calculadora"):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.conectar()

    def conectar(self):
        self.conn = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.conn.cursor()

    def crear_tablas(self):
        # Crear tabla de operaciones
        query_operaciones = """
        CREATE TABLE IF NOT EXISTS operaciones (
            id INT AUTO_INCREMENT PRIMARY KEY,
            descripcion VARCHAR(255) NOT NULL,
            fecha DATETIME NOT NULL
        );
        """
        self.cursor.execute(query_operaciones)

        # Crear tabla de resultados
        query_resultados = """
        CREATE TABLE IF NOT EXISTS resultados (
            id INT AUTO_INCREMENT PRIMARY KEY,
            valor DOUBLE NOT NULL
        );
        """
        self.cursor.execute(query_resultados)

        # Crear tabla intermedia operaciones_resultados
        query_intermedia = """
        CREATE TABLE IF NOT EXISTS operaciones_resultados (
            operacion_id INT NOT NULL,
            resultado_id INT NOT NULL,
            PRIMARY KEY (operacion_id, resultado_id),
            FOREIGN KEY (operacion_id) REFERENCES operaciones(id) ON DELETE CASCADE,
            FOREIGN KEY (resultado_id) REFERENCES resultados(id) ON DELETE CASCADE
        );
        """
        self.cursor.execute(query_intermedia)

        self.conn.commit()

    def guardar_operacion(self, descripcion, resultado):
        fecha = datetime.now()

        # Insertar en la tabla operaciones
        query_operacion = "INSERT INTO operaciones (descripcion, fecha) VALUES (%s, %s)"
        self.cursor.execute(query_operacion, (descripcion, fecha))
        operacion_id = self.cursor.lastrowid

        # Insertar en la tabla resultados
        query_resultado = "INSERT INTO resultados (valor) VALUES (%s)"
        self.cursor.execute(query_resultado, (resultado,))
        resultado_id = self.cursor.lastrowid

        # Insertar en la tabla intermedia
        query_intermedia = "INSERT INTO operaciones_resultados (operacion_id, resultado_id) VALUES (%s, %s)"
        self.cursor.execute(query_intermedia, (operacion_id, resultado_id))

        self.conn.commit()

    def obtener_historial(self):
        query = """
        SELECT o.descripcion, r.valor, o.fecha 
        FROM operaciones_resultados orr
        INNER JOIN operaciones o ON orr.operacion_id = o.id
        INNER JOIN resultados r ON orr.resultado_id = r.id
        ORDER BY o.fecha DESC;
        """
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def cerrar(self):
        self.conn.close()
