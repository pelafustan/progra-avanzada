import random as r


class Engine:
    def __init__(self):
        self.displacement = r.choice([1.2, 1.6])
        if self.displacement == 1.2:
            self.consuption = 20
        else:
            self.consuption = 14


class Tank:
    capacity = 32

    def __init__(self, volume=32):
        if volume > 32:
            self.volume = 32
            self.load = True
        elif volume > 0:
            self.volume = volume
            self.load = True
        else:
            self.volume = 0
            self.load = False

    def consume(self, quantity):
        if self.volume >= quantity:
            self.volume -= quantity
        else:
            self.volume = 0
            self.load = False


class Wheel:
    def __init__(self):
        self.damage = 0
        self.change = False

    def tear(self):
        self.damage += r.randint(1, 10)
        if self.damage >= 90:
            self.change = True


class Speedometer:
    def __init__(self, speed=0):
        self.speed = speed

    def show_speed(self):
        print("La velocidad es {} km/h".format(self.speed))


class Igniter:
    def __init__(self, fired=False):
        self.fired = fired

    def turn_on(self):
        if not self.fired:
            self.fired = True

    def turn_off(self):
        if self.fired:
            self.fired = False


class Car:
    def __init__(self, volume=32, no_wheels=4):
        self.speed = 0
        self.distance = 0
        self.engine = Engine()
        self.tank = Tank(volume)
        self.speedometer = Speedometer(self.speed)
        self.wheels = [Wheel() for i in range(no_wheels)]
        self.igniter = Igniter()

    def move(self):
        if self.igniter.fired is True:
            self.speed = r.uniform(5, 120)
            self.time = r.randint(0, 10)/3600
            self.distance = self.speed * self.time



tocomocho = Car(20, 4)
for i in range(len(tocomocho.wheels)):
    print("La rueda {} esta dañada en un {}%"
          .format(i+1, tocomocho.wheels[i].damage))

print(tocomocho.speed)
print(tocomocho.tank.volume)
tocomocho.speedometer.show_speed()
print(tocomocho.motor.consuption)
print(tocomocho.motor.displacement)
print(tocomocho.igniter.fired)
