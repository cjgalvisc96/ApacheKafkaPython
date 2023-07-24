import json

value_deserializer = lambda m: json.loads(m.decode("utf-8"))

APP_PORT = 5000
INFERENCE_TOPIC = "INFERENCE"
KAFKA_SERVER = "localhost:29092"
NOTIFICATION_TOPIC = "NOTIFICATION"
EMAIL_TOPIC = "EMAIL"
