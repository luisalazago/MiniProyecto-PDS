from flask import Flask, redirect, url_for, render_template, request

import sys
sys.path.append("../Funciones")
from usuario import verificar_contrasena, is_admin
from funciones_inventario import revisar_inventario

app = Flask(__name__)
usuario_activo = None
rol = None
fallo = False

# Funciones auxiliares
def adminReturn(val):
    ans = "empleado"
    if val: ans = "admin"
    return ans

# Manejo de la aplicación
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
    global fallo, usuario_activo, rol
    print(1)
    if(usuario_activo != None): return render_template("home.html", user = usuario_activo, 
                                                                    password = "Paila pa", 
                                                                    rol = rol)
    usuario = request.form["user"]
    contra = request.form["contra"]
    if verificar_contrasena(usuario, contra):
        usuario_activo = usuario
        rol = adminReturn(is_admin(usuario))
        return render_template("home.html", user = usuario, password = contra, rol = rol)
    else: fallo = True
    return redirect(url_for("login"))

@app.route("/ventas")
def ventas():
    return render_template("ventas.html")

@app.route("/inventario")
def inventario():
    return render_template("inventario.html", rol = rol)

@app.route("/inventario/des_inventario", methods = ["POST", "GET"])
def des_inventario():
    if("un_producto" in request.form):
        return render_template("ingresar_producto.html", rol = rol, fallo = False)
    else:
        return redirect(url_for("todos_productos"))

@app.route("/inventario/des_inventario/un_producto", methods = ["POST"])
def un_producto():
    id_producto = int(request.form["id_producto"])
    producto = revisar_inventario(id_producto)
    print(producto)
    if(not len(producto)):
        return render_template("ingresar_producto.html ", rol = rol, fallo = True)
    return render_template("un_producto.html", nombre = producto[0]["name_prod"], id_producto = producto[0]["id_prod"],
                                               cantidad =  producto[0]["cant_prod"], categoria =  producto[0]["cap_prod"],
                                               precio =  producto[0]["price_prod"], rol = rol)

@app.route("/inventario/des_inventario/todos_productos", methods = ["POST", "GET"])
def todos_productos():
    inventario_productos = revisar_inventario()
    return render_template("todo_productos.html", rol = rol, inventario = inventario_productos)

if __name__ == "__main__":
    app.run(debug = True)