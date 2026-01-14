def cashflow_forecast(income_history):
    if len(income_history) < 3:
        raise ValueError("Minimum 3 months income required")

    recent = income_history[-3:]
    avg_income = sum(recent) / len(recent)
    volatility = max(recent) - min(recent)

    stability_score = round(max(0, 1 - volatility / avg_income), 2)

    if recent[2] > recent[1] > recent[0]:
        trend = "Increasing"
    elif recent[2] < recent[1] < recent[0]:
        trend = "Decreasing"
    else:
        trend = "Fluctuating"

    return {
        "forecast_income": round(avg_income, 2),
        "volatility": volatility,
        "stability_score": stability_score,
        "trend": trend
    }
