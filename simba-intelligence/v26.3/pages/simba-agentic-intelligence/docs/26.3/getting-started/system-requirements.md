> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# System requirements

# System Requirements

Simba Intelligence is deployed as part of the Self-Service Analytics (formerly Logi Composer) Helm chart, so your cluster must be sized for the whole Self-Service Analytics deployment plus the Simba Intelligence components on top.

> **⚠️ Right-size for your workload:** The figures below are a starting point based on the chart's default resource **requests**. Actual requirements vary widely with data sources, concurrency, and which optional services you enable. Overprovision initially, measure, then adjust.

***

## Kubernetes Infrastructure

| Requirement | Detail |
| - | - |
| **Kubernetes** | 1.22+ (1.25+ and Gateway API CRDs v1.0.0+ if using Gateway API routing) |
| **Helm** | Version 3 |
| **Nodes** | 2+ worker nodes for production |
| **Storage** | Default StorageClass with dynamic provisioning; ReadWriteOnce volumes for most components — but see the shared-volume note below |
| **Ingress** | A functional ingress controller **you provide** — as of 26.3 the chart no longer installs one by default (`ingress.installController: false`) |
| **DNS** | Functional cluster DNS |

> **⚠️ Shared volume needs `ReadOnlyMany` and a pre-provisioned PV.** The chart creates a `composer-shared-volume` PersistentVolumeClaim by default (`composerSharedVolume.enabled: true`) with `accessModes: [ReadOnlyMany]`. Unlike the rest of the chart's storage, this PVC does **not** use dynamic provisioning — it statically binds to a PersistentVolume you create in advance with a matching name, size, and access mode, so a plain ReadWriteOnce-only StorageClass (typical cloud block storage such as EBS or a Persistent Disk) won't satisfy it. You'll need a storage backend that supports multi-node read access (NFS, CephFS, Azure Files, EFS, or similar) and a PV provisioned ahead of the install, or set `composerSharedVolume.enabled: false` if you don't need it.

***

## Compute

The chart README's **Kubernetes Requirements** section carries the authoritative per-service CPU and memory requests. As a baseline:

* **Self-Service Analytics core services** (`zoomdataWeb`, `queryEngine`, `sdkService`, `dataWriter`) — roughly **6.5 CPU cores and 13Gi memory** in requests.
* **Optional Self-Service Analytics services** (`screenshotService`, `reportService`, `dataGatewayService`) are disabled by default; add their requests if you enable them.
* **Simba Intelligence** (`simbaIntelligence.enabled: true`) adds the REST API service, Celery worker, Celery beat, Redis, the database-migration Job, and — when `simbaIntelligence.mcp.enabled: true` — the MCP server. See the `simbaIntelligence.*.resources` values for current defaults.
* **Bundled dependencies** (PostgreSQL, Consul, and where enabled the OpenTelemetry Collector or Prometheus), any External Data Connectors, and headroom for autoscaling are all on top of the above.

Get the current numbers straight from the chart:

```shell theme={null}
helm show readme composer/composer --version <VERSION>
helm show values composer/composer --version <VERSION>
```

***

## Database

PostgreSQL is required. The chart deploys an in-cluster, single-replica PostgreSQL (`postgresql.enabled: true`) that creates the `simbaintelligence` database alongside the `zoomdata-*` databases.

* **Production:** use an external managed PostgreSQL (Amazon RDS, Google Cloud SQL, Azure Database for PostgreSQL). Set `postgresql.enabled: false`, then configure `simbaIntelligence.database.host` and the Self-Service Analytics `*DbUrl` values. The external database must exist before installation — the migration Job applies the schema but does not create the database.
* **Development and QA:** the in-cluster PostgreSQL is intended for these environments only.

> **⚠️ 26.3 breaking change:** Chart-managed PostgreSQL now defaults to PostgreSQL 18, and the legacy Bitnami PostgreSQL subchart has been removed entirely. Upgrades from an existing Bitnami-based internal PostgreSQL **fail** with guidance to migrate to an external database first. See the chart README's **Internal Database** section.

***

## Redis

Simba Intelligence uses Redis as the Celery broker and semantic cache. The chart's in-cluster Redis is configured correctly out of the box.

If you point Simba Intelligence at an external Redis (`simbaIntelligence.redis.external.*`), that instance must have these modules loaded:

| Module | Library | Purpose |
| - | - | - |
| RediSearch | `redisearch.so` | Full-text and vector similarity search |
| RedisJSON | `rejson.so` | JSON document storage |
| RedisTimeSeries | `redistimeseries.so` | Time-series data |
| RedisBloom | `redisbloom.so` | Probabilistic data structures |

Also set `maxmemory-policy` to `volatile-ttl` so cached data with a TTL is evicted before critical data. A managed external Redis (ElastiCache, Azure Cache for Redis, Memorystore) is recommended for production, for the same reasons as an external database.

***

## Networking

**External access:**

* Outbound internet access for container image pulls, or an internal registry — see [Air-Gapped Deployment](../deployment/installation-and-setup/air-gapped-deployment)
* Outbound access to your AI/LLM provider endpoints — Simba Intelligence cannot function without it
* A load balancer or ingress for user access, with TLS certificates for production

**Internal:**

* Standard Kubernetes pod-to-pod networking and service discovery
* Network policies appropriate to your production standards

***

## Next Steps

➡️ [Installation Guide](./installation-guide) — deploy the chart

➡️ [Helm Chart Reference](../deployment/installation-and-setup/helm-chart-reference) — discover every configuration value
