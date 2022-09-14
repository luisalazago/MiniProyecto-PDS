from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)
usuarios = {"Luis": "pendejo"}
fallo = False

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
    global fallo
    usuario = request.form["user"]
    contra = request.form["contra"]
    if usuario in usuarios:
        print(contra, usuarios[usuario])
        if contra == usuarios[usuario]:
            print(2)
            return render_template("home.html", user = usuario, password = contra)
        else: fallo = True
    else: fallo = True
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug = True)