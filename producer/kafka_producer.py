import json
import time

from kafka import KafkaProducer

from producer.transaction_producer import generate_transaction


TOPIC_NAME = "transactions_raw"


producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda value: json.dumps(value).encode("utf-8")
)


def publish_transactions():
    transaction_number = 1

    while True:
        transaction = generate_transaction(transaction_number)

        producer.send(TOPIC_NAME, value=transaction)

        print(f"Published transaction: {transaction['transaction_id']}")

        transaction_number += 1
        time.sleep(2)


if __name__ == "__main__":
    publish_transactions()