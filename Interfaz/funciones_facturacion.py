"""
Funciones para interactuar con la base de datos por facturación.
"""

from os import system

# Módulo de facturación
def anadir_bd():
    pass

def obtenerVentas(idRegistro):
    pass

def facturarVenta():
    system("cls")
    print("===================================================")
    print("Bienvenido al modulo de facturacion. A continuacion seleccione la venta a facturar")
    print("===================================================")
    #idRegistro = int(input("Digite el numero del registro: "))
    #Se debe hacer automaticamente desde la base de datos
    venta_total = obtenerVentas(0)
    print(venta_total)
    