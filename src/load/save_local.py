import os
import json

def save_final(data, path="data/curated/weather.json"):
    os.makedirs(os.path.dirname(path), exist_ok=True)

    with open(path, "w") as f:
        json.dump(data, f, indent=2)