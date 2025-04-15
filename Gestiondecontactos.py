import json

class Contacto:
    def __init__(self, nombre, telefono, correo):
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo

class GestionContactos:
    def __init__(self):
        self.contactos = {}
        self.contador_ids = 1  

    def _check_telefono(self, telefono):
        try:
            int(telefono)
        except ValueError:
            raise ValueError("Teléfono incorrecto.")

    def _check_correo(self, correo):
        if "@" not in correo or "." not in correo:
            raise ValueError("Correo no válido.")

    def agregar_contacto(self, nombre, telefono, correo):
        self._check_telefono(telefono)
        self._check_correo(correo)
        id_contacto = self.contador_ids
        self.contactos[id_contacto] = Contacto(nombre, telefono, correo)
        self.contador_ids += 1
        print(f"Contacto {nombre} agregado exitosamente con ID {id_contacto}.")

    def mostrar_contactos(self):
        if not self.contactos:
            print("No hay contactos para mostrar.")
        for id_contacto, contacto in self.contactos.items():
            print(f"ID: {id_contacto} - Nombre: {contacto.nombre}, Teléfono: {contacto.telefono}, Correo: {contacto.correo}")

    def buscar_contacto(self, id_contacto):
        id_contacto = int(id_contacto)
        if id_contacto in self.contactos:
            contacto = self.contactos[id_contacto]
            print(f"ID: {id_contacto} - Nombre: {contacto.nombre}, Teléfono: {contacto.telefono}, Correo: {contacto.correo}")
        else:
            print("Contacto no encontrado.")

    def eliminar_contacto(self, id_contacto):
        id_contacto = int(id_contacto)
        if id_contacto in self.contactos:
            del self.contactos[id_contacto]
            print(f"Contacto con ID {id_contacto} eliminado.")
        else:
            print("Contacto no encontrado.")

    def guardar_archivo(self, nombre_archivo):
        try:
            with open(nombre_archivo, 'w') as archivo:
                datos_a_guardar = {
                    str(id_contacto): {
                        "nombre": contacto.nombre,
                        "telefono": contacto.telefono,
                        "correo": contacto.correo
                    } for id_contacto, contacto in self.contactos.items()
                }
                json.dump(datos_a_guardar, archivo, indent=4)
                print(f"Contactos guardados en '{nombre_archivo}'.")
        except Exception as e:
            print(f"Error al guardar el archivo: {e}")

    def cargar_archivo(self, nombre_archivo):
        try:
            with open(nombre_archivo, "r") as archivo:
                datos_cargados = json.load(archivo)
                for id_contacto, datos in datos_cargados.items():
                    contacto = Contacto(
                        nombre=datos["nombre"],
                        telefono=datos["telefono"],
                        correo=datos["correo"]
                    )
                    self.contactos[int(id_contacto)] = contacto
                    self.contador_ids = max(self.contador_ids, int(id_contacto) + 1)
                print("Contactos cargados.")
        except FileNotFoundError:
            print("Archivo no encontrado. Se iniciará una lista vacía.")
        except json.JSONDecodeError:
            print("El archivo tiene un formato incorrecto.")
        except Exception as e:
            print(f"Error al cargar el archivo: {e}")

def menu():
    gestor = GestionContactos()

    while True:
        print("\n--- Menú de Gestión de Contactos ---")
        print("1. Agregar contacto")
        print("2. Mostrar todos los contactos")
        print("3. Buscar contacto por ID")
        print("4. Eliminar contacto por ID")
        print("5. Guardar contactos en archivo")
        print("6. Cargar contactos desde archivo")
        print("7. Salir")

        opcion = input("Selecciona una opción (1-7): ")

        if opcion == "1":
            print("\n--- Agregar contacto ---")
            try:
                nombre = input("Nombre: ").strip()
                telefono = input("Teléfono: ").strip()
                correo = input("Correo electrónico: ").strip()
                gestor.agregar_contacto(nombre, telefono, correo)
            except ValueError as e:
                print(f"Error: {e}")
            except Exception:
                print("Ocurrió un error inesperado.")

        elif opcion == "2":
            print("\n--- Mostrar todos los contactos ---")
            try:
                gestor.mostrar_contactos()
            except Exception:
                print("Ocurrió un error inesperado.")

        elif opcion == "3":
            print("\n--- Buscar contacto por ID ---")
            try:
                id_a_buscar = input("Introduce la ID: ").strip()
                gestor.buscar_contacto(id_a_buscar)
            except ValueError:
                print("Error en el valor introducido.")
            except Exception:
                print("Ocurrió un error inesperado.")

        elif opcion == "4":
            print("\n--- Eliminar contacto por ID ---")
            try:
                id_a_eliminar = input("Introduce la ID: ").strip()
                gestor.eliminar_contacto(id_a_eliminar)
            except ValueError:
                print("Error en el valor introducido.")
            except Exception:
                print("Ocurrió un error inesperado.")

        elif opcion == "5":
            print("\n--- Guardar contactos ---")
            try:
                nombre_archivo = input("¿Qué nombre quieres ponerle al archivo?: ").strip()
                if nombre_archivo == "":
                    nombre_archivo = "contactos"
                archivo_a_guardar = nombre_archivo + ".json"
                gestor.guardar_archivo(archivo_a_guardar)
            except Exception:
                print("Ocurrió un error al guardar el archivo.")

        elif opcion == "6":
            print("\n--- Cargar contactos ---")
            try:
                nombre_archivo = input("¿Qué nombre tiene el archivo?: ").strip()
                if nombre_archivo == "":
                    nombre_archivo = "contactos"
                archivo_a_cargar = nombre_archivo + ".json"
                gestor.cargar_archivo(archivo_a_cargar)
            except Exception:
                print("Ocurrió un error al cargar el archivo.")

        elif opcion == "7":
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")

menu()