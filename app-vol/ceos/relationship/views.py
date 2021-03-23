from flask import make_response, request, jsonify
# from .models import TbVinculoFamiliar as CPFBound
from flask.views import MethodView
import random


class FamilyBondView(MethodView):

    def get(self, cpf):

        if cpf is None:
            response = {
                'message': 'No Content'
            }
            return make_response(jsonify(response)), 200
        else:
            response = []
            for i in range(10):
                response.append({
                    'id': i+1,
                    'cpf1': random.randint(i, cpf)
                })
            return make_response(jsonify(response)), 200
            
    def post(self):
        # create a new user
        pass

    def delete(self, cpf):
        # delete a single user
        pass

    def put(self, cpf):
        # update a single user
        pass
