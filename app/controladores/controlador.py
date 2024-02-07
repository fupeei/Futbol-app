from app import app
from flask import render_template, request, redirect, Response, send_file, flash
import requests
import random

@app.route("/")
def home():
    API_KEY = 'b038d907a68d47fd849e664f9cd2dd0d' 
    base_url = 'http://api.football-data.org/v4/persons/'
    random_number = random.randint(0, 1000) 
    player_id = str(random_number)
    url = base_url + player_id 
    headers = {'X-Auth-Token': API_KEY} 
    response = requests.get(url, headers=headers) 
    if response.status_code == 200:
        data = response.json() 
        print(data) 
    else: print('Error al realizar la solicitud:', response.status_code)
    return render_template("home.html", data = data)