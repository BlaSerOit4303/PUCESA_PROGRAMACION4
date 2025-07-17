from flask import Blueprint
from controllers.auth_controller import login, logout,register

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login_view():
    return login()

@auth_bp.route('/logout')
def logout_view():
    return logout()

@auth_bp.route('/registrar', methods=['GET', 'POST'])  # 👈 Esta es la que falta
def register_view():
    return register()
