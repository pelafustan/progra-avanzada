from Resource import Resource


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