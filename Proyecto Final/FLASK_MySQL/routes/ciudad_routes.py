from flask import Blueprint, session, redirect, url_for, flash
from controllers.ciudad_controller import (
    listar_ciudades as mostrar_ciudades,
    crear_ciudad as crear_ciudad_func,
    editar_ciudad as editar_ciudad_func
)

ciudad_bp = Blueprint("ciudades", __name__)

@ciudad_bp.route('/ciudades/')
def listar_ciudades():
    if 'usuario_id' not in session:
        return redirect(url_for('auth.login_view'))
    return mostrar_ciudades()

@ciudad_bp.route('/ciudades/crear', methods=['GET', 'POST'])
def crear_ciudad():
    return crear_ciudad_func()

@ciudad_bp.route('/ciudades/editar/<int:id>', methods=['GET', 'POST'])
def editar_ciudad(id):
    return editar_ciudad_func(id)

