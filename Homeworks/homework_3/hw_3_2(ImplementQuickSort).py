###          ESTRUCTURA DE DATOS          ###
### Nombre: Johana Duchi Tipan            ###
### Fecha : 17/11/2022                    ###
### Tema  : DEBER 3                       ###
### Ejercicio 2: Implement quick sort   ###

#Usa la técnica divide y vencerás para implementar el algoritmo de clasificación 
#rápida estudiado en clase.

def quick_sort(array):   
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

A=quick_sort([])
print (A)