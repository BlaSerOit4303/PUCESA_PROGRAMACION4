from flask import Blueprint, session, redirect, url_for, flash, request
from controllers.course_controller import mostrar_cursos, editar_curso, mostrar_formulario_edicion, eliminar_curso

course_bp = Blueprint("cursos", __name__)

@course_bp.route('/cursos/')
def cursos():
    if 'usuario_id' not in session:
        return redirect(url_for('auth.login_view'))

    if session.get('usuario_rol') != 'admin':
        flash("Acceso restringido solo para administradores", "warning")
        return redirect(url_for('main.index'))

    return mostrar_cursos()

@course_bp.route('/cursos/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    if 'usuario_id' not in session or session.get('usuario_rol') != 'admin':
        flash("Acceso restringido", "danger")
        return redirect(url_for('main.index'))

    if request.method == 'POST':
        return editar_curso(id, request.form)

    return mostrar_formulario_edicion(id)

@course_bp.route('/cursos/eliminar/<int:id>', methods=['POST'])
def eliminar(id):
    if 'usuario_id' not in session or session.get('usuario_rol') != 'admin':
        flash("Acceso restringido", "danger")
        return redirect(url_for('main.index'))

    return eliminar_curso(id)