from flask import Blueprint, session, redirect, url_for,request, flash
from models.ciudad_model import Ciudad
from extensions import db
from controllers.grafo_controller import (
    mostrar_panel_grafos,
    calcular_ruta,
    agregar_ruta,
    editar_ciudad_controller,
    actualizar_ciudad_controller   
)
#Importa la clase Blueprint para crear un blueprint de grafos
# Este blueprint maneja las rutas relacionadas con los grafos y ciudades
grafo_bp = Blueprint("grafos", __name__)
# Ruta para mostrar el panel de grafos
@grafo_bp.route('/grafos/')
def grafos():
    if 'usuario_id' not in session:
        return redirect(url_for('auth.login_view'))
    return mostrar_panel_grafos()
# Ruta para agregar una nueva ciudad
@grafo_bp.route('/grafos/agregar', methods=['POST'])
def agregar_ciudad():
    nombre = request.form.get('nombre').strip()
    if nombre:
        nueva = Ciudad(nombre=nombre)
        db.session.add(nueva)
        db.session.commit()
        flash("✅ Ciudad agregada correctamente", "success")
    return redirect(url_for('grafos.grafos'))
# Ruta para editar una ciudad existente
@grafo_bp.route('/grafos/editar_ciudad/<int:id>')
def editar_ciudad(id):
    return editar_ciudad_controller(id)
# Ruta para actualizar los datos de una ciudad
@grafo_bp.route('/grafos/actualizar_ciudad/<int:id>', methods=['POST'])
def actualizar_ciudad(id):
    return actualizar_ciudad_controller(id)
# Ruta para eliminar una ciudad
@grafo_bp.route('/grafos/eliminar/<int:id>', methods=['POST'])
def eliminar_ciudad(id):
    ciudad = Ciudad.query.get_or_404(id)
    db.session.delete(ciudad)
    db.session.commit()
    flash("🗑️ Ciudad eliminada", "info")
    return redirect(url_for('grafos.grafos'))
# Ruta para agregar una nueva ruta
@grafo_bp.route('/grafos/agregar_ruta', methods=['POST'])
def agregar_ruta_route():
    return agregar_ruta()
# Ruta para calcular la ruta entre dos ciudades
@grafo_bp.route('/grafos/calcular', methods=['POST'])
def calcular_ruta_route():
    return calcular_ruta()