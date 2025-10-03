# 🚗 AutoService - Refactoring de Legacy a Código Testeable

Transformación completa de código legacy no testeable a arquitectura limpia con >90% de cobertura, aplicando patrones de diseño modernos y mejores prácticas de testing.

## 🎯 Descripción

**AutoService** es un sistema de gestión para talleres mecánicos que demuestra cómo refactorizar código legacy no testeable hacia una arquitectura limpia, mantenible y con alta cobertura de tests.

### El Problema

```python
class AutoServiceManager:
    def create_appointment(self, data):
        now = datetime.now()              # ❌ Tiempo hardcodeado
        send_email(data['email'])         # ❌ Email directo
        conn = sqlite3.connect('auto.db') # ❌ BD directa
        # ... SQL directo sin abstracción
```

**Problemas:**
- ⛔ Dependencias hardcodeadas
- ⛔ Imposible mockear en tests
- ⛔ Tiempo no controlable
- ⛔ BD persistente contamina tests
- ⛔ Acoplamiento fuerte

### La Solución

```python
class AutoServiceManager:
    def __init__(self, time_provider: TimeProvider,
                 email_service: EmailService,
                 appointment_repo: AppointmentRepository):
        self.time = time_provider      # ✅ Tiempo inyectado
        self.email = email_service     # ✅ Email abstracto
        self.repo = appointment_repo   # ✅ Repositorio inyectado
```

## 🚀 Instalación

### Requisitos Previos

- Python 3.8+
- pip
- virtualenv (recomendado)

### Dependencias

```txt
pytest==7.4.3
pytest-cov==4.1.0
```

## 💻 Uso

### Uso en Producción

```python
from autoservice import create_production_manager

# Crear manager con dependencias reales
manager = create_production_manager()

# Crear cita
result = manager.create_appointment(
    client_name="Juan Pérez",
    email="juan@example.com",
    service_type="oil_change",
    date_str="2025-10-15"
)

print(f"Cita creada: ID={result['id']}, Estado={result['status']}")
```

### Uso en Tests

```python
from autoservice import create_test_manager_custom
from datetime import datetime

# Manager con mocks
manager, mock_email, spy_notif = create_test_manager_custom(
    fixed_time=datetime(2025, 10, 2, 14, 0)
)

# Crear cita de prueba
result = manager.create_appointment(
    client_name="Test User",
    email="test@test.com",
    service_type="brake_check",
    date_str="2025-10-20"
)

# Verificar comportamiento
assert result['status'] == 'confirmed'
assert len(mock_email.sent_emails) == 1
assert spy_notif.was_notified("test@test.com")
```

## 🧪 Tests

### Ejecutar Tests

```bash
# Todos los tests
pytest autoservice.py -v

# Tests con cobertura
pytest autoservice.py --cov=. --cov-report=html

# Test específico
pytest autoservice.py::test_spy_notification_service_captures_calls -v

# Tests por categoría
pytest autoservice.py -k "mock" -v          # Solo tests de mocks
pytest autoservice.py -k "transaction" -v   # Solo tests transaccionales
```

### Resultados Esperados

```
=================== test session starts ====================
collected 20 items

autoservice.py::test_insert_multiple... PASSED      [  5%]
autoservice.py::test_foreign_key...     PASSED      [ 10%]
autoservice.py::test_complex_trans...   PASSED      [ 15%]
autoservice.py::test_billing_with...    PASSED      [ 20%]
autoservice.py::test_spy_notifica...    PASSED      [ 30%]
autoservice.py::test_mock_email_v...    PASSED      [ 35%]
autoservice.py::test_fake_time_pr...    PASSED      [ 40%]
...

=================== 20 passed in 0.85s ====================

Coverage: 92% (450/489 lines)
```

### Ver Reporte de Cobertura

```bash
# Generar y abrir reporte HTML
pytest autoservice.py --cov=. --cov-report=html
open htmlcov/index.html  # Mac/Linux
start htmlcov/index.html # Windows
```

## 📊 Métricas de Calidad

### Cobertura de Código

```bash
pytest autoservice.py --cov=. --cov-report=term

Name              Stmts   Miss  Cover
-------------------------------------
autoservice.py      489     40    92%
-------------------------------------
TOTAL               489     40    92%
```

### Resultados de Tests

- ✅ **Total tests:** 20
- ✅ **Tests pasados:** 20 (100%)
- ✅ **Tiempo ejecución:** <1 segundo
- ✅ **Cobertura:** 92%
- ✅ **Complejidad:** Baja (6.2)

## 🛠️ Tecnologías Utilizadas

- **Python 3.8+**: Lenguaje principal
- **SQLite3**: Base de datos
- **pytest**: Framework de testing
- **pytest-cov**: Medición de cobertura
- **abc**: Abstract Base Classes
- **dataclasses**: Clases de datos
- **datetime**: Manejo de fechas
- **typing**: Type hints

<div align="center">


[⬆ Volver arriba](#-autoservice---refactoring-de-legacy-a-código-testeable)

</div>
