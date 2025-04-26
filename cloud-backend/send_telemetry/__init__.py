import logging
import azure.functions as func
import json
from datetime import datetime
from azure.eventhub import EventHubProducerClient, EventData

# Replace with your Event Hub connection string and name
EVENT_HUB_CONN_STR = "Endpoint=sb://<your-namespace>.servicebus.windows.net/;SharedAccessKeyName=<key-name>;SharedAccessKey=<key>"
EVENT_HUB_NAME = "<your-event-hub-name>"

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Sending telemetry data to Event Hub.')

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

    try:
        producer = EventHubProducerClient.from_connection_string(conn_str=EVENT_HUB_CONN_STR, eventhub_name=EVENT_HUB_NAME)
        event_data_batch = producer.create_batch()
        event_data_batch.add(EventData(json.dumps(telemetry_data)))
        producer.send_batch(event_data_batch)
        producer.close()
        return func.HttpResponse("Telemetry sent to Event Hub.", status_code=200)
    except Exception as e:
        logging.error(f"Error sending telemetry: {e}")
        return func.HttpResponse("Failed to send telemetry.", status_code=500)
