from flask import render_template, request, redirect, url_for, flash
from models.login_model import CuentaUsuario
from extensions import db
from utils.helpers import formatear_fecha
from datetime import datetime

fecha = formatear_fecha(datetime.now())

def obtener_usuarios():
    usuarios = CuentaUsuario.query.all()
    fecha = formatear_fecha(datetime.now())
    return render_template("usuarios.html", usuarios=usuarios, fecha=fecha)

def editar_usuario(id):
    usuario = CuentaUsuario.query.get_or_404(id)
    
    return render_template("editar_usuario.html", usuario=usuario)

def actualizar_usuario(id):
    usuario = CuentaUsuario.query.get_or_404(id)
    usuario.nombre_completo = request.form.get('nombre')
    usuario.email = request.form.get('email')
    db.session.commit()
    flash("✅ Usuario actualizado correctamente", "success")
    return redirect(url_for('usuarios.listar_usuarios'))

def eliminar_usuario(id):
    usuario = CuentaUsuario.query.get(id)
    if usuario and usuario.username != 'admin':
        db.session.delete(usuario)
        db.session.commit()
        flash("🗑️ Usuario eliminado", "info")
    else:
        flash("⚠️ No se puede eliminar el usuario administrador", "warning")
    return redirect(url_for('usuarios.listar_usuarios'))