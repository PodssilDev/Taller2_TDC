# Taller 2 - Teoría de la Computación 2022-1 
**Autores:** 
* [Matías Figueroa](https://github.com/MatiasFigueroaContreras)
* [Daniel Frez](https://github.com/DanielFrez)
* [Javier Sanhueza](https://github.com/Truncus12)
* [John Serrano](https://github.com/PodssilDev)

## Descripción
Este es el repositorio del **Taller 2 de Teoría de la Computación 2022-1**, donde se utiliza la Lógica Difusa para recomendar canciones y géneros musicales, a traves de un programa creado en Python 3.

## Prerrequisitos
Se necesita de:
* [Python 3](https://www.python.org/downloads/)
* [Numpy](https://pypi.org/project/numpy/)
```sh
pip install numpy
```
* [Matplotlib](https://pypi.org/project/matplotlib/)
```sh
pip install matplotlib
```
* [Scikit-Fuzzy](https://pypi.org/project/scikit-fuzzy/)
```sh
pip install scikit-fuzzy
```
* [Tkinter](https://docs.python.org/es/3/library/tkinter.html)
* [Custom Tkinter](https://github.com/TomSchimansky/CustomTkinter)
```sh
pip install customtkinter
```
## Instrucciones de Uso:
1. Se debe tener la carpeta src del código, donde dentro de ella se encuentra el archivo [taller2.py](https://github.com/PodssilDev/Taller2_TDC/blob/main/src/taller2.py). Para ello se recomienda clonar el repositorio directamente:
```sh
git clone https://github.com/PodssilDev/Taller2_TDC.git
```
2. Ejecutar el archivo "taller2.py". Si todas las extensiones fueron instaladas correctamente entonces se abrirá la 
interfaz gáfica
3. El siguiente paso es colocar los valores preferidos para la cantidad de integrantes, intensidad y ritmo.
* Si lo desea, el usuario puede visualizar las distintas gráficas de escalas presionando los botones
correspondientes. Note que si abre una ventana de gráfico, deberá cerrarla para abrir otra ventana de gráfico.
* Además de los valores, el usuario debe escoger si desea poder visualizar todos los gráficos de resultados
generados.
4. Con los valores ya colocados, al presionar el boton "Buscar Canciones", la interfaz gráfica pasará los datos
ingresados al programa. El programa mostrará, mediante la interfaz, el género preferido junto con las 
canciones recomendadas del género. 
* Notar que la cantidad de integrantes deben ser valores enteros de 1 al 9. La intensida y ritmo pueden
ser números enteros o decimales del 0 al 9. En caso de que lo anterior no se respete, el programa mostrará 
un mensaje para que el usuario pueda volver a ingresar las entradas.
5. Repetir desde el paso 3 hasta que se desee cerrar la interfaz gráfica, finalizando la ejecución 
del programa.

## Mas información
Para mas información sobre el desarrollo del programa, o los resultados obtenidos, revisar el [informe](https://github.com/PodssilDev/Taller2_TDC/blob/main/InformeFinal_Grupo3_Teoria_de_la_computacion.pdf) disponible en el repositorio.
