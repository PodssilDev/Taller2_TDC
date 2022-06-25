# Taller 2 - Grupo 3
# Autores: Matias Figueroa, Daniel Frez, Javier Sanhueza y John Serrano
# Teoria de la Computacion 2022-1

# BLOQUE DE DEFINICIONES
# ----------------------------------------------------------------------------
# IMPORTACION DE FUNCIONES
# ----------------------------------------------------------------------------

import skfuzzy as fuzz
import numpy as np
import matplotlib.pyplot as plt

# BLOQUE PRINCIPAL
#----------------------------------------------------------------------------

# Generos: Rock, Rap, Blues, Pop

# Parametros: Cantidad de integrantes, Sonidos fuertes y ritmos

# Escalas 
escala_genero = np.arange(0, 10, 0.1)
escala_integrantes = np.arange(1,10,1)
escala_intensidad_sonido = np.arange(0,10,0.1)
escala_ritmos = np.arange(0,10,0.1)

integrantes_bajo = fuzz.trimf(escala_integrantes, [1, 1, 3])
integrantes_medio = fuzz.trapmf(escala_integrantes, [2,3,4,6])
integrantes_alto = fuzz.trapmf(escala_integrantes,[4,6,10,10])

intensidad_sonido_baja = fuzz.trapmf(escala_intensidad_sonido, [0,0,2,4])
intensidad_sonido_media = fuzz.trapmf(escala_intensidad_sonido, [3,4,6,7]) 
intensidad_sonido_alta = fuzz.trapmf(escala_intensidad_sonido, [6,7,10,10])

ritmo_bajo = fuzz.trapmf(escala_ritmos, [0,0,2,4])
ritmo_medio = fuzz.trapmf(escala_ritmos, [3,4,6,7]) 
ritmo_alto = fuzz.trapmf(escala_ritmos, [6,7,10,10])

genero_rock = fuzz.trapmf(escala_genero, [0,0,2,3])
genero_rap = fuzz.trimf(escala_genero,[2,4,5.5])
genero_blues = fuzz.trimf(escala_genero, [4.5, 6.5, 8.5])
genero_pop = fuzz.trapmf(escala_genero, [7.5, 8, 10, 10])

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
plt.show()
'''
# ENTRADAS
# ----------------------------------------------------------------------------
cantidad_integrantes = int(input("Ingrese la cantidad de integrantes: "))
intensidad_sonido = float(input("Ingrese la intensidad del sonido (0-10, puede considerar decimales): "))
ritmo = float(input("Ingrese el ritmo (0-10, puede considerar decimales): "))

#  Funciones de pertencia

cantidad_integrantes_baja = fuzz.interp_membership(escala_integrantes, integrantes_bajo, cantidad_integrantes)
cantidad_integrantes_medio = fuzz.interp_membership(escala_integrantes, integrantes_medio, cantidad_integrantes)
cantidad_integrantes_alto = fuzz.interp_membership(escala_integrantes, integrantes_alto, cantidad_integrantes)

cantidad_intensidad_sonido_baja = fuzz.interp_membership(escala_intensidad_sonido, intensidad_sonido_baja, intensidad_sonido)
cantidad_intensidad_sonido_media = fuzz.interp_membership(escala_intensidad_sonido, intensidad_sonido_media, intensidad_sonido)
cantidad_intensidad_sonido_alta = fuzz.interp_membership(escala_intensidad_sonido, intensidad_sonido_alta, intensidad_sonido)

cantidad_ritmo_bajo = fuzz.interp_membership(escala_ritmos, ritmo_bajo, ritmo)
cantidad_ritmo_medio = fuzz.interp_membership(escala_ritmos, ritmo_medio, ritmo)
cantidad_ritmo_alto = fuzz.interp_membership(escala_ritmos, ritmo_alto, ritmo)

#print(cantidad_integrantes_baja)
#print(cantidad_integrantes_medio)
#print(cantidad_integrantes_alto)
# MAMDANI
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

regla_10 = np.fmin(np.fmin(cantidad_integrantes_medio, cantidad_intensidad_sonido_alta), cantidad_ritmo_alto)

# Regla 11
# Si la cantidad de integrantes es medio, con intensidad de sonido alta y ritmo medio, ENTONCES el genero es rock
regla_11 = np.fmin(np.fmin(cantidad_integrantes_alto, cantidad_intensidad_sonido_baja), cantidad_ritmo_bajo)

# Rock
regla_12 = np.fmin(np.fmin(cantidad_integrantes_alto, cantidad_intensidad_sonido_media), cantidad_ritmo_bajo)

# rap
regla_13 = np.fmin(np.fmin(cantidad_integrantes_baja, cantidad_intensidad_sonido_alta), cantidad_ritmo_alto)


# Preguntar sobre el grafico de generos, especificamente de como debe estructurarse el grafico
# si es que se puede aplicar menos variables para una regla o agregar mas de las mismas variable
# Como se trabaja el resultado desfucificado para representar el resultado final al usuario (Que pasa si queda en una intersección)

# Activacion de cada regla
regla_rock1 = np.fmin(regla_2, genero_rock)
regla_rock2 = np.fmin(regla_6, genero_rock)
regla_rock3 = np.fmin(regla_11, genero_rock)
regla_rock4 = np.fmin(regla_12, genero_rock)
regla_pop1 = np.fmin(regla_4, genero_pop)
regla_pop2 = np.fmin(regla_5, genero_pop)
regla_pop3 = np.fmin(regla_13, genero_pop)
regla_blues1 = np.fmin(regla_3, genero_blues)
regla_blues2 = np.fmin(regla_8, genero_blues)
regla_blues3 = np.fmin(regla_9, genero_blues)
regla_rap1 = np.fmin(regla_1, genero_rap)
regla_rap2 = np.fmin(regla_7, genero_rap)
regla_rap3 = np.fmin(regla_10, genero_rap)

# Agregacion
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

desfuzzificacion = fuzz.defuzz(escala_genero, agregacion12, 'bisector')

print(desfuzzificacion)
rock = fuzz.interp_membership(escala_genero, genero_rock, desfuzzificacion)
rap = fuzz.interp_membership(escala_genero, genero_rap, desfuzzificacion)
pop = fuzz.interp_membership(escala_genero, genero_pop, desfuzzificacion)
blues = fuzz.interp_membership(escala_genero, genero_blues, desfuzzificacion)

resultado = max(rock, rap, pop, blues)
if resultado == rock:
    print("Rock")
elif resultado == pop:
    print("Pop")
elif resultado == rap:
    print("Rap")
elif resultado == blues:
    print("Blues")


canciones_pop = ["Maroon 5- She will be loved", "Michael Jackson - Beat it", "The Weeknd - Blinding Lights", "Hunting high and low - Take on me",
                  "The Weeknd - Hype", "The Weeknd - Starboy", "The Chainsmokers - Closer", "Christian Kuria - Losing You", "Michael Jackson - Billie Jean"
                  "Frank Blunt - The Dirt Road", "BTS - Butter", "Kairi Yagi (Vivy) - Sing My Pleasure", "Yellowcard - Way Way"]

canciones_rock = ["Billy Talent - Red Flag", "Phil Collins - In The Air Tonight", "Autopilot Off - Clockworks", "Caesars - Jerk It Out",
                  "Mike Oldfield - Nuclear", "Brandon Yates - Olympus Mons", "Nirvana - Come as you are", "Wolfmother - Woman", "Set It Off - Wolf In Sheeps Clothing"
                  "The Who - Pinball Wizard", "The Peggies - FootPrints", "Sambomaster - Seishun kyousoukyoku"]

canciones_rap = ["KSI - Creature", "XXXTENTACION - SAD!", "Drake - Started From the Bottom", "Travis Scott - Antidote", "Wiz Khalifa - We Dem Boyz"
                 "Drake - God's Plan", "Coolio - Gangsta's Paradise", "Kanye West - Yeezy", "Dr. Dre - Still D.R.E."]

canciones_blues = ["John Lee Hooker - Boom Boom", "Stevie Ray Vaughan - Pride and Joy", "The beatles - Yer Blues", "B.B. King - The Thrill is Gone", 
                  "Led Zeppelin - I cant Quit You Baby", "Metro pa Quilpue - La Bkues Willis"]
