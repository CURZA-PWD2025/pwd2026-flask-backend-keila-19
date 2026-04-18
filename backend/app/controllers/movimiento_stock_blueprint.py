from flask import Blueprint, request
from app.controllers.movimiento_stock_controller import MovimientoStockController
from flask_jwt_extended import jwt_required

movimiento_bp = Blueprint('movimientos', __name__)

@movimiento_bp.route('/', methods=['GET'])
@jwt_required()
def get_movimientos():
    return MovimientoStockController.get_all()

@movimiento_bp.route('/', methods=['POST'])
@jwt_required()
def create_movimiento():
    # Enviamos el objeto 'request' al método create
    return MovimientoStockController.create(request)