def monitor_and_adjust(current_income, current_emi):
    ratio = current_emi / current_income

    if ratio > 0.4:
        return {"action": "Reduce EMI", "new_emi": round(current_emi * 0.75, 2)}
    return {"action": "No Change", "new_emi": current_emi}
