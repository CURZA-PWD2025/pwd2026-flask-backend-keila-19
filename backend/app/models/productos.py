from app.database import db
from .base_model import BaseModel

class Productos(BaseModel):
    __tablename__ = 'productos'
    
    nombre = db.Column(db.String(150), nullable=False)
    descripcion = db.Column(db.Text)
    precio_costo = db.Column(db.Numeric(10, 2), nullable=False)
    precio_venta = db.Column(db.Numeric(10, 2), nullable=False)
    stock_actual = db.Column(db.Integer, default=0)
    stock_minimo = db.Column(db.Integer, default=0)
    
    # Claves foráneas
    categoria_id = db.Column(db.Integer, db.ForeignKey('categorias.id'), nullable=False)
    proveedor_id = db.Column(db.Integer, db.ForeignKey('proveedores.id'))

    categoria = db.relationship('Categoria', back_populates='productos')
    proveedor = db.relationship('Proveedor', back_populates='productos')
    movimientos = db.relationship('MovimientoStock', back_populates='producto', cascade="all, delete-orphan")

    def to_dict(self):
        """Ajustado al formato JSON exacto de la consigna"""
        return {
            "id": self.id,
            "nombre": self.nombre,
            "precio_venta": "{:.2f}".format(self.precio_venta) if self.precio_venta else "0.00",
            "stock_actual": self.stock_actual,
            "stock_minimo": self.stock_minimo,
            "categoria": {
                "id": self.categoria.id,
                "nombre": self.categoria.nombre
            } if self.categoria else None,
            "proveedor": {
                "id": self.proveedor.id,
                "nombre": self.proveedor.nombre
            } if self.proveedor else None
        }