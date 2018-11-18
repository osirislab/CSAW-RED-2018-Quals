from flask import request
from flask_restplus import Namespace, Resource, fields

from ..service.user import login, logout, new_user, get_logged_in_user

api = Namespace('user', description='user related operations')
user_auth = api.model('auth_details', {
    'username': fields.String(required=True, description='username'),
    'password': fields.String(required=True, description='password '),
})

user_model = api.model('user', {
    'username': fields.String(readonly=True, description='username'),
    'money': fields.Integer(readonly=True, description='money')
})


@api.route('/')
@api.response(403, 'Auth Token Invalid.')
class User(Resource):
    @api.doc('get a user by token')
    @api.marshal_with(user_model)
    def get(self):
        """get a user by token"""
        user = get_logged_in_user(request)
        if not user:
            api.abort(403)
        else:
            return user


@api.route('/register')
class UserRegister(Resource):
    @api.response(201, 'User successfully created.')
    @api.doc('create a new user')
    @api.expect(user_auth, validate=True)
    def post(self):
        """Creates a new user """
        data = request.get_json()
        return new_user(data=data)


@api.route('/login')
class UserLogin(Resource):
    @api.doc('user login')
    @api.expect(user_auth, validate=True)
    def post(self):
        data = request.get_json()
        return login(data=data)


@api.route('/logout')
class LogoutAPI(Resource):
    @api.doc('logout a user')
    def post(self):
        auth_header = request.headers.get('Authorization')
        return logout(data=auth_header)
