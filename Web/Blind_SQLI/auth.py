from flask import request, redirect, url_for, flash, render_template, session, Blueprint, g
import functools
import pymysql.cursors

bp = Blueprint('auth', __name__, url_prefix='/auth')


DB = pymysql.connect(
    host='localhost',
    user='red_user',
    db='red',
    password='password',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        error = None
        with DB.cursor() as cursor:
            cursor.execute(
                "SELECT id FROM users WHERE username = '%s' and password = '%s'" %
                (username, password,)
            )
            res = cursor.fetchall()
            cursor.close()
        if len(res) != 0:
            user = username
        else:
            error = 'Incorrect username or password.'

        if error is None:
            session.clear()
            session['user_id'] = user
            return redirect('/')
        else:
            flash(('error', error))
            return render_template('auth/login.html'), 400

    return render_template('auth/login.html')


@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    try:
        if user_id is None:
            g.user = None
        else:
            g.user = user_id
    except:
        g.user = None


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view
