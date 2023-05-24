"""
Funciones para interactuar con la base de datos por ventas.
"""

import json
from datetime import datetime
from bd_conection import select

# Módulo de Informes
def filtro(data, tipo=None):
    """
    Filto sobre una lista de productos
    Entradas:
        data: list<dic()> con la información de la venta de los productos en un
              informe
        tipo: str con el codigo de la categoria que se quiere filtar. Si el no
              se define el tipo se asume que se quiere mostrar todo
    Salida:
        ans: list<dic()> con los productos que estan asociados al tipo que se
             quiere filtrar
    """
    ans = []
    if tipo == None: ans = data
    else:
        for a in data:
            if a['tipo_cod'] == tipo: ans.append(a)
        if len(ans) == 0: ans = data
    return ans


def obtenerProductos(fecha):
    """
    Función que obtiene de la BD la información de los productos vendidos en la
    fecha de hoy
    Entrada:
        fecha: str es la fecha de la cual se quieren hallar las ventas. El formato es
        año-mes-dia, ejemplo: 2022-9-14
    Salida:
        ans1: lista<tuple> con la información de los porductos donde se trae
              nombre, cantidad, precio, tipo, cod_tipo en ese orden
            ejemplo:
            ('Smirnoff            ', Decimal('1'), Decimal('40000'), 'Bebidas             ', Decimal('1000')),
        ans2: Decimal que es el total de las ventas realizadas en el dia
    """
    sql, sql2 = "SELECT * FROM reporteDiario(%s)", "SELECT * FROM reporteDiarioTotal(%s)"
    ans1, ans2 = select(sql, [fecha]), select(sql2, [fecha])
    return ans1, ans2

def filtrarInformes(archivo, tipo = None):
    """
    Función que filta un informe segun el tipo que se quiera
    Entradas:
        archivo: str con el nombre de un informe
        tipo: str el código del tipo que se quiere filtrar
    Salidas
        informe: dic() con el formato del informe donde se enviaran los productos
                 junto con el precio total de esos productos y la fecha del informe
                 Si no se asigno un tipo se devolvera el informe completo. De lo
                 contrario se enviara el informe filtrado
    """
    informe = {"productos": [], "precio_total": "0", "fecha": ""}
    try:
        file = open(archivo)
        informe, suma = json.load(file), 0
        fecha = informe["fecha"]
        data = filtro(informe["productos"] ,tipo)
        informe["productos"] = data
        for a in data: suma += int(a["total"])
        informe["precio_total"] = str(suma)
        informe["fecha"] = fecha
    except: print("""FileNotFoundError: [Errno 2] No such file or directory: '{}'""".format(archivo))
    return informe

def limpiarInformes():
    fecha1 = datetime.now()
    fecha1 = "{}-{}-{}".format(str(fecha1.year), str(fecha1.month), str(fecha1.day))
    archivo = open("../Bases_de_Datos/No_Relacionales/{}.json".format("reporte" + fecha1), "w")
    archivo.write("")
    archivo.close()

def generarInformes(fecha): 
    """
    Función que genera el informe de la venta del dia dada una fecha
    Entradas:
        fecha: str es la fecha de la cual se quiere hacer el informe. El formato es
        año-mes-dia, ejemplo: 2022-9-14
    Salida:
        archivo: .json con el informe de la fecha administrada siempre y cuando
                 hubieran ventas ese dia. El .json se guarda de manera local
                 en la carpeta ../Bases_de_Datos/No_Relacionales/
    """
    try:
        reporte, precio_total = obtenerProductos(fecha)
        informe_final = {}
        informe_final["productos"] = []
        for informe in reporte:
            temp = {
                "nombre": informe[0].strip(" "),
                "tipo": informe[3].strip(" "),
                "tipo_cod": str(informe[4]),
                "cantidad_producto": str(informe[1]),
                "total": str(informe[2])
            }
            informe_final["productos"].append(temp)
        informe_final["precio_total"] = str(precio_total[0][0])
        informe_final["fecha"] = fecha
        
        json_object = json.dumps(informe_final, indent = 4)
        archivo = open("../Bases_de_Datos/No_Relacionales/{}.json".format("reporte" + fecha), "w")
        archivo.write(json_object)
        archivo.close()
    except: print("""ErrorCreandoArchivo: [Errno 2] no ventas ese dia: '{}'""".format(fecha))
