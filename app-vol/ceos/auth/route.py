from flask import Blueprint

from .views import registration_view, login_view

auth = Blueprint('auth', __name__)

# Define the rule for the registration url --->  /register
# Then add the rule to the blueprint
auth.add_url_rule(
    '/register',
    view_func=registration_view,
    methods=['POST']
)

# Define the rule for the registration url --->  /login
auth.add_url_rule(
    '/login',
    view_func=login_view,
    methods=['POST']
)
