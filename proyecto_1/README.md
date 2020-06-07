# Proyecto 1

## Clases y Objetos

### Contexto

[IMDb](https://www.imdb.com/) es un sitio web que contiene información relacionada a películas, incluyendo descripción de trama, calificaciones -tanto de críticos especializados como usuarios- fechas de lanzamiento, entre otros datos.

El almacena antecedentes de casi todas las películas que se han estrenado e, incluso, de las que se planean estrenar -la más antigua es "Passage de Venus" de 1874 y una de las más 'nueva' es "Avatar 5", esperada para 2027.

Cuenta con más de 6 millones de títulos y es propiedad de [Amazon](https://www.amazon.com/) desde 1998.

### Proyecto

A partir del dataframe adjunto al repositorio, se crean listas de objetos que modelan a las películas y sus actores. Las películas tienen los atributos `title`, `year` y `cast`, que hacen referencia al título, año y reparto, respectivamente. Los objetos Actor poseen los atributos `name` y `movies`, indicando nombre y películas en las que ha actuado el actor, respectivamente.

Si se quiere encontrar a un actor en particular, se puede realizar una búsqueda a partir del nombre completo. Si no se conoce el nombre completo, se puede utilizar el nombre o apellido del actor/actriz para arrojar todas las coincidencias dentro de la lista de actores.

Una vez encontrado el nombre del actor, se relaciona éste con todos los objetos película, a través del atributo `cast`, para desplegar la lista de películas en las que actúa dicho actor/actriz, mediante el atributo `movies`.

En la rutina de ejemplo, dentro de `main.py`, se realiza una búsqueda de todas las coincidencias para el apellido `'De Niro'`. Se elije al actor `'Robert De Niro'` y se procede a obtener todas las películas de la lista en las que ha actuado. Además del listado de películas, se indica el período de actividad del actor/actriz.