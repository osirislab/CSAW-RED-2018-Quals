import datetime
import jwt

from functools import wraps
from flask import request

from ..app import db
from ..service.user import get_logged_in_auth


def rate_limit(reqs_per_sec):
    def decorator(f):
        def decorated(*args, **kwargs):

            auth = get_logged_in_auth(request)
            if not auth:
                response_object = {
                    'status': 'error',
                    'message': 'Provide a valid auth token.'
                }
                return response_object, 401
            curr_time = datetime.datetime.utcnow()
            interval = datetime.timedelta(seconds=(1 / reqs_per_sec))
            if curr_time - auth.last_modified < interval:
                auth.brute_check += 1
                db.session.commit()
                if auth.brute_check > 60:
                    db.session.delete(auth)
                    db.session.commit()
                    response_object = {
                        'status': 'error',
                        'message': 'You\'ve been banned'
                    }
                    return response_object, 429
                attempts = 60 - auth.brute_check
                response_object = {
                    'status': 'error',
                    'message': 'Will ban in %d more attempts' % attempts
                }
                return response_object, 429

            return f(*args, **kwargs)
        return decorated

    return decorator


def token_required():
    def decorator(f):
        def decorated(*args, **kwargs):

            auth = get_logged_in_auth(request)
            if not auth:
                response_object = {
                    'status': 'error',
                    'message': 'Provide a valid auth token.'
                }
                return response_object, 401

            return f(*args, **kwargs)
        return decorated
    return decorator


def admin_token_required():
    def decorator(f):
        def decorated(*args, **kwargs):
            auth = get_logged_in_auth(request)
            if auth and auth.admin:
                return f(*args, **kwargs)

            response_object = {
                'status': 'error',
                'message': 'admin token required'
            }
            return response_object, 401
        return decorated
    return decorator
