from flask import Flask
import hashlib

app = Flask(__name__)

@app.route('/<path:path>')
def blah(path):
    print (path)
    return "OK"
if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug = False)
