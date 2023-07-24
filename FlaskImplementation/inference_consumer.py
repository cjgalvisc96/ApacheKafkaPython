from kafka import KafkaConsumer, KafkaProducer
from shared import (EMAIL_TOPIC, INFERENCE_TOPIC, KAFKA_SERVER,
                    NOTIFICATION_TOPIC)

consumer = KafkaConsumer(INFERENCE_TOPIC, bootstrap_servers=KAFKA_SERVER)

producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER)


def inferencProcessFunction(data):
    producer.send(topic=NOTIFICATION_TOPIC, value=data)
    producer.flush()

    producer.send(topic=EMAIL_TOPIC, value=data)
    producer.flush()


for inf in consumer:
    inferencProcessFunction(data=inf.value)
