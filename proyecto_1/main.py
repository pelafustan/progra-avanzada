import pandas as pd
import re


class Actor:
    def __init__(self):
        self._name = None
        self._movies = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self._name = name

    @property
    def movies(self):
        return self._movies

    @movies.setter
    def movies(self, movie):
        if isinstance(movie, Movie):
            self._movies.append(movie)


class Movie:
    def __init__(self):
        self._title = None
        self._year = None
        self._cast = []

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if isinstance(value, str):
            self._title = value

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        if isinstance(value, int):
            self._year = value

    @property
    def cast(self):
        return self._cast

    @cast.setter
    def cast(self, actor):
        if isinstance(actor, Actor):
            self._cast.append(actor)


def process_data():
    """ Se obtienen las columnas 'title', 'year' y 'actors' del
    dataframe dado y se almacenan en un arreglo multidimensional,
    para posterior manipulación.
    """
    data = pd.read_csv(
        'IMDb movies.csv'
        ).loc[
            :, ['title', 'year', 'actors']
            ].values
    return data


def create_movies(data):
    """ A partir de las entradas del dataframe filtrado, se crea una
    lista de objetos tipo Movie y se llenan los atributos requeridos
    para la clase Movie.
    """
    movie_list = []
    for i in range(len(data)):
        obj_movie = Movie()
        obj_movie.title = data[i, 0]
        obj_movie.year = data[i, 1]
        if isinstance(data[i, 2], str):
            for actor in data[i, 2].split(', '):
                obj_actor = Actor()
                obj_actor.name = actor
                obj_movie.cast = obj_actor
        movie_list.append(obj_movie)
    return movie_list


def get_actors(data):
    """ A partir de la columna 'actors' del dataframe, se crea una
    lista de strings, la cual poseerá entradas repetidas. Mediante el
    uso de set, se crea una nueva lista strings únicos, la cual es
    usada para crear la lista de objetos tipo Actor.
    """
    actors_list = []
    actors_names = []
    for i in range(len(data)):
        if isinstance(data[i, 2], str):
            for entry in data[i, 2].split(', '):
                actors_names.append(entry)
    actors_names = list(set(actors_names))
    for actor in actors_names:
        obj_actor = Actor()
        obj_actor.name = actor
        actors_list.append(obj_actor)
    return actors_list


def substring_search(search_term, data_set):
    """ Pequeña función que usa regex para buscar coincidencias dentro
    de una lista de strings.
    """
    if isinstance(search_term, str):
        search_term = [search_term]
    matches = [
        match for match in data_set if all(
            re.search("\\b{}\\b".format(term), match) for term in search_term
        )
    ]
    return matches


def search_actor(actor_name, actors_list):
    """ Pequeña función para buscar los actores que cumplan con el
    criterio de búsqueda dentro de la lista de actores.
    """
    actors = []
    substring = [actor_name]
    for actor in actors_list:
        actors.append(actor.name)
    matches = substring_search(substring, actors)
    return matches


def connect_actor_and_movies(actor_name, actors_list, movies):
    """ Función que conecta el nombre de un actor/actriz y las
    películas en las que participa.

    Para 'optimizar' el uso de la función, se realizan modificaciones
    directas sobre la lista de actores; si se llegase a consultar
    nuevamente por el mismo actor, no será necesario entrar a realizar
    los ciclos for porque el dato ya se encuentra en la lista.
    """
    for i in range(len(actors_list)):
        if actors_list[i].name == actor_name:
            index = i
            break
    if not len(actors_list[index].movies):
        # Entra sólo si el actor no tiene películas ingresadas.
        for movie in movies:
            for actor in movie.cast:
                if actor_name == actor.name:
                    actors_list[index].movies = movie
                    break
    return actors_list[index]


def show_movies(actor):
    print('{} ha actuado en {} películas, las que son: '.format(
            actor.name,
            len(actor.movies)
            )
          )
    for movie in actor.movies:
        print('{} del año {}'.format(movie.title, movie.year))


def get_activity_years(actor):
    first = actor.movies[0].year
    last = actor.movies[0].year
    if len(actor.movies) != 1:
        for movie in actor.movies:
            if movie.year > last:
                last = movie.year
            elif movie.year < first:
                first = movie.year
    print('{} presenta películas entre los años {} y {}.'.format(
                actor.name,
                first,
                last
            )
          )
    print('Lo que se traduce en {} años de carrera.'.format(
                last - first
            )
          )


if __name__ == "__main__":
    data = process_data()
    movie_list = create_movies(data)
    actors_list = get_actors(data)
    search = "De Niro"
    matched = search_actor(search, actors_list)
    message = 'Las coincidencias para la búsqueda del término {} son:'.format(
        search
        )
    print(message)
    for match in matched:
        print(match)

    actor_name = 'Robert De Niro'  # Se elige un nombre de la búsqueda.
    actor = connect_actor_and_movies(
        actor_name, actors_list, movie_list
        )
    show_movies(actor)
    get_activity_years(actor)
