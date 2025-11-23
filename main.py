from flask import Flask, render_template, request, redirect
from database import get_db

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("contacto.html")

@app.route("/enviar", methods=["POST"])
def enviar():
    nombre = request.form.get("nombre")
    correo = request.form.get("correo")
    telefono = request.form.get("telefono")
    asunto = request.form.get("asunto")
    mensaje = request.form.get("mensaje")

    db = get_db()
    db.execute("""
        INSERT INTO contactos (nombre, correo, telefono, asunto, mensaje)
        VALUES (?, ?, ?, ?, ?)
    """, (nombre, correo, telefono, asunto, mensaje))
    
    db.commit()

    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
