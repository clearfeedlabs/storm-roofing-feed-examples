# Storm & Hail Damage Leads: NOAA Hail Reports by ZIP Code: examples

ZIP codes hit by hail, damaging wind, tornadoes and hurricanes from official NWS warnings, NOAA Storm Events and OpenFEMA declarations, scored by severity and joined with city roofing-permit surges. Street-level permit counts, no homeowner data. Incremental runs.

This repo shows how to call the [Hail & Storm Leads](https://apify.com/clearfeedlabs/storm-roofing-feed) Apify Actor from JavaScript or Python, and what the output looks like.

## What's new
- Clear input error when every source is off; empty runs explain why in the run status.

## Use cases
- Roofing and restoration contractors choosing where to canvass
- Insurance and claims teams monitoring storm exposure
- Building-material suppliers planning inventory
- Market research on storm-driven demand

## Quick start
1. Create a free Apify account and copy your API token from Settings > Integrations.
2. Set it as an environment variable: `export APIFY_TOKEN=...` (never commit it).
3. Edit `input.json`, then run one of:
   - JavaScript: `npm i apify-client && node run.mjs`
   - Python: `pip install apify-client && python run.py`

## Output fields (first of many)
`eventId`, `eventDate`, `eventType`, `source`, `state`, `county`, `countyFips`, `zip`, `zipCentroidLat`, `zipCentroidLon`, `maxHailInches`, `maxWindMph`, `tornadoEF`, `reportCount`, `nwsWarningIds`, `headline`, `femaDeclarationNumber`, `femaIncidentType`

See `sample-output.json` for one trimmed record.

## Ready-made example tasks
- [Austin hail roof permit surge](https://apify.com/clearfeedlabs/storm-roofing-feed/examples/austin-hail-roof-permit-surge)
- [Dallas fort worth roof permit surge](https://apify.com/clearfeedlabs/storm-roofing-feed/examples/dallas-fort-worth-roof-permit-surge)
- [Florida hurricane wind fema zips](https://apify.com/clearfeedlabs/storm-roofing-feed/examples/florida-hurricane-wind-fema-zips)

## Pricing
Pay per result: **$5.00 per 1,000 storm ZIP rows**, with no subscription. The [Store page](https://apify.com/clearfeedlabs/storm-roofing-feed) always shows current prices and every optional add-on event.

## FAQ
**Is this data official?** Yes. It comes from the public source named above, and each record links back to it.
**Do I need a login or proxy?** No. It uses documented public endpoints only.
**Can I schedule it?** Yes. Use Apify Schedules, the API or integrations (Zapier, Make, webhooks, MCP-compatible AI agents).

## Links
- Actor on the Apify Store: https://apify.com/clearfeedlabs/storm-roofing-feed
- Details & pricing: https://clearfeedlabs.com/actors/storm-roofing-feed/
- Clearfeed Labs: https://clearfeedlabs.com
- Bugs or questions: open an issue on the Actor's Issues tab on Apify.

Data comes from public sources and is provided as-is. Check the original source before relying on it. Not legal, financial or investment advice.

License: MIT
