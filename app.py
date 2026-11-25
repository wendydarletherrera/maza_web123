"""Sitio web de Auto Repuestos MAZA (Flask).

Ejecutar:  python app.py   y abrir http://127.0.0.1:5000
"""
import json
import os
from urllib.parse import quote

from flask import Flask, redirect, render_template, request

app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------------------
# Datos de la empresa (edita aquí y se actualiza en todo el sitio)
# ---------------------------------------------------------------------------
EMPRESA = {
    "nombre": "Auto Repuestos MAZA",
    "lema": "La pieza exacta, con garantía",
    "anios": 6,
    "gerente": "Luis Fernández Ramírez",
    "telefonos": ["72201855", "72755044"],
    "whatsapp": "59172201855",  # número con código de país, sin + ni espacios
    "sucursales": [
        {
            "ciudad": "Cochabamba",
            "direccion": "Av. Blanco Galindo, rotonda Perú, centro comercial Supermall, 1er piso, oficina T-33",
            "mapa": "https://www.google.com/maps/search/?api=1&query=Supermall+Cochabamba+Bolivia",
        },
        {
            "ciudad": "Santa Cruz",
            "direccion": "Doble Vía La Guardia, entre Av. Cuarto Anillo y calle Jorochito, acera sur",
            "mapa": "https://www.google.com/maps/search/?api=1&query=Doble+Via+La+Guardia+cuarto+anillo+Santa+Cruz+Bolivia",
        },
    ],
    # Reemplaza "#" por los enlaces reales de las cuentas
    "redes": {"TikTok": "#", "Instagram": "#"},
}

CATEGORIAS = [
    {"slug": "bobinas", "nombre": "Bobinas de encendido", "icono": "bobina", "en_linea": True,
     "desc": "Bobinas de 2, 3 y 4 pines y secas para marcas chinas, coreanas y japonesas."},
    {"slug": "bujias", "nombre": "Bujías de encendido", "icono": "bujia",
     "desc": "Bujías para motores a gasolina de uso diario y trabajo."},
    {"slug": "capuchones", "nombre": "Capuchones de bobina", "icono": "capuchon",
     "desc": "Capuchones y conectores para asegurar una buena chispa."},
    {"slug": "filtros", "nombre": "Filtros de aire", "icono": "filtro",
     "desc": "Filtros de aire, incluida nuestra marca propia MAZA."},
    {"slug": "munones", "nombre": "Muñones", "icono": "munon",
     "desc": "Muñones de dirección, de suspensión y estabilizadores."},
    {"slug": "retenes", "nombre": "Retenes de válvula", "icono": "reten",
     "desc": "Retenes de válvula y retenes sello de bujía."},
    {"slug": "empaques", "nombre": "Empaques de motor", "icono": "empaque",
     "desc": "Empaques de culata, de balancín y juegos de motor."},
    {"slug": "rotores", "nombre": "Rotores de distribuidor", "icono": "rotor",
     "desc": "Rotores para sistemas de encendido con distribuidor."},
    {"slug": "varios", "nombre": "Varios productos", "icono": "varios",
     "desc": "Brazos de cremallera, bujes de tijeral, mangueras corrugadas, múltiples, O-rings, filtros de inyector y varillas."},
]


def cargar_destacados():
    """Piezas destacadas que se muestran en el sitio (edita data/destacados.json)."""
    with open(os.path.join(BASE_DIR, "data", "destacados.json"), encoding="utf-8") as f:
        return json.load(f)


def enlace_whatsapp(mensaje: str) -> str:
    return f"https://wa.me/{EMPRESA['whatsapp']}?text={quote(mensaje)}"


@app.context_processor
def datos_globales():
    return {"empresa": EMPRESA, "categorias": CATEGORIAS, "wa": enlace_whatsapp}


@app.route("/")
def inicio():
    return render_template("index.html", destacados=cargar_destacados()[:4])


@app.route("/catalogo")
def catalogo():
    return render_template("catalogo.html", destacados=cargar_destacados())


@app.route("/nosotros")
def nosotros():
    return render_template("nosotros.html")


@app.route("/contacto", methods=["GET", "POST"])
def contacto():
    if request.method == "POST":
        f = request.form
        mensaje = (
            "Hola MAZA, quiero cotizar un repuesto.\n"
            f"Nombre: {f.get('nombre', '').strip()}\n"
            f"Soy: {f.get('tipo', '').strip()}\n"
            f"Ciudad: {f.get('ciudad', '').strip()}\n"
            f"Vehículo: {f.get('vehiculo', '').strip()}\n"
            f"Repuesto o código: {f.get('repuesto', '').strip()}"
        )
        return redirect(enlace_whatsapp(mensaje))
    return render_template("contacto.html")


@app.errorhandler(404)
def no_encontrado(_):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True)
