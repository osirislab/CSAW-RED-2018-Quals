from flask import Flask, url_for, send_from_directory
import hashlib

app = Flask(__name__)

@app.route('/<path:path>')
def blah(path):
    return send_from_directory('static', filename='extract.png')

if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug = False)
