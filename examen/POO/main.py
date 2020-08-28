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
        'resource_type': 'Book',
        'title': title,
        'year': year,
        "total_copies": copies,
        "available_copies": copies,
        "edition": edition,
        "author": author,
        "publisher": '',
        "volume": '',
        "issue": ''
    }

    return params


def create_journal(catalogue):
    code = input("Ingrese código: ")
    if code in catalogue['code'].values:
        print("Código ya está dentro del catálogo.")
        return False
    title = input("Ingrese título: ")
    print('Ingrese editorial')
    print('Si son varias editoriales, use una coma para separarlas')
    publisher = input()
    print('Ingrese el año.')
    year = int(input("Recuerde que debe ser un número: "))
    print('Ingrese el volumen.')
    volume = int(input("Recuerde que debe ser un número: "))
    print('Ingrese el número (issue).')
    issue = int(input("Recuerde que debe ser un número: "))
    print('Ingrese el número de ejemplares')
    copies = int(input("Recuerde que debe ser un número: "))

    params = {
        'code': code,
        'resource_type': 'Journal',
        'title': title,
        'year': year,
        "total_copies": copies,
        "available_copies": copies,
        "edition": '',
        "author": '',
        "publisher": publisher,
        "volume": volume,
        "issue": issue
    }

    return params


def create_entry():
    catalogue = pd.read_csv("catalogue.csv")
    print('Creando nueva entrada al catálogo')
    print('Para ingresar un libro elija 0. Para una revista, 1')
    opt = get_option(2)
    if opt == 0:
        book = create_book(catalogue)
        df_book = pd.DataFrame.from_dict(book)
        catalogue = pd.DataFrame.append(dfBook)
        catalogue.to_csv('catalogue.csv')
    else:
        journal = create_journal(catalogue)
        df_journal = pd.DataFrame.from_dict(journal)
        catalogue = pd.DataFrame.append(dfBook)
        catalogue.to_csv('catalogue.csv')


def gen_books():
    books_list = []
    data = pd.read_csv('catalogue.csv')
    data = data[(data.resource_type == 'Book')]
    data = data.loc[
        'title',
        'author',
        'code',
        'year',
        'total_copies',
        'available_copies'
    ].values
    for i in range(len(data)):
        obj_book = Book()
        obj_book.title = data[i, 0]
        obj_book.author = data[i, 1]
        obj_book.code = data[i, 2]
        obj_book.year = data[i, 3]
        obj_book.total_copies = data[i, 4]
        obj_book.available_copies = data[i, 5]
    return books_list


def gen_journals():
    journals_list = []
    data = pd.read_csv('catalogue.csv')
    data = data[(data.resource_type == 'Journal')]
    data = data.loc[
        'title',
        'code',
        'year',
        'publisher',
        'volume',
        'issue',
        'total_copies',
        'available_copies'
    ].values
    for i in range(len(data)):
        obj_journal = Journal()
        obj_journal.title = data[i, 0]
        obj_journal.code = data[i, 1]
        obj_journal.year = data[i, 2]
        obj_journal.publisher = data[i, 3]
        obj_journal.volume = data[i, 4]
        obj_journal.issue = data[i, 5]
        obj_journal.total_copies = data[i, 6]
        obj_journal.available_copies = data[i, 7]
    return journals_list


def prestar():
    opt = get_option(2)
    print('Menú de préstamo.')
    print('Presione 0 para prestar libro, 1 para revista')
    if opt == 0:
        code = input("Ingrese código del libro: ")

    else:
        code = input("Ingrese código de la revista: ")
