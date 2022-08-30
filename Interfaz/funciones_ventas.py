"""
Funciones para interactuar con la base de datos por ventas.
"""

from os import system
from datetime import datetime
from random import randint

# Módulo de Ventas.
def venta():
    print("")
    print("===================================================")
    id_producto = int(input("Digite el id del producto: "))
    cantidad_gastada = int(input("Digite la cantidad que se compro: "))
    print("===================================================")
    print("")
    return [id_producto, cantidad_gastada]

def registrarVenta():
    lista_de_productos = []
    system("cls")
    print("===================================================")
    print("Bienvenido al registro de ventas. Por favor digite los siguientes datos.")
    print("===================================================")
    cant_prod = int(input("Cuantos tipos de productos va a registrar: "))
    
    for i in range(cant_prod):
        lista_de_productos.append(venta())
    
    print("===================================================")
    precio_total = int(input("Ingrese el precio total: "))
    
    fecha = datetime.now()
    id_cliente_venta = randint(1000000000, 9999999999)
    idRegistro = randint(1000000000, 9999999999)
    
    while(id_cliente_venta == idRegistro): idRegistro = randint(1000000000, 9999999999)
   
    venta_total = [idRegistro, precio_total, lista_de_productos, id_cliente_venta, fecha] # Falta el id del usuario que se debe obtener por el sistema.
    return venta_total