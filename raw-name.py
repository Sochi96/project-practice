from flask import Flask, render_template, request
import requests

global PLAYER

app = Flask("Pheonix-App")

@app.route('/')
def hello():
   return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
	global PLAYER
	PLAYER = request.form['name']
	return render_template("weather-page.html", WHATEVER=PLAYER)


@app.route("/go", methods=["POST"])
def playGame():
	global PLAYER
	return "hello" + PLAYER


app.run(debug=True)
