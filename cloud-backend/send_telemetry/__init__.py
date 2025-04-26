import logging
import azure.functions as func
import json
from datetime import datetime

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Received telemetry data request.')

    telemetry_data = {
        "timestamp": datetime.utcnow().isoformat(),
        "vehicleId": "DEMO-001",
        "speed": 72,
        "battery": 88,
        "mediaStatus": "Playing",
        "location": {
            "lat": 13.0827,
            "lon": 80.2707
        }
    }

    return func.HttpResponse(json.dumps(telemetry_data), mimetype="application/json")
