# pip install apify-client  |  APIFY_TOKEN=... python run.py
import json, os, pathlib
from apify_client import ApifyClient
client = ApifyClient(os.environ["APIFY_TOKEN"])
run_input = json.loads((pathlib.Path(__file__).parent / "input.json").read_text())
run = client.actor("clearfeedlabs/storm-roofing-feed").call(run_input=run_input)
items = list(client.dataset(run["defaultDatasetId"]).iterate_items())
print(f"Got {len(items)} items")
print(json.dumps(items[:3], indent=2, default=str))
