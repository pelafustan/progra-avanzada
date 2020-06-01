from Actor import Actor
from Movie import Movie
import re
import pandas as pd


def process_data():
    # data = pd.read_csv('IMDb movies.csv').loc[:, ['title', 'year', 'actors']]
    data = pd.read_csv('IMDb movies.csv')
    data = data.loc[0:24, ['title', 'year', 'actors']]
    data = data.values
    return data


def create_movies(data):
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


# def get_all_actors(data):
#     actors_list = []
#     for i in range(len(data)):
#         for actor in data[i, 2].split(', '):
#             actors_list.append(actor)
#     actors_list = list(set(actors_list))
#     return actors_list


def substring_search(search_term, data_set):
    if isinstance(search_term, str):
        search_term = [search_term]
    matches = [
        match for match in data_set if all(
            re.search("\\b{}\\b".format(term), match) for term in search_term
        )
    ]
    return matches


if __name__ == "__main__":
    data = process_data()
    movie_list = create_movies(data)

    # for movie in movie_list:
    #     print(movie.title)
    #     for actor in movie.cast:
    #         print(actor.name)

    # actor_list = get_all_actors(data)
    # substring = ["Robert"]
    # matched = substring_search(substring, actor_list)
    # for match in matched:
    #     print(match)
