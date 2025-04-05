import json
import os
import time
from concurrent import futures

import grpc
import location_pb2
import location_pb2_grpc
from kafka import KafkaProducer

KAFKA_URL = os.environ["KAFKA_URL"]
KAFKA_TOPIC = os.environ["KAFKA_TOPIC"]

class locationServicer(location_pb2_grpc.LocationServiceServicer):
    def Create(self, request, context):            

        location_data = {
            "person_id": int(request.person_id),
            "longitude": request.longitude,
            "latitude": request.latitude,
            "creation_time": request.creation_time
        }
        print(location_data)

        producer = KafkaProducer(bootstrap_servers=KAFKA_URL)

        producer.send(KAFKA_TOPIC, json.dumps(location_data).encode('utf-8'))
        producer.flush()

        return location_pb2.locationMessage(**location_data)


# Initialize gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
location_pb2_grpc.add_LocationServiceServicer_to_server(locationServicer(), server)


print("Server starting on port 5005...")
server.add_insecure_port("[::]:5005")
server.start()
# Keep thread alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)
