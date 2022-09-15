"""
Funciones para interactuar con la base de datos para el inventario.
"""

from bd_conection import select

# Módulo del Inventario
def obtenerProducto(idProducto):
    """
    Función que obtiene la información de un unico producto de la BD
    Entradas:
        idProducto: codigo de indentificación del producto que se quiere
                    buscar
    Salida:
        ans: list<tuple> con la información del producto buscado. La información
             viene con la tupla codigoBarra, nombre, precio, cantidad, tipo
             Si el ID no esta en la BD devuelve una lista vacia
    """
    sql = """SELECT * FROM retornarinvPro(%s)"""
    datos = [(idProducto)]
    ans = select(sql, datos)
    return ans

def obtenerInventario():
    """
    Función que obtiene la información de todos los productos de la BD
    Entradas: None
    Salida:
        ans: list<tuple> con la información de todos los productos. La información
             viene con la tupla codigoBarra, nombre, precio, cantidad, tipo
    """
    sql = """SELECT * FROM retornarinv()"""
    ans = select(sql)
    return ans

def revisar_inventario(idProducto = None):
    """
    Función que obtiene la información de todos los productos de la BD
    Entradas: idProducto es el identificador del producto que se quiere buscar. Por
              defecto el valor a buscar es None que refiere a que se quiere ver todos
              los productos. Si este no es None se buscara un unico elemento
    Salida:
        informe: list<dic()> con la información de todos los productos. La información
                 es entregada de la siguiente manera:
                 id_prod, name_prod, cant_prod, cap_prod, price_prod
    """
    datos, informe = None, []
    if idProducto == None: datos = obtenerInventario()
    else: datos = obtenerProducto(idProducto)
    for lista in datos:
        temp = {}
        temp["id_prod"] = str(lista[0]).strip(" ")
        temp["name_prod"] = str(lista[1]).strip(" ")
        temp["cant_prod"] = str(lista[3]).strip(" ")
        temp["cap_prod"] = str(lista[4]).strip(" ")
        temp["price_prod"] = str(lista[2]).strip(" ")
        informe.append(temp)
    return informe

def revisarInventario1():
    """
    Pruebas locales Eliminar despues
    """
    des = int(input("Digite la opcion: "))
    while(des > 2 or des < 1):
        print("")
        print("Por favor digite un numero correcto.")
        des = int(input("Digite la opcion: "))
    print("")
    
    if(des == 2):
        idProducto = int(input("Digite el id del producto: "))
        lista = obtenerProducto(idProducto)
        print("")
        print("===================================================")
        print("Nombre del producto: {}".format(lista[0][0]))
        print("Cantidad del producto: {}".format(lista[0][1]))
        print("Capacidad maxima del producto: {}".format(lista[0][2]))
        print("Precio del producto: {}".format(lista[0][3]))
        print("===================================================")
    else:
        inventario = obtenerInventario()
        print("===================================================")
        print("Inventario disponible de la empresa XYZ")
        for lista in inventario:
            print("#####################################")
            print("Codigo del producto: {}".format(lista[0]))
            print("Nombre del producto: {}".format(lista[1]))
            print("Precio del producto: {}".format(lista[2]))
            print("Cantidad disponible del producto: {}".format(lista[3]))
            print("Tipo de producto: {}".format(lista[4]))
            print("#####################################")
        print("===================================================")
             

if __name__ == "__main__":
    print(obtenerInventario(), "´p")
    print(obtenerProducto(201000),"px")
    #print(revisar_inventario())
    #print(revisar_inventario(201000))
    #print(revisar_inventario(201010))
