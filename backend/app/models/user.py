from app.database import db
from .base_model import BaseModel
from werkzeug.security import generate_password_hash, check_password_hash

class User(BaseModel):
    __tablename__ = 'users'
    
    # Heredamos id, created_at y updated_at de BaseModel.
    nombre = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(200), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    activo = db.Column(db.String(1), default='S')
    
    # Clave foránea al Rol
    rol_id = db.Column(db.Integer, db.ForeignKey('roles.id'), nullable=False)
    
    # Relaciones bidireccionales
    # 1. Con Rol
    rol = db.relationship('Rol', back_populates='users')
    
    movimientos = db.relationship('MovimientoStock', back_populates='user')

    def __init__(self, nombre:str, email:str, password:str, rol_id:int = 2) -> None:
        self.nombre = nombre
        self.email = email
        self.rol_id = rol_id
        self.generate_password(password)
    
    def __repr__(self):
       return f"<User {self.nombre} - {self.email}>" 
     
    def to_dict(self):
      """Formato para respuestas JSON (como pide la consigna para /auth/me)"""
      return {
        'id': self.id,
        'nombre': self.nombre,
        'email': self.email,
        'activo': self.activo,
        'rol': self.rol.nombre if self.rol else None,
        'created_at': self.created_at.isoformat() if self.created_at else None
      }
      
    def validate_password(self, password:str) -> bool:
      return check_password_hash(self.password, password)
    
    def generate_password(self, password:str):
      self.password = generate_password_hash(password)