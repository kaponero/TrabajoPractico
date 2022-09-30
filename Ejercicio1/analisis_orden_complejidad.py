# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 17:31:26 2022

@author: Gabriela González
         Maximiliano Pérez Albarracín
         Alvaro Labanca
"""

import random
import time
import matplotlib.pyplot as plt

from LDE import ListaDobleEnlazada

#Se define la lista doblemente enlazada 

lista_LDE = ListaDobleEnlazada()
 #se crea vector de tiempos
tiempos = [[],[]]
#creacion de vector para variar tamaño de listas
valores_n = [10**i for i in range(1,5)]

for n in valores_n:
       
    #se crea la lista de python con valores al azar
    lista = [random.randint(0, 100) for _ in range(n)] 
    #se asigna el tiempo inicial
    tiempo_inicial = time.perf_counter()
    #se ordena la lista con el metodo avanzado
    lista.sort()
    #se asigna el tiempo final
    tiempo_final = time.perf_counter()
    #se guardan los tiempos en el vector
    tiempos[0].append(tiempo_final - tiempo_inicial)
  
    #se llena la lista LDE con valores al azar
    for n in range(n):
        lista_LDE.anexar(random.randint(0, 100)) 
    #se asigna el tiempo inicial
    tiempo_inicial = time.perf_counter()
    #se ordena la lista LDE con el metodo ordenar
    lista_LDE.ordenar()
    #se asigna el tiempo final
    tiempo_final = time.perf_counter()
    #se guardan los tiempos en el vector
    tiempos[1].append(tiempo_final-tiempo_inicial)
    
    


plt.clf()
plt.plot(valores_n, tiempos[0], label="Ordenamiento con funciónn sort")
plt.plot(valores_n, tiempos[1], label="Ordenamiento con metodo ordenar de LDE ")
plt.yscale('log')
plt.xlabel("tamaños de la lista")
plt.ylabel("tiempos del algoritmo")
plt.title("Tiempos en fn. del nro de elementos")
plt.legend()


