from database import Database
from models import UserModel

class TestDatabaseReal:
    """Clase para realizar pruebas funcionales en la BD REAL"""
    
    def __init__(self, host="localhost", database="pruebatest", user="root", password=""):
        """Inicializa la conexión a la base de datos real"""
        self.db = Database(host=host, database=database, user=user, password=password)
        self.user_model = None
    
    def setup(self):
        """Configura la conexión antes de las pruebas"""
        if not self.db.connect():
            print("❌ Error: No se pudo conectar a la base de datos")
            return False
        
        self.user_model = UserModel(self.db.get_connection())
        return True
    
    def teardown(self):
        """Limpia después de las pruebas"""
        self.db.disconnect()
        
    def test_leer_datos_reales(self):
        """Prueba: Leer datos reales de la base de datos"""
        print("\n📖 TEST: Leer datos reales de la base de datos")
        print("-" * 60)
        
        usuarios = self.user_model.listar_todos()
        
        if usuarios is not None:
            cantidad = len(usuarios)
            print(f"✅ ÉXITO: Se leyeron {cantidad} registros de la base de datos")
            
            if cantidad > 0:
                print(f"\n{'ID':<5} {'CÉDULA':<15} {'NOMBRE':<30}")
                print("-" * 50)
                for user in usuarios[:5]:  # Mostrar solo los primeros 5
                    print(f"{user['id']:<5} {user['cedula']:<15} {user['nombre']:<30}")
                
                if cantidad > 5:
                    print(f"... y {cantidad - 5} registros más")
            else:
                print("⚠️  La tabla está vacía (0 registros)")
            
            return True
        else:
            print(f"❌ FALLO: No se pudieron leer los datos")
            return False


def main():
    """Función principal para ejecutar las pruebas"""
    print("\n🧪 PRUEBAS FUNCIONALES - BASE DE DATOS REAL")
    print("="*60)
    print("IMPORTANTE: Estas pruebas se ejecutan en la base de datos real")
    print("           Asegúrate de tener MySQL corriendo y configurado")
    print("="*60)
    
    # Configuración de la base de datos
    host = input("\nHost (default: localhost): ") or "localhost"
    database = input("Base de datos (default: pruebatest): ") or "pruebatest"
    user = input("Usuario (default: root): ") or "root"
    password = input("Contraseña: ")
    
    print("\nIniciando pruebas...")
    
    test = TestDatabaseReal(host=host, database=database, user=user, password=password)
    
    if test.setup():
        test.test_leer_datos_reales()
        test.teardown()


if __name__ == "__main__":
    main()
