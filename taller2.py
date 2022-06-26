# Taller 2 - Grupo 3
# Autores: Matias Figueroa, Daniel Frez, Javier Sanhueza y John Serrano
# Teoria de la Computacion 2022-1

# Generos escogidos: Rock, Rap, Blues, Pop
# Parametros a considerar: Integrantes de un artista, Intensidad de una cancion, Ritmo de una cancion

# BLOQUE DE DEFINICIONES
# ----------------------------------------------------------------------------
# IMPORTACION DE FUNCIONES
# ----------------------------------------------------------------------------

from cProfile import label
import skfuzzy as fuzz # Importamos Scikit-Fuzzy como fuzz
import numpy as np # Se importa numpy como np
import matplotlib.pyplot as plt # Se importa Pyplot de Matplotlib como plt
import tkinter as tk # Importamos Tkinter para la interfaz grafica
import customtkinter as ctk # Importamos CustomTkinter para la interfaz grafica
from tkinter import messagebox # Importamos messagebox de Tkinter para la interfaz

# DEFINICIONES DE FUNCIONES
#----------------------------------------------------------------------------

'''
Entrada: Una lista de canciones y tres strings correspondientes a caracteristicas de musica
Salida: Una lista de canciones que cumplen con las caracteristicas dadas
Descripcion: Funcion que obtiene las canciones que cumplen con las caracteristicas dadas, retornando
el resultado en una lista. Para ello, recibe todas las canciones de un genero junto con las caracteristicas
a buscar
'''
def obtenerCanciones(lista_canciones, caracteristica1, caracteristica2, caracteristica3):
    n = len(lista_canciones) # Largo de la lista de canciones
    lista_canciones_final = []
    i = 0
    while(i < n): # Ciclo que busca obtener canciones que cumplan todas las caracteristicas
        if(lista_canciones[i][1] == caracteristica1):
            if(lista_canciones[i][2]) == caracteristica2:
                if(lista_canciones[i][3]) == caracteristica3:
                    lista_canciones_final.append(lista_canciones[i][0])
        i = i + 1
    if(len(lista_canciones_final) != 0): # Si se encontraron opciones
        listbox.insert(tk.END, "Canciones recomendadas del genero basado en sus preferencias: ")
        for cancion in lista_canciones_final:
            listbox.insert(tk.END, cancion) # Se muestran las canciones recomendadas
        listbox.insert(tk.END, "")
        listbox.insert(tk.END, "Otras canciones del género: ")
        for cancion in lista_canciones:
            if(cancion[0] not in lista_canciones_final): 
                listbox.insert(tk.END, cancion[0]) # Se muestran las otras canciones del genero
    else:  # Si no se encontraron canciones que cumplan todas las caracteristicas
        i = 0
        while(i < n): # Ciclo que busca obtener canciones que cumplan con la primera caracteristica
            if(lista_canciones[i][1] == caracteristica1):
                lista_canciones_final.append(lista_canciones[i][0])
            i = i + 1
        if(len(lista_canciones_final) != 0): # Si se encontraron canciones
            listbox.insert(tk.END, "Canciones recomendadas del genero basado en sus preferencias: ")
            for cancion in lista_canciones_final:
                listbox.insert(tk.END, cancion) # Se muestran las canciones recomendadas
            listbox.insert(tk.END, "")
            listbox.insert(tk.END, "Otras canciones del género: ")
            for cancion in lista_canciones:
                if(cancion[0] not in lista_canciones_final):
                    listbox.insert(tk.END, cancion[0]) # Se muestran las otras canciones del genero
    if(len(lista_canciones_final) == 0): # Si aun asi no se pudieron encontrar canciones
        i = 0
        listbox.insert(tk.END, "Canciones recomendadas del género: ")
        while(i<n): # Se retornan las canciones del genero correspondiente
            listbox.insert(tk.END, lista_canciones[i][0]) # Se muestran las canciones del genero
            i = i + 1
    return lista_canciones_final 

'''
Entrada: Tres arreglos correspondientes a los rangos de los integrantes de un artista de una cancion
Salida: Un string correspondiente a la cantidad escogida
Descripcion: Funcion que busca cual es el arreglo maximo, es decir, el arreglo que coincide con la
cantidad de integrantes solicitada y retorna un string para ser utilizado al momento de filtrar canciones
'''
def obtenerCaracteristica1(int_bajo,int_medio,int_alto):
    maximo = max(int_bajo, int_medio, int_alto)
    if(maximo == int_bajo):
        return "integrantes_bajo" # Integrantes menores a 4
    elif(maximo == int_medio):
        return "integrantes_medio" # Integrantes de 4 a 6
    else:
        return "integrantes_alto" # Integrantes desde 7 en adelante

'''
Entrada: Tres arreglos correspondientes a los rangos de las intensidades de una cancion
Salida: Un string correspondiente a la cantidad escogida
Descripcion: Funcion que busca cual es el arreglo maximo, es decir, el arreglo que coincide con la
cantidad de intensidad solicitada y retorna un string para ser utilizado al momento de filtrar canciones
'''
def obtenerCaracteristica2(intensidad_baja, intensidad_media, intensidad_alta):
    maximo = max(intensidad_baja, intensidad_media, intensidad_alta)
    if(maximo == intensidad_baja):
        return "intensidad_baja" # Intensidad menor a 4
    elif(maximo == intensidad_media):
        return "intensidad_media" # Intensidades entre 4 a 6
    else:
        return "intensidad_alta" # Intensidades desde 7 en adelante

'''
Entrada: Tres arreglos correspondientes a los rangos de los ritmos de una cancion
Salida: Un string correspondiente a la cantidad escogida
Descripcion: Funcion que busca cual es el arreglo maximo, es decir, el arreglo que coincide con la
cantidad de ritmo solicitada y retorna un string para ser utilizado al momento de filtrar canciones
'''
def obtenerCaracteristica3(ritmo_bajo, ritmo_medio, ritmo_alto):
    maximo = max(ritmo_bajo, ritmo_medio, ritmo_alto)
    if(maximo == ritmo_bajo):
        return "ritmo_bajo" # Ritmo menor a 4
    elif(maximo == ritmo_medio):
        return "ritmo_medio" # Ritmo entre 4 a 6
    else:
        return "ritmo_alto" # Ritmo desde 7 en adelante

'''
Entrada: Cuatros arreglos 
Salida: No tiene salida como tal
Descripcion: Funcion que busca llenar los datos de un grafico con la informacion correspondiente
'''
def llenar_datos_grafico(grafico, datos_fill_between, datos_lineax, datos_lineay):
    # Se llenan los datos con la informacion
    grafico.fill_between(datos_fill_between[0], datos_fill_between[1], facecolor=datos_fill_between[2], alpha=0.8)
    grafico.plot(datos_lineax[0], datos_lineax[1], "k", linewidth=1.5)
    grafico.plot(datos_lineay[0], datos_lineay[1], "k", linewidth=1.2, linestyle="--")

'''
Entrada: No tiene entrada
Salida: No tiene salida como tal
Descripcion: Funcion que crea el grafico de escala de numero de integrantes y lo muestra en pantalla.
'''
def mostrarIntegrantes():
    # Se grafican los rangos de escala
    plt.plot(escala_integrantes, integrantes_bajo, 'b', linewidth=1.5, label='Bajo')
    plt.plot(escala_integrantes,integrantes_medio, 'r', linewidth=1.5, label='Medio')
    plt.plot(escala_integrantes, integrantes_alto, 'g', linewidth=1.5, label='Alto')
    plt.title("Cantidad de integrantes del artista") # Configuraciones del grafico
    plt.legend()
    # Se muestra una ventana de exito.
    messagebox.showinfo("Gráficos Generados", "Gráficos generados con éxito. Recuerden cerrar la ventana de gráficos para ver más gráficos y resultados.")
    plt.show() # Se muestra el grafico

'''
Entrada: No tiene entrada
Salida: No tiene salida como tal
Descripcion: Funcion que crea el grafico de escala de intensidades de sonido y lo muestra en pantalla.
'''
def mostrarIntensidades():
    # Se grafican los rangos de escala
    plt.plot(escala_intensidad_sonido, intensidad_sonido_baja, 'b', linewidth=1.5, label='Baja')
    plt.plot(escala_intensidad_sonido, intensidad_sonido_media, 'r', linewidth=1.5, label='Media')
    plt.plot(escala_intensidad_sonido, intensidad_sonido_alta, 'g', linewidth=1.5, label='Alta')
    plt.title("Intensidad de sonido de una canción") # Configuraciones del grafico
    plt.legend()
    # Se muestra una ventana de exito
    messagebox.showinfo("Gráficos Generados", "Gráficos generados con éxito. Recuerden cerrar la ventana de gráficos para ver más gráficos y resultados.")
    plt.show() # Se muestra el grafico

'''
Entrada: No tiene entrada
Salida: No tiene salida como tal
Descripcion: Funcion que crea el grafico de escala de ritmos y lo muestra por pantalla
'''
def mostrarRitmo():
    # Se grafican los rangos de escala
    plt.plot(escala_ritmos, ritmo_bajo, 'b', linewidth=1.5, label='Bajo')
    plt.plot(escala_ritmos, ritmo_medio, 'r', linewidth=1.5, label='Medio')
    plt.plot(escala_ritmos, ritmo_alto, 'g', linewidth=1.5, label='Alto')
    plt.title("Ritmo de una canción") # Configuraciones del grafico
    plt.legend()
    # Se muestra una ventana de exito
    messagebox.showinfo("Gráficos Generados", "Gráficos generados con éxito. Recuerden cerrar la ventana de gráficos para ver más gráficos y resultados.")
    plt.show() # Se muestra el grafico

'''
Entrada: No tiene entrada
Salida: No tiene salida como tal
Descripcion: Funcion que crea el grafico de escala de generos y lo muestra por pantalla
'''
def mostrarGeneros():
    # Se grafican los rangos de escala
    plt.plot(escala_genero, genero_rock, 'b', linewidth=1.5, label='Rock')
    plt.plot(escala_genero, genero_rap, 'r', linewidth=1.5, label='Rap')
    plt.plot(escala_genero, genero_blues, 'g', linewidth=1.5, label='Blues')
    plt.plot(escala_genero, genero_pop, 'y', linewidth=1.5, label='Pop')
    plt.title('Generos escogidos') # Coniguraciones del grafico
    plt.legend()
    # Se muestra una ventana de exito
    messagebox.showinfo("Graficos Generados", "Gráficos generados con éxito. Recuerden cerrar la ventana de gráficos para ver más gráficos y resultados.")
    plt.show() # Se muestra el grafico

'''
Entrada: No tiene entrada como tal (Recibe informacion por la interfaz grafica)
Salida: No tiene salida como tal (Muestra la informacion por la interfaz grafica)
Descripcion: Funcion maestra que recibe la informacion proporcionada a traves de la interfaz grafica y la procesa para
realizar el proceso de logica difusa, para asi obtener el genero y canciones recomendadas. Tambien muestra los 
graficos correspondientes si asi se desea.
'''
def main_interfaz():
    listbox.delete(0,tk.END) # Se limpia el listbox cada vez que se buscan nuevos resultados
    cantidad_integrantes = entry1.get() # Se obtiene la cantidad de integrantes escogida
    intensidad_sonido = entry2.get() # Se obtiene la intensidad de sonido escogida
    ritmo = entry3.get() # Se obtiene el ritmo escogido
    eleccion = optionmenu_var.get() # Se obtiene la eleccion para mostrar los graficos
    # Verificaciones
    try: # La cantidad de integrantes debe ser un entero entre 1 y 10
        cantidad_integrantes = int(cantidad_integrantes)
        if(cantidad_integrantes <= 0 or cantidad_integrantes >= 10):
            messagebox.showinfo("Error", "La cantidad de integrantes debe ser un número entero entre 1 y 9!")
            return
    except ValueError:
        # Si no es un entero , o esta fuera del rango, se muestra un error
        messagebox.showinfo("Error", "La cantidad de integrantes debe ser un número entero entre 1 y 9!")
        return
    try:
        # La intensidad de sonido debe ser un entero o decimal entre 0 y 10
        intensidad_sonido = float(intensidad_sonido)
        if (intensidad_sonido < 0 or intensidad_sonido >= 10):
            messagebox.showinfo("Error", "La intensidad de sonido debe ser un número entre 0 y 9!")
            return
    except ValueError:
        # Si no es un entero o decimal, o esta fuera del rango, se muestra un error
        messagebox.showinfo("Error", "La intensidad de sonido debe ser un número entero o decimal entre 0 y 9!")
        return
    try:
        # El ritmo debe ser un entero o decimal entre 0 y 10
        ritmo = float(ritmo)
        if (ritmo < 0 or ritmo >= 10):
            messagebox.showinfo("Error", "El ritmo debe ser un número entre 0 y 9!")
            return
    except ValueError:
        # Si no es un entero o decimal, o esta fuera del rango, se muestra un error
        messagebox.showinfo("Error", "El ritmo debe ser un número entero o decimal entre 0 y 9!")
        return
    
    # Si todas las verificaciones pasaron, se procede a realizar el proceso de logica difusa

    #  Funciones de pertencia
    # Funciones de pertenencia de la cantidad de integrantes
    cantidad_integrantes_baja = fuzz.interp_membership(escala_integrantes, integrantes_bajo, cantidad_integrantes)
    cantidad_integrantes_medio = fuzz.interp_membership(escala_integrantes, integrantes_medio, cantidad_integrantes)
    cantidad_integrantes_alto = fuzz.interp_membership(escala_integrantes, integrantes_alto, cantidad_integrantes)
    
    # Se obtiene el numero de integrantes preferido para filtrar las canciones
    caracteristica1 = obtenerCaracteristica1(cantidad_integrantes_baja, cantidad_integrantes_medio, cantidad_integrantes_alto)
    
    # Funciones de pertenencia de la intensidad de sonido
    cantidad_intensidad_sonido_baja = fuzz.interp_membership(escala_intensidad_sonido, intensidad_sonido_baja, intensidad_sonido)
    cantidad_intensidad_sonido_media = fuzz.interp_membership(escala_intensidad_sonido, intensidad_sonido_media, intensidad_sonido)
    cantidad_intensidad_sonido_alta = fuzz.interp_membership(escala_intensidad_sonido, intensidad_sonido_alta, intensidad_sonido)
    
    # Se obtiene la intensidad de sonido preferida para filtrar las canciones
    caracteristica2 = obtenerCaracteristica2(cantidad_intensidad_sonido_baja, cantidad_intensidad_sonido_media, cantidad_intensidad_sonido_alta)
    
    # Funciones de pertenencia del ritmo
    cantidad_ritmo_bajo = fuzz.interp_membership(escala_ritmos, ritmo_bajo, ritmo)
    cantidad_ritmo_medio = fuzz.interp_membership(escala_ritmos, ritmo_medio, ritmo)
    cantidad_ritmo_alto = fuzz.interp_membership(escala_ritmos, ritmo_alto, ritmo)
    
    # Se obtiene el ritmo preferido para filtrar las canciones
    caracteristica3 = obtenerCaracteristica3(cantidad_ritmo_bajo, cantidad_ritmo_medio, cantidad_ritmo_alto)

    #  En este punto se utiliza la inferencia de MAMDANI para crear las reglas a utilizar
     
    # Regla 1
    # Si la cantidad de integrantes es bajo, con intensidad de sonido fuerte y ritmo medio, ENTONCES el genero es rap
    regla_1 = np.fmin(np.fmin(cantidad_integrantes_baja, cantidad_intensidad_sonido_alta), cantidad_ritmo_medio)
    
    # Regla 2
    # Si la cantidad de integrantes es medio, con intensidad de sonido fuerte y ritmo bajo, ENTONCES el genero es rock
    regla_2 = np.fmin(np.fmin(cantidad_integrantes_medio, cantidad_intensidad_sonido_alta), cantidad_ritmo_bajo)
    
    # Regla 3
    # Si la cantidad de integrantes es media o la intensidad de sonido es baja y el ritmo es medio, ENTONCES el genero es blues
    regla_3 = np.fmin(np.fmax(cantidad_integrantes_medio, cantidad_intensidad_sonido_baja), cantidad_ritmo_medio)
    
    # Regla 4
    # Si la cantidad de integrantes es alto o con intensidad de sonido baja y ritmo alto, ENTONCES el genero es pop
    regla_4 = np.fmin(np.fmax(cantidad_integrantes_alto, cantidad_intensidad_sonido_baja), cantidad_ritmo_alto)
    
    # Regla 5
    # Si la cantidad de integrantes es baja, con intensidad de sonido media y ritmo alto, ENTONCES el genero es pop
    regla_5 = np.fmin(np.fmin(cantidad_integrantes_baja, cantidad_intensidad_sonido_media), cantidad_ritmo_alto)
    
    # Regla 6
    # Si la cantidad de integrantes es alto, con intensidad de sonido alta y ritmo bajo, ENTONCES el genero es rock
    regla_6 = np.fmin(np.fmin(cantidad_integrantes_alto, cantidad_intensidad_sonido_alta), cantidad_ritmo_bajo)
    
    # Regla 7
    # Si la cantidad de integrantes baja, con intensidad de sonido media y ritmo bajo, ENTONCES el genero es rap
    regla_7 = np.fmin(np.fmin(cantidad_integrantes_baja, cantidad_intensidad_sonido_media), cantidad_ritmo_bajo)
    
    # Regla 8 
    # Si la cantidad de integrantes es baja o,  intensidad de sonido media y ritmo medio, ENTONCES el genero es blues
    regla_8 = np.fmax(cantidad_integrantes_baja, np.fmin(cantidad_intensidad_sonido_media, cantidad_ritmo_medio))
    
    # Regla 9
    # Si la cantidad de integrantes es baja, con intensidad de sonido media y ritmo bajo, ENTONCES el genero es blues
    regla_9 = np.fmin(np.fmin(cantidad_integrantes_baja, cantidad_intensidad_sonido_baja), cantidad_ritmo_bajo)
    
    # Regla 10
    # Si la cantidad de integrantes es medio, intensidad de sonido alto y ritmo alto, ENTONCES el genero es rap
    regla_10 = np.fmin(np.fmin(cantidad_integrantes_medio, cantidad_intensidad_sonido_alta), cantidad_ritmo_alto)
    
    # Regla 11
    # Si la cantidad de integrantes es alto, con intensidad de sonido alta y ritmo medio, ENTONCES el genero es rock
    regla_11 = np.fmin(np.fmin(cantidad_integrantes_alto, cantidad_intensidad_sonido_alta), cantidad_ritmo_medio)
    
    # Regla 12
    # Si la cantidad de integrantes es alta, con intensidad de sonido media y ritmo bajo, ENTONCES el genero es rock
    regla_12 = np.fmin(np.fmin(cantidad_integrantes_alto, cantidad_intensidad_sonido_media), cantidad_ritmo_bajo)
    
    # Regla 13
    # Si la cantidad de integrantes es baja, con intensidad de sonido alta y ritmo alto, ENTONCES el genero es pop
    regla_13 = np.fmin(np.fmin(cantidad_integrantes_baja, cantidad_intensidad_sonido_alta), cantidad_ritmo_alto)
    
    # Regla 14
    # Si la cantidad de integrantes es media, con intensidad de sonido media y ritmo bajo, ENTONCES el genero es pop
    regla_14 = np.fmin(np.fmin(cantidad_integrantes_medio, cantidad_intensidad_sonido_media), cantidad_ritmo_bajo)
    # Regla 15
    # Si la cantidad de integrantes es media o, la intesidad de sonido es baja y el ritmo es bajo, ENTONCES el genero es blues
    regla_15 = np.fmax(cantidad_integrantes_medio, np.fmin(cantidad_intensidad_sonido_baja, cantidad_ritmo_bajo))
    
    # Activacion de cada regla
    # Reglas correspondientes al genero Rock
    regla_rock1 = np.fmin(regla_2, genero_rock)
    regla_rock2 = np.fmin(regla_6, genero_rock)
    regla_rock3 = np.fmin(regla_11, genero_rock)
    regla_rock4 = np.fmin(regla_12, genero_rock)
    
    # Reglas correspondientes al genero Pop
    regla_pop1 = np.fmin(regla_4, genero_pop)
    regla_pop2 = np.fmin(regla_5, genero_pop)
    regla_pop3 = np.fmin(regla_13, genero_pop)
    regla_pop4 = np.fmin(regla_14, genero_pop)
    
    # Reglas correspondientes al genero Blues
    regla_blues1 = np.fmin(regla_3, genero_blues)
    regla_blues2 = np.fmin(regla_8, genero_blues)
    regla_blues3 = np.fmin(regla_9, genero_blues)
    regla_blues4 = np.fmin(regla_15, genero_blues)
    
    # Reglas correspondientes al genero Rap
    regla_rap1 = np.fmin(regla_1, genero_rap)
    regla_rap2 = np.fmin(regla_7, genero_rap)
    regla_rap3 = np.fmin(regla_10, genero_rap)
    
    # Se aplica Agregacion, para luego poder utilizar esto para la desfuzzificacion
    agregacion1 = np.fmax(regla_rock1, regla_pop1)
    agregacion2 = np.fmax(agregacion1, regla_rap1)
    agregacion3 = np.fmax(agregacion2, regla_blues1)
    agregacion4 = np.fmax(agregacion3, regla_rock2)
    agregacion5 = np.fmax(agregacion4, regla_pop2)
    agregacion6 = np.fmax(agregacion5, regla_rap2)
    agregacion7 = np.fmax(agregacion6, regla_blues2)
    agregacion8 = np.fmax(agregacion7, regla_blues3)
    agregacion9 = np.fmax(agregacion8, regla_rap3)
    agregacion10 = np.fmax(agregacion9, regla_rock3)
    agregacion11 = np.fmax(agregacion10, regla_rock4)
    agregacion12 = np.fmax(agregacion11 , regla_pop3)
    agregacion13= np.fmax(agregacion12, regla_pop4)
    agregacionFinal = np.fmax(agregacion13, regla_blues4)   

    # Se obtiene el valor desfuzzificado, utilizando el metodo BOA
    desfuzzificacion = fuzz.defuzz(escala_genero, agregacionFinal, 'bisector')
    # print(desfuzzificacion)
    
    # Se crean las funciones de pertenencia de los generos, para asi identificar cual es el genero preferido
    rock = fuzz.interp_membership(escala_genero, genero_rock, desfuzzificacion)
    rap = fuzz.interp_membership(escala_genero, genero_rap, desfuzzificacion)
    pop = fuzz.interp_membership(escala_genero, genero_pop, desfuzzificacion)
    blues = fuzz.interp_membership(escala_genero, genero_blues, desfuzzificacion)
    
    # Se obtiene el genero preferido
    resultado = max(rock, rap, pop, blues)

    listbox.insert(tk.END, "Resultados: ") # Se inserta un texto para escribir los resultados en la listbox
    if resultado == rock:
        listbox.insert(tk.END, "El genero preferido es: Rock")
        listbox.insert(tk.END, "") # Se agrega una linea al listbox
        lista_canciones = canciones_rock  # Se asignan las canciones de Rock
    elif resultado == pop:
        listbox.insert(tk.END, "El genero preferido es: Pop")
        listbox.insert(tk.END, "") # Se agrega una linea al listbox
        lista_canciones = canciones_pop # Se asignan las canciones de Pop
    elif resultado == rap:
        listbox.insert(tk.END, "El genero preferido es: Rap")
        listbox.insert(tk.END, "") # Se agrega una linea al listbox
        lista_canciones = canciones_rap # Se asignan las canciones de Rap
    elif resultado == blues:
        listbox.insert(tk.END, "El genero preferido es: Blues\n")
        listbox.insert(tk.END, "") # Se agrega una linea al listbox
        lista_canciones = canciones_blues # Se asignan las canciones de Blues
    
    # Se obtiene la lista de canciones, filtrando por caracteristicas.
    # En la funcion obtenerCanciones se seleccionan las canciones que cumplan con las caracteristicas
    # y se muestran en la interfaz grafica
    lista_canciones_final = obtenerCanciones(lista_canciones, caracteristica1, caracteristica2, caracteristica3)
    
    # Si el usuario decide que quiere ver los graficos, se generan y se muestran
    if(eleccion == "Si"):
        # Graficos        
        # Graficos para numero de integrantes
        # Integrantes Bajo
        integrantes_bajo_grafico_fill_between = [escala_integrantes, integrantes_bajo, 'teal', 'Bajo']
        integrantes_bajo_grafico_lineax = [[cantidad_integrantes, cantidad_integrantes], [0, cantidad_integrantes_baja]]
        integrantes_bajo_grafico_lineay = [[0, 10], [cantidad_integrantes_baja, cantidad_integrantes_baja]]
        
        # Integrantes Medio
        integrantes_medio_grafico_fill_between = [escala_integrantes, integrantes_medio, 'orangered', 'Medio']
        integrantes_medio_grafico_lineax = [[cantidad_integrantes, cantidad_integrantes], [0, cantidad_integrantes_medio]]
        integrantes_medio_grafico_lineay = [[0, 10], [cantidad_integrantes_medio, cantidad_integrantes_medio]]
        
        # Integrantes Alto
        integrantes_alto_grafico_fill_between = [escala_integrantes, integrantes_alto, 'mediumpurple', 'Alto']
        integrantes_alto_grafico_lineax = [[cantidad_integrantes, cantidad_integrantes], [0, cantidad_integrantes_alto]]
        integrantes_alto_grafico_lineay = [[0, 10], [cantidad_integrantes_alto, cantidad_integrantes_alto]]
        
        # Grafico para Intensidad del sonido
        # Intensidad del sonido baja
        intensidad_sonido_baja_grafico_fill_between = [escala_intensidad_sonido, intensidad_sonido_baja, 'teal', 'Baja']
        intensidad_sonido_baja_grafico_lineax = [[intensidad_sonido, intensidad_sonido], [0, cantidad_intensidad_sonido_baja]]
        intensidad_sonido_baja_grafico_lineay = [[0, 10], [cantidad_intensidad_sonido_baja, cantidad_intensidad_sonido_baja]]
        
        # Intensidad del sonido media
        intensidad_sonido_media_grafico_fill_between = [escala_intensidad_sonido, intensidad_sonido_media, 'orangered', 'Medio']
        intensidad_sonido_media_grafico_lineax = [[intensidad_sonido, intensidad_sonido], [0, cantidad_intensidad_sonido_media]]
        intensidad_sonido_media_grafico_lineay = [[0, 10], [cantidad_intensidad_sonido_media, cantidad_intensidad_sonido_media]]
        
        # Intensidad del sonido alta
        intensidad_sonido_alta_grafico_fill_between = [escala_intensidad_sonido, intensidad_sonido_alta, 'mediumpurple', 'Alto']
        intensidad_sonido_alta_grafico_lineax = [[intensidad_sonido, intensidad_sonido], [0, cantidad_intensidad_sonido_alta]]
        intensidad_sonido_alta_grafico_lineay = [[0, 10], [cantidad_intensidad_sonido_alta, cantidad_intensidad_sonido_alta]]
        
        # Graficos ritmo
        # Ritmo bajo
        ritmo_bajo_grafico_fill_between = [escala_ritmos, ritmo_bajo, 'teal', 'Baja']
        ritmo_bajo_grafico_lineax = [[ritmo, ritmo], [0, cantidad_ritmo_bajo]]
        ritmo_bajo_grafico_lineay = [[0, 10], [cantidad_ritmo_bajo, cantidad_ritmo_bajo]]
        
        # Ritmo medio
        ritmo_medio_grafico_fill_between = [escala_ritmos, ritmo_medio, 'orangered', 'Medio']
        ritmo_medio_grafico_lineax = [[ritmo, ritmo], [0, cantidad_ritmo_medio]]
        ritmo_medio_grafico_lineay = [[0, 10], [cantidad_ritmo_medio, cantidad_ritmo_medio]]
        
        # Ritmo alto
        ritmo_alto_grafico_fill_between = [escala_ritmos, ritmo_alto, 'mediumpurple', 'Alto']
        ritmo_alto_grafico_lineax = [[ritmo, ritmo], [0, cantidad_ritmo_alto]]
        ritmo_alto_grafico_lineay = [[0, 10], [cantidad_ritmo_alto, cantidad_ritmo_alto]]
        
        # De esta forma se puede graficar todo en una sola figura
        fig, (regla1_graficos, regla2_graficos, regla3_graficos, regla4_graficos, regla5_graficos, regla6_graficos, regla7_graficos, regla8_graficos, regla9_graficos, regla10_graficos, regla11_graficos, regla12_graficos, regla13_graficos, regla14_graficos, regla15_graficos, graficoFinal) = plt.subplots(16, 4, sharex=True, sharey=True)

        #Configuracion de la ventana
        fig.subplots_adjust(top=0.95, bottom=0.025)

        #Colores genero Rock, Rap, Blues, Pop
        #Rock
        color_rock = "mediumblue"
        color_rap = "forestgreen"
        color_blues = "chocolate"
        color_pop = "mediumvioletred"
        
        #Titulos
        regla1_graficos[0].set_title("Numero de Integrantes")
        regla1_graficos[1].set_title("Intensidad del sonido")
        regla1_graficos[2].set_title("Ritmo de la cancion")
        regla1_graficos[3].set_title("Genero")
         
        # Regla 1
        llenar_datos_grafico(regla1_graficos[0], integrantes_bajo_grafico_fill_between, integrantes_bajo_grafico_lineax, integrantes_bajo_grafico_lineay)
        llenar_datos_grafico(regla1_graficos[1], intensidad_sonido_alta_grafico_fill_between, intensidad_sonido_alta_grafico_lineax, intensidad_sonido_alta_grafico_lineay)
        llenar_datos_grafico(regla1_graficos[2], ritmo_medio_grafico_fill_between, ritmo_medio_grafico_lineax, ritmo_medio_grafico_lineay)
        regla1_graficos[3].fill_between(escala_genero, regla_rap1, facecolor=color_rap, alpha=0.7)
        regla1_graficos[3].plot(escala_genero, genero_rap, color_rap, linewidth=1, linestyle="--")
        
        # Regla 2
        llenar_datos_grafico(regla2_graficos[0], integrantes_medio_grafico_fill_between, integrantes_medio_grafico_lineax, integrantes_medio_grafico_lineay)
        llenar_datos_grafico(regla2_graficos[1], intensidad_sonido_alta_grafico_fill_between, intensidad_sonido_alta_grafico_lineax, intensidad_sonido_alta_grafico_lineay)
        llenar_datos_grafico(regla2_graficos[2], ritmo_bajo_grafico_fill_between, ritmo_bajo_grafico_lineax, ritmo_bajo_grafico_lineay)
        regla2_graficos[3].fill_between(escala_genero, regla_rock1, facecolor=color_rock, alpha=0.7)
        regla2_graficos[3].plot(escala_genero, genero_rock, color_rock, linewidth=1, linestyle="--")
        
        # Regla 3
        llenar_datos_grafico(regla3_graficos[0], integrantes_medio_grafico_fill_between, integrantes_medio_grafico_lineax, integrantes_medio_grafico_lineay)
        llenar_datos_grafico(regla3_graficos[1], intensidad_sonido_baja_grafico_fill_between, intensidad_sonido_baja_grafico_lineax, intensidad_sonido_baja_grafico_lineay)
        llenar_datos_grafico(regla3_graficos[2], ritmo_medio_grafico_fill_between, ritmo_medio_grafico_lineax, ritmo_medio_grafico_lineay)
        regla3_graficos[3].fill_between(escala_genero, regla_blues1, facecolor=color_blues, alpha=0.7)
        regla3_graficos[3].plot(escala_genero, genero_blues, color_blues, linewidth=1, linestyle="--")
        
        # Regla 4
        llenar_datos_grafico(regla4_graficos[0], integrantes_alto_grafico_fill_between, integrantes_alto_grafico_lineax, integrantes_alto_grafico_lineay)
        llenar_datos_grafico(regla4_graficos[1], intensidad_sonido_baja_grafico_fill_between, intensidad_sonido_baja_grafico_lineax, intensidad_sonido_baja_grafico_lineay)
        llenar_datos_grafico(regla4_graficos[2], ritmo_alto_grafico_fill_between, ritmo_alto_grafico_lineax, ritmo_alto_grafico_lineay)
        regla4_graficos[3].fill_between(escala_genero, regla_pop1, facecolor=color_pop, alpha=0.7)
        regla4_graficos[3].plot(escala_genero, genero_pop, color_pop, linewidth=1, linestyle="--")
        
        # Regla 5
        llenar_datos_grafico(regla5_graficos[0], integrantes_bajo_grafico_fill_between, integrantes_bajo_grafico_lineax, integrantes_bajo_grafico_lineay)
        llenar_datos_grafico(regla5_graficos[1], intensidad_sonido_media_grafico_fill_between, intensidad_sonido_media_grafico_lineax, intensidad_sonido_media_grafico_lineay)
        llenar_datos_grafico(regla5_graficos[2], ritmo_alto_grafico_fill_between, ritmo_alto_grafico_lineax, ritmo_alto_grafico_lineay)
        regla5_graficos[3].fill_between(escala_genero, regla_pop2, facecolor=color_pop, alpha=0.7)
        regla5_graficos[3].plot(escala_genero, genero_pop, color_pop, linewidth=1, linestyle="--")
        
        # Regla 6
        llenar_datos_grafico(regla6_graficos[0], integrantes_alto_grafico_fill_between, integrantes_alto_grafico_lineax, integrantes_alto_grafico_lineay)
        llenar_datos_grafico(regla6_graficos[1], intensidad_sonido_alta_grafico_fill_between, intensidad_sonido_alta_grafico_lineax, intensidad_sonido_alta_grafico_lineay)
        llenar_datos_grafico(regla6_graficos[2], ritmo_bajo_grafico_fill_between, ritmo_bajo_grafico_lineax, ritmo_bajo_grafico_lineay)
        regla6_graficos[3].fill_between(escala_genero, regla_rock2, facecolor=color_rock, alpha=0.7)
        regla6_graficos[3].plot(escala_genero, genero_rock, color_rock, linewidth=1, linestyle="--")
        
        # Regla 7
        llenar_datos_grafico(regla7_graficos[0], integrantes_bajo_grafico_fill_between, integrantes_bajo_grafico_lineax, integrantes_bajo_grafico_lineay)
        llenar_datos_grafico(regla7_graficos[1], intensidad_sonido_media_grafico_fill_between, intensidad_sonido_media_grafico_lineax, intensidad_sonido_media_grafico_lineay)
        llenar_datos_grafico(regla7_graficos[2], ritmo_bajo_grafico_fill_between, ritmo_bajo_grafico_lineax, ritmo_bajo_grafico_lineay)
        regla7_graficos[3].fill_between(escala_genero, regla_rap2, facecolor=color_rap, alpha=0.7)
        regla7_graficos[3].plot(escala_genero, genero_rap, color_rap, linewidth=1, linestyle="--")
        
        # Regla 8
        llenar_datos_grafico(regla8_graficos[0], integrantes_bajo_grafico_fill_between, integrantes_bajo_grafico_lineax, integrantes_bajo_grafico_lineay)
        llenar_datos_grafico(regla8_graficos[1], intensidad_sonido_media_grafico_fill_between, intensidad_sonido_media_grafico_lineax, intensidad_sonido_media_grafico_lineay)
        llenar_datos_grafico(regla8_graficos[2], ritmo_medio_grafico_fill_between, ritmo_medio_grafico_lineax, ritmo_medio_grafico_lineay)
        regla8_graficos[3].fill_between(escala_genero, regla_blues2, facecolor=color_blues, alpha=0.7)
        regla8_graficos[3].plot(escala_genero, genero_blues, color_blues, linewidth=1, linestyle="--")
        
        # Regla 9
        llenar_datos_grafico(regla9_graficos[0], integrantes_bajo_grafico_fill_between, integrantes_bajo_grafico_lineax, integrantes_bajo_grafico_lineay)
        llenar_datos_grafico(regla9_graficos[1], intensidad_sonido_media_grafico_fill_between, intensidad_sonido_media_grafico_lineax, intensidad_sonido_media_grafico_lineay)
        llenar_datos_grafico(regla9_graficos[2], ritmo_bajo_grafico_fill_between, ritmo_bajo_grafico_lineax, ritmo_bajo_grafico_lineay)
        regla9_graficos[3].fill_between(escala_genero, regla_blues3, facecolor=color_blues, alpha=0.7)
        regla9_graficos[3].plot(escala_genero, genero_blues, color_blues, linewidth=1, linestyle="--")
        
        # Regla 10
        llenar_datos_grafico(regla10_graficos[0], integrantes_medio_grafico_fill_between, integrantes_medio_grafico_lineax, integrantes_medio_grafico_lineay)
        llenar_datos_grafico(regla10_graficos[1], intensidad_sonido_alta_grafico_fill_between, intensidad_sonido_alta_grafico_lineax, intensidad_sonido_alta_grafico_lineay)
        llenar_datos_grafico(regla10_graficos[2], ritmo_alto_grafico_fill_between, ritmo_alto_grafico_lineax, ritmo_alto_grafico_lineay)
        regla10_graficos[3].fill_between(escala_genero, regla_rap3, facecolor=color_rap, alpha=0.7)
        regla10_graficos[3].plot(escala_genero, genero_rap, color_rap, linewidth=1, linestyle="--")
        
        # Regla 11
        llenar_datos_grafico(regla11_graficos[0], integrantes_medio_grafico_fill_between, integrantes_medio_grafico_lineax, integrantes_medio_grafico_lineay)
        llenar_datos_grafico(regla11_graficos[1], intensidad_sonido_alta_grafico_fill_between, intensidad_sonido_alta_grafico_lineax, intensidad_sonido_alta_grafico_lineay)
        llenar_datos_grafico(regla11_graficos[2], ritmo_medio_grafico_fill_between, ritmo_medio_grafico_lineax, ritmo_medio_grafico_lineay)
        regla11_graficos[3].fill_between(escala_genero, regla_rock3, facecolor="b", alpha=0.7)
        regla11_graficos[3].plot(escala_genero, genero_rock, "b", linewidth=1, linestyle="--")
        
        # Regla 12
        llenar_datos_grafico(regla12_graficos[0], integrantes_alto_grafico_fill_between, integrantes_alto_grafico_lineax, integrantes_alto_grafico_lineay)
        llenar_datos_grafico(regla12_graficos[1], intensidad_sonido_media_grafico_fill_between, intensidad_sonido_media_grafico_lineax, intensidad_sonido_media_grafico_lineay)
        llenar_datos_grafico(regla12_graficos[2], ritmo_bajo_grafico_fill_between, ritmo_bajo_grafico_lineax, ritmo_bajo_grafico_lineay)
        regla12_graficos[3].fill_between(escala_genero, regla_rock4, facecolor=color_rock, alpha=0.7)
        regla12_graficos[3].plot(escala_genero, genero_rock, color_rock, linewidth=1, linestyle="--")
        
        # Regla 13
        llenar_datos_grafico(regla13_graficos[0], integrantes_bajo_grafico_fill_between, integrantes_bajo_grafico_lineax, integrantes_bajo_grafico_lineay)
        llenar_datos_grafico(regla13_graficos[1], intensidad_sonido_alta_grafico_fill_between, intensidad_sonido_alta_grafico_lineax, intensidad_sonido_alta_grafico_lineay)
        llenar_datos_grafico(regla13_graficos[2], ritmo_alto_grafico_fill_between, ritmo_alto_grafico_lineax, ritmo_alto_grafico_lineay)
        regla13_graficos[3].fill_between(escala_genero, regla_pop3, facecolor=color_pop, alpha=0.7)
        regla13_graficos[3].plot(escala_genero, genero_pop, color_pop, linewidth=1, linestyle="--")
        
        # Regla 14
        llenar_datos_grafico(regla14_graficos[0], integrantes_medio_grafico_fill_between, integrantes_medio_grafico_lineax, integrantes_medio_grafico_lineay)
        llenar_datos_grafico(regla14_graficos[1], intensidad_sonido_media_grafico_fill_between, intensidad_sonido_media_grafico_lineax, intensidad_sonido_media_grafico_lineay)
        llenar_datos_grafico(regla14_graficos[2], ritmo_bajo_grafico_fill_between, ritmo_bajo_grafico_lineax, ritmo_bajo_grafico_lineay)
        regla14_graficos[3].fill_between(escala_genero, regla_pop4, facecolor=color_pop, alpha=0.7)
        regla14_graficos[3].plot(escala_genero, genero_pop, color_pop, linewidth=1, linestyle="--")
        # Regla 15
        llenar_datos_grafico(regla15_graficos[0], integrantes_medio_grafico_fill_between, integrantes_medio_grafico_lineax, integrantes_medio_grafico_lineay)
        llenar_datos_grafico(regla15_graficos[1], intensidad_sonido_baja_grafico_fill_between, intensidad_sonido_baja_grafico_lineax, intensidad_sonido_baja_grafico_lineay)
        llenar_datos_grafico(regla15_graficos[2], ritmo_bajo_grafico_fill_between, ritmo_bajo_grafico_lineax, ritmo_bajo_grafico_lineay)
        regla15_graficos[3].fill_between(escala_genero, regla_blues4, facecolor=color_blues, alpha=0.7)
        regla15_graficos[3].plot(escala_genero, genero_blues, color_blues, linewidth=1, linestyle="--")
        
        # Grafico final - agregacion más resultado
        #Para identificar los graficos (legends)
        graficoFinal[0].fill_between([0], [0], facecolor="teal", label="Bajo", alpha=0.8)
        graficoFinal[1].fill_between([0], [0], facecolor='orangered', label="Medio", alpha=0.8)
        graficoFinal[2].fill_between([0], [0], facecolor="mediumpurple", label="Alto", alpha=0.8)

        graficoFinal[2].plot(0, 0, color=color_rock, linestyle="--", label="Rock")
        graficoFinal[2].plot(0, 1, color=color_rap, linestyle="--", label="Rap")
        graficoFinal[2].plot(0, 1, color=color_pop, linestyle="--", label="Pop")
        graficoFinal[2].plot(0, 1, color=color_blues, linestyle="--", label="Blues")
        fig.legend(bbox_to_anchor=(0.1, 0.86))

        #Agregar numeracion en eje x par a los ultimos graficos
        for i in range(0, 3, 1):
            regla15_graficos[i].xaxis.set_tick_params(which='both', labelbottom=True)

        #Ocultar los graficos en blanco
        for g in graficoFinal:
            g.axis("off")

        graficoFinal[3].axis("on") #Mostrar el grafico final
        graficoFinal[3].fill_between(escala_genero, agregacionFinal, facecolor="g", alpha=0.6)
        graficoFinal[3].plot([desfuzzificacion, desfuzzificacion], [0, resultado], "k", linewidth=1.2)
        graficoFinal[3].plot([0], [1], linewidth=0)
    
        # Se muestran los graficos
        messagebox.showinfo("Gráficos Generados", "Gráficos generados con éxito. Recuerde cerrar la ventana de gráficos para ver más gráficos y resultados.")
        plt.show() 


# BLOQUE PRINCIPAL
#----------------------------------------------------------------------------

# Lista de canciones de POP
canciones_pop = [["Maroon 5- She will be loved", "integrantes_medio", "intensidad_media", "ritmo_medio"],
                ["Michael Jackson - Beat it", "integrantes_bajo", "intensidad_media", "ritmo_alto"], 
                ["The Weeknd - Blinding Lights", "integrantes_bajo", "intensidad_baja", "ritmo_alto"], 
                ["Hunting high and low - Take on me", "integrantes_bajo", "intensidad_media", "ritmo_alto"],
                ["The Weeknd - Hype", "integrantes_bajo","intensidad_baja", "ritmo_medio"], 
                ["The Weeknd - Starboy", "integrantes_bajo", "intensidad_baja", "ritmo_bajo"], 
                ["The Chainsmokers - Closer", "integrantes_bajo", "intensidad_baja", "ritmo_alto"],
                ["Christian Kuria - Losing You", "integrantes_alta","intensidad_baja","ritmo_alto"],
                ["Michael Jackson - Billie Jean", "integrantes_bajo", "intensidad_media", "ritmo_alto"],
                ["Frank Blunt - The Dirt Road", "integrantes_alto", "intensidad_baja", "ritmo_medio"],
                ["BTS - Butter", "integrantes_alta", "intensidad_alta","ritmo_alto"],
                ["Kairi Yagi (Vivy) - Sing My Pleasure", "integrantes_bajo", "intensidad_media", "ritmo_alto"], 
                ["Yellowcard - Way Way", "integrantes_medio", "intensidad_media", "ritmo_alto"]]

# Lista de canciones de ROCK
canciones_rock = [
                ["Billy Talent - Red Flag", "integrantes_medio", "intensidad_alta", "ritmo_bajo"],
                ["Phil Collins - In The Air Tonight", "integrantes_bajo","intensidad_media", "ritmo_medio"],
                ["Autopilot Off - Clockworks", "integrantes_medio", "intensidad_alta", "ritmo_bajo"],
                ["Caesars - Jerk It Out", "integrantes_medio", "intensidad_alta", "ritmo_medio"],
                ["Mike Oldfield - Nuclear", "integrantes_bajo", "intensidad_alta", "ritmo_bajo"],
                ["Brandon Yates - Olympus Mons", "integrantes_bajo", "intensidad_alta", "ritmo_bajo"],
                ["Nirvana - Come as you are", "integrantes_bajo", "", "ritmo_bajo"], 
                ["Wolfmother - Woman", "integrantes_medio", "intensidad_alta", "ritmo_bajo"], 
                ["Set It Off - Wolf In Sheeps Clothing","integrantes_bajo","intensidad_alta", "ritmo_medio"],
                ["The Who - Pinball Wizard","integrantes_alta","intensidad_media","ritmo_medio"],
                ["The Peggies - FootPrints", "integrantes_bajo","intensidad_media","ritmo_alto"],
                ["Sambomaster - Seishun kyousoukyoku", "integrantes_bajo", "intensidad_alta", "ritmo_bajo"],
                ]

# Lista de canciones de RAP
canciones_rap = [["KSI - Creature", "integrantes_bajo", "intensidad_media", "ritmo_alto"],
                ["XXXTENTACION - SAD!","integrantes_bajo", "intensidad_baja", "ritmo_alto"], 
                ["Drake - Started From the Bottom", "integrantes_bajo", "intensidad_baja", "ritmo_alto"],
                ["Travis Scott - Antidote", "integrantes_bajo", "intensidad_media", "ritmo_alto"],
                ["Wiz Khalifa - We Dem Boyz", "integrantes_bajo", "intensidad_media", "ritmo_alto"],
                ["Drake - God's Plan", "integrantes_bajo", "intensidad_baja", "ritmo_alto"],
                ["Coolio - Gangsta's Paradise", "integrantes_bajo", "intensidad_baja", "ritmo_alto"],
                ["Kanye West - Eazy", "integrantes_bajo", "intensidad_baja", "ritmo_bajo"],
                ["Dr. Dre - Still D.R.E.", "integrantes_bajo", "intensidad_media", "ritmo_bajo"]]

# Lista de canciones de BLUES
canciones_blues = [["John Lee Hooker - Boom Boom", "integrantes_bajo", "intensidad_media", "ritmo_medio"], 
                ["Stevie Ray Vaughan - Pride and Joy", "integrantes_bajo", "intensidad_alta", "ritmo_alto"], 
                ["The beatles - Yer Blues", "integrantes_medio", "intensidad_alta", "ritmo_bajo"], 
                ["B.B. King - The Thrill is Gone", "integrantes_bajo", "intensidad_baja", "ritmo_bajo"], 
                ["Led Zeppelin - I cant Quit You Baby", "integrantes_bajo", "intensidad_baja", "ritmo_bajo"],
                ["Metro pa Quilpue - La Blues Willis", "integrantes_bajo", "intensidad_media", "ritmo_medio"]]

# Creacion de de scalas
escala_integrantes = np.arange(1,10,1) # Escala de numero de integrantes
escala_intensidad_sonido = np.arange(0,10,0.1) # Escala de intensidad de sonido
escala_ritmos = np.arange(0,10,0.1) # Escala de ritmo
escala_genero = np.arange(0, 10, 0.1) # Escala de generos

# Creacion de los graficos
# Graficos numero de integrantes
integrantes_bajo = fuzz.trimf(escala_integrantes, [1, 1, 3]) # Triangulo: Integrantes menores a 4
integrantes_medio = fuzz.trapmf(escala_integrantes, [2,3,4,6]) # Trapecio: Integrantes de 4 a 6
integrantes_alto = fuzz.trapmf(escala_integrantes,[4,6,10,10]) # Trapecio: Integrantes desde 7 en adelante

# Graficos intensidad de sonido
intensidad_sonido_baja = fuzz.trapmf(escala_intensidad_sonido, [0,0,2,4]) # Trapecio: Intensidad menor a 4
intensidad_sonido_media = fuzz.trapmf(escala_intensidad_sonido, [3,4,6,7]) # Trapecio: Intensidad entre 4 a 6
intensidad_sonido_alta = fuzz.trapmf(escala_intensidad_sonido, [6,7,10,10]) # Trapecio: Intensidad desde 7 en adelante

# Graficos ritmo
ritmo_bajo = fuzz.trapmf(escala_ritmos, [0,0,2,4]) # Trapecio: Ritmo menor a 4
ritmo_medio = fuzz.trapmf(escala_ritmos, [3,4,6,7])  # Trapecio: Ritmo entre 4 a 6
ritmo_alto = fuzz.trapmf(escala_ritmos, [6,7,10,10]) # Trapecio: Ritmo desde 7 en adelante

# Graficos genero
genero_rock = fuzz.trapmf(escala_genero, [0,0,2,3]) # Trapecio: Rock
genero_rap = fuzz.trimf(escala_genero,[2,4,5.5]) # Triangulo: Rap
genero_blues = fuzz.trimf(escala_genero, [4.5, 6.5, 8.5]) # Triangulo: Blues
genero_pop = fuzz.trapmf(escala_genero, [7.5, 8, 10, 10]) # Trapecio: Pop

ctk.set_appearance_mode("Dark") # Se configura la ventana de la interfaz
ctk.set_default_color_theme("blue") 
app = ctk.CTk() # Se inicia la interfaz
app.title("Recomendador de géneros y canciones") # Se cambia el nombre del titulo de la ventana
app.geometry("1200x500") # Se cambia el tamaño de la ventana

listbox = tk.Listbox(app) # Se crea una Listbox, donde se escribiran los resultados
listbox.place(relx = 0.01, rely = 0.05, relwidth = 0.5, relheight= 0.7) # Se ajusta el tamaño y posicionamiento de la listbox

entry1 = ctk.CTkEntry(master=app) # Se crea el primer cuadro de texto, donde se escribira la cantidad de integrantes
entry1.pack(padx=20, pady=10) # Se configura el cuadro
entry1.place(relx=0.70,rely=0.18, relwidth = 0.1, relheight= 0.05) # Se posiciona el cuadro

# Se crea un texto para informar al usuario que ingresar
text_var1 = tk.StringVar(value="En escala del 1 al 9, ¿De cuantos integrantes prefiere que sea un artista?")
label1 = ctk.CTkLabel(master=app, textvariable=text_var1,
                               width=100,
                               height=25,
                               fg_color=("white", "gray30"),
                               corner_radius=8)
label1.place(relx=0.60,rely=0.10) # Se posiciona el texto

entry2 = ctk.CTkEntry(master=app) # Se crea el segundo cuadro de texto, donde se escribira la intensidad de sonodo
entry2.pack(padx=20, pady=10) # Se configura el cuadro
entry2.place(relx=0.70,rely=0.43, relwidth = 0.1, relheight= 0.05) # Se posiciona el cuadro

# Se crea otro texto para informar al usuario que puede usar decimales
text_var2 = tk.StringVar(value="Para las siguientes consultas puede considerar numeros decimales (Ej: 8.5)")
label2 = ctk.CTkLabel(master=app, textvariable=text_var2,
                               width=100,
                               height=25,
                               fg_color=("white", "gray30"),
                               corner_radius=8)
label2.place(relx=0.60,rely=0.25) # Se posiciona el texto

# Se crea otro texto para informar al usuario que debe ingresar
text_var3 = tk.StringVar(value="En escala del 0 al 9, ¿que tanto prefiere que una cancion tenga una intensidad de sonido?")
label3 = ctk.CTkLabel(master=app, textvariable=text_var3,
                               width=100,
                               height=25,
                               fg_color=("white", "gray30"),
                               corner_radius=8)
label3.place(relx=0.55,rely=0.35) # Se posiciona el texto

entry3 = ctk.CTkEntry(master=app) # Se crea el tercer cuadro de texto, donde se escribira el ritmo
entry3.pack(padx=20, pady=10) # Se configura el cuadro
entry3.place(relx=0.70,rely=0.60, relwidth = 0.1, relheight= 0.05) # Se posiciona el cuadro

# Se crea otro texto para informar al usuario que debe ingresar
text_var4 = tk.StringVar(value="En escala del 0 al 9, ¿Que tanto prefiere que una cancion tenga ritmo?")
label4 = ctk.CTkLabel(master=app, textvariable=text_var4,
                               width=100,
                               height=25,
                               fg_color=("white", "gray30"),
                               corner_radius=8)
label4.place(relx=0.60,rely=0.52) # Se posiciona el texto

# Se crea una caja de opciones para que el usuario elija si desea generar los graficos de resultados
optionmenu_var = ctk.StringVar(value="Si")  # Se configura el valor inicial
combobox = ctk.CTkComboBox(master=app,
                                     values=["Si", "No"],
                                     variable=optionmenu_var,
                                     state = "normal")
combobox.place(relx=0.70,rely=0.75, relwidth = 0.1, relheight= 0.05) # Se configura la caja de opciones

# Se crea un texto para realizar la pregunta al usuario si desea generar los graficos
text_var5 = tk.StringVar(value="¿Quiere generar todos los graficos de los resultados?")
label5 = ctk.CTkLabel(master=app, textvariable=text_var5,
                               width=100,
                               height=25,
                               fg_color=("white", "gray30"),
                               corner_radius=8)
label5.place(relx=0.63,rely=0.68) # Se posiciona el texto

# Se crea un boton para que el usuario pueda ver la grafica de escala de integrantes
button1 = ctk.CTkButton(master=app,
                                 width=120,
                                 height=32,
                                 border_width=0,
                                 corner_radius=8,
                                 text="Ver Gráfica Integrantes Artista",
                                 command=lambda:mostrarIntegrantes())
button1.place(relx=0.05,rely=0.80) # Se posiciona el boton

# Se crea un segundo boton para que el usuario pueda ver la grafica de escala de intensidad de sonido
button2 = ctk.CTkButton(master=app,
                                 width=120,
                                 height=32,
                                 border_width=0,
                                 corner_radius=8,
                                 text="Ver Gráfica Intensidad Canción",
                                 command=lambda:mostrarIntensidades())
button2.place(relx=0.05,rely=0.90) # Se posiciona el boton

# Se crea un tercer boton para que el usuario pueda ver la grafica de escala de ritmo
button3 = ctk.CTkButton(master=app,
                                 width=120,
                                 height=32,
                                 border_width=0,
                                 corner_radius=8,
                                 text="Ver Gráfica Ritmo Canción",
                                 command=lambda:mostrarRitmo())
button3.place(relx=0.25,rely=0.80) # Se posiciona el boton

# Se crea un cuarto boton para que el usuario pueda ver la grafica de escala de generos
button4 = ctk.CTkButton(master=app,
                                 width=120,
                                 height=32,
                                 border_width=0,
                                 corner_radius=8,
                                 text="Ver Gráfica Géneros Escogidos",
                                 command=lambda:mostrarGeneros())
button4.place(relx=0.25,rely=0.90) # Se posiciona el boton

# Se crea un ultimo boton para que el usuario pueda mandar la informacion de la interfaz grafica a la funcion maestra
button5 = ctk.CTkButton(master=app,
                                 width=120,
                                 height=32,
                                 border_width=0,
                                 corner_radius=8,
                                 text="Buscar Canciones",
                                 command=lambda:main_interfaz())
button5.place(relx=0.70,rely=0.85) # Se posiciona el boton

app.mainloop() # Se ejecuta la interfaz grafica
