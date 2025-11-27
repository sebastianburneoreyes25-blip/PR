import random
import numpy as np

MAXIMOTABLERO = 19

def colocarBarco(barco, posiciones):
    
    #posiciones es una lista que contiene tuplas de tuplas
    #ejemplo:
    #lista[0] = ((0,1),(1,0))
    
    colocado = False
    
    while not colocado:
    
        fila_correcta = False
        
        while not fila_correcta:
            #fila de inicio y de fin del barco, el fin será siempre la fila de inicio más el tamaño del barco menos 1 porque inicial está incluida
            fila_inicio = random.randint(0, MAXIMOTABLERO)
            fila_fin = fila_inicio + barco - 1
            
            if fila_fin <= MAXIMOTABLERO:
                fila_correcta = True
        
        
        columna_inicio = random.randint(0, MAXIMOTABLERO)
        columna_fin = columna_inicio   #como todos los barcos van en vertical, la columna inicial y la final son iguales.
        
        inicio = (fila_inicio, columna_inicio)
        fin = (fila_fin, columna_fin)
        
        posicion_barco = (inicio, fin)
        
        hay_colision = False
        
        for (inicio_existente, fin_existente) in posiciones:
            
            fila_inicio_existente, columna_inicio_existente = inicio_existente
            fila_fin_existente, columna_fin_existente = fin_existente
                    
            if columna_inicio_existente == columna_inicio:
                #recorremos las filas de nuestro nuevo barco
                if [fila_inicio,fila_fin].any()==barco:#Usamos la funcion any para determinar si hay un barco en las filas seleccionadas 
                                                       #Evitamos el uso de los bucles.
                    hay_colision=True
                        
        if not hay_colision:
            posiciones.append(posicion_barco)
            colocado = True     
            
    return posiciones   