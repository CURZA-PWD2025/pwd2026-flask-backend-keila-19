from app.database import db
from .base_model import BaseModel

class MovimientoStock(BaseModel):
    __tablename__ = 'movimientos_stock'
    
    tipo = db.Column(db.String(10), nullable=False) # 'entrada' o 'salida'
    cantidad = db.Column(db.Integer, nullable=False)
    motivo = db.Column(db.String(200))
    
    producto_id = db.Column(db.Integer, db.ForeignKey('productos.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    # Relaciones para acceder fácil a los datos
    producto = db.relationship('Producto', backref='movimientos')
    user = db.relationship('User', backref='movimientos')

    def to_dict(self):
        """Fundamental para que los GET funcionen"""
        return {
            "id": self.id,
            "tipo": self.tipo,
            "cantidad": self.cantidad,
            "motivo": self.motivo,
            "producto_id": self.producto_id,
            "user_id": self.user_id,
            "fecha_creacion": self.created_at.isoformat() if hasattr(self, 'created_at') else None,
            # Opcional: podrías incluir el nombre del producto para que el JSON sea más informativo
            "nombre_producto": self.producto.nombre if self.producto else None
        }