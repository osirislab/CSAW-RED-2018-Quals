import datetime
import json

from ..app import db
from ..model.user_click import UserClicker
from ..model.user import User
from ..service.clicker import clickers, get_clicker
from ..service.user import get_logged_in_user, get_logged_in_auth


def purchase_clicker(request):
    data = request.get_json()
    user = get_logged_in_user(request)
    clicker_name = data['name']
    if clicker_name not in clickers:
        response = {
            'status': 'error',
            'message': 'Clicker does not exist',
        }
        return response, 409

    user_clicker = UserClicker.query.filter_by(uuid=user.uuid,
                                               name=clicker_name).first()
    quantity = 0
    if user_clicker:
        quantity = user_clicker.quantity
    clicker = get_clicker(clicker_name)
    if quantity >= clicker['max']:
        response = {
            'status': 'error',
            'message': 'Clicker quantity limited to 10',
        }
        return response, 400
    price = clicker['price'] * (clicker['scale'] ** quantity)

    if round(user.money - price) >= 0:
        if not user_clicker:
            user_clicker = UserClicker(
                name=clicker_name,
                uuid=user.uuid
            )
            save(user_clicker)
            response = {
                'status': 'success',
                'message': 'Clicker purchased',
            }
        else:
            user_clicker.quantity += 1
            response = {
                'status': 'success',
                'message': 'Clicker upgraded',
            }
        user.money -= round(price)
        db.session.commit()
        return response, 201

    else:
        response = {
            'status': 'error',
            'message': 'Not enough money',
        }
        return response, 409


def use_clicker(request):
    data = request.get_json()
    user = get_logged_in_user(request)
    auth = get_logged_in_auth(request)
    if not user or not auth:
        response = {
            'status': 'error',
            'message': 'No Such User',
        }
        return response, 409
    clicker_name = data['name']
    if clicker_name not in clickers:
        response = {
            'status': 'error',
            'message': 'Clicker does not exist',
        }
        return response, 409
    clicker = get_clicker(clicker_name)
    user_clicker = UserClicker.query.filter_by(uuid=user.uuid,
                                               name=clicker_name).first()
    if not user_clicker:
        response = {
            'status': 'error',
            'message': 'Clicker not owned',
        }
        return response, 409
    if user.money + user_clicker.quantity * clicker['value'] > 3000000000000:
        user.money = user_clicker.quantity * clicker['value']
    else:
        user.money += user_clicker.quantity * clicker['value']
    curr_time = datetime.datetime.utcnow()
    time_diff = curr_time - user.record_time
    if time_diff > datetime.timedelta(seconds=5):
        user.record = 0
        user.record_time = curr_time
    else:
        user.record += user_clicker.quantity * clicker['value']
    auth.last_modified = curr_time
    db.session.commit()
    response = {
        'status': 'success',
        'message': 'Clicker successfully used',
    }
    return response, 201


def get_user_clickers(request):
    user = get_logged_in_user(request)
    clickers = UserClicker.query.filter_by(uuid=user.uuid).all()
    clicker_list = []
    for clicker in clickers:
        comb_clicker = {'name': clicker.name, 'quantity': clicker.quantity}
        clicker_data = get_clicker(clicker.name)
        comb_clicker['value'] = clicker.quantity * clicker_data['value']
        scale = clicker_data['scale'] ** clicker.quantity
        comb_clicker['price'] = int(clicker_data['price'] * scale)
        clicker_list.append(comb_clicker)
    return str(clicker_list)


def save(data):
    db.session.add(data)
    db.session.commit()
