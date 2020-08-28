class Resource:
    def __init__(
        self, title,
        code,
        year,
        total_copies=1,
        available_copies=1
    ):
        self.errors = [
            "Título inválido",
            "Código inválido",
            "Año debe ser un entero",
            "Error en el número de copias totales",
            "Error en el número de copias disponibles",
            "Copias disponibles no puede ser mayor que copias totales"
        ]
        self.__title = title
        self.__code = code
        self.__year = year
        if isinstance(total_copies, int):
            if isinstance(available_copies, int):
                if total_copies > 0 and available_copies > 0:
                    if total_copies >= available_copies:
                        self.__total_copies = total_copies
                        self.__available_copies = available_copies
                    else:
                        raise ValueError(self.errors[5])

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        if isinstance(value, str):
            self.__title = value.title()
        else:
            raise ValueError(self.errors[0])

    @property
    def code(self):
        return self.__code

    @code.setter
    def code(self, value):
        if isinstance(value, str):
            self.__code = value
        else:
            raise ValueError(self.errors[1])

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        if isinstance(value, int):
            self.__year = value
        else:
            raise ValueError(self.errors[2])

    @property
    def total_copies(self):
        return self.__total_copies

    @total_copies.setter
    def total_copies(self, value):
        if isinstance(value, int):
            if value > 0:
                self.__total_copies = value
            else:
                raise ValueError(self.errors[3])
        else:
            raise ValueError(self.errors[3])

    @property
    def available_copies(self):
        return self.__available_copies

    @available_copies.setter
    def available_copies(self, value):
        if isinstance(value, int):
            if value > 0:
                if value <= self.total_copies:
                    self.__available_copies = value
                else:
                    raise ValueError(self.errors[5])
            else:
                raise ValueError(self.errors[4])
        else:
            raise ValueError(self.errors[4])
