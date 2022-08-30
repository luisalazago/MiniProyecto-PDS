"""
Funciones para interactuar con la base de datos para el inventario.
"""

from os import system

# Módulo del Inventario
def obtenerProducto(idProducto):
    pass

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
    