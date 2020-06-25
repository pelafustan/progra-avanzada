import re


def check_digit(ssn):
    """Función que entrega el dígito verificador de un RUN/RUN.

    Recibe, como string, lo que está a la izquierda del dígito verificador,
    despojado de todo símbolo (e.g. si 12.345.678-9, se recibe 12345678).

    Para detalles del algoritmo, consultar
    https://es.wikipedia.org/wiki/C%C3%B3digo_de_control#M%C3%B3dulo_11
    """
    aux = ('234567'*(len(ssn)//6 + 1))[:len(ssn)]
    reverse = ssn[::-1]
    result = 11 - (sum(int(a)*int(b) for a, b in zip(aux, reverse)) % 11)
    if result == 10:
        dv = 0
    elif result == 11:
        dv = 'k'
    else:
        dv = str(result)
    return dv


def validate_ssn(ssn):
    """Función que valida si un RUT/RUN está correctamente ingresado.

    Si el RUN/RUT está compuesto sólo por números, e.g. 12.345.678-9, se puede
    ingresar como int, e.g. validate_ssn(123456789).

    Si el RUN/RUT tiene dígito verificador K, e.g. 12.345.678-K, se debe
    ingresar como string, esté despojado o no de puntos y guión, i.d. da lo
    mismo si se ingresa como validate_ssn('12345678k') o
    validate_ssn('12.345.678-K').

    El resultado de la validación se entrega como booleano.
    """
    if isinstance(ssn, int):
        ssn = str(ssn)
        if check_digit(ssn[:-1]) == ssn[-1]:
            return True
        else:
            return False
    elif isinstance(ssn, str):
        ssn = ssn.replace('.', '').replace('-', '').lower()
        # se valida si el último dígito es un número o 'k',
        # además de revisar si el 'cuerpo' del Rol es numérico,
        # junto con el análisis del dígito verificador
        if (ssn[-1] == 'k' or ssn[-1].isdigit()) and ssn[0:-1].isdigit():
            if check_digit(ssn[:-1]) == ssn[-1]:
                return True
        else:
            return False


def format_ssn(ssn):
    """Formatea el RUN/RUT, agregando puntos y guión."""
    if isinstance(ssn, int):
        ssn = str(ssn)
    main = format(int(ssn[:-1]), ',d').replace(',', '.')
    dv = ssn[-1]
    return f'{main}-{dv}'


def validate_name(name):
    """Función que valida que los nombres/apellidos ingresados sean strings y
    no contengan números.

    El resultado de la validación se entrega como booleano.
    """
    if isinstance(name, str):
        if not re.search(r'/d', name):
            return True
        else:
            return False
    else:
        return False


class Person:
    """Clase que modela a una persona, con atributos:

    - Nombre(s): string
    - Apellido paterno: string
    - Apellido materno: string
    - RUN/RUT: string (eventualmente int)

    Respecto al RUN/RUT, si éste está compuesto sólo de elementos numéricos,
    e.g. 12.345.678-9, puede pasarse como 123456789; si el dígito verificador
    es K, e.g. 12.345.678-K, necesariamente debe pasarse como string, no
    importando si es con puntos y guión o no: lo único que importa es que debe
    ingresarse la totalidad de los caracteres, i.e. si RUN/RUT es 12.345.678-K
    éste puede ingresarse como '12345678k', '12345678K', '12.345.678-K', etc.
    """
    def __init__(
        self,
        first_name='',
        fathers_last_name='',
        mothers_last_name='',
        ssn=''
    ):
        if validate_name(first_name):
            self.__first_name = first_name
        else:
            raise ValueError('Nombre(s) inválido.')

        if validate_name(fathers_last_name):
            self.__fathers_last_name = fathers_last_name
        else:
            raise ValueError('Apellido paterno inválido.')

        if validate_name(mothers_last_name):
            self.__mothers_last_name = mothers_last_name
        else:
            raise ValueError('Apellido materno inválido.')

        if validate_ssn(ssn):
            self.__ssn = ssn
        else:
            raise ValueError('RUN/RUT inválido.')

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, value):
        if validate_name(value):
            self.__first_name = value

    @property
    def fathers_last_name(self):
        return self.__fathers_last_name

    @fathers_last_name.setter
    def fathers_last_name(self, value):
        if validate_name(value):
            self.__last_name = value
        else:
            raise ValueError("Apellido paterno inválido")

    @property
    def mothers_last_name(self):
        return self.__mothers_last_name

    @mothers_last_name.setter
    def mothers_last_name(self, value):
        if validate_name(value):
            self.__mothers_last_name = value
        else:
            raise ValueError("Apellido materno inválido")

    @property
    def complete_name(self):
        f1 = f'{self.first_name}'
        f2 = f'{self.fathers_last_name}'
        f3 = f'{self.mothers_last_name}'
        return f'{f1} {f2} {f3}'

    @property
    def ssn(self):
        return format_ssn(self.__ssn)

    def __str__(self):
        return f'{self.complete_name}'


if __name__ == "__main__":
    persona = Person("José Patricio", "Parada", "Gutiérrez", 183427911)
    print(persona)
    print(persona.complete_name)
    print(persona.ssn)
    # persona2 = Person("José Patricio", "Parada", "Gutiérrez", 183427912)
