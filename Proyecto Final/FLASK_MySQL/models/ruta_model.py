from extensions import db
from models.ciudad_model import Ciudad

class Ruta(db.Model):
    __tablename__ = 'rutas'
    id = db.Column(db.Integer, primary_key=True)
    origen_id = db.Column(db.Integer, db.ForeignKey('ciudades.id'))
    destino_id = db.Column(db.Integer, db.ForeignKey('ciudades.id'))
    costo = db.Column(db.Integer)

    origen = db.relationship('Ciudad', foreign_keys=[origen_id])
    destino = db.relationship('Ciudad', foreign_keys=[destino_id])