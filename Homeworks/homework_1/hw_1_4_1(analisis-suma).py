###          ESTRUCTURA DE DATOS          ###
### Nombre: Johana Duchi Tipan            ###
### Fecha : 04/10/2022                    ###
### Tema  : DEBER 1                       ###
### Ejercicio 4.1.1: Analisis funcion suma  ###

#Ejecute las dos funciones y asegúrese de que devuelvan los mismos resultados. 
import time
import pandas as pd

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
def sum1(n):
    time.sleep(1)
    total = 0
    for i in range(1, n+1):
        total += i
    return total

@medidor_tiempo
def sum2(n):
    time.sleep(1)
    total = n*(n+1)//2
    return total

#EJECUTE LAS DOS FUNCIONES Y ASEGURESE DE QUE DEVUELVAN LOS MISMOS RESULTADOS
#USAR n=5,8,103,527

@medidor_tiempo
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
    df.columns = ['n', 'sum1 T(n)', 'sum2 T(n)']
    df.plot(x='n')
    
    return (resultado_suma1,resultado_suma2)

#Se crea el arreglo
l=[5,8,103,527]
arreglo_suma(l)