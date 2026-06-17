import pytest

from rules.data_quality import validate_transaction


def valid_transaction():
    return {
        "transaction_id": "TXN001",
        "customer_id": "CUST001",
        "amount": 100,
        "merchant": "Amazon",
        "country": "UK",
        "transaction_time": "2026-06-17T10:00:00Z",
        "channel": "card",
        "device_id": "DEV001",
        "is_new_device": False
    }


def test_valid_transaction_passes():
    assert validate_transaction(valid_transaction()) is True


def test_missing_customer_id_fails():
    transaction = valid_transaction()
    del transaction["customer_id"]

    with pytest.raises(ValueError):
        validate_transaction(transaction)


def test_negative_amount_fails():
    transaction = valid_transaction()
    transaction["amount"] = -10

    with pytest.raises(ValueError):
        validate_transaction(transaction)