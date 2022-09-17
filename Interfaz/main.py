# Bibliotecas y módulos usados para la aplicación web
from flask import Flask, redirect, url_for, render_template, request
from datetime import datetime

import json
import sys
sys.path.append("../Funciones")
from usuario import verificar_contrasena, is_admin, traer_nombre
from funciones_inventario import revisar_inventario
from funciones_informes import obtenerProductos, generarInformes

# Variables Globales
app = Flask(__name__)
usuario_activo = None
nombre_activo = ""
rol = None
fallo = False # Fallo usado para el login.

# Funciones auxiliares
def adminReturn(val):
    ans = "empleado"
    if val: ans = "admin"
    return ans

# Rutas principales
@app.route("/")
def login():
    global fallo
    texto = ""
    if fallo:
        texto = "Por favor digite un usuario existente."
        fallo = False
    return render_template("index.html", content = texto)

@app.route("/home", methods = ["POST", "GET"])
def home():
    """
    Esta es la página principal de la aplicación.
    """
    global fallo, usuario_activo, rol, nombre_activo
    if(usuario_activo != None): return render_template("home.html", user = usuario_activo, 
                                                                    rol = rol,
                                                                    nombre = nombre_activo)
    usuario = request.form["user"]
    contra = request.form["contra"]
    if verificar_contrasena(usuario, contra):
        usuario_activo = usuario # Cédula del usuario que está activo en la sesión. 
        rol = adminReturn(is_admin(usuario)) # Rol del usuario activo.
        nombre_activo = traer_nombre(usuario) # Nombre del usuario activo.
        return render_template("home.html", rol = rol, nombre = nombre_activo)
    else: fallo = True
    return redirect(url_for("login"))

# Rutas Ventas
@app.route("/ventas")
def ventas():
    """
    Este es el módulo de ventas.
    """
    return render_template("ventas.html")

# Rutas Inventario
@app.route("/inventario")
def inventario():
    """
    Página principal del inventario.
    """
    return render_template("inventario.html", rol = rol)

@app.route("/inventario/des_inventario", methods = ["POST", "GET"])
def des_inventario():
    """
    Muestra la página para buscar la información de un producto o redirecciona
    a la función para mostrar la información de todos los productos.
    """
    if("un_producto" in request.form):
        return render_template("ingresar_producto.html", rol = rol, fallo = False)
    else:
        return redirect(url_for("todos_productos"))

@app.route("/inventario/des_inventario/un_producto", methods = ["POST"])
def un_producto():
    """
    Muestra el error ingresado en la página para buscar el producto o muestra
    la información del producto porque la búsqueda fue exitosa.
    """
    id_producto = request.form["id_producto"]
    temp = id_producto
    producto = []
    if(temp != ''):
        id_producto = int(id_producto)
        producto = revisar_inventario(id_producto)
        print(producto)
    if(not len(producto) or temp == ''):
        return render_template("ingresar_producto.html ", rol = rol, fallo = True)
    return render_template("un_producto.html", nombre = producto[0]["name_prod"], id_producto = producto[0]["id_prod"],
                                               cantidad =  producto[0]["cant_prod"], categoria =  producto[0]["cap_prod"],
                                               precio =  producto[0]["price_prod"], rol = rol)

@app.route("/inventario/des_inventario/todos_productos", methods = ["POST", "GET"])
def todos_productos():
    """
    Mustra en cards la información de todos los productos de la
    base de datos.
    """
    inventario_productos = revisar_inventario()
    return render_template("todo_productos.html", rol = rol, inventario = inventario_productos)

# Rutas Informes
@app.route("/informes", methods = ["POST", "GET"])
def informes():
    """
    Página principal del módulo de informes.
    """
    return render_template("informes.html", rol = rol)

@app.route("/informes/des_informes", methods = ["POST"])
def des_informes():
    """
    Redireccina a la función de generar informe actual o muestra
    la página para hacer el filtro de los informes según el
    tipo.
    """
    if("generar" in request.form):
        return redirect(url_for("generar_informes"))
    else:
        return redirect(url_for("ingresar_filtro")) 

@app.route("/informes/des_informes/informe_generado", methods = ["POST", "GET"])
def generar_informes():
    """
    Genera el informe actual con los productos vendidos.
    """
    fecha2 = "2019-09-16"
    fecha = datetime.now()
    fecha = str(fecha.year) + "-" + str(fecha.month) + "-" + str(fecha.day)
    generarInformes(fecha)
    fallo_informe = 'False'
    productos = open("../Bases_de_Datos/No_Relacionales/reporte{}.json".format(fecha))
    productos = json.load(productos)
    print(productos)
    if(not len(productos["productos"])): fallo_informe = 'True'
    return render_template("generar_informe.html", rol = rol, productos = productos, fallo = fallo_informe)

@app.route("/informes/des_informes/ingresar_filtro", methods = ["POST"])
def ingresar_filtro ():
    """
    Permite seleccionar la opción de filtro que muestra varios
    botones, que permite visualizar todos los informes encontrados
    bajo ese filtro.
    """
    return "ª"

if __name__ == "__main__":
    app.run(debug = True)