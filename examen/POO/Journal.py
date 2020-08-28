from Resource import Resource


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
