"""
Funciones para interactuar con la base de datos para el inventario.
"""

from os import system
from bd_conection import select

# Módulo del Inventario
def obtenerProducto(idProducto):
    sql = """SELECT * FROM retornarinvPro(%s)"""
    datos = [(idProducto)]
    ans = select(sql, datos)
    print(ans)
    return ans

def obtenerInventario():
    sql = """SELECT * FROM retornarinv()"""
    ans = select(sql)
    print(ans)
    return ans

def revisarInventario():
    print("===================================================")
    print("Bienvenido al modulo del Inventario. A continuacion digite el producto a evaluar.")
    print("===================================================")
    print("Que desea hacer a continuacion: ")
    print("1) Revisar todo el inventario.")
    print("2) Revisar el inventario de un solo proudcto.")
    des = int(input("Digite la opcion: "))
    while(des > 2 or des < 1):
        print("")
        print("Por favor digite un numero correcto.")
        des = int(input("Digite la opcion: "))
    print("")
    
    if(des == 2):
        idProducto = int(input("Digite el id del producto: "))
        lista = obtenerProducto(idProducto)
        print("")
        print("===================================================")
        print("Nombre del producto: {}".format(lista[0]))
        print("Cantidad del producto: {}".format(lista[1]))
        print("Capacidad maxima del producto: {}".format(lista[2]))
        print("Precio del producto: {}".format(lista[3]))
        print("===================================================")
    else:
        inventario = obtenerInventario()
        print("===================================================")
        print("Inventario disponible de la empresa XYZ")
        for lista in inventario:
            print("#####################################")
            print("Codigo del producto: {}".format(lista[0]))
            print("Nombre del producto: {}".format(lista[1]))
            print("Precio del producto: {}".format(lista[2]))
            print("Cantidad disponible del producto: {}".format(lista[3]))
            print("Tipo de producto: {}".format(lista[4]))
            print("#####################################")
        print("===================================================")
             

if __name__ == "__main__":
    obtenerInventario()
    obtenerProducto(201000)
    revisarInventario()
