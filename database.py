import mysql.connector
from mysql.connector import Error

class Database:
    def __init__(self, host="localhost", database="pruebatest", user="root", password=""):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.connection = None
    
    def connect(self):
        """Establece conexión con la base de datos"""
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            if self.connection.is_connected():
                print("✓ Conexión exitosa a la base de datos")
                return True
        except Error as e:
            print(f"✗ Error al conectar: {e}")
            return False
    
    def disconnect(self):
        """Cierra la conexión"""
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("✓ Conexión cerrada")
    
    def get_connection(self):
        """Retorna la conexión activa"""
        return self.connection