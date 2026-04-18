from app.database import db
from .base_model import BaseModel

class Proveedor(BaseModel):
    __tablename__ = 'proveedores'
    nombre = db.Column(db.String(150), nullable=False)
    contacto = db.Column(db.String(100))
    telefono = db.Column(db.String(30))
    email = db.Column(db.String(120))
    # Relación inversa para ver sus productos
    productos = db.relationship('Producto', backref='proveedor', lazy=True)