from flask import Blueprint
from flask_cors import CORS

from .views import FamilyBondView
from ..db import db

blueprint = Blueprint('relationship', __name__)
CORS(blueprint)

def register_api(view, endpoint, url, pk='id', pk_type='int'):
    view_func = view.as_view(endpoint)
    blueprint.add_url_rule(url, defaults={pk: None},
                     view_func=view_func, methods=['GET',])
    blueprint.add_url_rule(url, view_func=view_func, methods=['POST',])
    blueprint.add_url_rule('%s<%s:%s>' % (url, pk_type, pk), view_func=view_func,
                     methods=['GET', 'PUT', 'DELETE'])



register_api(FamilyBondView, 'family_bond_view', '/naturalperson/', pk='cpf')
