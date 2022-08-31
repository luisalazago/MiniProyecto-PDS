"""
Funciones para interactuar con la base de datos por ventas.
"""

from os import system
from datetime import datetime
from random import randint
from funciones_facturacion import anadir_bd
from bd_conection import insert, select

# Módulo de Ventas.
def venta():
    print("")
    print("===================================================")
    id_producto = int(input("Digite el id del producto: "))
    cantidad_gastada = int(input("Digite la cantidad que se compro: "))
    print("===================================================")
    print("")
    return (id_producto, cantidad_gastada)

def registrarVenta():
    lista_de_productos = []
    system("cls")
    print("===================================================")
    print("Bienvenido al registro de ventas. Por favor digite los siguientes datos.")
    print("===================================================")
    cant_prod = int(input("Cuantos tipos de productos va a registrar: "))
    
    for _ in range(cant_prod):
        lista_de_productos.append(venta())
    
    print("===================================================")
    
    fecha1 = datetime.now()
    fecha2 = "{}-{}-{}".format(str(fecha1.year), str(fecha1.month), str(fecha1.day))
    id_cliente_venta = randint(1000000000, 9999999999)
    id_usuario = 1000000000
    infoVenta = ""
    sql = """insert into registroventa(usuario, idcliente_venta, infoventa, fecha)
             values (%s, %s, %s, %s)"""
    record = (id_usuario, id_cliente_venta, infoVenta, fecha2)
    rowcolum = 0
    if insert(sql, record) != -1:
        rowcolum = select("""SELECT max(idregistro) FROM registroventa""")
    print("rowcolum es", rowcolum[0][0])
    lista_de_productos = anadir_bd(rowcolum[0][0], lista_de_productos)
    venta_total = [lista_de_productos[0], lista_de_productos[1], id_cliente_venta, id_usuario, fecha2] # Falta el id del usuario que se debe obtener por el sistema.
    return venta_total

if __name__ == "__main__":
    print(registrarVenta())