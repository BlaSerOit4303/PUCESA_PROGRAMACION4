from flask import Blueprint, session, redirect, url_for, flash,request
from extensions import db
from werkzeug.security import generate_password_hash
from controllers.user_controller import (
    obtener_usuarios,
    editar_usuario,
    actualizar_usuario,
)
from models.login_model import CuentaUsuario
# Importa la clase Blueprint para crear un blueprint de usuarios
# Este blueprint maneja las rutas relacionadas con los usuarios
user_bp = Blueprint("usuarios", __name__)
# Ruta para listar todos los usuarios
@user_bp.route('/usuarios/')
def listar_usuarios():
    if 'usuario_id' not in session:
        return redirect(url_for('auth.login_view'))

    if session.get('usuario_rol') != 'admin':
        flash("Acceso restringido solo para administradores", "warning")
        return redirect(url_for('main.index'))  # redirige a inicio si no es admin

    return obtener_usuarios()
# Ruta para crear un nuevo usuario
@user_bp.route('/usuarios/crear', methods=['POST'])
def crear_usuario():
    if session.get('usuario_rol') != 'admin':
        flash("Acceso denegado", "danger")
        return redirect(url_for('main.index'))

    # Recoge los datos del formulario
    nombre = request.form['nombre']
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']

    # Valida y guarda
    nuevo = CuentaUsuario(
        nombre_completo=nombre,
        username=username,
        email=email,
        password_hash=generate_password_hash(password),
        rol='usuario'
    )
    db.session.add(nuevo)
    db.session.commit()
    flash("Usuario creado correctamente", "success")
    return redirect(url_for('usuarios.listar_usuarios'))
# Ruta para editar un usuario
@user_bp.route('/usuarios/editar/<int:id>')
def editar_usuario_route(id):
    if session.get('usuario_rol') != 'admin':
        flash("Acceso denegado", "danger")
        return redirect(url_for('main.index'))
    return editar_usuario(id)
# Ruta para actualizar un usuario
@user_bp.route('/usuarios/actualizar/<int:id>', methods=['POST'])
def actualizar_usuario_route(id):
    if session.get('usuario_rol') != 'admin':
        flash("Acceso denegado", "danger")
        return redirect(url_for('main.index'))
    return actualizar_usuario(id)
# Ruta para eliminar un usuario
@user_bp.route('/usuarios/eliminar/<int:id>', methods=['POST'])
def eliminar_usuario(id):
    if session.get('usuario_rol') != 'admin':
        flash("Acceso denegado", "danger")
        return redirect(url_for('main.index'))

    usuario = CuentaUsuario.query.get(id)
    if usuario and usuario.username != 'admin':
        db.session.delete(usuario)
        db.session.commit()
        flash("Usuario eliminado", "info")
    else:
        flash("No se puede eliminar el usuario administrador", "warning")

    return redirect(url_for('usuarios.listar_usuarios'))