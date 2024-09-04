import numpy as np
arr = np.arange(0,11)
print (arr)
trozo_de_arr = arr[0:6]
print (trozo_de_arr)
#a todo el array le ponemos valores en 0
trozo_de_arr[:] = 0
print (trozo_de_arr)
#imprimimos todo el array y observamos que todos los valorse se cambiaron
print(arr)
#Utilizamos Copy para solucionar esto
arr_copy = arr.copy()
arr_copy[:] = 100
print (arr_copy)
#La lista original no se modifico
print (arr)
