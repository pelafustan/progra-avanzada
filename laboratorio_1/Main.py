import random as r
import sys
import termios


def press_to_move():
    """Función para capturar el teclado.

    Más detalles en: https://stackoverflow.com/a/5004022
    """
    result = None
    fd = sys.stdin.fileno()
    oldterm = termios.tcgetattr(fd)
    newattr = termios.tcgetattr(fd)
    newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
    termios.tcsetattr(fd, termios.TCSANOW, newattr)
    try:
        result = sys.stdin.read(1)
    except IOError:
        pass
    finally:
        termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
    return result


class Engine:
    """Clase que instanciará el motor de un auto.

    Se elige de manera aleatoria la cilindrada y, en función de eso se
    asigna el consumo que tendrá el motor.
    """
    def __init__(self):
        self.displacement = r.choice([1.2, 1.6])
        if self.displacement == 1.2:
            self.consuption = 20
        else:
            self.consuption = 14


class Tank:
    """Clase que instanciará el estanque de un auto.

    Recibe como parámetro de entrada el volumen de combustible al
    momento de instanciar el tanque. Si no se pasa parámetro, se
    asume que el tanque está lleno.

    Posee un método que, en función de una cantidad, descuenta
    combustible del estanque, Tank.consume(L), en donde L es el
    volumen, en litros, a descontar.
    """
    def __init__(self, volume=32):
        self.capacity = 32
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
    """Clase que instanciará una rueda del auto.

    Se asigna un daño cero en la rueda al momento de instanciar, además
    de una variable booleana que indica si es necesario cambiar la
    rueda. El daño se mide en porcentaje.

    Posee el método Wheel.tear() que asigna un desgaste aleatorio de la
    rueda, entre 1 y 10 y se lo agrega al atributo Wheel.damage.
    """
    def __init__(self):
        self.damage = 0
        self.change = False

    def tear(self):
        self.damage += r.randint(1, 10)
        if self.damage >= 90:
            self.change = True


class Speedometer:
    """Clase que muestra la velocidad en un momento dado"""
    def show_speed(self, speed):
        print("La velocidad actual es {} km/h.".format(speed))


class Igniter:
    """Clase que instancia el encendido del auto.

    Posee el atributo booleano Igniter.fired, que indica si el auto
    está encendido o no.

    Posee los métodos Igniter.turn_on() e Igniter.turn_off() que
    cambian el valor del atributo Igniter.fired.
    """
    def __init__(self, fired=False):
        self.fired = fired

    def turn_on(self):
        if not self.fired:
            self.fired = True

    def turn_off(self):
        if self.fired:
            self.fired = False


class Car:
    """Clase principal para construir el auto.

    Se conforma a partir de las clases anteriores, recibiendo como
    parámetros para instanciarse el volumen de combustible en  que
    habrá en el tanque y el numero de ruedas del vehículo.

    Posee el método Car.move(), que permite mover el vehículo,
    presionando una tecla, hasta que el vehículo se quede sin
    combustible o el usuario presione <C-c>.

    También posee el método Car.refill(L), que permite rellenar el
    tanque del vehículo en L litros.
    """
    def __init__(self, volume=32, no_wheels=4):
        self.speed = 0
        self.distance = 0
        self.cumulative_distance = 0
        self.flat = False
        self.engine = Engine()
        self.tank = Tank(volume)
        self.speedometer = Speedometer()
        self.wheels = [Wheel() for wheel in range(no_wheels)]
        self.igniter = Igniter()

    def refill(self, volume):
        self.tank.volume += volume

    def move(self):
        if not self.igniter.fired and self.tank.load:
            print("El auto está apagado.")
            print("Presione una tecla para encenderlo: ")
            press_to_move()
            self.igniter.turn_on()
            self.tank.consume(self.tank.capacity*0.01)
            if self.tank.load:
                self.move()
            else:
                print("No queda combustible.")
                print("Fin del viaje")
        elif self.igniter.fired and self.tank.load:
            self.speed = r.uniform(5, 120)
            self.time = r.randint(0, 10) / 3600
            self.distance = self.speed * self.time
            self.cumulative_distance += self.distance
            self.tank.consume(self.distance/self.engine.consuption)
            message1 = "El auto avanzó {} km en {} segundos."
            message2 = "El auto ha avanzado un total de {} km."
            message3 = "Se consumieron {} L de combustible."
            message4 = "Quedan {} L en el tanque."
            message5 = "El desgaste de la rueda {} es {}%"
            self.speedometer.show_speed(self.speed)
            print(message1.format(self.distance, self.time*3600))
            print(message2.format(self.cumulative_distance))
            print(message3.format(self.distance/self.engine.consuption))
            print(message4.format(self.tank.volume))
            for i in range(len(self.wheels)):
                self.wheels[i].tear()
                print(message5.format(i+1, self.wheels[i].damage))
                if self.wheels[i].change:
                    self.flat = True
                    if self.igniter.fired:
                        print("Rueda {} mal estado".format(i+1))
                        print("Apagando motor.")
                        self.igniter.turn_off()
                        print("Cambiando rueda.")
                        self.wheels[i] = Wheel()
                    else:
                        print("Rueda {} mal estado".format(i+1))
                        print("Cambiando rueda.")
                        self.wheels[i] = Wheel()
            if self.flat:
                self.flat = False
                self.move()
            else:
                print("Presione una tecla para avanzar: ")
                press_to_move()
                self.move()
        elif not self.tank.load:
            print("No queda combustible.")
            print("Fin del viaje")


if __name__ == "__main__":
    tocomocho = Car(0.5, 4)
    tocomocho.move()
    print("".join('='*60))
    print("En el tanque hay {} L.".format(tocomocho.tank.volume))
    print("Tengo una luca en el bolsillo, le woa zampar su litro.")
    tocomocho.refill(1)
    print("Ahora hay {} L en el tanque.".format(tocomocho.tank.volume))
