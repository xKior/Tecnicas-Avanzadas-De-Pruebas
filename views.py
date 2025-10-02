def mostrar_menu():
    """Muestra el menú principal"""
    print("\n" + "="*40)
    print("  GESTIÓN DE USUARIOS - PRUEBATEST")
    print("="*40)
    print("1. Crear usuario")
    print("2. Listar todos los usuarios")
    print("3. Buscar usuario por cédula")
    print("4. Actualizar usuario")
    print("5. Eliminar usuario")
    print("6. Salir")
    print("="*40)

def solicitar_datos_usuario():
    """Solicita cédula y nombre para crear usuario"""
    cedula = input("Ingresa la cédula: ")
    nombre = input("Ingresa el nombre: ")
    return cedula, nombre

def solicitar_cedula():
    """Solicita solo la cédula"""
    return input("Ingresa la cédula: ")

def solicitar_nombre():
    """Solicita solo el nombre"""
    return input("Ingresa el nombre: ")

def confirmar_accion(mensaje="¿Estás seguro? (s/n): "):
    """Solicita confirmación del usuario"""
    respuesta = input(mensaje)
    return respuesta.lower() == 's'

def mostrar_usuarios(usuarios):
    """Muestra lista de usuarios en formato tabla"""
    if not usuarios:
        print("\n✗ No hay usuarios registrados")
        return
    
    print(f"\n{'ID':<5} {'CÉDULA':<15} {'NOMBRE':<30}")
    print("-" * 50)
    for user in usuarios:
        print(f"{user['id']:<5} {user['cedula']:<15} {user['nombre']:<30}")

def mostrar_usuario(usuario):
    """Muestra información de un solo usuario"""
    if usuario:
        print(f"\n✓ Usuario encontrado:")
        print(f"  ID: {usuario['id']}")
        print(f"  Cédula: {usuario['cedula']}")
        print(f"  Nombre: {usuario['nombre']}")
    else:
        print("\n✗ Usuario no encontrado")

def pausar():
    """Pausa la ejecución hasta que el usuario presione ENTER"""
    input("\nPresiona ENTER para continuar...")