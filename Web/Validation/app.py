#!/usr/bin/env python3

from sys import argv
host = argv[1] if len(argv) > 1 else '0.0.0.0'
port = argv[2] if len(argv) > 1 else 1234

from flask import Flask, render_template, g, request, redirect, flash, send_file, url_for
from db import get_db
import os
import hashlib
import time
import subprocess
from flag import flag

app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY=b'\x9f\x94@t\x9e\xc0\x84\x14^#\x11t\x11\xafc\x85\xa4\xf3\x1d\xcf\xea]\x8b\xdd='
)

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
    url = 'http://127.0.0.1:1234' + url
    print(url)
    cmd = ['/usr/bin/timeout','15','/usr/bin/chromium-browser','--headless','--disable-gpu','--remote-debugging-port=9222','--no-sandbox',url]
    print(' '.join(cmd))
    subprocess.Popen(cmd)


@app.route('/flag.txt')
def gib_flag_plz():
    if request.remote_addr != '127.0.0.1':
        return 'error', 404
    return flag


@app.route('/verify/<assignment_id>')
def verify(assignment_id):
    if request.remote_addr != '127.0.0.1':
        return 'error', 404
    db = get_db()
    content = db.execute(
        'SELECT content FROM user_submissions WHERE id = ?',
        (assignment_id,)
    ).fetchone()[0]
    db.execute('delete from user_submissions where id = ?', (assignment_id,))
    db.commit()
    return render('verify.html', content=content)


def submit_assignment(content):
    db = get_db()
    sql1 = "INSERT INTO user_submissions (content) VALUES (?);"
    sql2 = "SELECT id FROM user_submissions WHERE content = ?"
    db.execute(sql1, (content,))
    assignment_id = db.execute(sql2, (content,)).fetchone()[0]
    db.commit()
    return assignment_id


def sha2(s):
    return hashlib.sha256(s.encode()).hexdigest()

@app.route('/')
def index():
    return render('index.html', content='Do your homework!')

@app.route('/class/<class_name>')
@app.route('/class/<class_name>/<extension>')
@app.route('/class/<class_name>/<extension>/<assignment_name>')
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
            db = get_db()
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


@app.route('/submit', methods=('POST',))
def submit():
    content = request.form['submission']
    assignment_id = submit_assignment(content)
    run_chrome('/verify/{}'.format(assignment_id))
    return redirect('/')


if __name__ == '__main__':
    app.run(
        host=host,
        port=port
    )
