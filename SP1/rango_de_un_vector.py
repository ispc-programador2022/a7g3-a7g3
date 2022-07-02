lista = [1,2,3,4,5,6]

def elementos(list):
    contador = 0
    for element in list:
        contador+= 1
    return contador

print("la cantidad de elementos en el vector es: ", elementos(lista))