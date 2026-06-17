import json
import random
from datetime import datetime, timezone
from pathlib import Path

from rules.data_quality import validate_transaction
from rules.fraud_rules import calculate_risk_score, assign_risk_band


OUTPUT_FILE = Path("data/transactions_scored.jsonl")


def generate_transaction(transaction_number: int) -> dict:
    """Create one fake transaction."""

    transaction = {
        "transaction_id": f"TXN{transaction_number:06d}",
        "customer_id": f"CUST{random.randint(1, 20):03d}",
        "amount": round(random.uniform(5, 2500), 2),
        "merchant": random.choice(["Amazon", "Tesco", "Apple", "Netflix", "Uber", "Airline"]),
        "country": random.choice(["UK", "UK", "UK", "US", "IN", "AE"]),
        "transaction_time": datetime.now(timezone.utc).isoformat(),
        "channel": random.choice(["card", "online", "mobile"]),
        "device_id": f"DEV{random.randint(1, 50):03d}",
        "is_new_device": random.choice([True, False])
    }

    return transaction


def score_transaction(transaction: dict) -> dict:
    """Validate a transaction and add risk score."""

    validate_transaction(transaction)

    risk_score = calculate_risk_score(transaction)
    risk_band = assign_risk_band(risk_score)

    transaction["risk_score"] = risk_score
    transaction["risk_band"] = risk_band

    return transaction


def write_transactions_to_file(number_of_transactions: int = 100) -> None:
    """Generate scored transactions and write them to a JSONL file."""

    OUTPUT_FILE.parent.mkdir(exist_ok=True)

    with OUTPUT_FILE.open("w", encoding="utf-8") as file:
        for transaction_number in range(1, number_of_transactions + 1):
            transaction = generate_transaction(transaction_number)
            scored_transaction = score_transaction(transaction)

            file.write(json.dumps(scored_transaction) + "\n")

    print(f"Generated {number_of_transactions} scored transactions at {OUTPUT_FILE}")


if __name__ == "__main__":
    write_transactions_to_file()