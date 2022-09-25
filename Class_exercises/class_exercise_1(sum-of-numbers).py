###          ESTRUCTURA DE DATOS          ###
### Nombre: Johana Duchi Tipan            ###
### Fecha : 30/08/2022                    ###
### Tema  : Control de versiones Git      ###
### Ejercicio 2: Practicar con Git        ###

#Write a function that takes calculates the sum of numbers from 1 to n, where n is the input #
#Escribe una funcion que calcule la suma de numeros de 1 a n, donde n es la entrada          #

def suma (n):
    result = 0
    for suma in range(1, n+1):
        result = result + suma
    print("La suma de numeros de 1 a {} es: {}".format(n,result))

suma(10)   