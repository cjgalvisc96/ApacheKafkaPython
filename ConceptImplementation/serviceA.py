import json
from time import sleep

from kafka import KafkaProducer
from shared import logger

SERVICE_B_KAFKA_TOPIC = "service_b_kafka_topic"
MESSAGE_DEFAULT_ENCODE = "utf-8"

service_a_producer = KafkaProducer(bootstrap_servers="localhost:29092")
while True:
    message_to_send_to_service_b_kafka_topic = json.dumps(
        obj={"key_test": "value_test"}
    ).encode(encoding=MESSAGE_DEFAULT_ENCODE)

    service_a_producer.send(
        topic=SERVICE_B_KAFKA_TOPIC, value=message_to_send_to_service_b_kafka_topic
    )
    logger.info(
        f"ServiceA send the message={message_to_send_to_service_b_kafka_topic} to {SERVICE_B_KAFKA_TOPIC}"
    )
    sleep(2)
