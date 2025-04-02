from kafka import KafkaProducer

TOPIC_NAME = "locations"
KAFKA_SERVER = 'udaconnect-kafka-controller-0.kafka-headless.default.svc.cluster.local:9092'
API_VERSION = (4, 0 ,0)

producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER, api_version=API_VERSION)
producer.send(TOPIC_NAME, b'{"person_id": 1, "longitude": 1.0, "latitude": 2.0}')
producer.flush()
producer.close()