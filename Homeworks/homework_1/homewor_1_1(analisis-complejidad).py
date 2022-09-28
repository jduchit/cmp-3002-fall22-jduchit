###          ESTRUCTURA DE DATOS          ###
### Nombre: Johana Duchi Tipan            ###
### Fecha : 27/09/2022                    ###
### Tema  : DEBER 1                       ###
### Ejercicio 1: Análisis de complejidad  ###

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
                          
#Se define el data frame con datos bidimensionales (filas y columnas)
r = pd.DataFrame()
r['n1'] = np.arange(1,100,10)

#Se definen las 2 funciones a comparar
r['nlog(n)'] = (np.arange(1,100,10)) * (np.log2(np.arange(1,100,10)))
r['n^2'] = np.power(((np.arange(1,100,10))),2)

#Se traza el grafico
r.plot(x='n1', logy=True, lw=2, figsize=(12, 6))
plt.grid()                

