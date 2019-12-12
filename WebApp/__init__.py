from flask import Flask, render_template, request, url_for
import sqlite3
from PIL import Image
import cv2
import time

def instanciaBD():
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    cur.execute("CREATE TABLE auto(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, marca VARCHAR(15), modelo VARCHAR(15), color VARCHAR(15), año INTEGER(5), placa VARCHAR(10), nombre VARCHAR(20), apellido VARCHAR(20))")
    
    return con.commit()

def nuevousuario(nombre, apellido, email, usuario, contraseña):
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    cur.execute("INSERT INTO transito(nombre, apellido, email, usuario, contraseña) VALUES(?,?,?,?,?)", (nombre, apellido, email, usuario, contraseña))

    return con.commit()
    
def iniciosesion(usuari, contraseña):
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    cur.execute("SELECT contraseña FROM transito WHERE usuario= '%s'"% usuari)

    contraseñabd = cur.fetchall()
    for i in contraseñabd:
        if contraseña == i[0]:
            return True
        else:
            return False


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("login.html")

@app.route('/home', methods=["POST", "GET"])
def iniciar_sesion():
    if request.method == 'POST':
        nombre = request.form['usuario']
        contraseña = request.form['contraseña']
        
        validacion = iniciosesion(nombre, contraseña)
    
        if validacion == True:
            print("Valido")
            return render_template("home.html")
        else:
            print("No Valido")
            return render_template("login.html")

@app.route('/register')
def register():
    return render_template('register.html')
    
@app.route('/registry', methods=['POST'])
def nuevo_usuario():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        email = request.form['email']
        usuario = request.form['usuario']
        contraseña = request.form['contraseña']

        nuevousuario(nombre, apellido, email, usuario, contraseña)

        return render_template("login.html")

@app.route('/proceso', methods=["POST", "GET"])
def procesar_placa():
    imagen = request.form['img']
    ruta = "Placas\\"+imagen
    print(ruta)
    time.sleep(5)
    return render_template("table.html")

@app.route('/table', methods=["POST"])
def table():
    con = sqlite3.connect('database.db')
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM auto")
    filas = cur.fetchall()
    return render_template("table.html", filas = filas)

if __name__ == "__main__":
    # instanciaBD()
    app.run(debug= True)