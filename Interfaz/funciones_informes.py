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
    print("Bienvenido al modulo de generacion de informes. Se va a generar el reporte de las ventas del dia.")
    print("===================================================")
    
    reporte, precio_total = obtenerProductos()
    fecha = datetime.now()
    informe = {
        "nombre": reporte[0][0],
        "precio": reporte[0][2],
        "tipo": reporte[0][3],
        "cantidad_producto": reporte[0][1],
        "fecha": fecha,
        "precio_total": precio_total[0][0]
    }
    
    json_object = json.dump(informe, indent = 4)
    archivo = open("../Bases_de_Datos/No_Relacionales/reportes.json", "a")
    archivo.write(json_object)
    archivo.close()
    print("Se ha generado el informe con exito!")

if __name__ == "__main__":
    generarInformes()
