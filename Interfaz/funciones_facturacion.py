"""
Funciones para interactuar con la base de datos por facturación.
"""

from os import system
from datetime import datetime

# Módulo de facturación
def obtenerVentas(idRegistro):
    pass

def facturarVenta():
    system("cls")
    print("===================================================")
    print("Bienvenido al modulo de facturacion. A continuacion seleccione la venta a facturar")
    print("===================================================")
    idRegistro = int(input("Digite el numero del registro: "))
    venta_total = obtenerVentas(idRegistro)
    print(venta_total)
    