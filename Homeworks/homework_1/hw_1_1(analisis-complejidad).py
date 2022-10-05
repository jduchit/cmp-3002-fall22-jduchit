###          ESTRUCTURA DE DATOS          ###
### Nombre: Johana Duchi Tipan            ###
### Fecha : 04/10/2022                    ###
### Tema  : DEBER 1                       ###
### Ejercicio 1: Análisis de complejidad  ###

import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""
La funcion medidor_tiempo se encarga de medir el tiempo de ejecucion de un programa.
"""
def medidor_tiempo(funcion):
    def funcion_medida(*args, **kwargs):
        inicio = time.time()*10**6
        c = funcion(*args, **kwargs)
        fin = ((time.time()*10**6)-10**6)
        print("\nLa funcion analizada es: ",funcion.__name__," , el tiempo que se demora el programa en ejecutarse es: {} micro segundos".format(fin - inicio))
        return c
    return funcion_medida

"""
La funcion graficas_complejidad compara graficamente el crecimiento de nlogn con n^2
"""
@medidor_tiempo
def graficas_complejidad():
    time.sleep(1)
    #Se define el data frame con datos bidimensionales (filas y columnas)
    r = pd.DataFrame()
    r['n1'] = np.arange(1,100,10)

    #Se definen las 2 funciones a comparar
    r['nlog(n)'] = r['n1'] * (np.log2(r['n1']))
    r['n^2'] = np.power(r['n1'],2)

    #Se traza el grafico
    r.plot(x='n1', logy=True, lw=2, figsize=(12, 6))#Traza en escala logaritmica 
    plt.grid()                

graficas_complejidad()    