from flask import Flask, render_template, send_from_directory
from card import Card

app = Flask(__name__)

outs = {
	"resume": "/out/cv",
	"cv": "/raw/cv.pdf",
	"twitter": "https://twitter.com/iandioch",
	"linkedin": "https://ie.linkedin.com/in/iandioch",
	"facebook": "https://facebook.com/noahdonnelly",
	"github": "https://github.com/iandioch" 
}

def create_card(name):
	return Card(name, "cards/" + name + "/template.html", "cards/" + name + "/data.json")

cards = {
	"openbugbounty": create_card("openbugbounty"),
	"euler": create_card("euler"),
}

@app.route("/card/<string:name>")
def get_card(name):
	if name in cards:
		return cards[name].get_data()
	return "ERROR"

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
	print('TEMPLATE, yeah bb')
	return render_template('index.html', cards=[vars(cards[c]) for c in sorted(cards)])

@app.route("/<path:loc>")
def get_root(loc):
	print('Requested "%s"' % loc)
	if loc == '' or loc == '/':
		return get_index()
	return get_raw(loc)

if __name__ == "__main__":
	app.run(host="needs.money", port=80)
