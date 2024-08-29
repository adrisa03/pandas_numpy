import numpy as np
#Escalor 0 dimensiones
scalar = np.array(42)
print(scalar)
print(scalar.ndim)

#Vector 1 dimensiones
vector = np.array([1,2,3])
print(vector)
print(vector.ndim)

#Matriz 2 dimensiones
matriz = np.array([[1,2,3],[4,5,6]])
print(matriz)
print(matriz.ndim)

#Tensor 3 dimensiones
tensor = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(tensor)
print(tensor.ndim)

#Agregar y eliminar dimensiones
vector = np.array([1,2,3],ndmin=10)
print(vector)
print(vector.ndim)

#Expandir
expand = np.expand_dims(np.array([1,2,3]),axis=0)
print (expand)
print (expand.ndim)

#Eliminar dimensiones innecesarias
print (vector, vector.ndim)
vector_2 = np.squeeze(vector)
print(vector_2, vector_2.ndim)




