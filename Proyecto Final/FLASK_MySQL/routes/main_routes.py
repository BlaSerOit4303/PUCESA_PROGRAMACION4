from flask import Blueprint, session, redirect, url_for, render_template
from controllers.dashboard_controller import obtener_dashboard_info

main_bp = Blueprint("main", __name__)

@main_bp.route('/')
def index():
    if 'usuario_id' not in session:
        return redirect(url_for('auth.login_view'))

    dashboard_data = obtener_dashboard_info(
        session.get('usuario_nombre'),
        session.get('usuario_rol')
    )
    return render_template("index.html", **dashboard_data)