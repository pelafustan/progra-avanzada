from Person import Person
from datetime import datetime


def validate_reg_number(reg_number):
    if isinstance(reg_number, int):
        reg_number = str(reg_number)
    elif isinstance(reg_number, str):
        if not reg_number.isdigit():
            return False
    if int(reg_number[0:4]) > datetime.now().year:
        return False
    # TODO: add validation to career code.


class Student(Person):
    def __init__(
        self,
        first_name,
        fathers_last_name,
        mothers_last_name,
        ssn,
        reg_number,
        courses
    ):
        super().__init__(first_name, fathers_last_name, mothers_last_name, ssn)
