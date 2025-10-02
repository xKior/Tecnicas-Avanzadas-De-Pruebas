
from mysql.connector import Error

class UserModel:
    def __init__(self, db_connection):
        self.connection = db_connection
    
    def crear(self, cedula, nombre):
        """Inserta un nuevo usuario"""
        try:
            cursor = self.connection.cursor()
            query = "INSERT INTO users (cedula, nombre) VALUES (%s, %s)"
            cursor.execute(query, (cedula, nombre))
            self.connection.commit()
            return cursor.lastrowid
        except Error as e:
            print(f"✗ Error al crear usuario: {e}")
            return None
    
    def listar_todos(self):
        """Obtiene todos los usuarios"""
        try:
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM users")
            usuarios = cursor.fetchall()
            return usuarios
        except Error as e:
            print(f"✗ Error al listar usuarios: {e}")
            return []
    
    def buscar_por_cedula(self, cedula):
        """Busca un usuario por cédula"""
        try:
            cursor = self.connection.cursor(dictionary=True)
            query = "SELECT * FROM users WHERE cedula = %s"
            cursor.execute(query, (cedula,))
            usuario = cursor.fetchone()
            return usuario
        except Error as e:
            print(f"✗ Error al buscar usuario: {e}")
            return None
    
    def actualizar(self, cedula, nuevo_nombre):
        """Actualiza el nombre de un usuario"""
        try:
            cursor = self.connection.cursor()
            query = "UPDATE users SET nombre = %s WHERE cedula = %s"
            cursor.execute(query, (nuevo_nombre, cedula))
            self.connection.commit()
            return cursor.rowcount > 0
        except Error as e:
            print(f"✗ Error al actualizar usuario: {e}")
            return False
    
    def eliminar(self, cedula):
        """Elimina un usuario por cédula"""
        try:
            cursor = self.connection.cursor()
            query = "DELETE FROM users WHERE cedula = %s"
            cursor.execute(query, (cedula,))
            self.connection.commit()
            return cursor.rowcount > 0
        except Error as e:
            print(f"✗ Error al eliminar usuario: {e}")
            return False