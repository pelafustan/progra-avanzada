import random as r


class Doggo:
    def __init__(self, name, color, breed, age, gender, weight):
        self.name = name.title()
        self.color = color
        self.breed = breed
        self.age = age
        self.gender = gender.lower()
        if self.gender not in ["macho", "hembra"]:
            raise ValueError("Debe ser macho o hembra.")
        self.weight = weight
        if self.weight <= 0:
            raise ValueError("El peso debe ser mayor a cero.")
        self.actions = [
            "ladra al infinito", "come su alimento",
            "juega", "olfatea a las visitas",
            "orina la alfombra", "defeca en el patio",
            "araña la puerta para salir",
            "muerde al cartero", "defiende la casa",
            "se persigue la cola", "se sienta"
        ]
        if self.gender == "macho":
            self.actions.append("pelea a muerte por territorio")

    def get_name(self):
        return self.name

    def get_color(self):
        return self.color

    def get_breed(self):
        return self.breed

    def get_age(self):
        return self.age

    def set_age(self, age):
        if age < 0:
            raise ValueError("La edad debe ser mayor a cero")
        self.age = age

    def get_gender(self):
        return self.gender

    def set_weight(self, weight):
        if weight < 0:
            raise ValueError("El peso debe ser mayor a cero.")
        self.weight = weight

    def get_weight(self):
        return self.weight

    def get_actions(self):
        return self.actions

    def set_action(self, action):
        """Dogs can learn new tricks"""
        self.actions.append(action.lower())

    def del_action(self, action):
        if action in self.actions:
            self.actions.remove(action)

    def do_action(self):
        """Dogs can do whatever they wants in the list of actions"""
        return r.choice(self.actions)

    def do_specific_action(self, action):
        """Dogs can do tricks if you tell them what to do"""
        if action in self.actions:
            return action
        else:
            raise ValueError("Acción no existe")

    def correct_action(self, old_action, new_action):
        """Dogs also can change their behavior"""
        if old_action in self.actions:
            self.del_action(old_action)
            self.set_action(new_action)
        else:
            raise ValueError("Acción no existe")


if __name__ == "__main__":
    perrito = Doggo("yo no fui", "negro", "quiltro", 2, "MACHO", 5)

    print("{} puede:".format(perrito.get_name()))
    for action in perrito.actions:
        print(action)

    nuevo_truco = "da la pata"
    print("{} aprende '{}'".format(perrito.get_name(), nuevo_truco))
    perrito.set_action(nuevo_truco)

    print("Ahora {} {}".format(perrito.get_name(),
                               perrito.do_specific_action(nuevo_truco)))

    print("Se corregirá un comportamiento de {}".format(perrito.get_name()))
    old_action = "orina la alfombra"
    new_action = "orina en el patio"
    perrito.correct_action(old_action, new_action)

    print("Ahora {} puede:".format(perrito.get_name()))
    for action in perrito.actions:
        print(action)

    print("{} hará algunas acciones aleatorias:".format(perrito.get_name()))
    for i in range(10):
        print(perrito.do_action())
