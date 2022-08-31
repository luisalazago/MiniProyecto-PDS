"""
Interfaz temporal de la Empresa XYZ
"""

import sys
from os import system
from funciones_ventas import registrarVenta
from funciones_facturacion import facturarVenta
from funciones_inventario import revisarInventario
from funciones_informes import generarInformes, filtrarInformes, limpiarInformes
from bd_conection import select 

def main():
    # estado_programa = True
    # while(estado_programa):
    #     system("cls")
    #     print("===================================================")
    #     print("Bienvenido a la Empresa XYZ")
    #     print("===================================================")
    #     print("A continuación aparecerá el menú de usuario:")
    #     print("1) Registrar venta.")
    #     print("2) Facturar venta.")
    #     print("3) Revisar inventario.")
    #     print("4) Generar informe.")
    #     print("5) Filtrar informes.")
    #     print("6) Limpiar informes.")
    #     print("7) Salir del programa.")
    #     x = 0
    #     try: x = int(input("Seleccione un numero: "))
    #     except: x = 0
    #     while(x < 1 or x > 5):
    #         print("===================================================")
    #         print("El numero no esta permitido, por favor seleccione uno correcto.")
    #         print("1) Registrar venta.")
    #         print("2) Facturar venta.")
    #         print("3) Revisar inventario.")
    #         print("4) Generar informe.")
    #         print("5) Filtrar informes.")
    #         print("6) Limpiar informes.")
    #         print("7) Salir del programa.")
    #         try: x = int(input("Seleccione un numero: "))
    #         except: x = 0
    #     print("===================================================")
    #     if(x == 1): registrarVenta()
    #     elif(x == 2): facturarVenta()
    #     elif(x == 3): revisarInventario()
    #     elif(x == 4): generarInformes()
    #     elif(x == 5): filtrarInformes()
    #     elif(x == 6): limpiarInformes()
    #     else:
    #         print("")
    #         print("Se ha cerrado la sesion, vuelva pronto c:!")
    #         estado_programa = False
    select("""SELECT * FROM VENTA""", "", "venta") 

main()