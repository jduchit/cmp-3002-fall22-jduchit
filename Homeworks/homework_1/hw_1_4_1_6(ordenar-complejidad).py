###          ESTRUCTURA DE DATOS                   ###
### Nombre: Johana Duchi Tipan                     ###
### Fecha : 29/09/2022                             ###
### Tema  : DEBER 1                                ###
### Ejercicio 4.1.6:Complejidad Asintotica         ###

#Ordene las siguientes funciones en orden decreciente de complejidad 
#asintótica ( 𝑂(𝑓(𝑛)) )

import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

"""
La funcion contador_tiempo se encarga de medir el tiempo de ejecucion de un programa. Se utilizo una nueva funcion
porque se necesitaba retornar fin-inicio a diferencia de la original que retorna c.
"""
def medidor_tiempo(funcion):
    def funcion_medida(*args, **kwargs):
        inicio = time.time()*10**6
        c = funcion(*args, **kwargs)
        fin = ((time.time()*10**6)-10**6)
        print("\nLa funcion analizada es: ",funcion.__name__," , el tiempo que se demora el programa en ejecutarse es: {} micro segundos".format(fin - inicio))
        return c
    return funcion_medida

@medidor_tiempo
def funciones_complejidad():
    time.sleep(1)
    r = pd.DataFrame()
    r['n'] = np.arange(1,100,10)
    r['f1(n) = sqrt(n)'] = np.sqrt(r['n'])
    r['f2(n) = n^3'] = np.power(r['n'],3)
    r['f3(n) = (n  4 ) '] = np.power(r['n'],4)
    r['f4(n) = sumatoria de i=2 a n de (i-1) '] = np.power(r['n'],2)
    
    #Se traza el grafico
    r.plot(x='n', logy=True, lw=2, figsize=(12, 6))#Traza en escala logaritmica 
    plt.grid()
funciones_complejidad()