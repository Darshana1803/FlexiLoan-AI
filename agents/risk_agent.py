def evaluate_risk(forecast_income, base_emi, has_existing_emi=False, income_trend="Fluctuating"):
    emi_ratio = base_emi / forecast_income
    risk_score = emi_ratio

    if has_existing_emi:
        risk_score += 0.15

    if income_trend == "Decreasing":
        risk_score += 0.10
    elif income_trend == "Increasing":
        risk_score -= 0.05

    if risk_score < 0.30:
        risk_level = "Low"
    elif risk_score < 0.50:
        risk_level = "Medium"
    else:
        risk_level = "High"

    return {
        "emi_ratio": round(emi_ratio, 2),
        "risk_score": round(risk_score, 2),
        "risk_level": risk_level
    }
