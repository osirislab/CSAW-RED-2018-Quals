import uuid

from ..app import db, uuid_rand
from ..model.auth import Auth
from ..model.user import User
from ..service.blacklist import save_token
from .. import config


def uuid4():
    a = "%32x" % uuid_rand.getrandbits(128)
    rd = a[:12] + '4' + a[13:16] + 'a' + a[17:]
    return uuid.UUID(rd)


def new_user(data):
    user = Auth.query.filter_by(username=data['username']).first()
    if not user:
        if len(data['password']) < 8:
            response = {
                'status': 'error',
                'message': 'Password too short',
            }
            return response, 400
        if len(data['username']) < 4:
            response = {
                'status': 'error',
                'message': 'Username too short',
            }
            return response, 400
        unique_id = str(uuid4())
        new_auth = Auth(
            uuid=unique_id,
            username=data['username'],
            password=data['password']
        )
        new_user = User(
            username=data['username'],
            uuid=unique_id,
        )
        save(new_auth)
        save(new_user)
        return generate_token(new_auth)
    else:
        response = {
            'status': 'error',
            'message': 'User already exists',
        }
        return response, 409


def new_admin():
    unique_id = str(uuid4())
    new_auth = Auth(
        uuid=unique_id,
        username='admin',
        password=config.admin_password,
        admin=True
    )
    new_user = User(
        username='admin',
        uuid=unique_id
    )
    save(new_auth)
    save(new_user)


def generate_token(user):
    try:
        auth_token = user.encode_auth_token(user.id)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.',
            'Authorization': auth_token.decode(),
            'uuid': user.uuid
        }
        return response_object, 201
    except Exception as e:
        response_object = {
            'status': 'error',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401


def get_logged_in_auth(new_request):
    auth_token = new_request.headers.get('Authorization')
    if auth_token:
        resp = Auth.decode_auth_token(auth_token)
        if not isinstance(resp, str):
            return Auth.query.filter_by(id=resp).first()
    return None


def get_logged_in_user(new_request):
    auth = get_logged_in_auth(new_request)
    if auth:
        return User.query.filter_by(uuid=auth.uuid).first()
    return None


def login(data):
    try:
        auth = Auth.query.filter_by(username=data.get('username')).first()
        if auth and auth.check_password(data.get('password')):
            auth_token = auth.encode_auth_token(auth.id)
            if auth_token:
                response_object = {
                    'status': 'success',
                    'message': 'Successfully logged in.',
                    'Authorization': auth_token.decode()
                }
                return response_object, 200
        else:
            response_object = {
                'status': 'error',
                'message': 'email or password does not match.'
            }
            return response_object, 401
    except Exception as e:
        response_object = {
            'status': 'error',
            'message': 'Try again'
        }
        return response_object, 500


def logout(data):
    if data:
        resp = Auth.decode_auth_token(data)
        if not isinstance(resp, str):
            return save_token(token=data)
        else:
            response_object = {
                'status': 'error',
                'message': resp
            }
            return response_object, 401
    else:
        response_object = {
            'status': 'error',
            'message': 'Provide a valid auth token.'
        }
        return response_object, 403


def save(data):
    db.session.add(data)
    db.session.commit()
