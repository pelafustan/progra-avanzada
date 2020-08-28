from Resource import Resource


class Book(Resource):
    def __init__(
        self,
        title=None,
        author=None,
        code=None,
        year=None,
        edition=None,
        total_copies=1,
        available_copies=1
    ):
        super().__init__(title, code, year, total_copies, available_copies)
        if isinstance(author, str):
            self.__author = [author]
        elif isinstance(author, list):
            self.__author = author
        if isinstance(edition, int):
            self.__edition = edition

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, value):
        if isinstance(value, str):
            if self.__author[0]:
                self.__author.append(value)
            else:
                self.__author = [value.title()]
        elif isinstance(value, list):
            self.__author = value

    @property
    def edition(self):
        return self.__edition

    @edition.setter
    def edition(self, value):
        if isinstance(value, int):
            if value > 0:
                self.__edition = value
            else:
                raise ValueError
        else:
            raise ValueError

    def __str__(self):
        msg1 = f'Título: {self.title}'
        msg2 = f"Autor: {', '.join(self.author)}"
        msg3 = f'Código: {self.code}'
        msg4 = f'Edición: {self.edition}'
        return f'{msg1}\n{msg2}\n{msg3}\n{msg4}\n'
