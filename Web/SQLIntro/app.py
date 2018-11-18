#!/usr/bin/env python3

from sys import argv
host = argv[1] if len(argv) == 3 else '127.0.0.1'
port = argv[2] if len(argv) == 3 else 5000

from flask import Flask, render_template, g, request, redirect, flash, send_file, url_for
import auth
import os
import hashlib
import time
import subprocess
from flag import flag


app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY=b'\x9f\x94@t\x9e\xc0\x84\x14^#\x11t\x11\xafc\x85\xa4\xf3\x1d\xcf\xea]\x8b\xdd='
)

app.register_blueprint(auth.bp)

classes = [
#    'Math',
]

class_assignments = {
    'Math'   : {'assignment 1': 'write a report'},
    'english': {'assignment 2': 'write an essay'}
}
class_overview = {
    'Math'   : 'Math class',
    'English': 'English class'
}


def render(template, **kwargs):
    kwargs['g'] = g
    kwargs['classes'] = classes
    return render_template(template, **kwargs)


def sha2(s):
    return hashlib.sha256(s.encode()).hexdigest()

@app.route('/')
@auth.login_required
def index():
    return render(
        'index.html',
        content=flag
    )


if __name__ == '__main__':
    app.run(
        host=host,
        port=port
    )
