# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""
import random # se importa la libreria para poder generar numeros aleatorios 

def merge_sort(data):# esta version se pasa como parametro un arreglo de datos
    mid = len (data) //2 # se divide la mitad del arreglo
    if len(data)> 1: #preguntamos si la longitud del data es mayor a uno 
        L=data[mid:] # vamos a dividir el arreglo obteniendo los valores que se encuentran en la izquierda
        R=data[:mid] # los valores que se encuentran en la derecha del arreglo
        
        data.clear()
        # se hace dos llamadas recursivas 
        merge_sort(L) # le vamos a pasar el arreglo de la izquierda
        merge_sort(R) # le voy a pasar el arreglo de la derecha esto va ser que se dividadan todos esos arreglos 
        #hasta que todos los elemntos sean igual que uno
        
        #este bloque corresponde al proceso de fusion de los elementos
        while len(L)>0 and len(R)>0:# mientras la longitud del arreglo de la izquierda sea mayor a cero y la longitud del arreglo de la derecha sea mayor a cero
            if L[0]< R[0]: # preguntamos si el elemento  que se encuentra en la posicion cero del arreglo de la izquierda 
                #es menor al elemnto que se encuentra en la posicion cero del arreglo de la derecha
                data.append(L.pop(0)) #  lo que va ser es que va a agregar al arreglo data el lemnto que esta en la posicion cero de las reglas de la izquierda
                
            else:# si la instruccion no se cumple 
                data.append(R.pop(0)) # se va agregar el elemento de la posicion cero del arreglo de 
                #la derecha al arreglo data y lo mismo va eliminar ese elemnto de la posicion
                
        while len(L) >  0: # cuando la longitud de la regla de la izquierda sea mayor a cero va a agregar el arreglo data el elemento que se encuentre la posicion cero de la regla de la
           #izquierda y vuelve a entrar el ciclo se va actualizar la posicion ya que se esta eliminando
            data.append(L.pop(0))
           
        while len (R) > 0: # se pasa con el arreglo de la derecha
            data.append(R.pop(0))
        
    return data # retorna la lista ordenada
       
print (" \n******************************Mezcla Directa******************** \n")
data =[random.randint(-50, 50) for i in range(20)] #  se genera un arreglo un dato a la cual estoy generando
#numeros aleatorios que se encuentran de menos 5o,50 en un rango de 20 elementos
print(f"arreglo original:{data} \n") # se imprime el arreglo original para que se pueda notar cuales son los elementos que se generaron
x=merge_sort(data)
print(f"Arreglo ordenado:{x} \n") # se va imprimir el arreglo ordenado haciendo la llamada a la funcion
# version bajo short pasandole como parametro el arreglo de datos
