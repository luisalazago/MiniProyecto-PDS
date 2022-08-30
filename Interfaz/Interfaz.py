"""
Interfaz temporal de la Empresa XYZ
"""

from os import system
from funciones_ventas import registrarVenta
from funciones_facturacion import facturarVenta
from funciones_inventario import revisarInventario
from funciones_informes import generarInformes, filtrarInformes

def main():
    system("cls")
    print("===================================================")
    print("Bienvenido a la Empresa XYZ")
    print("===================================================")
    print("A continuación aparecerá el menú de usuario:")
    print("1) Registrar venta.")
    print("2) Facturar venta.")
    print("3) Revisar inventario.")
    print("4) Generar informe.")
    print("5) Filtrar informes.")
    x = int(input("Seleccione un numero: "))
    while(x < 1 or x > 4):
        print("===================================================")
        print("El numero no esta permitido, por favor seleccione uno correcto.")
        print("1) Registrar venta.")
        print("2) Facturar venta.")
        print("3) Revisar inventario.")
        print("4) Generar informe.")
        print("5) Filtrar informes.")
        x = int(input("Seleccione un numero: "))
    print("===================================================")
    if(x == 1): registrarVenta()
    elif(x == 2): facturarVenta()
    elif(x == 3): revisarInventario()
    elif(x == 4): generarInformes()
    else: filtrarInformes()

main()