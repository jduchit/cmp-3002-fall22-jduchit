###                 ESTRUCTURA DE DATOS              ###
### Nombre: Johana Duchi Tipan                       ###
### Fecha : 17/11/2022                               ###
### Tema  : DEBER 3                                  ###
### Ejercicio 3: Compare quick sort and merge sort   ###

#1. Genere 1000 permutaciones aleatorias de matrices de enteros entre 1 y 10000.
#2. Ejecute merge sort y quick sort para cada una de las permutaciones
#3. Calcule el tiempo de ejecución y compárelas.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time
import time
"""
La funcion contador_tiempo se encarga de medir el tiempo de ejecucion de un programa.
"""
def contador_tiempo(funcion):
    def funcion_medida(*args, **kwargs):
        inicio= time.time()*10**6
        return abs((time.time()-inicio))
    return funcion_medida

arrays = []
for i in range(0,1000):
    array = np.random.permutation(10000)
    arrays.append(array)
    print(arrays[i])

@contador_tiempo
def merge_sort(nums):
    time.sleep(1)
    if len(nums) <= 1:
        return nums
    pivot = int(len(nums) / 2)
    left = merge_sort(nums[0:pivot])
    right = merge_sort(nums[pivot:])
    return merge(left, right)

def merge(left, right):
    left_pointer = 0
    right_pointer = 0
    sorted_list = []
    while left_pointer < len(left) and right_pointer < len(right):
        if left[left_pointer] < right[right_pointer]:
            sorted_list.append(left[left_pointer])
            left_pointer += 1
        else:
            sorted_list.append(right[right_pointer])
            right_pointer += 1
    
    sorted_list.extend(left[left_pointer:])
    sorted_list.extend(right[right_pointer:])
    
    return sorted_list

@contador_tiempo
def quick_sort(array):
    time.sleep(1)
    #Si el arreglo tiene longitud 1, ya esta ordenad
    if len(array) <=1:
        arreglo_ordenado = array
    else:
        #Se selecciona el pivote que sera el primer elemento del arreglo
        pivote = array[0]
        #Se inicializan 3 arreglos para elementos mayores, menores e iguales
        greater = []
        less = []
        equal = [] 
        for i in array:
            if i > pivote:
                greater.append(i)
            elif i < pivote:
                less.append(i)
            else: 
                equal.append(i)
        arreglo_ordenado = quick_sort(less)+equal+quick_sort(greater)
    return arreglo_ordenado

timeMS= []
for i in range(0,1000):
    timeMS.append(merge_sort(arrays[i]))
    print(timeMS[i])

timeQS= []
for i in range(0,1000):
    timeQS.append(quick_sort(arrays[i]))
    print(timeMS[i])    

df = pd.DataFrame(zip(timeMS,timeQS))
df.columns = [ 'Merge Sort','Quick Sort']
df
 
plt.plot(df)
plt.yscale('log')
plt.show()