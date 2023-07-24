from kafka import KafkaConsumer
from shared import INFERENCE_TOPIC, KAFKA_SERVER, value_deserializer

consumer = KafkaConsumer(
    INFERENCE_TOPIC,
    value_deserializer=value_deserializer,
    bootstrap_servers=KAFKA_SERVER,
)


def sendEmail(data):
    print(f"Email={data} sent")


for email in consumer:
    sendEmail(data=email.value)
