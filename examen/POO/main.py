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
        "resource_type",
        "title",
        "code",
        "year",
        "total_copies",
        "available_copies",
        "edition",
        "author",
        "publisher",
        "volume",
        "issue"
    ])
    return df
