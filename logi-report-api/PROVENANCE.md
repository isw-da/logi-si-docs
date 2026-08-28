# Where this spec came from, and what it is worth

## Source

`logireportserver.yaml`, copied out of a running Logi Report Server **26.2 SP1**
container from:

```
/opt/LogiReport/Server/help/webapi/logireportserver.yaml
```

The server ships a bundled Swagger UI at `help/webapi/webapi-docs/` whose
`swagger-initializer.js` loads `../logireportserver.yaml`. So this is the
vendor's own published API definition, not something reconstructed from prose.

- **Spec format:** Swagger 2.0 (`swagger: "2.0"`), title "Logi Report Server",
  spec version 1.3.0
- **Base path:** `/jrserver/api/v1.2`
- **124 paths, 225 operations, 11 tags**
- SHA-256 recorded in `api/spec/SPEC.sha256` and re-checked against the running
  container by `scripts/verify_api.py`, both of which live in
  [`logi-report-kb`](https://github.com/isw-da/logi-report-kb) rather than here.
  This repository carries a copy of the spec and its index, not the gate.

## How this compares with Composer

| | Logi Report | Logi Composer |
|---|---|---|
| Spec format | **Swagger 2.0** | **OpenAPI 3.1.0** |
| Paths | 124 | 223 |
| Operations | 225 | 344 |
| Tags | 11 | 74 |
| How obtained | shipped file inside the server install | pulled from a live `/discovery/api-docs` |

The Composer column describes `../composer-api/composer-openapi.json` as it
stands, which is the SI-bundled 26.2.1 pull of 27 August 2026. The hosted
instance served 220 paths and 338 operations, and `../composer-api/ENDPOINTS.md`
indexes both.

**The format difference is the practical catch.** Anything consuming both (an MCP
server, a codegen step, a validator) must either handle Swagger 2.0 and OpenAPI
3.1 or convert one to the other. Do not assume a tool that works against
`composer-openapi.json` will work here unchanged.

## Two checks that were tried and discarded

Recorded so nobody adds them back believing they prove something.

**1. "A real endpoint returns non-404 on the live server."** Discarded. The server
returns **401 for every path under `/jrserver/api`**, including fabricated ones:

```
/jrserver/api/v1.2/bookmark      401     (real)
/jrserver/api/v1.2/zzzznotreal   401     (invented)
/jrserver/api/v9.9/tree          401     (invented version)
```

The control returned exactly what the real endpoints returned, so the check
cannot distinguish a genuine endpoint from an invented one. It would have passed
against a completely fabricated spec.

**2. "A spec path appears as a string in the server jars."** Discarded. Real paths
(`bookmark/default/clear`, `node/rptcatrelation`, `sso/register`) and the control
string all returned **zero** matching jars. It proves nothing either way.

## What the gate actually proves, and what it does not

The gate is `scripts/verify_api.py` in `logi-report-kb`, and it runs there rather
than here. The copy of the spec in this repository is byte-identical to the one
that gate covers: `shasum -a 256` on `logireport-openapi.yaml` here and on
`logi-report-kb/api/spec/logireport-openapi.yaml` gave the same digest,
`b98899cd...5957`, on 28 August 2026.

**Proves:** the spec is byte-identical to the one the running 26.2 SP1 server
ships, the JSON mirror agrees with the YAML, and `ENDPOINTS.md` lists every one
of the 225 operations with none silently dropped.

**Does not prove:** that every documented endpoint behaves as described, or that
the server implements nothing beyond the spec. Verifying behaviour needs an
authenticated call per endpoint, which has not been done. Treat the spec as
authoritative on **surface**, not on **behaviour**.
