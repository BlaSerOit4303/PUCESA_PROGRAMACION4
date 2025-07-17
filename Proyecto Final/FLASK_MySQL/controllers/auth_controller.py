from flask import render_template, request, session, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from extensions import db
from models.login_model import CuentaUsuario

def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        usuario = CuentaUsuario.query.filter_by(username=username).first()

        if usuario and check_password_hash(usuario.password_hash, password):
            session['usuario_id'] = usuario.id
            session['usuario_nombre'] = usuario.nombre_completo
            session['usuario_rol'] = usuario.rol

            flash(f"✅ Bienvenido, {usuario.nombre_completo}", "success")
            return redirect(url_for('main.index'))
        else:
            flash("❌ Usuario o contraseña incorrecta.", "danger")
            return redirect(url_for('auth.login_view'))

    return render_template("login.html")

def logout():
    session.clear()
    flash("✅ Sesión cerrada correctamente", "info")
    return redirect(url_for('auth.login_view'))

def register():
    if request.method == 'POST':
        username = request.form['username']
        nombre = request.form['nombre']
        email = request.form['email']
        password = request.form['password']
        confirm = request.form['confirm']

        if password != confirm:
            flash("⚠️ Las contraseñas no coinciden.", "warning")
            return redirect(url_for('auth.register_view'))

        if CuentaUsuario.query.filter_by(username=username).first():
            flash("⚠️ El nombre de usuario ya está en uso.", "warning")
            return redirect(url_for('auth.register_view'))

        if CuentaUsuario.query.filter_by(email=email).first():
            flash("⚠️ El correo electrónico ya está registrado.", "warning")
            return redirect(url_for('auth.register_view'))

        nuevo = CuentaUsuario(
            username=username,
            nombre_completo=nombre,
            email=email,
            password_hash=generate_password_hash(password),
            rol='usuario'
        )
        db.session.add(nuevo)
        db.session.commit()

        flash("✅ Usuario creado con éxito. Ya puedes iniciar sesión.", "success")
        return redirect(url_for('auth.login_view'))

    return render_template("register.html")