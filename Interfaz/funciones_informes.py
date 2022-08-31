"""
Funciones para interactuar con la base de datos por ventas.
"""

import json
from datetime import datetime
from bd_conection import select

# Módulo de Informes
def filtro(tipo):
    pass

def obtenerProductos():
    sql = "SELECT * FROM reporteDiario()"
    ans1 = select(sql)
    sql = "SELECT * FROM reporteDiarioTotal()"
    ans2 = select(sql)
    print(ans1, ans2)
    return ans1, ans2
    

def filtrarInformes():
    print("===================================================")
    print("Bienvenido al modulo de filtrado de informes. A continuacion llene los datos para filtrar los infromes.")
    print("===================================================")
    tipo = str(input("Ingrese el tipo a filtrar: "))
    informes = filtro(tipo)
    print(informes)
    

def generarInformes():
    print("===================================================")
    print("Bienvenido al modulo de generacion de informes. A continuacion llene los datos para generar el informe.")
    print("===================================================")
    idProducto = int(input("Digite el id del producto: "))
    
    nombre, precio, tipo, cantidad_producto, cantidad_total = obtenerProductos(idProducto)
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
    archivo = open("../Bases_de_Datos/No_Relacionales/reportes.json", "a")
    archivo.write(json_object)
    archivo.close()

if __name__ == "__main__":
    obtenerProductos()