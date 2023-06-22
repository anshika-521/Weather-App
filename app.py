from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

def get_weather(location):
    api_key = '99320609da2d47f984990349232106'
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={location}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather_data = {
            "city": data["location"]["name"],
            "country": data["location"]["country"],
            "temperature": data["current"]["temp_c"],
            "condition": data["current"]["condition"]["text"],
            "icon": data["current"]["condition"]["icon"],
        }
        return weather_data
    return None

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        location = request.form['location']
        weather_data = get_weather(location)
        return render_template('index.html', weather_data=weather_data)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
    