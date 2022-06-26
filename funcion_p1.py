# 9- función p1, retorna el producto de los 2 primero más el 3er parámetros, usando las
#funciones anteriores.

from Funcion_producto import multiplicacion
n1=int(input("ingrese un numero:"))
n2=int(input("ingrese un numero:"))
n3=int(input("ingrese un numero:"))

def suma (n1,n2):
    return n1+n2
def producto_suma (n1, n2, n3): 
    return suma(multiplicacion(n1,n2),n3)

print("Resultado de la actividad 09 = ", producto_suma(n1, n2,n3))
