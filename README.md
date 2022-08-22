# Taller DevOps Tecnologías Emergentes

## Autor

Este ejercicio es realizado por **Jhon Sebastián Londoño Cárdenas**, estudiante de Ingeniería de Sistemas y Computación de la *Pontificia Universidad Javeriana Cali* como un entregable para la asignatura de Tecnologías Emergentes.

## Prerequisitos

Como prerequisitos se tiene:

- Se debe tener instalado Docker.
- Se debe tener instalado Git, así como una cuenta en GitHub.
- Tener instalada una versión de Python 3, preferiblemente Python 3.6 en adelante.
- Es recomendable crear un ambiente virtual donde se lleven a cabo las operaciones de cada proyecto que se tenga por separado: https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/26/python-virtual-env/ .
- Instalar la herramienta FastAPI, la cual facilita la creación de la API y su utilización.
- Instalar la herramienta uvicorn[standard], la cual provee un servidor local donde ejecutar pruebas sobre el ejercicio.
- Instalar la herrmienta requests, la cual permite trabajar con peticiones REST que involucran la API, el servidor y datos generados gracias a mockapi.io.


## ¿Cómo ejecutar la app?


Para ejecutar la aplicación se debe descargar el código que está en el repositorio y realizar los siguientes pasos:

- Usar la consola para acceder hasta la ruta donde se encuentra la carpeta que contiene todo el proyecto con los elementos descargados.
- Recomendable crear un ambiente virtual para el proyecto, lo cual se puede hacer con las instrucciones en el siguiente enlace dependiendo del sistema operativo que se utiliza: https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/26/python-virtual-env/ .
- Una vez descargado y accedido al ambiente del proyecto bastará con ejecutar el comando *uvicorn main:app --reload*, de esta manera se iniciará el servidor y con él la aplicación. Podremos comprobar que esto funciona gracias a un mensaje en la consola que indica que el proceso de inicio se ha completado. Otra forma de comprobarlo es accediendo a http://localhost:8000/items y verificando que muestra los datos traídos de mockapi.io.
- Para detener el servidor y por ende, la aplicación, se debe oprimir *Ctrl + C key*.


## ¿Cómo probar la app?

Las pruebas en la aplicación se pueden hacer a través de Swagger Inspector, el cual no es compatible con el navegador Opera. Para ingresar a la herramienta se hace utiliza el siguiente enlace: https://inspector.swagger.io/builder .

Se debe descargar también una extensión para el navegador donde se use esta herramienta. Este recurso cuenta con un lugar para colocar el enlace de la API que se va a utilizar y el cual dependerá del protocolo sobre el cual se quieran realizar las pruebas.

### Método GET
Usando:

http://localhost:8000/items

### Método PUT
Usando:

http://localhost:8000/items/{item_id}

Se pasa además el cuerpo del json con el que se desea actualizar el elemento que corresponde a {item_id}:

```
{
    "name": "loquesea",
    "price": 12345,
    "is_offer": false
}
```


### Método DELETE
Usando:

http://localhost:8000/items/{item_id}

El {item_id} corresponde al indicador del elemento que se quiere eliminar. No necesita el cuerpo, solo el id.

### Método POST
Usando:

http://localhost:8000/items

Se pasa además el cuerpo del json con el que se desea crear el nuevo elemento:

```
{
    "name": "loquesea",
    "price": 12345,
    "is_offer": false
}
```
No se pasa el id porque lo crea al final de los elementos existentes..

**Nota:** en el documento se adjuntan pruebas del funcionamiento de todos los métodos.