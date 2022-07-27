#Desarrollar una función P1_RESTA que retorne la resta de los 2 primeros por el 3er parámetro, 
#usando las funciones anteriores.
from resta import resta
from producto import multiplicacion

def p1_resta(n1,n2,n3):
    resultadoResta=resta(n1,n2)
    resultadoProducto=multiplicacion(resultadoResta,n3)
    return resultadoProducto
