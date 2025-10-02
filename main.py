from database import Database
from models import UserModel
from mock_data import get_mock_connection  # NUEVO: importar datos simulados
from views import *

def main():
    # ===== CAMBIA SOLO ESTA LÍNEA PARA ALTERNAR ENTRE REAL Y SIMULADO =====
    
    # OPCIÓN 1: Usar base de datos REAL
    db = Database(host="localhost", database="pruebatest", user="root", password="")
    if not db.connect():
        print("No se pudo conectar a la base de datos.")
        return
    connection = db.get_connection()
    
    # OPCIÓN 2: Usar datos SIMULADOS (descomenta esta línea y comenta las 5 de arriba)
    # connection = get_mock_connection()
    
    # ========================================================================
    
    # El resto del código permanece EXACTAMENTE igual
    user_model = UserModel(connection)
    
    while True:
        mostrar_menu()
        opcion = input("\nSelecciona una opción: ")
        
        if opcion == "1":
            cedula, nombre = solicitar_datos_usuario()
            resultado = user_model.crear(cedula, nombre)
            if resultado:
                print(f"✓ Usuario creado exitosamente (ID: {resultado})")
        
        elif opcion == "2":
            usuarios = user_model.listar_todos()
            mostrar_usuarios(usuarios)
        
        elif opcion == "3":
            cedula = solicitar_cedula()
            usuario = user_model.buscar_por_cedula(cedula)
            mostrar_usuario(usuario)
        
        elif opcion == "4":
            cedula = solicitar_cedula()
            nuevo_nombre = solicitar_nombre()
            if user_model.actualizar(cedula, nuevo_nombre):
                print(f"✓ Usuario actualizado exitosamente")
            else:
                print("✗ No se pudo actualizar el usuario")
        
        elif opcion == "5":
            cedula = solicitar_cedula()
            if confirmar_accion():
                if user_model.eliminar(cedula):
                    print(f"✓ Usuario eliminado exitosamente")
                else:
                    print("✗ No se pudo eliminar el usuario")
        
        elif opcion == "6":
            print("\n¡Hasta luego!")
            break
        
        else:
            print("✗ Opción no válida")
        
        pausar()
    
    # Cerrar conexión
    if hasattr(connection, 'close'):
        connection.close()


if __name__ == "__main__":
    main()
