"""
Interfaz temporal de la Empresa XYZ
"""

import sys
from os import system
from funciones_ventas import registrarVenta
from funciones_facturacion import facturarVenta
from funciones_inventario import revisarInventario
from funciones_informes import generarInformes, filtrarInformes
from bd_conection import select 

def main():
    # print("===================================================")
    # print("Bienvenido a la Empresa XYZ")
    # print("===================================================")
    # print("A continuación aparecerá el menú de usuario:")
    # print("1) Registrar venta.")
    # print("2) Facturar venta.")
    # print("3) Revisar inventario.")
    # print("4) Generar informe.")
    # print("5) Filtrar informes.")
    # x = 0
    # try: x = int(input("Seleccione un numero: "))
    # except: x = 0
    # while(x < 1 or x > 5):
    #     print("===================================================")
    #     print("El numero no esta permitido, por favor seleccione uno correcto.")
    #     print("1) Registrar venta.")
    #     print("2) Facturar venta.")
    #     print("3) Revisar inventario.")
    #     print("4) Generar informe.")
    #     print("5) Filtrar informes.")
    #     try: x = int(input("Seleccione un numero: "))
    #     except: x = 0
    # print("===================================================")
    # if(x == 1): registrarVenta()
    # elif(x == 2): facturarVenta()
    # elif(x == 3): revisarInventario()
    # elif(x == 4): generarInformes()
    # else:
    select("""SELECT * FROM VENTA""", "", "venta") 

main()