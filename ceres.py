from flask import Flask, send_from_directory
from jinja2 import Template, Environment, FileSystemLoader
from card import Card
import sys
import json

app = Flask(__name__)

env = Environment(loader=FileSystemLoader('/home/noah/prog/ceres/templates'))

outs = {
    "resume": "/out/cv",
    "cv": "/raw/cv.pdf",
    "twitter": "https://twitter.com/iandioch",
    "linkedin": "https://ie.linkedin.com/in/iandioch",
    "facebook": "https://facebook.com/noahdonnelly",
    "github": "https://github.com/iandioch" 
}

def render_template(name, d):
    template = env.get_template(name)
    return template.render(d)

def create_card(name):
    return Card(name, "cards/" + name + "/data.json")

cards = {
    "openbugbounty": create_card("openbugbounty"),
    "euler": create_card("euler"),
    "kattis": create_card("kattis"),
    "lastfm": create_card("lastfm"),
    "blog": create_card("blog"),
    "twitter": create_card("twitter"),
    "untappd": create_card("untappd"),
}

@app.route("/cards")
def get_cards():
    d = {card:json.loads(cards[card].get_data()) for card in cards}
    return json.dumps(d)

@app.route("/raw/<path:loc>")
def get_raw(loc):
    return send_from_directory('raw', loc)

@app.route("/out/<path:loc>")
def get_out(loc):
    if loc in outs:
        return '<meta http-equiv="refresh" content="0;url=%s">'%outs[loc]
    return "<h1>uwu what's this</h1>"

@app.route("/")
def get_index():
    return render_template('index.html', {})

@app.route("/<path:loc>")
def get_root(loc):
    print('Requested "%s"' % loc)
    if loc == '' or loc == '/':
        return get_index()
    return get_raw(loc)

if __name__ == "__main__":
    app.run(host="localhost", port=9010)
