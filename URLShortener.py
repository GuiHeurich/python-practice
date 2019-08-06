import flask
from flask import request, jsonify
import random

app = flask.Flask(__name__)
app.config['DEBUG'] = True

def shorten(url):
    urls = {}
    short_url = list(url.split("//")[-1].split(".")[1])
    short_url = random.sample(short_url, 3)
    urls['short_url'] = '/%s' % ("".join(short_url))
    urls['url'] = url
    return urls

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Welcome to URL Shortener</h1>'''

@app.route('/url', methods=['POST'])
def parse_request():
    data = request.get_json(force=True)
    urls = shorten(data['url'])
    return jsonify(urls)

app.run()
