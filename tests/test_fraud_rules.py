from rules.fraud_rules import (
    calculate_risk_score,
    assign_risk_band
)


def test_high_risk_transaction():

    transaction = {
        "amount": 1500,
        "country": "US",
        "channel": "mobile",
        "is_new_device": True
    }

    score = calculate_risk_score(transaction)

    assert score == 100
    assert assign_risk_band(score) == "HIGH"


def test_low_risk_transaction():

    transaction = {
        "amount": 20,
        "country": "UK",
        "channel": "card",
        "is_new_device": False
    }

    score = calculate_risk_score(transaction)

    assert score == 0
    assert assign_risk_band(score) == "LOW"