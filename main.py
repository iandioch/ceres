from flask import Flask

app = Flask(__name__)

@app.route("/")
def get_root():
	return "Hello World!"

@app.route("/card/<string:name>")
def get_card(name):
	return name

if __name__ == "__main__":
	app.run(host="needs.money", port=9010)
