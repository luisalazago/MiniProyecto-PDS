import funciones_facturacion
import funciones_informes
import funciones_inventario
import funciones_ventas
import usuario


def test1():
    lista_de_productos = [(201000, 2)]
    id_usuario = 1000
    funciones_ventas.registrarVenta(lista_de_productos, id_usuario)

def test2():
    funciones_facturacion.obtenerVentas(1)

def test3():
    fecha = "2023-5-24"
    funciones_informes.generarInformes(fecha)
    archivo = "../Bases_de_Datos/No_Relacionales/reporte{}.json".format(fecha)
    funciones_informes.filtrarInformes(archivo, "2000")

def test4():
    funciones_inventario.revisar_inventario()
    funciones_inventario.revisar_inventario(201000)

def test5():
    usuario.traer_nombre(0)
    usuario.traer_nombre(1000000001)
    usuario.verificar_contrasena(1000000001, 1234)
    usuario.verificar_contrasena(1000000001, 1233)
    usuario.verificar_contrasena(10000000, 1234)
    usuario.is_admin(1000000001)

if __name__ == "__main__":
    test1()
    test2()
    test3()
    test4()
    test5()