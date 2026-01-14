def structure_loan(forecast_income, risk_level, has_existing_emi=False):
    if risk_level == "Low":
        ratio = 0.30
        tenure = 12
    elif risk_level == "Medium":
        ratio = 0.25
        tenure = 18
    else:
        ratio = 0.20
        tenure = 24

    if has_existing_emi:
        ratio -= 0.05
        tenure += 6

    emi = round(forecast_income * ratio, 2)

    return {
        "adaptive_emi": emi,
        "tenure_months": tenure,
        "policy": "Dynamic EMI based on income and risk"
    }
