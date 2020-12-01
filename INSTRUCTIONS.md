# Instrucciones para correr la app

1. Usar docker-compose para levantar la app:
```sh
docker-compose up
```
2. Esperar aproximadamente 3 -  minutos a que el contenedor de MySQL este listo (MyAdmin y la aplicación de Flask estarán listos antes, pero no se tendrá acceso a la BD) y que se ejecute el contenedor para insertar los datos.

3. Después de los periodos de tiempo dados hayan transcurrido, ya se podrá accesar a la BD, por lo tanto MyAdmin y la aplicación de Flask ya estarán usables.

- [PhpMyAdmin](localhost:8080)
- [Flask App](http://localhost:5000/)

4. Para las request se debe usar el método ``post()`` del módulo ``requests`` de python ejemplo:

```python
import requests
import pprint
url = 'http://localhost:5000/api/track_by_id/1'
json_obj = requests.post(url)
data = json_obj.json()
pprint.pprint(data)
```

- Los Urls de API usables están en el archivo:
    - [api_urls.txt](api_urls.txt)

- Las búsquedas en la app de artistas, canciones y track, son por nombre o 
título.