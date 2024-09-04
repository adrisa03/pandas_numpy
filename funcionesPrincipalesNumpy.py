import numpy as np
#Definamos numereos aleatorios del 1 a l 20  en un vector
arr =np.random.randint(1,20,10)
print (arr)
#Ahora llevamos el vector a una estructura matricial
matriz = arr.reshape(2,5)
print (matriz)
#Con max obtenemos el valor maximo del arreglo
maximo = arr.max()
print (maximo)
maximo = matriz.max()
print (maximo)
#Creamos un array de dos dimensiones
a = np.array([[1,2],[3,4]])
b = np.array([[5,6]])
#concatenamos los dos arrays con concatenate por el eje 0 axis
c = np.concatenate((a,b),axis=0)
print (c)
#concatenamos los dos arrays con concatenate por el eje 1 axis
d = np.concatenate((a,b),axis=1)
print (d)
#Transponemos el array
e = np.transpose(a)
print (e)
#Transponemos el array
print (a)
