// npm i apify-client  |  APIFY_TOKEN=... node run.mjs
import { ApifyClient } from 'apify-client';
import { readFileSync } from 'node:fs';
const client = new ApifyClient({ token: process.env.APIFY_TOKEN });
const input = JSON.parse(readFileSync(new URL('./input.json', import.meta.url)));
const run = await client.actor('clearfeedlabs/storm-roofing-feed').call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(`Got ${items.length} items`);
console.log(JSON.stringify(items.slice(0, 3), null, 2));
