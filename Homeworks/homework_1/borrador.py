def mide_tiempo(funcion):
    def funcion_medida(*args, **kwargs):
        inicio = time.time() #primera variable del time 
        c = funcion(*args, **kwargs) 
        print(time.time() - inicio) #hora de inicio y hora de fin
        return c
    return funcion_medida
