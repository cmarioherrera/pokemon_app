
## Pokémon API


## Instruciones de instalación.

### Instalación

Clonar el repositorio desde github:

```sh
$ git clone git@github.com:cmarioherrera/pokemon_app.git

Crear un entorno virtual con python3:

```sh
$ cd pokemon_app
$ python3 -m venv venv
```

Activa el entorno virtual:

```sh
$ source venv/bin/activate
```

Instalación de dependencias del proyecto:

```sh
(venv) $ pip install -r requirements.txt
```

### Iniciar base de datos

Crear base de datos SQLite y cargar datos desde archivo pokemon.csv.  Usar el siguiente script:

```
(venv) $ python init_db.py
```

### Ejecución del servidor local de Flask


Especificar el archivo contenedor de la aplicación de Flask y el
entorno de ejecución:
```sh
(venv) $ export FLASK_APP=app.py
(venv) $ export FLASK_ENV=development
```

Ejecutar servidor de desarrollo.
```sh
(venv) $ flask run
```

# Documentación con Swagger y recursos.

Ingresar a 'http://localhost:5000/' donde tenemos los siquientes endpoints:

* Documentación  http://localhost:5000/apidocs
* Autenticación http://localhost:5000/api/v1/login
* Recurso de pokemon http://localhost:5000/api/v1/pokemons


Con el endpoint /api/v1/login generamos un token de autenticación con las crecendiales username: "user1" y password: "secret1", copiamos la respuesta ("Bearer {token}") en la vista Authorize, luego podemos a la vista del endpoint /api/v1/pokemons y hacer peticiones con las diferentes opciones.


# Ambiente de producción en AWS.

Ingresar a "http://18.216.187.220/apidocs/" donde tenemos acceso a los diferentes endpoint mencionados.
