import json

from flask import Flask, jsonify, request
from kafka import KafkaProducer
from shared import APP_PORT, INFERENCE_TOPIC, KAFKA_SERVER

app = Flask(import_name=__name__)

producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER)


@app.route("/kafka/push_to_consumers", methods=["POST"])
def kafka_producer():
    json_payload = json.dumps(obj=dict(request.get_json())).encode("utf-8")

    producer.send(topic=INFERENCE_TOPIC, value=json_payload)
    producer.flush()

    return jsonify({"result": "Message send to the consumers"})


if __name__ == "__main__":
    app.run(debug=True, port=APP_PORT)
