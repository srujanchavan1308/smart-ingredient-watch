def create_alert(analysis_result):
    label = analysis_result.get("alert_color", "Yellow")
    if label == "Red":
        risk = "High"
    elif label == "Green":
        risk = "Low"
    else:
        risk = "Moderate"
        
    alert = {
        "ingredient": analysis_result.get("ingredient", ""),
        "risk_level": risk,
        "side_effects": analysis_result.get("side_effects", "Unknown"),
        "alert_color": label
    }
    return alert
