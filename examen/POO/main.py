import pandas as pd
from Book import Book
from Journal import Journal


def load_catalogue():
    try:
        catalogue = pd.read_csv("catalogue.csv")
        return catalogue
    except FileNotFoundError:
        print("No se ha creado el catálogo aún.")


def create_catalogue():
    df = pd.DataFrame(columns=[
        "code",
        "resource_type",
        "title",
        "year",
        "total_copies",
        "available_copies",
        "edition",
        "author",
        "publisher",
        "volume",
        "issue"
    ])
    df.to_csv("catalogue.csv")


def get_option(rng):
    opts = list(range(rng))
    opt = int(input("Ingrese opción: "))
    if opt in opts:
        return opt
    else:
        raise ValueError("Opción no válida")


def create_entry(catalogue):
    print('Creando nueva entrada al catálogo')
    print('Para ingresar un libro elija 0. Para una revista, 1')
    opt = get_option(2)
    if opt == 0:
        create_book(catalogue)
    else:
        pass


def create_book(catalogue):
    code = input("Ingrese código: ")
    if code in catalogue['code'].values:
        print("Código ya está dentro del catálogo.")
        return False
    title = input("Ingrese título: ")
    print('Ingrese autor o autores.')
    print('Si son varios autores, use una coma para separarlos')
    author = input()
    print('Ingrese el año.')
    year = int(input("Recuerde que debe ser un número: "))
    print('Ingrese la edición.')
    edition = int(input("Recuerde que debe ser un número: "))
    print('Ingrese el número de ejemplares')
    copies = int(input("Recuerde que debe ser un número: "))

    params = {
        'code': code,
        'title': title,
        'author': author,
        'year': year,
        'edition': edition,
        'copies': copies
    }

    return params
