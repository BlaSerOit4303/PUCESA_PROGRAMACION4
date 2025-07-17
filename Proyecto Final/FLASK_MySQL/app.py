# Importa la clase Flask para crear la aplicación web
from flask import Flask

# Importa la configuración desde el archivo config.py (lee las variables de entorno)
from config import Config

# Importa la instancia de SQLAlchemy desde extensions.py
from extensions import db
from werkzeug.security import generate_password_hash
from models.login_model import CuentaUsuario


# Función de fábrica para crear y configurar la aplicación Flask
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    # Crear usuario admin por defecto
    with app.app_context():
        admin = CuentaUsuario.query.filter_by(username='admin').first()
        if not admin:
            nuevo_admin = CuentaUsuario(
                username='admin',
                nombre_completo='Administrador Principal',
                email='admin@admin.com',
                password_hash=generate_password_hash('123'),
                rol='admin'
            )
            db.session.add(nuevo_admin)
            db.session.commit()
            

    # Registrar blueprints
    from routes.main_routes import main_bp
    from routes.ciudad_routes import ciudad_bp
    from routes.user_routes import user_bp
    from routes.grafo_routes import grafo_bp
    from routes.course_routes import course_bp
    from routes.auth_routes import auth_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(ciudad_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(grafo_bp)
    app.register_blueprint(course_bp)
    app.register_blueprint(auth_bp)

    return app  # ✅ Muy importante

# Instanciar la aplicación
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
