import os.path
import random
import string
import uuid

from flask_restplus import Api, Namespace, Resource, fields
from flask import Blueprint, request

from .util.decorator import admin_token_required, token_required
from .controller.user import api as user_ns
from .controller.clicker import api as clicker_ns
from .service.user import get_logged_in_user
from .model.user import User
from .model.auth import Auth
from .app import db

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='CLICKER 2.0 REST API',
          version='1.0',
          description='clicker 2.0'
          )

default = Namespace('default', description='Default namespace', doc=False)


def random_string():
    random_str = ''
    lowercase = string.ascii_lowercase
    index = random.randint(0, len(lowercase) - 1)
    for character in [lambda x: x[index] for i in range(10)]:
        random_str += character(lowercase)
    return random_str


@default.route('/', doc=False)
class Default(Resource):
    def get(self):
        """Creates a new user"""
        if request.headers.get('bring_back_random_click') == random_string():
            f_path = os.path.dirname(__file__) + '/../../flags/flag1.txt'
            with open(f_path, 'r') as f:
                return f.read().strip()
        else:
            api.abort(404)


@default.route('/money', doc=False)
class MoneyDefault(Resource):
    @token_required()
    def get(self):
        user = get_logged_in_user(request)
        if user.money >= 0:
            api.abort(404)
        else:
            f_path = os.path.dirname(__file__) + '/../../flags/flag2.txt'
            with open(f_path, 'r') as f:
                return f.read().strip()


@default.route('/admin/money', doc=False)
class AdminMoneyDefault(Resource):
    @admin_token_required()
    @api.param('uuid', 'uuid', required=True)
    @api.param('value', 'value', required=True)
    def post(self):
        data = request.get_json()
        if not data or 'value' not in data or 'uuid' not in data:
            api.abort(404)
        value = int(data['value'])
        user = User.query.filter_by(uuid=data['uuid']).first()
        if not user or value < 0:
            api.abort(404)
        else:
            if user.money + value > 3000000000000:
                user.money = 3000000000000
            else:
                user.money += value
            db.session.commit()


@default.route('/admin/uuid', doc=False)
class AdminUUIDDefault(Resource):
    @admin_token_required()
    @api.param('uuid', 'uuid', required=True)
    @api.param('value', 'value', required=True)
    def post(self):
        data = request.get_json()
        value = int(data['value'])
        auth = Auth.query.filter_by(uuid=data['uuid']).first()
        if not auth or value < 0:
            api.abort(404)
        else:
            auth.uuid = str(uuid.UUID(int=int(uuid.UUID(auth.uuid)) + value))
            db.session.commit()


@default.route('/record', doc=False)
class RecordDefault(Resource):
    @token_required()
    def get(self):
        user = get_logged_in_user(request)
        if user.record < 5000000000:
            api.abort(404)
        else:
            f_path = os.path.dirname(__file__) + '/../../flags/flag3.txt'
            with open(f_path, 'r') as f:
                return f.read().strip()


api.namespaces.pop(0)
api.add_namespace(default, path='/default')
api.add_namespace(clicker_ns, path='/clicker')
api.add_namespace(user_ns, path='/user')
