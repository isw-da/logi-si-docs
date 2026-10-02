> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Helm chart reference

# Helm Chart Reference Guide

Simba Intelligence ships inside the Self-Service Analytics (formerly Logi Composer) Helm chart. That chart is the source of truth for every configuration option, and it is updated with each release — so rather than restating its tables here, this guide shows you how to read them directly.

For a first deployment, start with the [Installation Guide](../../getting-started/installation-guide) and come back here when you need to customize.

## Prerequisites

Install [Helm](https://helm.sh/docs/intro/install/) 3 and verify it:

```shell theme={null}
helm version
```

## Adding the Repository

```shell theme={null}
helm repo add composer https://composer-repo.logianalytics.com/helm-charts/stable/
helm repo update
```

### Finding Versions

```shell theme={null}
helm search repo composer/composer --versions
```

Chart versions follow semantic versioning; the `appVersion` column shows the Self-Service Analytics release each chart deploys.

## Reading the Chart

Everything you need lives in three files. You can read them without downloading anything:

```shell theme={null}
# Default configuration values — the complete schema
helm show values composer/composer --version <VERSION>

# Installation and configuration guide, with parameter tables
helm show readme composer/composer --version <VERSION>

# Chart metadata, version, and subchart dependencies
helm show chart composer/composer --version <VERSION>
```

Redirect the values to a file to use as the starting point for your own overrides:

```shell theme={null}
helm show values composer/composer --version <VERSION> > my-values.yaml
```

To examine the templates as well, pull and extract the chart:

**Linux/macOS/WSL:**

```bash theme={null}
helm pull composer/composer --version <VERSION>
tar -xzf composer-<VERSION>.tgz
cd composer/
```

**Windows PowerShell:**

```powershell theme={null}
helm pull composer/composer --version <VERSION>
Expand-Archive -Path "composer-<VERSION>.tgz" -DestinationPath "."
cd composer\
```

| File | Contains |
| - | - |
| `values.yaml` | Complete configuration schema with defaults and inline comments |
| `README.md` | Parameter tables, database setup, external secrets, ingress examples, change list |
| `Chart.yaml` / `Chart.lock` | Chart version, `appVersion`, and pinned subchart dependency versions |
| `templates/` | The Kubernetes resources the chart creates |

> **📋 Best resource:** The chart README's **Parameters** section explains what each commonly-overridden key does, including its type and default. The values file covers everything else.

***

## Where Simba Intelligence Lives in the Values

| Area | Values path |
| - | - |
| Simba Intelligence master switch | `simbaIntelligence.enabled` |
| MCP server (opt-in) | `simbaIntelligence.mcp.enabled` |
| REST API service | `simbaIntelligence.website.*` |
| Celery worker and beat | `simbaIntelligence.celery.worker.*`, `simbaIntelligence.celery.beat.*` |
| Data retention windows | `simbaIntelligence.celery.worker.questionRecordRetentionDays`, `.purgeTaskResultsDays` |
| Database migration Job | `simbaIntelligence.dbMigrate.*` |
| Database connection | `simbaIntelligence.database.*` |
| Redis (in-chart or external) | `simbaIntelligence.redis.*`, `simbaIntelligence.redis.external.*` |
| Ingress routes | `ingress.simbaIntelligence.path`, `.mcp.path`, `.wellKnown.path` |
| Self-Service Analytics services | Top level — `zoomdataWeb.*`, `queryEngine.*`, `edc.*`, and so on |

Each `simbaIntelligence.website` / `.mcp` / `.celery.worker` / `.dbMigrate` block follows the same shape as the other services in the chart: `image`, `resources`, probes, `extraEnvs`, autoscaling, security contexts, and `priorityClassName`.

> **📝 Note:** Both retention keys default to `""`, which omits the environment variable entirely and leaves the application default of 90 days in effect. Only the worker reads them. See [Environment Variables Reference](../../reference/supplementary-resources/environment-variables-reference#data-retention).

***

## Two Common Installation Requirements

**`zoomdataWeb.adminPassword` is mandatory — and must meet Self-Service Analytics' own password policy.** Simba Intelligence authenticates against the Self-Service Analytics API with it. The chart validates that it is set and **fails the install or upgrade** if it is missing — but that check only confirms the value is present, not that Self-Service Analytics will accept it. The application itself requires at least 9 characters with 1 lowercase, 1 uppercase, 1 number, and 1 special character (`!@#$%^&*()-_=+,.:;<>`); a non-compliant password passes the Helm-level check but makes the `zoomdataWeb` pod fail at startup instead. Use `zoomdataWeb.existingSecret` to source a compliant password from a Secret instead.

> **⚠️ Changing this password after first install:** The chart-managed PostgreSQL only applies its `initdb` credentials once, on first boot. If you change `defaultDbPassword` or a per-service database password on an existing release, the database itself keeps the old password and every service that reads the new one will fail to authenticate. Rotate database passwords through PostgreSQL directly (or through your external managed database's own tooling), not by editing values on an existing release.

**`simbaIntelligence.composerPublicUrl` must resolve.** This is the browser-reachable Self-Service Analytics URL. Empty (recommended) auto-derives it from the first `ingress.hosts` entry, then the first `gatewayapi.httproute.hostnames` entry. Unlike the admin password, an unresolved URL is **not** an install-time failure — the install succeeds, `NOTES.txt` prints a warning, every pod reports healthy, and Simba Intelligence then errors at runtime the first time it needs the URL. Set `ingress.hosts`, `gatewayapi.httproute.hostnames`, or `composerPublicUrl` explicitly.

> **Prerequisite:** Trusted access must also be enabled in Self-Service Analytics itself. It is enabled by default.

***

## Installing and Upgrading

```shell theme={null}
# Validate before installing — shows exactly what will be created
helm install <release-name> composer/composer --version <VERSION> \
  -f my-values.yaml --dry-run --debug

# Install
helm install <release-name> composer/composer --version <VERSION> -f my-values.yaml

# Upgrade
helm upgrade <release-name> composer/composer --version <VERSION> -f my-values.yaml
```

See [Upgrade Procedures](../operations-and-maintenance/upgrade-procedures) for upgrade planning and the 26.3 breaking changes.

### Quick Reference

```shell theme={null}
helm list                                   # List installed releases
helm status <release-name>                  # Check release status
helm history <release-name>                 # View release history
helm get values <release-name>              # Get current release values
helm rollback <release-name> <revision>     # Roll back
helm uninstall <release-name>               # Remove release
```

***

## Configuration Topics in the Chart README

Rather than duplicating them, these topics are covered in depth in the chart's own README — read it with `helm show readme composer/composer --version <VERSION>`:

* **Database** — internal PostgreSQL, external managed databases, and the Simba Intelligence `database.host`/`.port`/`.name` values
* **External Secrets** — sourcing database, Redis, license, and admin credentials from Secrets you manage
* **Traffic Routing** — ingress examples per controller (NGINX, Traefik, ALB, GCE) and Kubernetes Gateway API, including the Simba Intelligence and MCP routes
* **Observability and Autoscaling** — the bundled Prometheus, Prometheus Adapter, and OpenTelemetry Collector dependencies, and HPA configuration
* **Helm Chart Change List** — user-facing changes per release, newest first

> **⚠️ Subchart values:** Not every value available in a dependency chart is compatible with the way this chart configures it. For heavy customization of PostgreSQL or Redis, disable the bundled service and use an external one instead.

***

## Troubleshooting

```shell theme={null}
# Release status
helm status <release-name>

# Everything the chart created
kubectl get all -l app.kubernetes.io/instance=<release-name>

# Simba Intelligence pods specifically
kubectl get pods -l app.kubernetes.io/component=composer-simba-intelligence

# Database migration Job — app pods wait on this
kubectl get jobs -l app.kubernetes.io/instance=<release-name>
kubectl logs -l app.kubernetes.io/component=composer-simba-intelligence-dbmigrate --tail=100

# Pods stuck in Init are waiting on the schema
kubectl logs <pod-name> -c wait-for-database-schema

# Detail on a specific pod
kubectl describe pod <pod-name>
kubectl logs <pod-name>
```

**Simba Intelligence features missing from the Self-Service Analytics UI:**

1. Confirm `simbaIntelligence.enabled: true` in your released values (`helm get values <release-name>`).
2. Confirm the REST API responds at `<contextPath>/intelligence/apidocs/` — if it loads, the backend is healthy.
3. Confirm `composerPublicUrl` resolved correctly (see above).
4. Confirm the enhanced-experience toggle is enabled in Self-Service Analytics settings.

For Helm-level issues, see the [official Helm troubleshooting guide](https://helm.sh/docs/topics/troubleshooting/).

***

**Remember:** `values.yaml`, `README.md`, and `Chart.yaml` in the chart you are actually deploying are the authoritative source. When this page and the chart disagree, the chart is right.
