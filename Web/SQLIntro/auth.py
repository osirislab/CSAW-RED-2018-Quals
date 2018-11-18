from flask import request, redirect, url_for, flash, render_template, session, Blueprint, g
# from werkzeug.security import check_password_hash, generate_password_hash
from db import get_db
import functools


bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        if db.execute(
                "SELECT * FROM users WHERE username = '%s' and password = '%s'" %
                (username, password,)
        ).fetchone() is not None:
            user = username
        else:
            error = 'Incorrect username or password.'
        # user = db.execute(
        #     'SELECT * FROM users WHERE username = "%s"' % username
        # ).fetchone()

        # if user is None:
        #     error = 'Incorrect username.'
        # elif not check_password_hash(user[2], password):
        #     error = 'Incorrect password.'

        if error is None:
            session.clear()
            session['user_id'] = user
            return redirect(url_for('index'))

        flash(('error', error))

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
            g.user = get_db().execute(
                'SELECT username FROM users WHERE username = "%s"' % (user_id,)
            ).fetchone()[0]
    except:
        g.user = None


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view
