class Resource:
    def __init__(self, title=None, code=None, year=None):
        self.__title = title
        self.__code = code
        self.__year = year

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        if isinstance(value, str):
            self.__title = value.title()

    @property
    def code(self):
        return self.__code

    @code.setter
    def code(self, value):
        if isinstance(value, str):
            self.__code = value

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        if isinstance(value, int):
            self.__year = value


class Book(Resource):
    def __init__(self, title=None, author=None, code=None, year=None):
        super().__init__(title, code, year)
        if isinstance(author, str):
            self.__author = [author]
        elif isinstance(author, list):
            self.__author = author
        elif not author:
            self.__author = [author]
        self.__isborrow = False

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
    def isborrow(self):
        return self.__isborrow

    @isborrow.setter
    def isborrow(self, value):
        if isinstance(value, bool):
            self.__isborrow = value

    def __str__(self):
        if self.isborrow:
            msg0 = 'Sí'
        else:
            msg0 = 'No'
        msg1 = f'Título: {self.title}'
        msg2 = f"Autor: {', '.join(self.author)}"
        msg3 = f'Código: {self.code}'
        msg4 = f'En biblioteca: {msg0}'
        return f'{msg1}\n{msg2}\n{msg3}\n{msg4}'


class Journal(Resource):
    def __init__(
        self,
        title=None,
        code=None,
        year=None,
        publisher=None,
        volume=None,
        issue=None
    ):
        super().__init__(title, code, year)
        self.__publisher = publisher
        self.__volume = volume
        self.__issue = issue

    @property
    def publisher(self):
        return self.__publisher

    @publisher.setter
    def publisher(self, value):
        if isinstance(value, str):
            if self.__publisher[0]:
                self.__publisher.append(value)
            else:
                self.__publisher = [value.title()]
        elif isinstance(value, list):
            self.__publisher = value

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, value):
        if isinstance(value, int):
            self.__volume = value

    @property
    def issue(self):
        return self.__issue

    @issue.setter
    def issue(self, value):
        if isinstance(value, int):
            self.__issue = value

    def __str__(self):
        msg1 = f'Título: {self.title}'
        msg2 = f'Código: {self.code}'
        msg3 = f'Editorial: {", ".join(self.publisher)}'
        msg4 = f'Volumen: {self.volume}'
        msg5 = f'Número: {self.issue}'
        return f'{msg1}\n{msg2}\n{msg3}\n{msg4}\n{msg5}'


if __name__ == "__main__":
    libro = Book(
        'El Ingenioso Hidalgo Don Quijote de la Mancha',
        'Miguel de Cervantes y Saavedra',
        'A1234',
        1605
    )
    revista = Journal(
        'Bioinformatics',
        'B1234',
        2020,
        [
            'Oxford University Press',
            'International Society for Computational Biology'
        ],
        36,
        11
    )
    print(libro)
    print(revista)
