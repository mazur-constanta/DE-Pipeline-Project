import time
import json
import os

from src.extract.fetch_data import fetch_weather
from src.transform.clean_transform import clean_transform
from src.transform.enrich_transform import enrich_transform
from src.transform.validate_transform import validate_transform
from src.load.save_local import save_final
from src.utils.logger import get_logger

logger = get_logger()


def validate_output_file(path="data/curated/weather.json"):
    if not os.path.exists(path):
        raise FileNotFoundError(f"Output file not found: {path}")

    with open(path, "r") as f:
        data = json.load(f)

    if not data:
        raise ValueError("Output file is empty")

    return data


def preview_data(data, n=10):
    logger.info("👀 Data preview:")
    for i, (k, v) in enumerate(data.items()):
        if i >= n:
            break
        logger.info("%s: %s", k, v)


def run_summary(start_time, final_data):
    duration = round(time.time() - start_time, 3)

    return {
        "status": "SUCCESS",
        "records_processed": 1,
        "duration_sec": duration,
        "temperature": final_data.get("temperature"),
        "wind_level": final_data.get("wind_level"),
        "is_hot": final_data.get("is_hot"),
    }


def run_pipeline():
    start_time = time.time()

    logger.info("🚀 Starting Open-Meteo pipeline...")

    try:
        # EXTRACT
        logger.info("📥 Extracting data...")
        raw = fetch_weather()

        # TRANSFORM
        logger.info("🧼 Cleaning data...")
        clean = clean_transform(raw)

        logger.info("🧠 Enriching data...")
        enriched = enrich_transform(clean)

        logger.info("🛡 Validating data...")
        validated = validate_transform(enriched)

        # DEBUG VISIBILITY
        preview_data(validated)

        # LOAD
        logger.info("💾 Loading data...")
        save_final(validated)

        # FILE VALIDATION
        output = validate_output_file()
        logger.info("📁 File validation OK. keys=%s", list(output.keys()))

        # SUMMARY
        summary = run_summary(start_time, validated)
        logger.info("📊 Run Summary: %s", summary)

        logger.info("✅ Pipeline finished successfully!")

    except Exception as e:
        logger.error("❌ Pipeline failed: %s", str(e))
        raise


if __name__ == "__main__":
    run_pipeline()