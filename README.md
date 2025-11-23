# Cmn-flask-server

Servidor Flask para la parte 1 de la entrega final de la materia "Comunicaciones 2" — Universidad de Antioquia.

Descripción
-----------

Este proyecto contiene un servidor web mínimo implementado con Flask para soportar la entrega práctica del curso. Incluye rutas básicas, una plantilla para el formulario de contacto y recursos estáticos.

Características
- Servidor Flask sencillo y fácil de ejecutar.
- Plantillas en `templates/` (ej. `contacto.html`).
- Recursos estáticos en `static/` (ej. `styles.css`).
- Scripts de inicialización de la base de datos en `initdb.py` y lógica en `database.py`.

Prerequisitos
- Python 3.8+ (recomendado Python 3.10+)
- `pip` para instalar dependencias
- tener instalado flask
- tener instalada la bd sqlite

Instalación rápida
------------------

1. Clona el repositorio (si aún no lo tienes):

```bash
git clone https://github.com/BrahiamAcosta/Cmn-flask-server.git
cd Cmn-flask-server
```

Inicializar la base de datos
---------------------------

```bash
python initdb.py
```

Ejecución del servidor
----------------------


```bash
python main.py
```