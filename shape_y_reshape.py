import numpy as np

#Generamos numeros aleatorios entre 1 y 10 con una estructura de 3x2
arr = np.random.randint(1,10,(3,2))
#Imprimimos el arreglo
print ("Forma original: ", arr.shape)
print (arr)
#Cambianmos la forma del arreglo a una forma de (1,6)
arr_reshaped = arr.reshape(1,6)
print ("Forma nueva del array con reshape: ", arr_reshaped)
print (arr)