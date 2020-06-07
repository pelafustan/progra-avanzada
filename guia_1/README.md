# Guía 1

1. Implemente la clase Tarjeta que permita manipular la siguiente información:
    * Nombre del titular
    * Saldo de la tarjeta
   Además, implemente un método que permita actualizar el saldo de la tarjeta producto de una compra. Considere el uso de un constructor explícito.

2. Crear una clase llamada Libro que guarde la información de cada uno de los libros de una biblioteca. La clase debe guardar el título del libro, autor, número de ejemplares del libro y número de ejemplares prestados. La clase contendrá los siguientes métodos:
    * Constructor con parámetros para la clase libro.
    * Constructor por defecto para la clase biblioteca.
    * Setter y getter para los atributos privados.

3. Natalia está muy interesada en los programas de seguridad informática, por lo que ideó un algoritmo para encriptar números. El algoritmo que creo Natalia consiste en, al ingresar un número de 4 dígitos:
    * Reemplazar cada dígito por la sumatoria de cada dígito hasta su posición, e.g.
        * para el caso 1234, (1)(1+2)(1+2+3)(1+2+3+4); el resultado sería 1360.
        * Considera la suma de 10 como 0, 11 como 1 y así sucesivamente.
    * Sumar 7 a cada uno de los dígitos, e.g. (1+7)(3+7)(6+7)(0+7).
    * Intercambiar el primer dígito con el tercero y el segundo con el cuarto.
   Finalizar el algoritmo con la impresión del número resultante.

4. Pepe salió a celebrar su santo con un grupo de amigos y decidieron ir a comer a un restaurat. Pepe y sus amigos acostumbran a pagar la cuenta por partes iguales, es decir, cada uno paga lo mismo. Sin embargo, la cuenta incluye el consumo de todos los comensales y no considera el IVA (19%) ni la propina (10%). El problema es que no saben cuánto debe pagar cada uno, por lo que usted debe entregar una solución.

5. Crear una clase llamada Perro, con los atributos y acciones que tienen los perros. Sobre las acciones, podemos imaginar que ellos ladran, juegan, comen y, si son machos, se pelean entre ellos por territorio. Desde la clase principal, deberá crea una instancia a la clase Perro (objeto) y darle vida, complementando y extendiendo los datos de los atributos y acciones ejemplificadas.

6. Escriba una clase Cuenta para representar una cuenta bancaria. Los datos de la cuenta son:
    * Nombre del cliente.
    * Número de cuenta.
    * Saldo.
    * Tipo de interés.
   La clase debe contener los siguientes métodos:
    * Constructor
    * Setter y getter para asignar y obtener los datos de la cuenta.
    * Método ingreso que aumente el saldo de la cuenta en la cantidad que se indique. Se debe validar que esa cantidad no puede ser negativa.
    * Método giro para disminuir el saldo en una cantidad, pero antes se debe comprobar que hay saldo suficiente. La cantidad no puede ser negativa.
   Como condiciones se pide que:
    * Los métodos ingreso y giro devuelvan `True` si la operación se ha realizado con éxito o `False` en caso contrario.
    * Método para transferencia, el que permite pasar dinero de una cuenta a otra siempre que en la cuenta de origen haya dinero suficiente.