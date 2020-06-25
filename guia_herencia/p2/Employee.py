from datetime import datetime
from Person import Person


def validate_year(year):
    if year > 1980 and year <= datetime.now().year:
        return True
    else:
        return False


def validate_annex(annex):
    if isinstance(annex, int):
        annex = str(annex)
    elif isinstance(annex, str):
        try:
            int(annex)
        except ValueError:
            return False
    if len(annex) != 3:
        return False
    if int(annex) >= 1 and int(annex) <= 999:
        return True
    else:
        return False


class Employee(Person):
    def __init__(
        self,
        first_name,
        fathers_last_name,
        mothers_last_name,
        ssn,
        hired_year,
        annex
    ):
        super().__init__(first_name, fathers_last_name, mothers_last_name, ssn)
        if validate_year(hired_year):
            self.__year = hired_year
        else:
            raise ValueError("Año de contratación no válido.")
        if validate_annex(annex):
            self.__annex = annex
        else:
            raise ValueError("Anexo no válido")

    @property
    def annex(self):
        return self.__annex

    @annex.setter
    def annex(self, value):
        if validate_annex(value):
            self.__annex = value

    @property
    def hired_year(self):
        return self.__year
