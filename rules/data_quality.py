REQUIRED_FIELDS = [
    "transaction_id",
    "customer_id",
    "amount",
    "merchant",
    "country",
    "transaction_time",
    "channel",
    "device_id",
    "is_new_device"
]


def validate_transaction(transaction: dict) -> bool:
    for field in REQUIRED_FIELDS:
        if field not in transaction:
            raise ValueError(f"Missing required field: {field}")

        if transaction[field] is None:
            raise ValueError(f"Null value found for field: {field}")

    if transaction["amount"] <= 0:
        raise ValueError("Amount must be greater than zero")

    return True