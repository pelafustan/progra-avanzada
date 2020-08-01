# Proyecto 2

## Molecule Viewer

Molecule Viewer es una pequeña aplicación escrita en Python para poder visualizar proteínas en formato `.pdb`, usando [PyMOL](https://www.pymol.org) en el backend para generar la imágen de la proteína.

## Prerrequisitos

Para poder hace un correcto uso del programa, ese necesario tener las siguientes librerías de Python instaladas:

* [NumPy](https://numpy.org/install/)
* [SciPy](https://www.scipy.org/scipylib/download.html)
* [Pandas](https://pandas.pydata.org/getting_started.html)
* [BioPandas](http://rasbt.github.io/biopandas/installation/)

Además de, obviamente, [Python](https://www.python.org/downloads/).

## Instalación

Basta con clonar el repositorio y moverse dentro de la carpeta del proyecto

```
git clone https://github.com/pelafustan/progra-avanzada.git
cd progra-avanzada/proyecto_2
```

Una vez dentro, ejecutar `python molecule_viewer.py` y se abrirá el programa.

## Uso

La ventana principal del programa corresponde a

<img alt="YAP" src="https://i.imgur.com/B0BSOP8.png">

donde los elementos que la componen son:

1. Botón para seleccionar el directorio de trabajo. A un costado de eso, aparece una etiqueta que indica el directorio actual de trabajo.
2. Un lista con todos los archivos `.pdb` dentro del directorio de trabajo.
3. Un extracto del encabezado del archivo `.pdb` seleccionado.
4. Una representación de la molécula seleccionada.

## Agradecimientos

* [Google](https://www.google.com/)
* [Stack Overflow](https://stackoverflow.com)
* Cafeína