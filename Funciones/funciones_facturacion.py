"""
Funciones para interactuar con la base de datos por facturación.
"""

from bd_conection import select, insertMany

# Módulo de facturación (siguiente sprint)
def anadir_bd(rowcolum, lista_de_productos):
    sql = """insert into venta(idventa, idproducto, cantidad)
             values (%s, %s, %s)"""
    record = []
    for ide, c in lista_de_productos: record.append((rowcolum, ide, c))
    n = insertMany(sql, record)
    if n != -1:
        return obtenerVentas(rowcolum)
    return [[], []]

def obtenerVentas(idRegistro):
    sql1 = "SELECT * FROM facturar(%s)"
    factura = [(idRegistro)]
    sql2 = "SELECT * FROM total(%s)"
    ans1 = select(sql1, factura)
    ans2 = select(sql2, factura)
    return ans1, ans2

