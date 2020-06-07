# Laboratorio 1

## Objetivos:
* Crear clases y objetos.
* Definir atributos y métodos.
* Aplicar visibilidad a los atributos y acceder mediante métodos al control de los atributos.
* Definir responsabilidades "justas" a cada una de las clases.
* Interactuar entre las relaciones definidas entre las clases mediante acciones que afecten atributos o estados.
* Crear y manipular una colección de objetos.
* Definir un programa `main` que controle la aplicación orientada a objetos.
* Buenas prácticas de programación (uso de `pylint` o `flake8`).

### Laboratorio:

1. Se requiere construir un automóvil con las siguientes características (objetos):
    * Puede poseer un motor con cilindrada 1.2 o 1.6 (azar).
    * Tiene un estanque de combustible de 32 litros de capacidad.
    * Posee 4 ruedas.
    * Tiene un velocímetro.

#### Condiciones:
* Al momento de crear el objeto auto se deberá generar una instancia para crear un objeto de tipo motor, que se pasará como parámetro al objeto de tipo auto.
* Un atributo de motor deberá ser implementado a partir de un `random` para determinar su cilindrada.
* A través de un setter deberá implementar las ruedas, el velocímetro y el estanque del objeto auto.
* Un método a crear será el que controle el encendido y apagado del auto. Una de sus condiciones es que su estado inicial será detenido, por lo que se debe encender y cambiar el estado del atributo (puede ser booleano).
* Al encender el objeto auto, se consumirá el 1% del combustible.
* Otra condición del objeto estanque es que si la cilindrada del motor es 1.2, el consumo de combustible será de 1 litro por cada 20 km, en velocidad máxima. Si es 1.6, el consumo será de 14 km por cada litro, en velocidad máxima.
* La velocidad máxima será de 120 km/h.
* El auto se moverá en linea recta y existirá un método que permita esto. La acción de mover el auto será a través de una tecla y, cada vez que se presione, llamará a éste método de la clase auto.
* Para determinar el consumo de combustible, se aplicará la fórmula <img src="https://latex.codecogs.com/svg.latex?\large&space;d=v\cdot&space;t" title="\large d=v\cdot t" />, donde:
    * <img src="https://latex.codecogs.com/svg.latex?\large&space;d" title="\large d" /> es la distancia recorrida.
    * <img src="https://latex.codecogs.com/svg.latex?\large&space;v" title="\large v" /> es la velocidad del móvil.
    * <img src="https://latex.codecogs.com/svg.latex?\large&space;t" title="\large t" /> es el tiempo que dura el movimiento (`random` entre 1 y 10 segundos).
* El control de velocidad queda a libre disposición de implementar y NO se complique con la aceleración.
* Las ruedas sufren desgaste por cada avance del vehículo; éstas se deterioran entre un 1% y 10% por cada movimiento del auto.
* Deberá siempre reportar el estado del auto, como de sus partes.
* Si se queda sin combustible, el auto se detiene y la aplicación culmina.