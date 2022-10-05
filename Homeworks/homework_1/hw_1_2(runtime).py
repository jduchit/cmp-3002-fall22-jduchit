###          ESTRUCTURA DE DATOS          ###
### Nombre: Johana Duchi Tipan            ###
### Fecha : 04/10/2022                    ###
### Tema  : DEBER 1                       ###
### Ejercicio 2: Run Time                 ###

import time
import numpy as np
import pandas as pd
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

@medidor_tiempo
def tiempo_ejecucion():
    time.sleep(1)
    #Se define el data frame
    r = pd.DataFrame()
    
    #Se definen los puntos en x y en y 
    r['n'] = np.array([1000,2000,4000,8000,16000,32000,64000])
    r['run_time'] = np.array([0.0,0.02,0.2,0.6,2.6,10.4,41.6])
   
    """ 
    La  funcion numpy.polynomial.polynomial.polyfit nos permite aproximar 
    un conjunto de datos es la version mas actual, sin embargo se opto por 
    la version antigua np.poly1d porque numpy.polynomial.polynomial.polyfit
    retorna el resultado en forma de array y al momento de imprimir el 
    polinomio se tenia que hacer un ajuste en el formato de impresion para
    identificar los terminos x^0,x^1,x^2 lo que no sucede con la version anterior
    """
    #regresion lineal
    regresion_lineal = np.poly1d(np.polyfit(r['n'],r['run_time'], 1))               
    print ("Regresion lineal:\n",(regresion_lineal))
    #minimos cuadrados
    minimos_cuadrados= np.poly1d(np.polyfit(r['n'],r['run_time'], 2)) 
    print ("Minimos cuadrados:\n",(minimos_cuadrados))
   
    '''
    La funcion scattter se concentra en cada punto mientras
    plot aplica las propiedades a todos los puntos 
    '''
    eje= np.arange(0, 64000, 42)
    plt.scatter(r['n'],r['run_time']) 
    plt.plot(r['n'],r['run_time'])
    plt.plot(eje, regresion_lineal(eje))
    plt.plot(eje, minimos_cuadrados(eje))
    plt.grid()
    plt.legend(['(n, run_time) - puntos','n, run_time','Regresion Lineal', 'Minimos Cuadrados'])
    
tiempo_ejecucion()
