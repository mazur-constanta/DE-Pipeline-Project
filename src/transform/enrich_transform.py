# derived columns
# joins (if needed)
# business logic

def enrich_transform(data):
    data["is_hot"] = data["temperature"] > 25
    data["wind_level"] = (
        "low" if data["windspeed"] < 10 else
        "medium" if data["windspeed"] < 25 else
        "high"
    )
    return data