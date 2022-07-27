# LA NECESITO PARA PODER CALCULAR LA FUNCION 21 => 06 - función que calcule el rango del vector obtenido en genrnd.
def rangeVector (vector): 
    vector = sorted(vector)
    res = [vector[0], vector[-1]]
    return res

#  21 - función que calcule devuelva el maximo del vector obtenido en genrnd.
def maxVector (vector): 
    return rangeVector(vector)[1]