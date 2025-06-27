# 📇 Sistema de Gestión de Contactos

> Una aplicación de consola desarrollada en Python para gestionar contactos de manera eficiente, con funcionalidades CRUD completas y persistencia de datos en formato JSON.

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![JSON](https://img.shields.io/badge/Storage-JSON-green.svg)](https://json.org)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Code Style](https://img.shields.io/badge/Code%20Style-PEP8-brightgreen.svg)](https://pep8.org)

## 📋 Descripción

El Sistema de Gestión de Contactos es una aplicación de línea de comandos desarrollada en Python que permite gestionar una agenda de contactos personal. El proyecto demuestra competencias en programación orientada a objetos, manejo de archivos, validación de datos y diseño de interfaces de usuario en consola.

### 🎯 Objetivos del Proyecto

- **Demostrar competencias en Python** con programación orientada a objetos
- **Implementar operaciones CRUD** completas (Crear, Leer, Actualizar, Eliminar)
- **Gestionar persistencia de datos** con archivos JSON
- **Aplicar validación de datos** robusta para entrada de usuario
- **Crear una interfaz de usuario** intuitiva en consola

## ✨ Características

### 🔧 Funcionalidades Principales

- **➕ Agregar Contactos**: Crear nuevos contactos con validación de datos
- **📋 Mostrar Contactos**: Visualizar todos los contactos almacenados
- **🔍 Buscar por ID**: Encontrar contactos específicos mediante identificador único
- **🗑️ Eliminar Contactos**: Remover contactos por ID con confirmación
- **💾 Persistencia Automática**: Guardado y carga automática desde archivo JSON
- **🔄 Carga de Datos**: Importar contactos desde archivos externos

### 🏗️ Características Técnicas

- **Validación Robusta**: Verificación de formato de email y números de teléfono
- **IDs Únicos**: Asignación automática de identificadores únicos
- **Manejo de Errores**: Gestión elegante de errores y casos edge
- **Interfaz Intuitiva**: Menú interactivo fácil de navegar
- **Código Limpio**: Estructura modular y bien documentada

## 🚀 Instalación y Uso

### Prerrequisitos

- Python 3.8 o superior
- No requiere librerías externas (solo biblioteca estándar de Python)

### Instalación

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/jorge-fuentes-94/sistemagestioncontactos.git
   cd sistemagestioncontactos
   ```

2. **Ejecutar la aplicación**
   ```bash
   python main.py
   ```

### Uso de la Aplicación

Al ejecutar la aplicación, verás el siguiente menú:

```
═══════════════════════════════════════
    📇 GESTOR DE CONTACTOS v1.0
═══════════════════════════════════════

--- Menú de Gestión de Contactos ---

1. ➕ Agregar contacto
2. 📋 Mostrar todos los contactos
3. 🔍 Buscar contacto por ID
4. 🗑️ Eliminar contacto por ID
5. 💾 Guardar contactos en archivo
6. 📂 Cargar contactos desde archivo
7. 🚪 Salir

Selecciona una opción (1-7): 
```

#### Ejemplo de Uso: Agregar Contacto

```
➕ Agregar nuevo contacto

Nombre: Juan Pérez
Teléfono: +34 123 456 789
Email: juan.perez@email.com

✅ Contacto agregado exitosamente!
📋 ID asignado: 1
```

#### Ejemplo de Uso: Mostrar Contactos

```
📋 Lista de todos los contactos:

┌─────┬─────────────┬─────────────────┬─────────────────────────┐
│ ID  │ Nombre      │ Teléfono        │ Email                   │
├─────┼─────────────┼─────────────────┼─────────────────────────┤
│ 1   │ Juan Pérez  │ +34 123 456 789 │ juan.perez@email.com    │
│ 2   │ Ana García  │ +34 987 654 321 │ ana.garcia@email.com    │
└─────┴─────────────┴─────────────────┴─────────────────────────┘

Total de contactos: 2
```

## 🏗️ Arquitectura del Proyecto

### Estructura de Archivos

```
sistemagestioncontactos/
├── main.py                    # Punto de entrada de la aplicación
├── gestiondecontactos.py      # Lógica principal del gestor
├── contactos.json            # Archivo de datos (generado automáticamente)
├── README.md                 # Documentación del proyecto
└── tests/                    # Tests unitarios (futuro)
    ├── __init__.py
    ├── test_gestor.py
    └── test_validaciones.py
```

### Componentes Principales

#### 📱 Clase Principal (GestorContactos)

```python
class GestorContactos:
    """
    Gestor principal para operaciones CRUD de contactos.
    
    Attributes:
        contactos (list): Lista de contactos almacenados
        archivo_datos (str): Ruta del archivo de persistencia
        siguiente_id (int): Próximo ID disponible para asignar
    """
    
    def __init__(self, archivo="contactos.json"):
        self.contactos = []
        self.archivo_datos = archivo
        self.siguiente_id = 1
        self.cargar_contactos()
    
    def agregar_contacto(self, nombre, telefono, email):
        """Agrega un nuevo contacto con validación."""
        
    def mostrar_contactos(self):
        """Muestra todos los contactos en formato tabla."""
        
    def buscar_contacto(self, id_contacto):
        """Busca un contacto por ID."""
        
    def eliminar_contacto(self, id_contacto):
        """Elimina un contacto por ID."""
```

#### ✅ Sistema de Validación

```python
def validar_email(email):
    """
    Valida el formato de email usando expresiones regulares.
    
    Args:
        email (str): Email a validar
        
    Returns:
        bool: True si el email es válido, False en caso contrario
    """
    import re
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(patron, email) is not None

def validar_telefono(telefono):
    """
    Valida el formato de número de teléfono.
    Acepta formatos: +34 123 456 789, 123-456-789, 123456789
    
    Args:
        telefono (str): Número de teléfono a validar
        
    Returns:
        bool: True si el teléfono es válido, False en caso contrario
    """
    import re
    # Eliminar espacios y guiones para validación
    telefono_limpio = re.sub(r'[\s\-\(\)]', '', telefono)
    
    # Verificar que contenga solo dígitos y opcionalmente un + al inicio
    patron = r'^\+?[0-9]{9,15}$'
    return re.match(patron, telefono_limpio) is not None
```

#### 💾 Gestión de Persistencia

```python
def guardar_contactos(self):
    """
    Guarda los contactos en archivo JSON con manejo de errores.
    """
    try:
        datos = {
            'contactos': self.contactos,
            'siguiente_id': self.siguiente_id,
            'fecha_actualizacion': datetime.now().isoformat()
        }
        
        with open(self.archivo_datos, 'w', encoding='utf-8') as archivo:
            json.dump(datos, archivo, indent=2, ensure_ascii=False)
            
        print("✅ Contactos guardados exitosamente")
        
    except Exception as e:
        print(f"❌ Error al guardar contactos: {e}")

def cargar_contactos(self):
    """
    Carga los contactos desde archivo JSON.
    """
    try:
        if os.path.exists(self.archivo_datos):
            with open(self.archivo_datos, 'r', encoding='utf-8') as archivo:
                datos = json.load(archivo)
                
            self.contactos = datos.get('contactos', [])
            self.siguiente_id = datos.get('siguiente_id', 1)
            
            print(f"📂 Cargados {len(self.contactos)} contactos")
        else:
            print("📝 Archivo de datos no encontrado. Iniciando con lista vacía.")
            
    except Exception as e:
        print(f"❌ Error al cargar contactos: {e}")
        self.contactos = []
        self.siguiente_id = 1
```

## 🧪 Casos de Uso y Ejemplos

### Caso de Uso 1: Gestión Básica de Contactos

```python
# Crear instancia del gestor
gestor = GestorContactos()

# Agregar contactos
gestor.agregar_contacto("María López", "+34 600 123 456", "maria@email.com")
gestor.agregar_contacto("Carlos Ruiz", "91-234-5678", "carlos@empresa.com")

# Mostrar todos los contactos
gestor.mostrar_contactos()

# Buscar contacto específico
contacto = gestor.buscar_contacto(1)
if contacto:
    print(f"Encontrado: {contacto['nombre']}")

# Eliminar contacto
gestor.eliminar_contacto(2)
```

### Caso de Uso 2: Validación de Datos

```python
# Ejemplos de validación de email
emails_validos = [
    "usuario@dominio.com",
    "test.email+tag@example.org",
    "user123@sub.domain.co.uk"
]

emails_invalidos = [
    "email_sin_arroba.com",
    "@dominio.com",
    "usuario@",
    "espacios en@email.com"
]

# Ejemplos de validación de teléfono
telefonos_validos = [
    "+34 123 456 789",
    "91-234-5678",
    "600123456",
    "+1 (555) 123-4567"
]

telefonos_invalidos = [
    "123",  # Muy corto
    "abc123456",  # Contiene letras
    "++34123456789",  # Doble signo +
]
```

## 📊 Características del Código

### Métricas del Proyecto

- **Líneas de código**: ~250 líneas
- **Funciones**: 12 funciones principales
- **Clases**: 1 clase principal (GestorContactos)
- **Validaciones**: 2 tipos (email y teléfono)
- **Formato de datos**: JSON para persistencia
- **Encoding**: UTF-8 para soporte internacional

### Patrones de Diseño Implementados

- **Singleton Pattern**: Una instancia del gestor por aplicación
- **Command Pattern**: Cada opción del menú ejecuta un comando específico
- **Strategy Pattern**: Diferentes estrategias de validación
- **Template Method**: Estructura común para operaciones CRUD

### Buenas Prácticas Aplicadas

- ✅ **Nombres descriptivos**: Variables y funciones con nombres claros
- ✅ **Documentación**: Docstrings en todas las funciones
- ✅ **Manejo de errores**: Try-catch para operaciones de archivo
- ✅ **Validación de entrada**: Verificación de datos antes de procesamiento
- ✅ **Separación de responsabilidades**: Lógica separada por funciones
- ✅ **Encoding UTF-8**: Soporte para caracteres especiales

## 🔧 Funcionalidades Avanzadas

### Validación Robusta de Datos

```python
def validar_datos_contacto(nombre, telefono, email):
    """
    Valida todos los datos de un contacto antes de agregarlo.
    
    Returns:
        tuple: (es_valido, lista_errores)
    """
    errores = []
    
    # Validar nombre
    if not nombre or len(nombre.strip()) < 2:
        errores.append("El nombre debe tener al menos 2 caracteres")
    
    # Validar teléfono
    if not validar_telefono(telefono):
        errores.append("Formato de teléfono inválido")
    
    # Validar email
    if not validar_email(email):
        errores.append("Formato de email inválido")
    
    return len(errores) == 0, errores
```

### Búsqueda Avanzada

```python
def buscar_contactos_por_nombre(self, termino_busqueda):
    """
    Busca contactos que contengan el término en el nombre.
    
    Args:
        termino_busqueda (str): Término a buscar
        
    Returns:
        list: Lista de contactos que coinciden
    """
    termino = termino_busqueda.lower()
    resultados = []
    
    for contacto in self.contactos:
        if termino in contacto['nombre'].lower():
            resultados.append(contacto)
    
    return resultados
```

### Exportación de Datos

```python
def exportar_a_csv(self, nombre_archivo="contactos_export.csv"):
    """
    Exporta los contactos a formato CSV.
    
    Args:
        nombre_archivo (str): Nombre del archivo de exportación
    """
    import csv
    
    try:
        with open(nombre_archivo, 'w', newline='', encoding='utf-8') as archivo:
            writer = csv.writer(archivo)
            
            # Escribir encabezados
            writer.writerow(['ID', 'Nombre', 'Teléfono', 'Email'])
            
            # Escribir datos
            for contacto in self.contactos:
                writer.writerow([
                    contacto['id'],
                    contacto['nombre'],
                    contacto['telefono'],
                    contacto['email']
                ])
        
        print(f"✅ Contactos exportados a {nombre_archivo}")
        
    except Exception as e:
        print(f"❌ Error al exportar: {e}")
```

## 🧪 Testing y Calidad

### Tests Unitarios (Planificados)

```python
import unittest
from gestiondecontactos import GestorContactos, validar_email, validar_telefono

class TestGestorContactos(unittest.TestCase):
    
    def setUp(self):
        """Configuración para cada test."""
        self.gestor = GestorContactos("test_contactos.json")
    
    def test_agregar_contacto_valido(self):
        """Test para agregar un contacto válido."""
        resultado = self.gestor.agregar_contacto(
            "Test User", 
            "+34 123 456 789", 
            "test@email.com"
        )
        self.assertTrue(resultado)
        self.assertEqual(len(self.gestor.contactos), 1)
    
    def test_validacion_email(self):
        """Test para validación de emails."""
        self.assertTrue(validar_email("test@example.com"))
        self.assertFalse(validar_email("email_invalido"))
    
    def test_validacion_telefono(self):
        """Test para validación de teléfonos."""
        self.assertTrue(validar_telefono("+34 123 456 789"))
        self.assertFalse(validar_telefono("123"))
```


## 🛠️ Tecnologías Utilizadas

| Tecnología | Versión | Propósito |
|------------|---------|-----------|
| Python | 3.8+ | Lenguaje de programación |
| JSON | Estándar | Formato de almacenamiento |
| Regex | Biblioteca estándar | Validación de datos |
| OS | Biblioteca estándar | Operaciones de archivo |
| Datetime | Biblioteca estándar | Manejo de fechas |

## 🎯 Habilidades Demostradas

### Competencias en Programación

- **Python Orientado a Objetos**: Clases, métodos, encapsulación
- **Manejo de Archivos**: Lectura/escritura JSON con encoding UTF-8
- **Validación de Datos**: Expresiones regulares y lógica de validación
- **Manejo de Errores**: Try-catch y gestión de excepciones
- **Interfaz de Usuario**: Menús interactivos en consola
- **Persistencia de Datos**: Almacenamiento y recuperación de información

### Competencias en Diseño

- **Arquitectura Modular**: Separación clara de responsabilidades
- **Patrones de Diseño**: Implementación de patrones reconocidos
- **Experiencia de Usuario**: Interfaz intuitiva y mensajes claros
- **Documentación**: Código bien documentado y README completo
- **Buenas Prácticas**: Código limpio y mantenible

## 👨‍💻 Autor

**Jorge Fuentes Jiménez**
- GitHub: [@jorge-fuentes-94](https://github.com/jorge-fuentes-94)
- LinkedIn: [Jorge Fuentes Jiménez](https://linkedin.com/in/jorgefuentesjimenez)
- Email: jf7494@gmail.com

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo [LICENSE](LICENSE) para más detalles.

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/NuevaFuncionalidad`)
3. Commit tus cambios (`git commit -m 'Agregar nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/NuevaFuncionalidad`)
5. Abre un Pull Request

## 📞 Soporte

Si tienes preguntas o encuentras algún problema:

- Abre un [issue](https://github.com/jorge-fuentes-94/sistemagestioncontactos/issues)
- Contacta al autor por email
- Revisa la documentación de [Python](https://docs.python.org/)

---

⭐ **¡Si este proyecto te resulta útil para aprender Python, no olvides darle una estrella!** ⭐

