#!/usr/bin/env python3

from sys import argv
host = argv[1] if len(argv) == 3 else '127.0.0.1'
port = argv[2] if len(argv) == 3 else 5000


from flask import Flask, render_template, g, request, redirect, flash, send_file, url_for
from flag import flag
from db import get_db
import os
import hashlib
import time
import subprocess

app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY=b'\x9f\x94@t\x9e\xc0\x84\x14^#\x11t\x11\xafc\x85\xa4\xf3\x1d\xcf\xea]\x8b\xdd='
)


classes = [
#    'Math',
]

class_assignments = {
    'Math'   : {} #{'assignment 1': 'write something interesting'},
}
class_overview = {
    'Math'   : 'Math class',
}


def render(template, **kwargs):
    kwargs['g'] = g
    kwargs['classes'] = classes
    return render_template(template, **kwargs)


def get_assignments(username):
    db = get_db()
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

def sha2(s):
    return hashlib.sha256(s.encode()).hexdigest()

@app.route('/')
def index():
    return render('index.html', class_name='Home')

@app.route('/search', methods=('GET', 'POST'))
def search():
    data=[]
    if request.method == 'POST':
        search_text = request.form.get('search_text')
        sql = \
        "SELECT discription FROM user_submissions "\
        "WHERE assignment_name = '%s';"\
        % (search_text)
        db = get_db()
        data = list(map(
            lambda x: x[0],
            db.execute(sql).fetchall()
        ))
        db.commit()
    return render(
        'search.html',
        data=data
    )


if __name__ == '__main__':
    app.run(
        host=host,
        port=port
    )
