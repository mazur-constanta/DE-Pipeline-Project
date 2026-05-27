# null handling
# schema normalization
# type casting
# deduplication

def clean_transform(data):
    return {
        "temperature": float(data["temperature"]),
        "windspeed": float(data["windspeed"]),
        "weather_code": int(data["weather_code"]),
        "latitude": float(data["latitude"]),
        "longitude": float(data["longitude"]),
        "timestamp": data["timestamp"]
    }