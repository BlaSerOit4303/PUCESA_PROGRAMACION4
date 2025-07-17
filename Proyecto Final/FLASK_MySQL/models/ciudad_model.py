from extensions import db
# Esta clase representa el modelo de Ciudad en la base de datos
class Ciudad(db.Model):
    __tablename__ = 'ciudades'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False, unique=True)