from flask import Flask, render_template, request
import requests

global PLAYER
global ACCURATE
global WARMNESS
global THEPLACE
global ATMOSPHERE

app = Flask("Pheonix-App")

@app.route('/')
def hello():
   return render_template("index.html")
#This is the landing page for local:5000
@app.route("/submit", methods=["POST"])
def submit():
	global PLAYER
	PLAYER = request.form['name']
	return render_template("weather-page.html", WHATEVER=PLAYER)

"""@app.route("/go", methods=["POST"])
def playGame():
	global PLAYER
	return "hello" + PLAYER""" #not sure this is relevant

@app.route("/weather", methods=["POST"])
def showWeather():
	global ACCURATE
	ACCURATE = request.form['city']

	endpoint = "http://api.openweathermap.org/data/2.5/weather"
	payload = {"q": ACCURATE, "units":"metric", "appid":"b2881e99916c9f734029b9cd9a2aeb78"}

	response = requests.get(endpoint, params=payload)
	data = response.json()

	

	temperature = data["main"]["temp"]
	name = data["name"]
	weather = data["weather"][0]["main"]
	print u"It's {}C in {}, and the sky is {}".format(temperature, name, weather)
	
	return render_template("after-weather.html", WHATEVER=PLAYER, WARMNESS=temperature, THEPLACE=name, ATMOSPHERE=weather)



app.run(debug=True)
