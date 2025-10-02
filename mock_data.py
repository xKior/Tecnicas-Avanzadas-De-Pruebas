class MockConnection:
    """Simula una conexión a la base de datos"""
    def __init__(self):
        self.data = [
            {'id': 1, 'cedula': '1234567890', 'nombre': 'Juan Pérez'},
            {'id': 2, 'cedula': '0987654321', 'nombre': 'María García'},
            {'id': 3, 'cedula': '1122334455', 'nombre': 'Carlos Rodríguez'}
        ]
        self.next_id = 4
    
    def cursor(self, dictionary=False):
        """Retorna un cursor simulado"""
        return MockCursor(self.data, self.next_id, dictionary)
    
    def commit(self):
        """Simula commit de transacción"""
        pass
    
    def is_connected(self):
        """Simula estado de conexión"""
        return True
    
    def close(self):
        """Simula cierre de conexión"""
        pass


class MockCursor:
    """Simula un cursor de base de datos"""
    def __init__(self, data, next_id, dictionary=False):
        self.data = data
        self.next_id = next_id
        self.dictionary = dictionary
        self.lastrowid = None
        self.rowcount = 0
        self.result = None
    
    def execute(self, query, params=None):
        """Simula ejecución de query"""
        query_lower = query.lower()
        
        if "insert" in query_lower:
            # Simular INSERT
            cedula, nombre = params
            nuevo_usuario = {
                'id': self.next_id,
                'cedula': cedula,
                'nombre': nombre
            }
            self.data.append(nuevo_usuario)
            self.lastrowid = self.next_id
            self.next_id += 1
            self.rowcount = 1
        
        elif "select" in query_lower:
            # Simular SELECT
            if params:  # WHERE cedula = ?
                cedula = params[0]
                self.result = next((u for u in self.data if u['cedula'] == cedula), None)
            else:  # SELECT ALL
                self.result = self.data.copy()
        
        elif "update" in query_lower:
            # Simular UPDATE
            nuevo_nombre, cedula = params
            for usuario in self.data:
                if usuario['cedula'] == cedula:
                    usuario['nombre'] = nuevo_nombre
                    self.rowcount = 1
                    return
            self.rowcount = 0
        
        elif "delete" in query_lower:
            # Simular DELETE
            cedula = params[0]
            for i, usuario in enumerate(self.data):
                if usuario['cedula'] == cedula:
                    self.data.pop(i)
                    self.rowcount = 1
                    return
            self.rowcount = 0
    
    def fetchall(self):
        """Retorna todos los resultados"""
        return self.result if self.result else []
    
    def fetchone(self):
        """Retorna un resultado"""
        return self.result


def get_mock_connection():
    """Retorna una conexión simulada"""
    return MockConnection()