from flask import Blueprint, render_template
from app.dao.referenciales.ciudad.CiudadDao import CiudadDao
from app.dao.referenciales.ciudad.ProductoDao import ProductoDao
from app.dao.referenciales.ciudad.FabricanteDao import FabricanteDao

ciumod = Blueprint('ciudad', __name__, template_folder='templates')

@ciumod.route('/ciudad-index')
def ciudadIndex():
    ciudao = CiudadDao()
    return render_template('ciudad-index.html', lista_ciudades=ciudao.getCiudades())

@ciumod.route('/ciudad-agregar')
def ciudadAgregar():
    return render_template('ciudad-agregar.html')

@ciumod.route('/producto-index')
def productoIndex():
    proddao = ProductoDao()
    return render_template('producto-index.html', lista_productos=proddao.getProductos())

@ciumod.route('/producto-agregar')
def productoAgregar():
    return render_template('producto-agregar.html')

@ciumod.route('/fabricante-index')
def fabricanteIndex():
    fabrdao = FabricanteDao()
    return render_template('fabricante-index.html', lista_fabricantes=fabrdao.getFabricantes())

@ciumod.route('/fabricante-agregar')
def fabricanteAgregar():
    return render_template('fabricante-agregar.html')

