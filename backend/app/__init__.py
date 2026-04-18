from flask import Flask
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from app.config import Config
from app.database import db

# IMPORTANTE: Importamos los modelos aquí para que Flask-Migrate los detecte
from app.models.user import User
from app.models.rol import Rol
from app.models.categoria import Categoria
from app.models.proveedor import Proveedor
from app.models.productos import Productos
from app.models.movimiento_stock import MovimientoStock

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializar extensiones
    db.init_app(app)
    Migrate(app, db)
    JWTManager(app)

# REGISTRO DE BLUEPRINTS
    # 1. Autenticación
    from app.controllers.auth_controller import auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    # 2. Categorías
    from app.controllers.categoria_blueprint import categoria_bp
    app.register_blueprint(categoria_bp, url_prefix='/categorias')

    # 3. Proveedores
    from app.controllers.proveedor_controller import proveedor_bp # Verifica el nombre del archivo
    app.register_blueprint(proveedor_bp, url_prefix='/proveedores')

    # 4. Productos
    from app.controllers.producto_controller import producto_bp # Verifica el nombre del archivo
    app.register_blueprint(producto_bp, url_prefix='/productos')

    # 5. Movimientos
    from app.controllers.movimiento_stock_blueprint import movimiento_bp
    app.register_blueprint(movimiento_bp, url_prefix='/movimientos')

    return app