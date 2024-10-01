from flask import Blueprint, render_template
from app.dao.referenciales.fabricante.FabricanteDao import FabricanteDao

ciumod = Blueprint('fabricante', __name__, template_folder='templates')


@ciumod.route('/fabricante-index')
def fabricanteIndex():
    fabrdao = FabricanteDao()
    return render_template('fabricante-index.html', lista_fabricantes=fabrdao.getFabricantes())

@ciumod.route('/fabricante-agregar')
def fabricanteAgregar():
    return render_template('fabricante-agregar.html')

