from app.database import db
from datetime import datetime

class BaseModel(db.Model):
    __abstract__ = True  # Esto indica que no se creará una tabla "BaseModel" en la DB
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)