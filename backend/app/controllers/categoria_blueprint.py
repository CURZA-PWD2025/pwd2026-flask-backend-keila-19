from flask import Blueprint, request
from app.controllers.categoria_controller import CategoriaController

categoria_bp = Blueprint('categorias', __name__)

@categoria_bp.route('/', methods=['GET'])
def get_categorias():
    return CategoriaController.get_all()

@categoria_bp.route('/', methods=['POST'])
# Aquí iría el decorador @rol_access('admin') después
def create_categoria():
    return CategoriaController.create(request)