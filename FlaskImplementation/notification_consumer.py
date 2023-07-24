from kafka import KafkaConsumer
from shared import INFERENCE_TOPIC, KAFKA_SERVER, value_deserializer

consumer = KafkaConsumer(
    INFERENCE_TOPIC,
    value_deserializer=value_deserializer,
    bootstrap_servers=KAFKA_SERVER,
)


def sendNotification(data):
    print(f"Notification ={data} sent")


for notification in consumer:
    sendNotification(data=notification.value)
