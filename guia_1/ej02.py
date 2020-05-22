class Book:
    def __init__(self, title, author, copies=1, borrowed=0):
        self.title = title
        self.author = author
        self.total_copies = copies
        self.borrowed = borrowed
        self.available_copies = self.total_copies - self.borrowed

    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title

    def get_author(self):
        return self.author

    def set_author(self, author):
        self.author = author

    def get_total_copies(self):
        return self.total_copies

    def set_total_copies(self, copies):
        self.total_copies += copies

    def get_available_copies(self):
        return self.available_copies

    def set_available_copies(self, copies):
        self.available_copies += copies
        if self.available_copies > self.total_copies:
            self.set_total_copies(self.available_copies)

    def get_borrowed(self):
        return self.borrowed

    def set_borrowed(self, borrowed):
        if self.available_copies > borrowed:
            self.borrowed += borrowed
            self.available_copies_copies -= self.borrowed
        else:
            print("No se puede gestionar el préstamos, libros insuficientes.")
            print("Quedan {} ejemplares".format(self.available_copies))


if __name__ == "__main__":
    mobydick = Book("Moby Dick", "Melville", 100, 5)
    print("Se añadió el libro {} al catálogo".format(mobydick.get_title()))
    print("Se han prestado {} ejemplares.".format(mobydick.get_borrowed()))
    print("Hay disponibles {} copias, de un total de {} ejemplares"
          .format(mobydick.get_available_copies(),
                  mobydick.get_total_copies()))
