"""
Funciones para interactuar con la base de datos por ventas.
"""

from os import system
from datetime import datetime
import json

from Interfaz.funciones_inventario import obtenerProducto

# Módulo de Informes
def filtro(tipo):
    pass

def obtenerProducto(idProducto):
    pass

def filtrarInformes():
    system("cls")
    print("===================================================")
    print("Bienvenido al modulo de filtrado de informes. A continuacion llene los datos para filtrar los infromes.")
    print("===================================================")
    tipo = str(input("Ingrese el tipo a filtrar: "))
    informes = filtro(tipo)
    print(informes)
    

def generarInformes():
    system("cls")
    print("===================================================")
    print("Bienvenido al modulo de generacion de informes. A continuacion llene los datos para generar el informe.")
    print("===================================================")
    idProducto = int(input("Digite el id del producto: "))
    
    nombre, precio, tipo, cantidad_producto, cantidad_total = obtenerProducto(idProducto)
    fecha = datetime.now()
    informe = {
        "nombre": nombre,
        "precio": precio,
        "tipo": tipo,
        "cantidad_producto": cantidad_producto,
        "fecha": fecha,
        "cantidad_total": cantidad_total,
        "idProducto": idProducto
    }
    
    json_object = json.dump(informe, indent = 4)
    archivo = open("Bases de Datos\No Relacionales\reportes.json", "a")
    archivo.write(json_object)
    archivo.close()