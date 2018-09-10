from flask import request, redirect, url_for, flash, render_template, session, Blueprint, g
# from werkzeug.security import check_password_hash, generate_password_hash
#from db import get_db
import functools
import pymysql.cursors

bp = Blueprint('auth', __name__, url_prefix='/auth')


def get_db():
    return pymysql.connect(
        host='localhost',
        user='root',
        db='red',
        password='youonlygetoneshot',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )


def execute(db, query):
    with db.cursor() as cursor:
        #print(query)
        cursor.execute(query)
        return cursor.fetchall()


#@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        elif db.execute(
            "SELECT id FROM users WHERE username = '%s'" % username
        ).fetchone() is not None:
            error = 'User {} is already registered.'.format(username)

        if error is None:
            db.execute(
                "INSERT INTO users (username, password) VALUES ('%s', '%s')" %
                (username, password)
            )
            db.commit()
            return redirect(url_for('auth.login'))

        flash(error)

    return render_template('auth/register.html')


@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        db = get_db()
        error = None
        res = execute(db,
            "SELECT id FROM users WHERE username = '%s' and password = '%s'" %
            (username, password,)
        )
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
    # print(user_id)

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
