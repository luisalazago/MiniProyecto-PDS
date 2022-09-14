"""
Interfaz temporal de la Empresa XYZ
"""

from datetime import datetime
from funciones_ventas import registrarVenta
from funciones_inventario import revisarInventario
from funciones_informes import generarInformes, filtrarInformes, limpiarInformes

def main():
    estado_programa = True
    while(estado_programa):
        x = 0
        print("===================================================")
        print("Bienvenido a la Empresa XYZ")
        while(x < 1 or x > 6):
            print("===================================================")
            print("A continuación aparecerá el menú de usuario:")
            print("1) Registrar venta.")
            print("2) Revisar inventario.")
            print("3) Generar informe.")
            print("4) Filtrar informes.")
            print("5) Limpiar informes.")
            print("6) Salir del programa.")
            x = int(input("Seleccione un numero: "))
            if x < 1 or x > 6: print("El numero no esta permitido, por favor seleccione uno correcto.")
        print("===================================================")
        if(x == 1): registrarVenta()
        elif(x == 2): revisarInventario()
        elif(x == 3):
            fecha1 = datetime.now()
            fecha1 = "{}-{}-{}".format(str(fecha1.year), str(fecha1.month), str(fecha1.day)) 
            generarInformes(fecha1)
        elif(x == 4): filtrarInformes()
        elif(x == 5): limpiarInformes()
        else:
            print("")
            print("Se ha cerrado la sesion, vuelva pronto c:!")
            print("")
            estado_programa = False

main()