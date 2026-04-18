from flask import Response, jsonify, request
from app.models.movimiento_stock import MovimientoStock
from app.models.productos import Producto 
from app.controllers import Controller
from app.database import db
from flask_jwt_extended import get_jwt_identity

class MovimientoStockController(Controller):

    @staticmethod
    def create(req) -> tuple[Response, int]:
        data = req.get_json()
        producto_id = data.get('producto_id')
        tipo = data.get('tipo') 
        cantidad = data.get('cantidad')
        
        # Validación de cantidad según consigna (mayor a 0)
        if not cantidad or cantidad <= 0:
            return jsonify({"error": "La cantidad debe ser mayor a 0"}), 400

        producto = db.session.get(Producto, producto_id)
        if not producto:
            return jsonify({"error": "Producto no encontrado"}), 404

        # LÓGICA DE NEGOCIO
        if tipo == 'entrada':
            producto.stock_actual += cantidad
        elif tipo == 'salida':
            if producto.stock_actual < cantidad:
                # Formato de error según la consigna
                return jsonify({"error": "Stock insuficiente para registrar la salida"}), 400
            producto.stock_actual -= cantidad
        else:
            return jsonify({"error": "Tipo de movimiento inválido"}), 400

        nuevo_movimiento = MovimientoStock(
            tipo=tipo,
            cantidad=cantidad,
            motivo=data.get('motivo'),
            producto_id=producto_id,
            user_id=get_jwt_identity() # El ID del usuario que viene en el token
        )

        db.session.add(nuevo_movimiento)
        db.session.commit() 
        
        return jsonify({"message": "Movimiento registrado con éxito"}), 201

    @staticmethod
    def get_all() -> tuple[Response, int]:
        """Solo para admin"""
        movimientos = db.session.execute(db.select(MovimientoStock)).scalars().all()
        return jsonify([m.to_dict() for m in movimientos]), 200

    @staticmethod
    def get_my_movements() -> tuple[Response, int]:
        """Nuevo: para la ruta /movimientos/mis/"""
        current_user_id = get_jwt_identity()
        movimientos = db.session.execute(
            db.select(MovimientoStock).where(MovimientoStock.user_id == current_user_id)
        ).scalars().all()
        return jsonify([m.to_dict() for m in movimientos]), 200

    @staticmethod
    def show(id: int) -> tuple[Response, int]:
        movimiento = db.session.get(MovimientoStock, id)
        if not movimiento:
            return jsonify({"error": "Movimiento no encontrado"}), 404
        return jsonify(movimiento.to_dict()), 200

    @staticmethod
    def update(request_data: dict, id: int) -> tuple[Response, int]:
        return jsonify({"msg": "La edición de movimientos no está permitida"}), 501

    @staticmethod
    def destroy(id: int) -> tuple[Response, int]:
        return jsonify({"msg": "La eliminación de movimientos no está permitida"}), 501