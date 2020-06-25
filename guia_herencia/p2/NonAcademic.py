from Employee import Employee


def validate_section(section):
    sections = [
        'Secretaría',
        'Biblioteca',
        'Decanato'

    ]
    if isinstance(section, str):
        if section in sections:
            return True
        else:
            return False
    else:
        return False


class NonAcademic(Employee):
    def __init__(
        self,
        first_name,
        fathers_last_name,
        mothers_last_name,
        ssn,
        hired_year,
        annex,
        section
    ):
        super().__init__(
            first_name,
            fathers_last_name,
            mothers_last_name,
            ssn,
            hired_year,
            annex
        )

        if validate_section(section):
            self.__section = section

        @property
        def role(self):
            return self.__section

        @role.setter
        def role(self, value):
            if validate_section(value):
                self.__section = value
            else:
                raise ValueError('Sección incorrecta')
