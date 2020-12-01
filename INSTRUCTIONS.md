# Instrucciones para correr la app

1. Usar docker-compose para levantar la app:
```sh
docker-compose up
```
2. Esperar aproximadamente 3 -  minutos a que el contenedor de MySQL este listo (MyAdmin y la aplicación de Flask estarán listos antes, pero no se tendrá acceso a la BD) y que se ejecute el contenedor para insertar los datos.

3. Después de los periodos de tiempo dados hayan transcurrido, ya se podrá accesar a la BD, por lo tanto phpMyAdmin y la aplicación de Flask ya estarán usables.

- [PhpMyAdmin](http://localhost:8080/)
- [Flask App](http://localhost:5000/)

- Los datos para acceder a phpMyAdmin son:
    - Usuario: user1
    - Password: dbsecret123

4. Para las request se debe usar el método ``post()`` del módulo ``requests`` de python ejemplo:

```python
import requests
import pprint
url = 'http://localhost:5000/api/track_by_id/1'
json_obj = requests.post(url)
data = json_obj.json()
pprint.pprint(data)
```

- Los Urls de API usables están en el archivo, simplemente cambia la string tu código y en el caso de que sea necesario añade el valor a buscar:
    - [api_urls.txt](api_urls.txt)



### Las búsquedas en la app de artistas, canciones y track, son por nombre o título.

- Nota: Si queres buscar algo y estar seguro de que va tener un resultado, checa los apartados para mostrar todos los registros de artista, álbum y canciones.
    - [Every Artist](http://localhost:5000/artist/_everyone_)
    - [Every Album](http://localhost:5000/album/_all_)
    - [Every Track](http://localhost:5000/track/_all_)

- Para buscar un artista, ir al apartado de buscar un artista, escribir el nombre y pulsar el botón.
- También es posible hacer la busqueda por URL por ejemplo

        http://localhost:5000/artist/The+Midnight

     - Cuando se va a buscar en URL usando un término que necesite varias palabra, cambie los espacios por caracteres de '+'.


- Para buscar un álbum, ir al apartado de buscar un álbum, escribir el título y pulsar el botón.
- También es posible hacer la busqueda por URL por ejemplo

        http://localhost:5000/album/Endless+Summer

- Para buscar una canción, ir al apartado de buscar una canción, escribir el título y pulsar el botón.
- También es posible hacer la busqueda por URL por ejemplo

        http://localhost:5000/track/Sunset


