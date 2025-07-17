from extensions import db
from datetime import datetime

class CuentaUsuario(db.Model):
    __tablename__ = 'cuenta_usuario'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    nombre_completo = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True)
    rol = db.Column(db.String(10), nullable=False, default='usuario')
    creado_en = db.Column(db.DateTime, default=datetime.utcnow)