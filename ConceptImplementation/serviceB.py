import json

from kafka import KafkaConsumer
from shared import logger

SERVICE_B_KAFKA_TOPIC = "service_b_kafka_topic"
MESSAGE_DEFAULT_ENCODE = "utf-8"

service_b_consumer = KafkaConsumer(
    SERVICE_B_KAFKA_TOPIC, bootstrap_servers="localhost:29092"
)
while True:
    for service_b_kakfa_topic_message in service_b_consumer:
        consumed_message = json.loads(s=service_b_kakfa_topic_message.value.decode())
        logger.info(f"ServiceB consume the message={consumed_message} from ServiceA")
