###                 ESTRUCTURA DE DATOS              ###
### Nombre: Johana Duchi Tipan                       ###
### Fecha : 17/11/2022                               ###
### Tema  : DEBER 3                                  ###
### Ejercicio 3: Implement factorials with recursion ###

#1. Usa la recursividad para implementar el factorial.
#2. Ejecute su código para números entre 1 y 10000.
#3. Calcular el tiempo de ejecución y trazarlo.
#5. Implemente memorización para mejorar el rendimiento de su código.
#6. Mida el tiempo de ejecución cuando calcule el factorial para números entre 1 y 10000.
import pandas as pd
import matplotlib.pyplot as plt
import time

"""
La funcion contador_tiempo se encarga de medir el tiempo de ejecucion de un programa.
"""
def contador_tiempo(funcion):
    def funcion_medida(*args, **kwargs):
        fin = time.time()*10**6
        return abs((fin-time.time()))
    return funcion_medida

@contador_tiempo
def factorial (num):
    time.sleep(1)
    if num == 0 or num == 1:
        resultado = 1
    elif num > 1:
        resultado = num*factorial(num-1)
    return resultado

 
factorial_times=[]
for i in range(1,10000):
    factorial_times.append(factorial(i))
    
df1 = pd.DataFrame(zip(factorial_times))
df1.columns = ['Factorial']
df1

df1.plot()

def factorial1(num):
    cache=[]
    def factorial_Memoization(num):
        if num==0 or num == 1:
            res = 1
        if num in cache.keys():
            res = cache[num]
        else:
            res = num*factorial(num-1)
            cache[num] = res
        return res
    return factorial_Memoization(num)

factorialm_times=[]
for i in range(1,10000):
    factorialm_times.append(factorial1(i))
    
df1 = pd.DataFrame(zip(factorialm_times))
df1.columns = ['Factorial Memoization']
df1

df1.plot()

