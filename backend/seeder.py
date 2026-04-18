from app import create_app
from app.database import db
from app.models.rol import Rol
from app.models.user import User
from app.models.categoria import Categoria
from app.models.proveedor import Proveedor
from app.models.productos import Productos

app = create_app()

with app.app_context():
    # 1. Crear Roles
    rol_admin = Rol(nombre='admin')
    rol_op    = Rol(nombre='operador')
    db.session.add_all([rol_admin, rol_op])
    db.session.commit()

    # 2. Crear Usuario Admin (Fijate que la clave es admin123)
    admin = User(username='admin', email='admin@stock.com', rol=rol_admin)
    admin.generate_password('admin123')
    db.session.add(admin)

    # 3. Crear Categorías
    alm = Categoria(nombre='Almacén', descripcion='Productos secos')
    lim = Categoria(nombre='Limpieza', descripcion='Artículos de limpieza')
    db.session.add_all([alm, lim])

    # 4. Crear Proveedor
    prov = Proveedor(nombre='Distribuidora Norte', telefono='2994001234')
    db.session.add(prov)
    db.session.commit() # Commit intermedio para obtener los IDs

    # 5. Crear Productos iniciales
    db.session.add_all([
        Productos(nombre='Harina 000', precio_costo=280, precio_venta=350,
                   stock_actual=50, stock_minimo=10,
                   categoria_id=alm.id, proveedor_id=prov.id),
        Productos(nombre='Lavandina 1L', precio_costo=150, precio_venta=210,
                   stock_actual=30, stock_minimo=5,
                 categoria_id=lim.id, proveedor_id=prov.id),
    ])
    db.session.commit()
    print("¡Seed completado con éxito!")