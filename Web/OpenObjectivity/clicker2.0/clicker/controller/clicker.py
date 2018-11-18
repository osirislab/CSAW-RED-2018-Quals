from flask import request
from flask_restplus import Namespace, Resource, fields

from ..service.clicker import get_clicker, get_all_clickers, get_clicker_field
from ..service.user_click import purchase_clicker, use_clicker
from ..service.user_click import get_user_clickers
from ..util.decorator import token_required, rate_limit

api = Namespace('clicker', description='clicker related operations')


@api.route('/')
class AllClicker(Resource):
    @api.response(200, 'Retrived all clickers')
    @api.doc('Get all clickers')
    def get(self):
        """Get all clickers"""
        return get_all_clickers()


@api.route('/<name>')
@api.param('name', 'The clicker name')
@api.param('field', 'The clicker field to check')
@api.response(404, 'Clicker not found.')
class Clicker(Resource):
    @api.doc('Get a clicker by name')
    def get(self, name):
        """Get a clicker by name"""
        field = request.args.get('field')
        if field:
            clicker = get_clicker_field(name, field)
        else:
            clicker = get_clicker(name)
        if not clicker:
            api.abort(404)
        else:
            return clicker


@api.route('/purchase')
class PurchaseClicker(Resource):
    @api.param('name', 'The clicker name', required=True)
    @api.response(201, 'Clicker purchased')
    @token_required()
    @api.doc('Purchase a clicker by name')
    def post(self):
        """Purchase a clicker by name"""
        clicker = purchase_clicker(request=request)
        if not clicker:
            api.abort(404)
        else:
            return clicker


@api.route('/click')
class UseClicker(Resource):
    @api.doc('Use a clicker by name')
    @api.param('name', 'The clicker name', required=True)
    @api.response(201, 'Clicker used')
    @token_required()
    @rate_limit(2)
    def post(self):
        """Use a clicker by name"""
        clicker = use_clicker(request)
        if not clicker:
            api.abort(404)
        else:
            return clicker


@api.route('/user')
class GetClickers(Resource):
    @api.doc('Get user clickers')
    @api.response(404, 'User not found')
    @token_required()
    def get(self):
        """Get a clicker by user"""
        clicker = get_user_clickers(request)
        return clicker
