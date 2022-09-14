from flask import Flask, redirect, url_for, render_template, request

import sys
sys.path.append("../Funciones")
from usuario import verificar_contrasena, is_admin

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

@app.route("/home", methods = ["POST"])
def home():
    global fallo, usuario_activo, rol
    if(usuario_activo != None): return render_template("home.html", user = usuario_activo, password = "Paila pa", rol = rol)
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

@app.route("/inventario/un_producto")
def un_producto():
    return "Hola Producto!"

if __name__ == "__main__":
    app.run(debug = True)