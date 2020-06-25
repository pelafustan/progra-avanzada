# Guía 2: Herencia

1. Escriba un programa para una biblioteca que contenga libros y revistas.
    * Las características comunes se almacenan tanto para las revistas como para los libros son el código, el título y el año de publicación. Estas tres características se pasan por parámetro al constructor al momento de crear los objetos.
    * Los libros tienen además un atributo prestado. Los libros, cuando se crean, no están prestados.
    * Las revistas tienen un número de edición. En el momento de crear las revistas se pasa el número de edición como parámetro al constructor.
    * Tanto las revistas como los libros deben tener un método `__str__` que devuelva el valor de los atributos concatenados (formateados) para mostrar al usuario de forma clara qué libro o revista se trata.
    * También tienen un método que devuelve el año de publicación y otro el código.
    * Para prevenir posibles cambios en el programa, se tiene que implementar una clase tipo "interfaz" que se llame "controlador" con los métodos `prestar()`, `devolver()` y `prestado()` o funciones propias para controlar esto.

2. Se pretende realizar una aplicación para esta facultad que gestione la información sobre las personas que vinculadas con la misma bajo las siguientes condiciones:
    * Existirá una clasificación que puede ser en tres tipos: estudiantes, profesores y administrativos.
    * Por cada persona se debe conocer, al menos, su nombre y apellidos, además de su número de identificación.
    * Con respecto a los empleados, sean del tipo que sean, hay que saber su año de incorporación a la facultad y qué número de anexo tienen asignado.
    * En cuando a los estudiantes, se requiere almacenar el curso en le que están matriculados.
    * Por lo que se refiere a los profesores, es necesario gestionar a qué departamento pertenecen (Bioinformática, Computación, etc.).
    * Sobre el administrativo, hay que conocer a qué sección está asignado (biblioteca, decanato, secretaría).

    El  ejercicio consiste, en primer lugar, definir el tipo de herencia y luego programar las clases definidas. Para cada una de las clases, crear sus constructores con o sin parámetros necesarios, definir atributos y métodos correspondientes a cada una de las clases.

    La finalidad es encontrar a una persona y dónde está ubicada dentro de la facultad.