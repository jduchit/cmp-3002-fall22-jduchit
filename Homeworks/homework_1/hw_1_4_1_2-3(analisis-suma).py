###          ESTRUCTURA DE DATOS                   ###
### Nombre: Johana Duchi Tipan                     ###
### Fecha : 29/09/2022                             ###
### Tema  : DEBER 1                                ###
### Ejercicio 4.1.2-3: Analisis tiempo de ejecucion  ###

#Use la biblioteca de tiempo de Python para estimar el tiempo de ejecución de 
#las entradas de  𝑛=[1,10,10^2,10^3,10^4,10^5,10^6,10^7,10^8,10^9] 
#Trace el tiempo de ejecución como una función

import time
import pandas as pd
from IPython.display import display

"""
La funcion contador_tiempo se encarga de medir el tiempo de ejecucion de un programa. Se utilizo una nueva funcion
porque se necesitaba retornar fin-inicio a diferencia de la original que retorna c.
"""
def contador_tiempo(funcion):
    def funcion_medida(*args, **kwargs):
        inicio = time.time()*10**6
        c = funcion(*args, **kwargs)
        fin = ((time.time()*10**6)-10**6)
        print("\nLa funcion analizada es: ",funcion.__name__," , el tiempo que se demora el programa en ejecutarse es: {} micro segundos".format(fin - inicio))
        return (fin-inicio)
    return funcion_medida

@contador_tiempo
def sum1(n):
    time.sleep(1)
    total = 0
    for i in range(1, n+1):
        total += i
    return total

"""
Suma de n numeros con la formula de Gauss
"""
@contador_tiempo
def sum2(n): 
    time.sleep(1)
    total = n*(n+1)//2 #division entera
    return total

@contador_tiempo
def arreglo_suma(n):
    time.sleep(1)
    #Se crean dos arreglos vacios para los resultados de suma 1 y suma 2
    resultado_suma1=[]
    resultado_suma2=[]
    
    for i in (n):      
        resultado_suma1.append(sum1(i))
        resultado_suma2.append(sum2(i))
    
    #Se genera una tabla con los resultados de la suma 
    df = pd.DataFrame(zip(n,resultado_suma1,resultado_suma2))
    df.columns = ['n', 'T1(n)', 'T2(n)']
    display(df)
    df.plot(x='n')
    
    return (resultado_suma1,resultado_suma2)

m=[1,10,10**2,10**3,10**4,10**5,10**6,10**7,10**8,10**9]
arreglo_suma(m)