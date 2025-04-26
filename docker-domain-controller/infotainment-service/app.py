from flask import Flask, jsonify
import random
import time

app = Flask(__name__)

@app.route('/telemetry')
def telemetry():
    data = {
        'timestamp': time.strftime('%Y-%m-%dT%H:%M:%SZ'),
        'vehicleId': 'TEST123',
        'speed': random.randint(60, 120),
        'battery': random.randint(20, 100),
        'location': {'lat': 13.0827, 'lon': 80.2707}
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
