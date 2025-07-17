# controllers/provincia_controller.py
from flask import render_template, request, redirect, url_for, flash
from models.ciudad_model import Ciudad
from extensions import db
from datetime import datetime
from utils.helpers import formatear_fecha
# Esta función lista todas las ciudades
def listar_ciudades():
    ciudades = Ciudad.query.all()
    fecha = formatear_fecha(datetime.now())
    return render_template("ciudades.html", ciudades=ciudades, fecha=fecha)
# Esta función maneja la creación de nuevas ciudades
def crear_ciudad():
    if request.method == 'POST':
        nombre = request.form.get('nombre', '').strip()

        if not nombre:
            flash("El nombre no puede estar vacío", "warning")
            return redirect(url_for('ciudades.crear_ciudad'))

        existente = Ciudad.query.filter_by(nombre=nombre).first()
        if existente:
            flash("La ciudad ya existe", "danger")
            return redirect(url_for('ciudades.crear_ciudad'))

        nueva = Ciudad(nombre=nombre)
        db.session.add(nueva)
        db.session.commit()
        flash("Ciudad creada exitosamente", "success")
        return redirect(url_for('ciudades.listar_ciudades'))

    return render_template("crear_ciudad.html")
# Esta función maneja la edición de una ciudad específica
def editar_ciudad(id):
    ciudad = Ciudad.query.get_or_404(id)

    if request.method == 'POST':
        nuevo_nombre = request.form.get('nombre', '').strip()

        if not nuevo_nombre:
            flash("⚠️ El nombre no puede estar vacío", "warning")
            return redirect(url_for('ciudades.editar_ciudad', id=id))

        existente = Ciudad.query.filter_by(nombre=nuevo_nombre).first()
        if existente and existente.id != id:
            flash("❌ Ya existe otra ciudad con ese nombre", "danger")
            return redirect(url_for('ciudades.editar_ciudad', id=id))

        ciudad.nombre = nuevo_nombre
        db.session.commit()
        flash("✅ Ciudad actualizada correctamente", "success")
        return redirect(url_for('grafos.grafos'))

    return render_template("editar_ciudad.html", ciudad=ciudad)
# Esta función actualiza los datos de una ciudad
def actualizar_ciudad(id):
    ciudad = Ciudad.query.get_or_404(id)
    ciudad.nombre = request.form.get('nombre')
    db.session.commit()
    flash("✅ Ciudad actualizada", "success")
    return redirect(url_for('grafos.grafos'))