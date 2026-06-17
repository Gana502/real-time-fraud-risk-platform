from fastapi import FastAPI

from rules.data_quality import validate_transaction
from rules.fraud_rules import calculate_risk_score, assign_risk_band

app = FastAPI()


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.post("/score-transaction")
def score_transaction(transaction: dict):

    validate_transaction(transaction)

    risk_score = calculate_risk_score(transaction)
    risk_band = assign_risk_band(risk_score)

    return {
        "transaction_id": transaction["transaction_id"],
        "risk_score": risk_score,
        "risk_band": risk_band
    }