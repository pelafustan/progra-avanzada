from Employee import Employee


def validate_departament(departament):
    departaments = [
        'Bioinformática',
        'Ciencias De La Computación',
        'Electromecánica Y Conversión de Energía',
        'Ingeniería Industrial',
        'Ingeniería Y Gestión De La Construcción'
        'Tecnologías Industriales'
    ]
    if isinstance(departament, str):
        if departament.title() in departaments:
            return True
        else:
            return False
    else:
        return False


class Academic(Employee):
    def __init__(
        self,
        first_name,
        fathers_last_name,
        mothers_last_name,
        ssn,
        hired_year,
        annex,
        departament
    ):
        super().__init__(
            first_name,
            fathers_last_name,
            mothers_last_name,
            ssn,
            hired_year,
            annex
        )
        if validate_departament(departament):
            self.__departament = departament
        else:
            raise ValueError('Departamento no corresponde.')

    @property
    def departament(self):
        return self.__departament

    @departament.setter
    def departament(self, value):
        if validate_departament(value):
            self.__departament = value
