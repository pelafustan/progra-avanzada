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
