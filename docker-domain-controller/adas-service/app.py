from flask import Flask, jsonify
import random
import time

app = Flask(__name__)

@app.route('/adas-data')
def adas_data():
    data = {
        'timestamp': time.strftime('%Y-%m-%dT%H:%M:%SZ'),
        'vehicleId': 'ADAS001',
        'laneDepartureWarning': random.choice([True, False]),
        'collisionWarning': random.choice([True, False]),
        'blindSpotMonitor': random.choice([True, False]),
        'distanceToCarAhead': random.randint(5, 100)  # in meters
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
