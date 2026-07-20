# Composer visual/dashboard API on SI 26.2 — verified behaviours

Field-verified 2026-07-20 against SI 26.2.0 (chart install, kind), building a
four-widget dashboard programmatically end to end. Nothing here is in the
official docs; everything was established by driving the live API.
Companion operational guide:
`isw-da/simba-intelligence-skill/simba-intelligence-setup/references/composer-dashboard-api.md`.

## Endpoints exercised

| Call | Notes |
|---|---|
| `GET /discovery/api/sources` | vendor media type `application/vnd.composer.v3+json`; basic auth admin works |
| `GET /api/sources/{id}/fields` | field `name` vs `label` (business label) |
| `GET /api/sources/{id}/visual-types` | id field is `visualTypeId` |
| `GET /api/sources/{id}/visual-types/{vt}/initial-visual` | THE template source; never hand-craft |
| `POST /api/visuals`, `PUT /api/visuals/{id}` | `level` must be `IN_DASHBOARD` |
| `POST /api/dashboards`, `PUT /api/dashboards/{id}` | widget swap via PUT works |
| `GET/POST /discovery/api/license` | licence read/apply; `DISABLE_BI_FEATURES` gates the whole BI surface |

## Behaviours not documented anywhere

1. **Visual filters are `path`/`operation`/`value`**, e.g.
   `{"path": "alert_type", "operation": "IN", "value": ["cycle", "fan_in"]}`.
   `name`/`operator` keys render as "invalid filters" in the widget.
2. **Metric funcs verified:** `sum`, `distinct_count`. The row-count
   pseudo-metric `{"name": "count"}` is rejected (KPI shows "Metric:
   Unavailable"). Colour metric slots (`Bar Color`) need `func` too or the
   visual dies with "unsupported metric function".
3. **KPI `Comparison Metric` must be non-empty**; `[]` crashes the widget
   client-side (`TypeError ... reading 'value'`).
4. **Variable vocabulary by type:** KPI `Metric`/`Comparison Metric`/
   `Conditional Formatting`; UBER_BARS `Multi Group By`/`Metric`/`Bar Color`;
   DONUT `Group By`/`Size`; LINE_CHART `Y Axis`/`Trend Attribute`.
5. **SPA routes:** `/discovery/` 302-redirects to
   `/discovery/visualization/home`; dashboards at
   `/discovery/visualization/{tenantId}_{dashboardId}`; sources at
   `/discovery/source/library`. Spring 400s any `//` in a path, and the SPA
   builds asset URLs from `location.pathname`, so reverse proxies must pass
   redirects through untouched.
6. **Dashboard data is WebSocket-fed**; HTTP-only proxies show spinners
   forever. Headless screenshots need a real-time wait (Chrome
   `--virtual-time-budget` fires before WS data lands).
7. **After a pg_restore of the zoomdata DBs, sequences lag their tables**; the
   first API write dies on `acl_entry_pkey`. Resync sequences before first
   write (full SQL in the skill repo reference).
