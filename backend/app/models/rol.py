from app.database import db
from .base_model import BaseModel

class Rol(BaseModel):
    __tablename__ = "roles"
    
    # Heredamos id, created_at y updated_at de BaseModel
    nombre = db.Column(db.String(50), unique=True, nullable=False)
    activo = db.Column(db.String(1), default='S')
    
    # Relación bidireccional con User
    # Esto permite hacer: mi_rol.users para ver la lista de usuarios
    users = db.relationship('User', back_populates='rol')

    def __init__(self, nombre: str) -> None:
        self.nombre = nombre
        
    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'activo': self.activo,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }