# coding: utf-8

from flask import Blueprint, jsonify
from flask_security import login_required
from ..db import db, ma

api = Blueprint('relationship', __name__)

# status
# 200 - ok
# 201 - created - POST
# 400 - Bad request (sintaxe invalida, nao entendeu)
# 401 - Unauthorized
# 403 - Forbidden
# 404 - Not found
# 408 - request timeout

class RelationShip(db.Model):
    __tablename__ = 'tb_relacao_pf_pf_31012019'

    id = db.Column(db.BigInteger, primary_key=True)
    relacao = db.Column(db.String(4000))
    fonte = db.Column(db.String(4000))
    tipo = db.Column(db.String(4000))
    cpf1 = db.Column(db.BigInteger)
    cpf2 = db.Column(db.BigInteger)

class RelationShipSchema(ma.ModelSchema):
    class Meta:
        model = RelationShip

@api.route('/relationship/<int:id>', methods=['GET'])
def get_relationship_id(id):

    try:
        rst = RelationShip.query.get_or_404(id)
    except:
        return jsonify({"message": "Not found."}), 404

    schema = RelationShipSchema(strict=True)

    return schema.jsonify(rst)


@api.route('/test', methods=['GET'])
@login_required
def test():
    return 'logado'
