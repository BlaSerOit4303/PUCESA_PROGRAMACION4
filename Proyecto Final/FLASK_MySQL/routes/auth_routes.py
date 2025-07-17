from flask import Blueprint
from controllers.auth_controller import login, logout,register
# Importa la clase Blueprint para crear un blueprint de autenticación
# Este blueprint maneja las rutas relacionadas con la autenticación de usuarios
auth_bp = Blueprint('auth', __name__)
# Rutas para autenticación de usuarios
@auth_bp.route('/login', methods=['GET', 'POST'])
def login_view():
    return login()
# Esta ruta maneja el cierre de sesión de los usuarios
@auth_bp.route('/logout')
def logout_view():
    return logout()
# Esta ruta maneja el registro de nuevos usuarios
@auth_bp.route('/registrar', methods=['GET', 'POST'])  # 👈 Esta es la que falta
def register_view():
    return register()
