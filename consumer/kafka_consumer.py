import json
from pathlib import Path

from kafka import KafkaConsumer

from rules.data_quality import validate_transaction
from rules.fraud_rules import calculate_risk_score, assign_risk_band


TOPIC_NAME = "transactions_raw"
OUTPUT_FILE = Path("data/kafka_transactions_scored.jsonl")


def score_transaction(transaction: dict) -> dict:
    validate_transaction(transaction)

    risk_score = calculate_risk_score(transaction)
    risk_band = assign_risk_band(risk_score)

    transaction["risk_score"] = risk_score
    transaction["risk_band"] = risk_band

    return transaction


def consume_transactions():
    consumer = KafkaConsumer(
        TOPIC_NAME,
        bootstrap_servers="localhost:9092",
        auto_offset_reset="earliest",
        enable_auto_commit=True,
        group_id="fraud-risk-consumer",
        value_deserializer=lambda value: json.loads(value.decode("utf-8"))
    )

    OUTPUT_FILE.parent.mkdir(exist_ok=True)

    with OUTPUT_FILE.open("a", encoding="utf-8") as file:
        for message in consumer:
            transaction = message.value
            scored_transaction = score_transaction(transaction)

            file.write(json.dumps(scored_transaction) + "\n")
            file.flush()

            print(
                f"Consumed and scored: "
                f"{scored_transaction['transaction_id']} "
                f"- {scored_transaction['risk_band']}"
            )


if __name__ == "__main__":
    consume_transactions()