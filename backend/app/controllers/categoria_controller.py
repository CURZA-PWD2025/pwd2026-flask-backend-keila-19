from flask import Response, jsonify, request
from app.models.categoria import Categoria
from app.controllers import Controller
from app.database import db

class CategoriaController(Controller):
    
    @staticmethod
    def get_all() -> tuple[Response, int]:
        categorias = db.session.execute(db.select(Categoria)).scalars().all()
        return jsonify([{"id": c.id, "nombre": c.nombre, "descripcion": c.descripcion} for c in categorias]), 200

    @staticmethod
    def show(id: int) -> tuple[Response, int]:
        categoria = db.session.get(Categoria, id)
        if not categoria:
            return jsonify({"error": "Categoría no encontrada"}), 404
        return jsonify({"id": categoria.id, "nombre": categoria.nombre}), 200

    @staticmethod
    def create(req_data) -> tuple[Response, int]:
        data = req_data.get_json()
        nueva_cat = Categoria(nombre=data.get('nombre'), descripcion=data.get('descripcion'))
        db.session.add(nueva_cat)
        db.session.commit()
        return jsonify({"message": "Categoría creada"}), 201

    @staticmethod
    def update(request_data: dict, id: int) -> tuple[Response, int]:
        categoria = db.session.get(Categoria, id)
        if not categoria: return jsonify({"error": "No existe"}), 404
        categoria.nombre = request_data.get('nombre', categoria.nombre)
        db.session.commit()
        return jsonify({"message": "Actualizada"}), 200

    @staticmethod
    def destroy(id: int) -> tuple[Response, int]:
        categoria = db.session.get(Categoria, id)
        if not categoria: return jsonify({"error": "No existe"}), 404
        # Validación del TP: No borrar si tiene productos
        if categoria.productos:
            return jsonify({"error": "No se puede eliminar: tiene productos asociados"}), 409
        db.session.delete(categoria)
        db.session.commit()
        return jsonify({"message": "Eliminada"}), 200