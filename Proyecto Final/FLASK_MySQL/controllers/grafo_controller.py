from flask import render_template, request, redirect, url_for, flash
from models.ciudad_model import Ciudad
from models.ruta_model import Ruta
from extensions import db
import random
from utils.grafos.grafo_logica import generar_ruta_grafico

def mostrar_panel_grafos():
    ciudades = Ciudad.query.order_by(Ciudad.nombre).all()
    rutas = Ruta.query.all()
    return render_template("grafos.html",
        ciudades=ciudades,
        rutas=rutas,
        resultado=None,
        ruta=None,
        costo=None,
        random=random.randint(1, 1000000)
    )

import random
from flask import render_template, request, redirect, url_for, flash
from models.ciudad_model import Ciudad
from models.ruta_model import Ruta
from utils.grafos.grafo_logica import generar_ruta_grafico

def calcular_ruta():
    # 1) Leer IDs y convertir a nombres
    origen_id  = int(request.form.get('origen'))
    destino_id = int(request.form.get('destino'))
    costa      = request.form.get('costa') == "1"

    origen  = Ciudad.query.get(origen_id).nombre
    destino = Ciudad.query.get(destino_id).nombre

    # 2) Cargar todas las ciudades y rutas
    ciudades = Ciudad.query.all()
    rutas     = Ruta.query.all()

    # 3) Validación básica
    if origen_id == destino_id:
        flash("❌ No puedes elegir la misma ciudad como origen y destino.", "warning")
        return redirect(url_for('grafos.grafos'))

    # 4) Construir lista de aristas para NetworkX
    edges = [
        (r.origen.nombre, r.destino.nombre, r.costo)
        for r in rutas
    ]

    # 5) Calcular ruta, costo y generar imagen
    ruta, costo, mensaje, nombre_imagen = generar_ruta_grafico(
        origen, destino, edges, costa
    )

    # 6) Renderizar plantilla, pasando ruta y costo al panel de resultados
    return render_template("grafos.html",
        ciudades      = ciudades,
        rutas         = rutas,
        resultado     = mensaje,
        ruta          = ruta,
        costo         = costo,
        imagen_grafo  = f"img/{nombre_imagen}" if nombre_imagen else None,
        random        = random.randint(1, 1000000)
    )

    
def agregar_ruta():
    origen_id = int(request.form.get('origen'))
    destino_id = int(request.form.get('destino'))
    costo = int(request.form.get('costo'))

    if origen_id == destino_id:
        flash("❌ No puedes crear una ruta con origen y destino iguales", "warning")
        return redirect(url_for('grafos.grafos'))

    nueva_ruta = Ruta(origen_id=origen_id, destino_id=destino_id, costo=costo)
    db.session.add(nueva_ruta)
    db.session.commit()
    flash("✅ Ruta agregada correctamente", "success")
    return redirect(url_for('grafos.grafos'))

def editar_ciudad_controller(id):
    ciudad = Ciudad.query.get_or_404(id)
    return render_template("editar_ciudad.html", ciudad=ciudad)

def actualizar_ciudad_controller(id):
    ciudad = Ciudad.query.get_or_404(id)
    ciudad.nombre = request.form.get('nombre')
    db.session.commit()
    flash("✅ Ciudad actualizada", "success")
    return redirect(url_for('grafos.grafos'))
