#!/usr/bin/env python3


flag = 'flag{MOVING_UP_IN_THE_WORLD_BRUHH}'
host='127.0.0.1'
port=5000

from flask import Flask, render_template, g, request, redirect, flash, send_file, url_for
import auth
import os
import hashlib
import time
import subprocess

app = Flask(__name__, static_url_path='', static_folder='')
app.config.from_mapping(
    SECRET_KEY=b'\x9f\x94@t\x9e\xc0\x84\x14^#\x11t\x11\xafc\x85\xa4\xf3\x1d\xcf\xea]\x8b\xdd='
)

app.register_blueprint(auth.bp)

classes = [
    'Math',
]

class_assignments = {
    'Math'   : {'assignment 1': 'write something interesting'},
}
class_overview = {
    'Math'   : 'Math class',
}


def render(template, **kwargs):
    kwargs['g'] = g
    kwargs['classes'] = classes
    return render_template(template, **kwargs)


def run_chrome(url):
    url = 'http://127.0.0.1:5000' + url
#    print(url)
    cmd = ['/usr/bin/timeout','15','/usr/bin/chromium-browser','--headless','--disable-gpu','--remote-debugging-port=9222',url]
    print(' '.join(cmd))
    subprocess.Popen(cmd)


def get_assignments(username):
    db = auth.get_db()
    raw = db.execute(
        'SELECT class_name, assignment_name, submission FROM user_submissions WHERE username = ?',
        (username,)
    ).fetchall()
    data = {}
    for class_name, assignment_name, submission in raw:
        if class_name not in data:
            data[class_name] = {}
        data[class_name][assignment_name] = submission
    return data

def submit_assignment(class_name, assignment_name, content):
    db = auth.get_db()
    res = db.execute("""
    SELECT * FROM user_submissions 
    WHERE class_name = ? AND assignment_name = ? AND username = ?;
    """, (class_name, assignment_name, g.user)).fetchall()
    if len(res) == 0:
        sql = """
        INSERT INTO user_submissions 
        (submission, username, class_name, assignment_name, discription) 
        VALUES (?, ?, ?, ?, ?);
        """
    else:
        sql = """
        UPDATE user_submissions SET submission = ?
        WHERE username = ? AND class_name = ? AND assignment_name = ? AND discription = ?;
        """
    #print(sql)
    db.execute(sql, (
        content,
        g.user,
        class_name,
        assignment_name,
        f"{class_name}/{assignment_name}"
    ))
    db.commit()


def sha2(s):
    return hashlib.sha256(s.encode()).hexdigest()

@app.route('/')
@auth.login_required
def index():
    return render('index.html', class_name='Home')


@app.route('/verify/<class_name>/<assignment_name>')
@auth.login_required
def verify_assignment(class_name, assignment_name):
    try:
        db = auth.get_db()
        assignment_id = int(db.execute(
            """
            SELECT id FROM user_submissions
            WHERE username = ? AND class_name = ? AND assignment_name = ?;
            """, (g.user, class_name, assignment_name)
        ).fetchone()[0])
        run_chrome(f'/internal_verify/{assignment_id}')
        flash(('success','sucessfully verified'))
    except:
        flash(('error', 'error verifying'))
    return redirect(f'/') #view/{class_name}/{assignment_name}')

@app.route('/internal_verify/<submission_id>')
#@auth.login_required
def internal_verify(submission_id):
    if request.remote_addr != '127.0.0.1':
        return 'error', 404
    db = auth.get_db()
    content = db.execute(
        """
        SELECT submission FROM user_submissions
        WHERE id = ?;
        """, (submission_id)
    ).fetchone()[0]
    return render('verify.html', content=content)


@app.route('/class/<class_name>')
@app.route('/class/<class_name>/<extension>')
@app.route('/class/<class_name>/<extension>/<assignment_name>')
@auth.login_required
def class_page_ex(class_name, extension=None, assignment_name=None):
    # print(extension, assignment_name)
    if class_name not in classes:
        flash(('error', f'not valid request {request.url}'))
        return redirect('/')
    if assignment_name is not None:
        return render(
            'class.html',
            class_name=class_name,
            extension=extension,
            assignment_name=assignment_name,
        )
    elif extension is not None:
        if extension == 'submissions':
            db = auth.get_db()
            all_assignments = get_assignments(g.user)
            if class_name not in all_assignments:
                all_assignments[class_name] = {}
            content = all_assignments[class_name]
            for key in content:
                if len(content[key]) >= 10:
                    content[key] = content[key][:10] + '...'
            return render(
                'class.html',
                class_name=class_name,
                extension=extension,
                content=content
            )
        elif extension == 'assignments':
            return render(
                'class.html',
                class_name=class_name,
                extension=extension,
                content=class_assignments[class_name]
            )
    else:  # overview
        return render(
            'class.html',
            class_name=class_name,
            content=class_overview[class_name]
        )


#@app.route('/upload/<class_name>/<assignment_name>', methods=('GET', 'POST'))
#@auth.login_required
def upload(class_name, assignment_name):
    if class_name not in classes or assignment_name not in class_assignments[class_name]:
        flash(('error', f'not valid request {request.url}'))
        return redirect('/')
    if request.method == 'POST':
        filename = sha2(f"{g.user}{class_name}{assignment_name}{str(time.time())}")
        file_address = f'user_uploads/submissions/{filename}'
        data = request.files.get('submission')
        if data.content_type != 'application/pdf':
            flash(('error', 'invalid file format'))
            return redirect(f'/upload/{class_name}/{assignment_name}')
        data.save(file_address)
        submit_assignment(class_name, assignment_name, file_address)
        return redirect(f'/view/{class_name}/{assignment_name}')
    else:
        return render(
            'upload.html',
            class_name=class_name,
            assignment_name=assignment_name
        )


#@app.route('/user_uploads/<file_name>')
#@auth.login_required
def serve_submission(file_name):
    src = os.path.join(
        os.path.abspath(os.path.dirname(__file__)),
        'uploads/' + file_name
    )
    return send_file(src)


@app.route('/view/<class_name>/<assignment_name>')
@auth.login_required
def view(class_name, assignment_name):
    if class_name not in classes or assignment_name not in class_assignments[class_name]:
        flash(('error', f'not valid request {request.url}'))
        return redirect('/')
    submissions = get_assignments(g.user)
    if class_name not in submissions or assignment_name not in submissions[class_name]:
        flash(('error',f"{assignment_name} not yet submitted"))
        return redirect('/')
    assignment_file = False
    if submissions[class_name][assignment_name].startswith('user_uploads/'):
        assignment_file = True
    return render(
        'view.html',
        class_name=class_name,
        assignment_name=assignment_name,
        assignment_file=assignment_file,
        assignment_submission=submissions[class_name][assignment_name],
    )


@app.route('/submit/<class_name>/<assignment_name>', methods=('POST',))
@auth.login_required
def submit(class_name, assignment_name):
    if class_name not in classes or assignment_name not in class_assignments[class_name]:
        flash(('error', f'not valid request {request.url}'))
        return redirect('/')
    content = request.form['submission']
    submit_assignment(class_name, assignment_name, content)
    return redirect(f'/view/{class_name}/{assignment_name}')


@app.route('/profile_pictures/<file_name>')
@auth.login_required
def profile_pictures(file_name):
    src = os.path.join(
        os.path.abspath(os.path.dirname(__file__)),
        'profile_pictures/' + file_name
    )
    if file_name != 'default.jpg' and file_name != g.user:
        return "", 404
    return send_file(src)


#@app.route('/profile', methods=("GET", "POST"))
#@auth.login_required
def profile():
    if request.method == 'POST':
        photo = request.files.get('profile_picture')
        photo.save(f'user_uploads/profile_pictures/{sha2(g.user)}')
        return redirect('/profile')
    picture_location = 'user_uploads/profile_pictures/default.jpg'
    if os.path.isfile(f'user_uploads/profile_pictures/{sha2(g.user)}'):
        picture_location = f"/profile_pictures/{sha2(g.user)}"
    return render(
        'profile.html',
        picture_location=picture_location
    )

#@app.route('/search', methods=('GET', 'POST'))
#@auth.login_required
def search():
    data=[]
    if request.method == 'POST':
        search_text = request.form.get('search_text')
        sql = """
        SELECT class_name, assignment_name, submission FROM user_submissions
        WHERE username = '%s' AND (assignment_name LIKE '%s' OR class_name LIKE '%s');
        """ % (g.user, search_text, search_text)
        db = auth.get_db()
        data = db.execute(sql).fetchall()
        db.commit()
        print(data)
    return render(
        'search.html',
        data=data
    )


if __name__ == '__main__':
    app.run(
        host=host,
        port=port
    )
