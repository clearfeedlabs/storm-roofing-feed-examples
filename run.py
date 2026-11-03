# pip install apify-client  |  APIFY_TOKEN=... python run.py
import json, os
from apify_client import ApifyClient
client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("clearfeedlabs/storm-roofing-feed").call(run_input=json.load(open("input.json")))
items = client.dataset(run["defaultDatasetId"]).list_items().items
print(f"Got {len(items)} items")
print(json.dumps(items[:3], indent=2))
