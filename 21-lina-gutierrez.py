import random

# LA NECESITO PARA PODER CALCULAR LA FUNCION 21 => 06 - función que calcule el rango del vector obtenido en genrnd.
def rangeVector (vector): 
    vector = sorted(vector)
    res = [vector[0], vector[-1]]
    return res

#  21 - función que calcule devuelva el mínimo del vector obtenido en genrnd..
def minVector (vector): 
    return rangeVector(vector)[0]

#### TESTING ####

# LA NECESITO PARA PODER TESTEAR LA FUNCION 21 => función genrnd que retorna una lista con 50 números aleatorios.
def genrnd(): 
    listArray = []
    for i in range(50):
        listArray.append(random.randint(-500, 500))
    return listArray

vector = genrnd()

print('Resultado de la actividad 21 =>', minVector (vector))