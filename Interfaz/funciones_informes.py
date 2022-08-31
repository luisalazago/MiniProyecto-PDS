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

def limpiarInformes():
    print("")
    print("===================================================")
    archivo = open("../Bases_de_Datos/No_Relacionales/reportes.json", "w")
    archivo.write("")
    archivo.close()
    print("Se ha limpiado el archivo reportes.json")
    print("===================================================")
    print("")

def generarInformes():
    print("===================================================")
    print("Bienvenido al modulo de generacion de informes. Se va a generar el reporte de las ventas del dia.")
    print("===================================================")
    
    reporte, precio_total = obtenerProductos()
    fecha1 = datetime.now()
    fecha2 = "{}-{}-{}".format(str(fecha1.year), str(fecha1.month), str(fecha1.day))
    informe_final = {}
    for informe in reporte:
        temp = {
            "precio": str(informe[2]),
            "tipo": informe[3],
            "cantidad_producto": str(informe[1]),
        }
        informe_final[informe[0]] = temp
    informe_final["precio_total"] = str(precio_total[0][0])
    informe_final["fecha"] = fecha2
    
    json_object = json.dumps(informe_final, indent = 4)
    archivo = open("../Bases_de_Datos/No_Relacionales/reportes.json", "a")
    archivo.write(json_object)
    archivo.write("")
    archivo.close()
    print("Se ha generado el informe con exito!")

if __name__ == "__main__":
    generarInformes()
