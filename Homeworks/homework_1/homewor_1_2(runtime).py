###          ESTRUCTURA DE DATOS          ###
### Nombre: Johana Duchi Tipan            ###
### Fecha : 27/09/2022                    ###
### Tema  : DEBER 1                       ###
### Ejercicio 2: Run Time  ###

import matplotlib.pyplot as plt

n=[1000,2000,4000,8000,16000,32000,64000]
run_time=[0.0,0.02,0.2,0.6,2.6,10.4,41.6]

'''
La funcion scattter se concentra en cada punto mientras
plot aplica las propiedades a todos los puntos 
'''
plt.scatter(n,run_time) 
plt.plot(n,run_time)
