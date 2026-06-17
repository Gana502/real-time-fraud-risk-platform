def calculate_risk_score(transaction: dict) -> int:

    score = 0

    if transaction["amount"] > 1000:
        score += 40

    if transaction["country"] != "UK":
        score += 25

    if transaction["channel"] in ["online", "mobile"]:
        score += 10

    if transaction["is_new_device"]:
        score += 25

    return min(score, 100)


def assign_risk_band(score: int) -> str:

    if score >= 70:
        return "HIGH"

    elif score >= 40:
        return "MEDIUM"

    return "LOW"