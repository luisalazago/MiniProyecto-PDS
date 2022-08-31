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
    system("cls")
    print("===================================================")
    print("Bienvenido al modulo del Inventario. A continuacion digite el producto a evaluar.")
    print("===================================================")
    idProducto = int(input("Digite el id del producto: "))
    nombre, cantidad, capacidad, precio = obtenerProducto(idProducto)
    print("")
    print("===================================================")
    print("Nombre del producto: ".format(nombre))
    print("Cantidad del producto: ".format(cantidad))
    print("Capacidad maxima del producto: ".format(capacidad))
    print("Precio del producto: ".format(precio))
    print("===================================================")

if __name__ == "__main__":
    obtenerInventario()
    obtenerProducto(201000)