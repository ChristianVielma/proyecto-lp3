from flask import Blueprint, render_template
from app.dao.referenciales.producto.ProductoDao import ProductoDao

ciumod = Blueprint('producto', __name__, template_folder='templates')


@ciumod.route('/producto-index')
def productoIndex():
    proddao = ProductoDao()
    return render_template('producto-index.html', lista_productos=proddao.getProductos())

@ciumod.route('/producto-agregar')
def productoAgregar():
    return render_template('producto-agregar.html')


