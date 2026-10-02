> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Installation guide

# Installation Guide

Starting with the 26.3 release, Simba Intelligence is installed as part of the Self-Service Analytics (formerly Logi Composer) Helm chart. There is no separate Simba Intelligence chart to install — you deploy Self-Service Analytics and turn Simba Intelligence on with a single value.

> **📘 Upgrading from the standalone chart?** If you already run Simba Intelligence from the standalone `simba-intelligence-chart`, moving to the integrated chart is a migration, not a `helm upgrade`. A *Simba Intelligence to Self-Service Analytics Transition Guide* covers that path — contact your insightsoftware representative for a copy. See also [Upgrade Procedures](../deployment/operations-and-maintenance/upgrade-procedures).
>
> For hands-on help planning or executing the migration, [insightsoftware Support](https://insightsoftware.com/support/product-support/) and Professional Services can guide you through it — contact your representative to engage them.

## Prerequisites

Before you begin, ensure you have:

* A Kubernetes cluster (1.22+; 1.25+ with Gateway API CRDs v1.0.0+ if you use Gateway API routing)
* [Helm](https://helm.sh/) 3 and `kubectl` configured for your cluster
* An ingress controller already running in the cluster — the chart no longer installs one by default
* An AI/LLM provider account (Gemini Enterprise Agent Platform, Azure OpenAI, AWS Bedrock, or Microsoft Foundry)

See [System Requirements](./system-requirements) for sizing, database, and networking detail.

## 1. Add the Helm Repository

```shell theme={null}
helm repo add composer https://composer-repo.logianalytics.com/helm-charts/stable/
helm repo update
```

List the available chart versions:

```shell theme={null}
helm search repo composer/composer --versions
```

## 2. Create a Values File

Start from the chart README's own `base.yaml` (see its **TL;DR** and **Installing** sections) — it already covers the database passwords and other baseline settings. Add the Simba Intelligence values on top:

```yaml theme={null}
# Self-Service Analytics admin password.
# Required when Simba Intelligence is enabled — the install fails without it.
# Must be at least 9 characters with 1 lowercase, 1 uppercase, 1 number, and
# 1 special character (!@#$%^&*()-_=+,.:;<>) — Self-Service Analytics rejects
# a non-compliant password at startup.
zoomdataWeb:
  adminPassword: "ChangeMe12345!"

ingress:
  enabled: true
  className: "nginx"        # match your cluster's ingress controller
  hosts:
    - analytics.example.com

simbaIntelligence:
  enabled: true
  # MCP server (/mcp and /.well-known) is opt-in — omit or set false if unused
  mcp:
    enabled: true
```

Two values matter more than the rest when enabling Simba Intelligence:

* **`zoomdataWeb.adminPassword`** — Simba Intelligence authenticates against the Self-Service Analytics API with it. The chart fails the install or upgrade outright if it is missing, and Self-Service Analytics itself rejects a password that doesn't meet its complexity policy (9+ characters, 1 lowercase, 1 uppercase, 1 number, 1 special character) — the `web` pod will otherwise fail to start. Use `zoomdataWeb.existingSecret` to source it from a Secret you manage instead.
* **`simbaIntelligence.composerPublicUrl`** — the browser-reachable URL of Self-Service Analytics. Leaving it empty (recommended) auto-derives it from the first `ingress.hosts` entry. If it cannot be derived, the install still **succeeds** and every pod reports healthy, but Simba Intelligence fails at runtime the first time the URL is needed. Set `ingress.hosts` as shown above, or set `composerPublicUrl` explicitly.

> **🔐 Secrets:** For production, source passwords from Kubernetes Secrets you manage — see the **External Secrets** section of the chart README.

> **🗄️ Database:** The chart deploys an in-cluster PostgreSQL for development and QA. For production, use an external managed database — set `postgresql.enabled: false` and configure `simbaIntelligence.database.host` along with the Self-Service Analytics `*DbUrl` values. See the chart README's **Database** section.

## 3. Install

```shell theme={null}
helm install <release-name> composer/composer --version <VERSION> -f composer-values.yaml
```

Watch the rollout:

```shell theme={null}
kubectl get pods -l app.kubernetes.io/instance=<release-name> -w
```

The Simba Intelligence pods wait on a database-migration Job before they start, so expect them to sit in `Init` for the first minute or two.

> **📋 Post-install notes:** The chart prints `NOTES.txt` after a successful install, including a warning if `composerPublicUrl` could not be resolved. Read it.

## 4. Access the Application

Self-Service Analytics is served at your ingress hostname under `zoomdataWeb.contextPath` (default `/composer`), for example `https://analytics.example.com/composer`.

Simba Intelligence features are used **inside the Self-Service Analytics interface** — the standalone Simba Intelligence UI has been retired. The Simba Intelligence service itself is now a REST API, documented at `<contextPath>/intelligence/apidocs/`.

Check the ingress if the application is not reachable:

```shell theme={null}
kubectl get ingress -l app.kubernetes.io/instance=<release-name>
```

## Need More Control?

For all available configuration values, external database and secret setup, and ingress examples for specific controllers (NGINX, Traefik, ALB, GCE) or Gateway API:

➡️ [**Helm Chart Reference**](../deployment/installation-and-setup/helm-chart-reference)

## Next Steps

* Configure your LLM provider — [LLM Provider Configuration](../guides/admin-guides/llm-provider-configuration)
* Set up data sources and enable users — [Quick Start Guide](./quick-start-guide)
* Deploy without internet access — [Air-Gapped Deployment](../deployment/installation-and-setup/air-gapped-deployment)
* Operate the deployment — [Administrator Guide](../guides/admin-guides/administrator-guide)
