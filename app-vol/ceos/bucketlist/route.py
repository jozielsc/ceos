from flask import Blueprint, request, jsonify, abort, make_response
from .models import Bucketlist
from ..auth.models import User


bucket = Blueprint('bucketlist', __name__)

@bucket.route('/test', methods=['GET'])
def test():
    bucketlists = Bucketlist.get_all()
    results = []

    for bucketlist in bucketlists:
        obj = {
            'id': bucketlist.id,
            'name': bucketlist.name,
            'created_at': bucketlist.created_at,
            'modified_at': bucketlist.modified_at,
            'created_by': bucketlist.created_by
        }
        results.append(obj)
    return make_response(jsonify(results)), 200

@bucket.route('/', methods=['POST', 'GET'])
def bucketlists():
    try:
        auth_header = request.headers.get('Authorization')
        access_token = auth_header.split(" ")[1]

        if access_token:
            user_id = User.decode_token(access_token)

            if not isinstance(user_id, str):

                if request.method == "POST":
                    name = str(request.data.get('name', ''))
                    if name:
                        bucketlist = Bucketlist(name=name, created_by=user_id)
                        bucketlist.save()
                        response = jsonify({
                            'id': bucketlist.id,
                            'name': bucketlist.name,
                            'created_at': bucketlist.created_at,
                            'modified_at': bucketlist.modified_at,
                            'created_by': user_id
                        })

                        return make_response(response), 201
                else:
                    # GET
                    bucketlists = Bucketlist.query.filter_by(created_by=user_id)
                    results = []

                    for bucketlist in bucketlists:
                        obj = {
                            'id': bucketlist.id,
                            'name': bucketlist.name,
                            'created_at': bucketlist.created_at,
                            'modified_at': bucketlist.modified_at,
                            'created_by': bucketlist.created_by
                        }
                        results.append(obj)
                    return make_response(jsonify(results)), 200
            else:
                response = {
                    'message': 'Nao autorizado.'
                }
                # 401 - Unauthorized
                return make_response(jsonify(response)), 401
    except Exception as e:
        # Create a response containing an string error message
        response = {
            'message': str(e)
        }

        return make_response(jsonify(response)), 500

@bucket.route('/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def bucketlist_manipulation(id, **kwargs):
    # get the access token from the authorization header
    auth_header = request.headers.get('Authorization')
    access_token = auth_header.split(" ")[1]

    if access_token:
        # Get the user id related to this access token
        user_id = User.decode_token(access_token)

        if not isinstance(user_id, str):
            # If the id is not a string(error), we have a user id
            # Get the bucketlist with the id specified from the URL (<int:id>)
            bucketlist = Bucketlist.query.filter_by(id=id).first()
            if not bucketlist:
                # There is no bucketlist with this ID for this User, so
                # Raise an HTTPException with a 404 not found status code
                abort(404)

            if request.method == "DELETE":
                # delete the bucketlist using our delete method
                bucketlist.delete()
                return {
                    "message": "bucketlist {} deleted".format(bucketlist.id)
                }, 200

            elif request.method == 'PUT':
                # Obtain the new name of the bucketlist from the request data
                name = str(request.data.get('name', ''))

                bucketlist.name = name
                bucketlist.save()

                response = {
                    'id': bucketlist.id,
                    'name': bucketlist.name,
                    'created_at': bucketlist.created_at,
                    'modified_at': bucketlist.modified_at,
                    'created_by': bucketlist.created_by
                }
                return make_response(jsonify(response)), 200
            else:
                # Handle GET request, sending back the bucketlist to the user
                response = {
                    'id': bucketlist.id,
                    'name': bucketlist.name,
                    'created_at': bucketlist.created_at,
                    'modified_at': bucketlist.modified_at,
                    'created_by': bucketlist.created_by
                }
                return make_response(jsonify(response)), 200
        else:
            # user is not legit, so the payload is an error message
            message = user_id
            response = {
                'message': message
            }
            # return an error response, telling the user he is Unauthorized
            return make_response(jsonify(response)), 401
