from flask import Flask, render_template, jsonify
import random
import time

app = Flask(__name__)

# Simulated IoT data
def get_sensor_data():
    return {
        "temperature": round(random.uniform(20.0, 30.0), 2),
        "humidity": round(random.uniform(30.0, 70.0), 2),
        "timestamp": time.strftime('%H:%M:%S')
    }

@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/data')
def data():
    return jsonify(get_sensor_data())

if __name__ == '__main__':
    app.run(debug=True)
