"""
Funciones para interactuar con la base de datos por ventas.
"""

from os import system
from datetime import datetime
from random import randint
from funciones_facturacion import anadir_bd
from bd_conection import insert, select

# Módulo de Ventas.

def registrarVenta(lista_de_productos, id_usuario, id_cliente_venta = "", info_venta = ""): 
    fecha = datetime.now()
    fecha = "{}-{}-{}".format(str(fecha.year), str(fecha.month), str(fecha.day))
    sql = """insert into registroventa(usuario, idcliente_venta, infoventa, fecha)
             values (%s, %s, %s, %s)"""
    record = (id_usuario, id_cliente_venta, info_venta, fecha)
    rowcolum = 0
    if insert(sql, record) != -1:
        rowcolum = select("""SELECT max(idregistro) FROM registroventa""")
        lista_de_productos = anadir_bd(rowcolum[0][0], lista_de_productos)
    # venta_total = [lista_de_productos[0], lista_de_productos[1], id_cliente_venta, id_usuario, fecha2] # Falta el id del usuario que se debe obtener por el sistema.
    else:
        lista_de_productos = []
    return (lista_de_productos, rowcolum)
