"""
Funciones para interactuar con la base de datos por facturación.
"""

from os import system
from bd_conection import select

# Módulo de facturación (siguiente sprint)
def anadir_bd():
    pass

def obtenerVentas(idRegistro):
    sql = "SELECT * FROM facturar(%s)"
    factura = [(idRegistro)]
    sql = "SELECT * FROM total(%s)"
    total = [idRegistro]
    ans1 = select(sql, factura)
    ans2 = select(sql, total)
    print(ans1, ans2)
    return ans1, ans2

def facturarVenta():
    system("cls")
    print("===================================================")
    print("Bienvenido al modulo de facturacion. A continuacion seleccione la venta a facturar")
    print("===================================================")
    #idRegistro = int(input("Digite el numero del registro: "))
    #Se debe hacer automaticamente desde la base de datos
    venta_total = obtenerVentas(0)
    print(venta_total)
    