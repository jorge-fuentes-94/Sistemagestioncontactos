# Gestión de contactos

Agenda de contactos por consola en Python, hecha para practicar programación orientada a objetos y persistencia en JSON. Todo está en `Gestiondecontactos.py`.

## Qué hace

Un menú con siete opciones: añadir, listar, buscar por id, borrar por id, guardar en un `.json`, cargar desde un `.json` y salir.

- `Contacto` guarda nombre, teléfono y correo.
- `GestionContactos` guarda los contactos en un diccionario por id, valida el teléfono (solo números) y el correo (que lleve `@` y `.`), y gestiona el guardado y la carga.
- Al cargar un archivo, el contador de ids continúa desde el más alto, para no repetir ninguno.

## Cómo probarlo

No necesita instalar nada:

```bash
python Gestiondecontactos.py
```

## Limitaciones

- Solo se guarda si eliges la opción 5; al salir no se guarda nada solo.
- No se puede editar un contacto: hay que borrarlo y crearlo de nuevo.
- La validación del correo es muy básica.
