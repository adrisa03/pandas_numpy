import numpy as np

#lista = list(range(0,10)) #Crea una lista de 0 a 9
list =np.arange(0,10)
lista = np.arange(0,20)
lista = np.arange(0,20,2) #Crea una lista de 0 a 19 de dos en dos
lista = np.zeros(3) #Crea una lista de 3 ceros
lista = np.zeros((10,10)) #Crea una lista de 10x10 con ceros
lista = np.ones((10,5)) #Crea una lista de 10x5 con unos
lista = np.linspace(0,10,10)
lista = np.linspace(0,10,100)
lista = np.eye(4)
lista =np.random.rand()
lista =np.random.rand(4)
lista =np.random.rand(4,5)
lista =np.random.randint(1,15)
lista =np.random.randint(1,100,(10,10))
print (lista)

