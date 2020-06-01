from Actor import Actor


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
