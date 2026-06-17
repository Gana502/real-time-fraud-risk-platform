from producer.transaction_producer import generate_transaction, score_transaction


def test_generate_transaction_has_required_fields():
    transaction = generate_transaction(1)

    assert "transaction_id" in transaction
    assert "customer_id" in transaction
    assert "amount" in transaction


def test_score_transaction_adds_risk_fields():
    transaction = generate_transaction(1)

    scored_transaction = score_transaction(transaction)

    assert "risk_score" in scored_transaction
    assert "risk_band" in scored_transaction