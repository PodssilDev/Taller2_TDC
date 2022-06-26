# Taller 2 - Grupo 3
# Autores: Matias Figueroa, Daniel Frez, Javier Sanhueza y John Serrano
# Teoria de la Computacion 2022-1

# BLOQUE DE DEFINICIONES
# ----------------------------------------------------------------------------
# IMPORTACION DE FUNCIONES
# ----------------------------------------------------------------------------

import skfuzzy as fuzz # Importamos Scikit-Fuzzy como fuzz
import numpy as np # Se importa numpy como np
import matplotlib.pyplot as plt # Se importa Pyplot de Matplotlib como plt

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
    if(len(lista_canciones_final) == 0): # Si no se encontraron canciones que cumplan todas las caracteristicas
        i = 0
        while(i < n): # Ciclo que busca obtener canciones que cumplan con la primera caracteristica
            if(lista_canciones[i][1] == caracteristica1):
                lista_canciones_final.append(lista_canciones[i][0])
            i = i + 1
    if(len(lista_canciones_final) == 0): # Si aun asi no se pudieron encontrar canciones
        i = 0
        while(i<n): # Se retornan las canciones del genero correspondiente
            lista_canciones_final.append(lista_canciones[i][0])
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

# ENTRADAS
# ----------------------------------------------------------------------------

cantidad_integrantes = int(input("En escala del 1 al 10, ¿De cuantos integrantes prefiere que sea un artista?: "))
intensidad_sonido = float(input("En escala del 0 al 10 (puede considerar decimales) ¿que tanto prefiere que una cancion tenga una intensidad de sonido?: "))
ritmo = float(input("En escala del 0 al 10 (puede considerar decimales) ¿Que tanto prefiere que una cancion tenga ritmo?: "))

# BLOQUE PRINCIPAL
#----------------------------------------------------------------------------

# Generos escodigos: Rock, Rap, Blues, Pop
# Parametros a considerar: Integrantes de un artista, Intensidad de una cancion, Ritmo de una cancion

# Creacion de de scalas
escala_genero = np.arange(0, 10, 0.1) # Escala de generos
escala_integrantes = np.arange(1,10,1) # Escala de numero de integrantes
escala_intensidad_sonido = np.arange(0,10,0.1) # Escala de intensidad de sonido
escala_ritmos = np.arange(0,10,0.1) # Escala de ritmo

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

# Graficos de genero
genero_rock = fuzz.trapmf(escala_genero, [0,0,2,3]) # Trapecio: Rock
genero_rap = fuzz.trimf(escala_genero,[2,4,5.5]) # Triangulo: Rap
genero_blues = fuzz.trimf(escala_genero, [4.5, 6.5, 8.5]) # Triangulo: Blues
genero_pop = fuzz.trapmf(escala_genero, [7.5, 8, 10, 10]) # Trapecio: Pop
'''
plt.plot(escala_integrantes, integrantes_bajo, 'b', linewidth=1.5, label='Bajo')
plt.plot(escala_integrantes,integrantes_medio, 'r', linewidth=1.5, label='Medio')
plt.plot(escala_integrantes, integrantes_alto, 'g', linewidth=1.5, label='Alto')
plt.plot(escala_intensidad_sonido, intensidad_sonido_baja, 'b', linewidth=1.5, label='Baja')
plt.plot(escala_intensidad_sonido, intensidad_sonido_media, 'r', linewidth=1.5, label='Media')
plt.plot(escala_intensidad_sonido, intensidad_sonido_alta, 'g', linewidth=1.5, label='Alta')
plt.plot(escala_ritmos, ritmo_bajo, 'b', linewidth=1.5, label='Bajo')
plt.plot(escala_ritmos, ritmo_medio, 'r', linewidth=1.5, label='Medio')
plt.plot(escala_ritmos, ritmo_alto, 'g', linewidth=1.5, label='Alto')
plt.plot(escala_genero, genero_rock, 'b', linewidth=1.5, label='Rock')
plt.plot(escala_genero, genero_rap, 'r', linewidth=1.5, label='Rap')
plt.plot(escala_genero, genero_blues, 'g', linewidth=1.5, label='Blues')
plt.plot(escala_genero, genero_pop, 'y', linewidth=1.5, label='Pop')
plt.title('Generos escogidos')
plt.legend()
plt.show()
'''
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

# En este punto se utiliza la inferencia de MAMDANI para crear las reglas a utilizar

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
# Si la cantidad de integrantes es baja, con intensidad de sonido media y ritmo medio, ENTONCES el genero es blues
regla_8 = np.fmin(np.fmin(cantidad_integrantes_baja, cantidad_intensidad_sonido_media), cantidad_ritmo_medio)

# Regla 9
# Si la cantidad de integrantes es baja, con intensidad de sonido media y ritmo bajo, ENTONCES el genero es blues
regla_9 = np.fmin(np.fmin(cantidad_integrantes_baja, cantidad_intensidad_sonido_baja), cantidad_ritmo_bajo)

# Regla 10
# Si la cantidad de integrantes es medio, con intensidad de sonido alto y ritmo alto, ENTONCES el genero es rap
regla_10 = np.fmin(np.fmin(cantidad_integrantes_medio, cantidad_intensidad_sonido_alta), cantidad_ritmo_alto)

# Regla 11
# Si la cantidad de integrantes es medio, con intensidad de sonido alta y ritmo medio, ENTONCES el genero es rock
regla_11 = np.fmin(np.fmin(cantidad_integrantes_alto, cantidad_intensidad_sonido_baja), cantidad_ritmo_bajo)

# Regla 12
# Si la cantidad de integrantes es alta, con intensidad de sonido media y ritmo bajo, ENTONCES el genero es rock
regla_12 = np.fmin(np.fmin(cantidad_integrantes_alto, cantidad_intensidad_sonido_media), cantidad_ritmo_bajo)

# Regla 13
# Si la cantidad de integrantes es baja, con intensidad de sonido alta y ritmo alto, ENTONCES el genero es rap
regla_13 = np.fmin(np.fmin(cantidad_integrantes_baja, cantidad_intensidad_sonido_alta), cantidad_ritmo_alto)

# Regla 14
# Si la cantidad de integrantes es media, con intensidad de sonido media y ritmo bajo, ENTONCES el genero es pop
regla_14 = np.fmin(np.fmin(cantidad_integrantes_medio, cantidad_intensidad_sonido_media), cantidad_ritmo_bajo)

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
agregacionFinal = np.fmax(agregacion12, regla_pop4)

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

# SALIDA
# ----------------------------------------------------------------------------

# Se imprime el genero obtenido y se asigna la lista de canciones correspondiente
print("\n")
if resultado == rock:
    print("El genero preferido es: Rock\n")
    lista_canciones = canciones_rock
elif resultado == pop:
    print("El genero preferido es: Pop\n")
    lista_canciones = canciones_pop
elif resultado == rap:
    print("El genero preferido es: Rap\n")
    lista_canciones = canciones_rap
elif resultado == blues:
    print("El genero preferido es: Blues\n")
    lista_canciones = canciones_blues

# Se obtiene la lista de canciones, filtrando por caracteristicas. Se imprimen el nombre de 
# las canciones obtenidas
lista_canciones_final = obtenerCanciones(lista_canciones, caracteristica1, caracteristica2, caracteristica3)
print("Canciones recomendadas del genero basado en sus preferencias: ")
for cancion in lista_canciones_final:
    print(cancion)

#Graficos
escala_genero0 = np.zeros_like(escala_genero)
escala_integrantes0 = np.zeros_like(escala_integrantes)
escala_intensidad_sonido0 = np.zeros_like(escala_intensidad_sonido)
escala_ritmos0 = np.zeros_like(escala_ritmos)

fig, (regla1_graficos, regla3_graficos, regla3_graficos, regla4_graficos, regla5_graficos, regla6_graficos, regla7_graficos, regla8_graficos, regla9_graficos, regla10_graficos, regla11_graficos, regla12_graficos, regla13_graficos, regla14_graficos, graficoFinal) = plt.subplots(15, 4)

#Graficos para numero de integrantes
#Integrantes Bajo
integrantes_bajo_grafico = plt.fill_between(escala_integrantes, escala_integrantes0, integrantes_bajo, facecolor='b', alpha=0.8, label='Bajo')
integrantes_bajo_grafico.plot([cantidad_integrantes, cantidad_integrantes], [0, cantidad_integrantes_baja], "k", linewidth=1.5)
integrantes_bajo_grafico.plot([0, cantidad_integrantes], [cantidad_integrantes_baja, cantidad_integrantes_baja], "k", linewidth=1.5, linestyle="--")

#Integrantes Medio
integrantes_medio_grafico = plt.fill_between(escala_integrantes, escala_integrantes0,integrantes_medio, facecolor='r', alpha=0.8, label='Medio')
integrantes_medio_grafico.plot([cantidad_integrantes, cantidad_integrantes], [0, cantidad_integrantes_medio], "k", linewidth=1.5)
integrantes_medio_grafico.plot([0, cantidad_integrantes], [cantidad_integrantes_medio, cantidad_integrantes_medio], "k", linewidth=1.5, linestyle="--")

#Integrantes Alto
integrantes_alto_grafico = plt.fill_between(escala_integrantes, escala_integrantes0, integrantes_alto, facecolor='g', alpha=0.8, label='Alto')
integrantes_alto_grafico.plot([cantidad_integrantes, cantidad_integrantes], [0, cantidad_integrantes_alto], "k", linewidth=1.5)
integrantes_alto_grafico.plot([0, cantidad_integrantes], [cantidad_integrantes_alto, cantidad_integrantes_alto], "k", linewidth=1.5, linestyle="--")

#Grafico para Intensidad del sonido
#Intensidad del sonido baja
intensidad_sonido_baja_grafico = plt.fill_between(escala_intensidad_sonido, escala_intensidad_sonido0, intensidad_sonido_baja, facecolor='b', alpha=0.8, label='Baja')
intensidad_sonido_baja_grafico.plot([intensidad_sonido, intensidad_sonido], [0, cantidad_intensidad_sonido_baja], "k", linewidth=1.5)
intensidad_sonido_baja_grafico.plot([0, intensidad_sonido], [cantidad_intensidad_sonido_baja, cantidad_intensidad_sonido_baja], "k", linewidth=1.5, linestyle="--")

#Intensidad del sonido media
intensidad_sonido_media_grafico = plt.fill_between(escala_intensidad_sonido, escala_intensidad_sonido0, intensidad_sonido_media, facecolor='r', alpha=0.8, label='Media')
intensidad_sonido_media_grafico.plot([intensidad_sonido, intensidad_sonido], [0, cantidad_intensidad_sonido_media], "k", linewidth=1.5)
intensidad_sonido_media_grafico.plot([0, intensidad_sonido], [cantidad_intensidad_sonido_media, cantidad_intensidad_sonido_media], "k", linewidth=1.5, linestyle="--")

#Intensidad del sonido alta
intensidad_sonido_alta_grafico = plt.fill_between(escala_intensidad_sonido, escala_intensidad_sonido0, intensidad_sonido_alta, facecolor='g', alpha=0.8, label='alta')
intensidad_sonido_alta_grafico.plot([intensidad_sonido, intensidad_sonido], [0, cantidad_intensidad_sonido_alta], "k", linewidth=1.5)
intensidad_sonido_alta_grafico.plot([0, intensidad_sonido], [cantidad_intensidad_sonido_alta, cantidad_intensidad_sonido_alta], "k", linewidth=1.5, linestyle="--")

#Graficos ritmo
#Ritmo bajo
ritmo_bajo_grafico = plt.fill_between(escala_ritmos, escala_ritmos0, ritmo_bajo, facecolor='b', alpha=0.8, label='Baja')
ritmo_bajo_grafico.plot([ritmo, ritmo], [0, cantidad_ritmo_bajo], "k", linewidth=1.5)
ritmo_bajo_grafico.plot([0, ritmo], [cantidad_ritmo_bajo, cantidad_ritmo_bajo], "k", linewidth=1.5, linestyle="--")

#Ritmo medio
ritmo_medio_grafico = plt.fill_between(escala_ritmos, escala_ritmos0, ritmo_medio, facecolor='r', alpha=0.8, label='Baja')
ritmo_medio_grafico.plot([ritmo, ritmo], [0, cantidad_ritmo_medio], "k", linewidth=1.5)
ritmo_medio_grafico.plot([0, ritmo], [cantidad_ritmo_medio, cantidad_ritmo_medio], "k", linewidth=1.5, linestyle="--")

#Ritmo alto
ritmo_alto_grafico = plt.fill_between(escala_ritmos, escala_ritmos0, ritmo_alto, facecolor='g', alpha=0.8, label='Baja')
ritmo_alto_grafico.plot([ritmo, ritmo], [0, cantidad_ritmo_alto], "k", linewidth=1.5)
ritmo_alto_grafico.plot([0, ritmo], [cantidad_ritmo_alto, cantidad_ritmo_alto], "k", linewidth=1.5, linestyle="--")

#Regla 1
regla1_graficos[0] = integrantes_bajo_grafico
regla1_graficos[1] = intensidad_sonido_alta_grafico
regla1_graficos[2] = ritmo_medio_grafico
regla1_graficos[3].fill_between(escala_genero, escala_genero0, regla_rap1, facecolor="b", alpha=0.7)
regla1_graficos[3].plot(escala_genero, genero_rap, "b", linewidth=0.6, linestyle="--")

#Regla 2
regla3_graficos[0] = integrantes_medio_grafico
regla3_graficos[1] = intensidad_sonido_alta_grafico
regla3_graficos[2] = ritmo_bajo_grafico
regla3_graficos[3].fill_between(escala_genero, escala_genero0, regla_rock1, facecolor="b", alpha=0.7)
regla3_graficos[3].plot(escala_genero, genero_rock, "b", linewidth=0.6, linestyle="--")

#Regla 3
regla3_graficos[0] = integrantes_medio_grafico
regla3_graficos[1] = intensidad_sonido_baja_grafico
regla3_graficos[2] = ritmo_medio_grafico
regla3_graficos[3].fill_between(escala_genero, escala_genero0, regla_blues1, facecolor="b", alpha=0.7)
regla3_graficos[3].plot(escala_genero, genero_blues, "b", linewidth=0.6, linestyle="--")

#Regla 4
regla4_graficos[0] = integrantes_alto_grafico
regla4_graficos[1] = intensidad_sonido_baja_grafico
regla4_graficos[2] = ritmo_alto_grafico
regla4_graficos[3].fill_between(escala_genero, escala_genero0, regla_pop1, facecolor="b", alpha=0.7)
regla4_graficos[3].plot(escala_genero, genero_pop, "b", linewidth=0.6, linestyle="--")

#Regla 5
regla5_graficos[0] = integrantes_bajo_grafico
regla5_graficos[1] = intensidad_sonido_media_grafico
regla5_graficos[2] = ritmo_alto_grafico
regla5_graficos[3].fill_between(escala_genero, escala_genero0, regla_pop2, facecolor="b", alpha=0.7)
regla5_graficos[3].plot(escala_genero, genero_pop, "b", linewidth=0.6, linestyle="--")

#Regla 6
regla6_graficos[0] = integrantes_alto_grafico
regla6_graficos[1] = intensidad_sonido_alta_grafico
regla6_graficos[2] = ritmo_bajo_grafico
regla6_graficos[3].fill_between(escala_genero, escala_genero0, regla_rock2, facecolor="b", alpha=0.7)
regla6_graficos[3].plot(escala_genero, genero_rock, "b", linewidth=0.6, linestyle="--")

#Regla 7
regla7_graficos[0] = integrantes_bajo_grafico
regla7_graficos[1] = intensidad_sonido_media_grafico
regla7_graficos[2] = ritmo_bajo_grafico
regla7_graficos[3].fill_between(escala_genero, escala_genero0, regla_rap2, facecolor="b", alpha=0.7)
regla7_graficos[3].plot(escala_genero, genero_rap, "b", linewidth=0.6, linestyle="--")

#Regla 8
regla8_graficos[0] = integrantes_bajo_grafico
regla8_graficos[1] = intensidad_sonido_media_grafico
regla8_graficos[2] = ritmo_medio_grafico
regla8_graficos[3].fill_between(escala_genero, escala_genero0, regla_blues2, facecolor="b", alpha=0.7)
regla8_graficos[3].plot(escala_genero, genero_blues, "b", linewidth=0.6, linestyle="--")

#Regla 9
regla9_graficos[0] = integrantes_bajo_grafico
regla9_graficos[1] = intensidad_sonido_media_grafico
regla9_graficos[2] = ritmo_bajo_grafico
regla9_graficos[3].fill_between(escala_genero, escala_genero0, regla_blues3, facecolor="b", alpha=0.7)
regla9_graficos[3].plot(escala_genero, genero_blues, "b", linewidth=0.6, linestyle="--")

#Regla 10
regla10_graficos[0] = integrantes_medio_grafico
regla10_graficos[1] = intensidad_sonido_alta_grafico
regla10_graficos[2] = ritmo_alto_grafico
regla10_graficos[3].fill_between(escala_genero, escala_genero0, regla_rap3, facecolor="b", alpha=0.7)
regla10_graficos[3].plot(escala_genero, genero_rap, "b", linewidth=0.6, linestyle="--")

#Regla 11
regla11_graficos[0] = integrantes_medio_grafico
regla11_graficos[1] = intensidad_sonido_alta_grafico
regla11_graficos[2] = ritmo_medio_grafico
regla11_graficos[3].fill_between(escala_genero, escala_genero0, regla_rock3, facecolor="b", alpha=0.7)
regla11_graficos[3].plot(escala_genero, genero_rock, "b", linewidth=0.6, linestyle="--")

#Regla 12
regla12_graficos[0] = integrantes_alto_grafico
regla12_graficos[1] = intensidad_sonido_baja_grafico
regla12_graficos[2] = ritmo_bajo_grafico
regla12_graficos[3].fill_between(escala_genero, escala_genero0, regla_rock4, facecolor="b", alpha=0.7)
regla12_graficos[3].plot(escala_genero, genero_rock, "b", linewidth=0.6, linestyle="--")

#Regla 13
regla13_graficos[0] = integrantes_alto_grafico
regla13_graficos[1] = intensidad_sonido_baja_grafico
regla13_graficos[2] = ritmo_bajo_grafico
regla13_graficos[3].fill_between(escala_genero, escala_genero0, regla_rock4, facecolor="b", alpha=0.7)
regla13_graficos[3].plot(escala_genero, genero_rock, "b", linewidth=0.6, linestyle="--")

#Regla 14
regla14_graficos[0] = integrantes_medio_grafico
regla14_graficos[1] = intensidad_sonido_media_grafico
regla14_graficos[2] = ritmo_bajo_grafico
regla14_graficos[3].fill_between(escala_genero, escala_genero0, regla_pop4, facecolor="b", alpha=0.7)
regla14_graficos[3].plot(escala_genero, genero_pop, "b", linewidth=0.6, linestyle="--")

#Grafico final - agregacion más resultado
graficoFinal[3].fill_between(escala_genero, escala_genero0, agregacionFinal, facecolor="g", alpha=0.6)
graficoFinal[3].plot([desfuzzificacion, desfuzzificacion], [0, resultado], "k", linewidth=1.5)
graficoFinal[3].plot([0, desfuzzificacion], [resultado, resultado], "k", linewidth=1.5)
