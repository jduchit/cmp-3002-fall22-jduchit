###          ESTRUCTURA DE DATOS                   ###
### Nombre: Johana Duchi Tipan                     ###
### Fecha : 04/10/2022                             ###
### Tema  : DEBER 1                                ###
### Ejercicio 4.1.7:Eliminacion de elementos       ###

#Implementar los métodos de la clase Array que se ocupan de la eliminación 
#de elementos. Considere los 3 casos que consideramos en clase.
import time

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

import ctypes

class Array(object):
    """
    Implementation of the array data structure
    """

    def __init__(self, n):
        """
        Initialize the class
        """
        self.l = 0
        self.n = n
        self.array = self._create_array(self.n)        
    
    def _create_array(self, n):
        """
        Creates a new array of capacity n
        """
        return (n * ctypes.py_object)()

class Array(Array):
    def __init__(self, n, values=None):
        self.l = 0
        self.n = n
        self.array = self._create_array(self.n)
        if values:
            self.initialize_array(values)
    
    def initialize_array(self, values):
        """
        Initialize array
        """
        if self.n != len(values):
            raise ValueError("element count different than capacity")
        for item in values:
            self.array[self.l] = item
            self.l += 1
            
    def __getitem__(self, item_index):
        """
        Return element at item_index
        """
        if (item_index < 0) or (item_index >= self.n):
            raise IndexError('index out of range!')
        try:
            x = self.array[item_index]
        except ValueError:
            x = None
        return x
    
    def __setitem__(self, item_index, item):
        """
        Set element at item_index
        """
        if (item_index < 0) or (item_index >= self.n):
            raise IndexError('index out of range!')
        self.array[item_index] = item
    
    def list_array(self):
        """
        List elements of the array
        using list comprehension
        """
        return ", ".join(str(x) if x is not None else '_' for x in self)

    def list_array2(self):
        y = []
        for x in self:
            if x is not None:
                y.append(str(x))
            else:
                y.append('_')
        return ", ".join(y)

    def insert(self, index, element):
        """
        implementation of insert
        """
        if self.l == self.n:
            raise ValueError("no more capacity")
        if (index < 0) or (index > self.l):
            raise IndexError('index out of range!')
        x = self.l
        while x > index:
            self.array[x] = self.array[x-1]
            x -= 1
        self.array[index] = element
        self.l += 1
    
    def insert_to_tail(self, item):
        """
        Add new item to the tail of the array
        """
        if self.l == self.n:
            raise ValueError("no more capacity")
        self.array[self.l] = item
        self.l += 1
        
    def insert_to_head(self, item):
        """
        Add new item to the beginning of the array
        """
        if self.l == self.n:
            raise ValueError("no more capacity")
        i = self.l
        while (i > 0):
            self.array[i] = self.array[i-1]
            i -= 1
        self.array[0] = item
        self.l += 1

    def delete(self, index):
        if(self.l>1 and (index >= 0 and index <= self.l-1)):
            i = index
            while i > self.l-1:
                self.array[i] = self.array[i+1]
                i += 1
            self.array[self.l-1] = '_'
            self.l -= 1   
        else:
            print("Fuera de rango")
            
    def delete_to_tail(self):
        if self.l != 0:
            self.array[self.l-1] = None
            self.l -= 1
        else:
            print("El arreglo esta vacio")
    
    def delete_to_head(self):
        if self.l != 0:
            i=1
            while (i <self.l-1):
                self.array[i] = self.array[i-1]
                i += 1
            self.array[self.l] = '_'
            self.l -= 1
        else:
            print('index out of range!')
            
dias_semana = Array(7,['Lunes','Martes','Miercoles','Jueves','Viernes','Sabado', 'Domingo'])
dias_semana.list_array()

dias_semana.delete_to_head()
dias_semana.delete_to_tail()
dias_semana.delete(4)