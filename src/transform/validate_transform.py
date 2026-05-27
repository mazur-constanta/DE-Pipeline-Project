# data quality checks:
# row count
# schema validation
# null thresholds

def validate_transform(data):
    assert -50 < data["temperature"] < 60, "Invalid temperature"
    assert 0 <= data["windspeed"] < 200, "Invalid windspeed"
    assert data["weather_code"] is not None, "Missing weather code"
    return data