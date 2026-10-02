> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Air gapped deployment

# Air-Gapped Deployment

This guide covers deploying Simba Intelligence, as part of the Self-Service Analytics (formerly Logi Composer) Helm chart, in environments without direct internet access — air-gapped networks, restricted corporate environments, or private clouds that require all container images to come from an internal registry.

## Overview

A standard deployment pulls most images from Docker Hub (a few dependency images come from other registries, such as `ghcr.io`) and the chart from the Self-Service Analytics Helm repository. In a restricted environment you mirror both: push every required image to your internal registry, transfer the chart, then override the image locations in your values file.

### What You'll Need

* A machine with internet connectivity, for pulling images and the chart
* An internal container registry (Azure Container Registry, AWS ECR, Harbor, Artifactory, or any OCI-compliant registry)
* `docker` CLI or equivalent container tooling
* `helm` CLI
* A Kubernetes cluster with access to the internal registry

***

## Step 1: Determine the Image List

Image names and tags change between chart releases, so derive the list from the exact chart version you are deploying rather than from a static table.

On the internet-connected machine:

```bash theme={null}
helm repo add composer https://composer-repo.logianalytics.com/helm-charts/stable/
helm repo update

# Render the chart with the values you intend to deploy, then extract every image
helm template composer/composer --version <VERSION> -f my-values.yaml \
  | awk '$1 == "image:" { gsub(/"/, "", $2); print $2 }' | sort -u > images.txt
```

**Windows PowerShell:**

```powershell theme={null}
helm template composer/composer --version <VERSION> -f my-values.yaml |
  Select-String -Pattern '^\s*image:\s*"?([^"\s]+)"?' |
  ForEach-Object { $_.Matches[0].Groups[1].Value } |
  Sort-Object -Unique | Set-Content images.txt
```

> **💡 Render with your real values file.** Optional services and subcharts — `simbaIntelligence.mcp`, `screenshotService`, `reportService`, `dataGatewayService`, Prometheus, the OpenTelemetry Collector — only contribute images when they are enabled. Rendering with the values you will actually deploy gives you exactly the set you need and nothing more.

The list will include the Simba Intelligence application image (used by the REST API service, Celery worker, Celery beat, MCP server, and the database-migration Job), the Self-Service Analytics service images, and infrastructure images such as PostgreSQL, Redis, and Consul. Default registries and tags are visible in `helm show values composer/composer --version <VERSION>` under the root `image` key and the per-service `image` blocks.

***

## Step 2: Pull, Tag, and Push

Using the `images.txt` produced in Step 1:

```bash theme={null}
REGISTRY="myregistry.example.com"

while read -r img; do
  docker pull "$img"
  # Strip the source registry host, keep the repository path and tag
  dest="$REGISTRY/${img#*/}"
  docker tag "$img" "$dest"
  docker push "$dest"
done < images.txt
```

Adjust the destination naming to match your registry's conventions — some registries require a fixed project or namespace prefix.

***

## Step 3: Transfer the Helm Chart

```bash theme={null}
# On the internet-connected machine
helm pull composer/composer --version <VERSION>
```

Transfer the resulting `composer-<VERSION>.tgz` to the air-gapped environment and install from the local file.

***

## Step 4: Override Image Locations

Add image overrides to your values file. Most services follow one of two patterns, discoverable via `helm show values` — but a few utility and dependency images are **not** in `values.yaml` at all and are easy to miss. Render the chart with your overrides (as in Step 1) and confirm every image in the output points at your registry before relying on this list.

```yaml theme={null}
# air-gapped-values.yaml

# Root default for Self-Service Analytics service images
image:
  registry: "myregistry.example.com/insightsoftware"
  # Utility images used by init containers (wait-consul, health-check scripts).
  # Not present in values.yaml or `helm show values` output — only discoverable
  # by reading templates/_helpers.tpl. Easy to miss; the chart pulls these
  # from Docker Hub by default regardless of the registry override above.
  override:
    curl: myregistry.example.com/insightsoftware/curl
    alpine: myregistry.example.com/library/alpine:3.16

imagePullSecrets:
  - name: registry-credentials

# Simba Intelligence images use a full repository path
simbaIntelligence:
  enabled: true
  website:
    image:
      repository: myregistry.example.com/insightsoftware/simba-intelligence
  dbMigrate:
    image:
      repository: myregistry.example.com/insightsoftware/simba-intelligence
  mcp:
    enabled: true
    image:
      repository: myregistry.example.com/insightsoftware/simba-intelligence
  celery:
    worker:
      image:
        repository: myregistry.example.com/insightsoftware/simba-intelligence
    beat:
      image:
        repository: myregistry.example.com/insightsoftware/simba-intelligence
  redis:
    image:
      registry: myregistry.example.com
      repository: redis

# In-cluster PostgreSQL (omit when using an external managed database)
internalPostgresql:
  image:
    registry: myregistry.example.com
    repository: postgres

# Consul is a chart dependency (not a Simba Intelligence or Self-Service
# Analytics service) and configures its own images independently of the
# root `image.*` key entirely.
consul:
  global:
    image: myregistry.example.com/hashicorp/consul:1.22.1
    imageK8S: myregistry.example.com/hashicorp/consul-k8s-control-plane:1.9.1

# Reloader is a chart dependency enabled by default (reloader.enabled: true).
# Its image is hosted on ghcr.io, not Docker Hub — a second external source
# to mirror alongside docker.io. Set reloader.enabled: false instead if you
# don't need it.
reloader:
  reloader:
    deployment:
      image:
        name: myregistry.example.com/stakater/reloader
        tag: v1.0.121
```

> **📝 Note:** `internalPostgresql.image.override.enabled` / `.name` replaces the entire image reference, which is useful when your registry layout does not map cleanly onto registry/repository/tag.

> **⚠️ Verify with `helm template`:** After building your overrides, confirm nothing was missed:
>
> ```bash theme={null}
> helm template composer/composer --version <VERSION> -f air-gapped-values.yaml \
>   | grep "image:" | sort -u
> ```
>
> Every line should reference your internal registry. Any Docker Hub reference still present means an image (a dependency subchart, a utility image, or a newly added service in a later chart version) needs its own override — the two patterns above don't cover every image in the chart.

***

## Step 5: Create an Image Pull Secret

If your internal registry requires authentication:

```bash theme={null}
kubectl create secret docker-registry registry-credentials \
  --docker-server=myregistry.example.com \
  --docker-username=<username> \
  --docker-password=<password> \
  --namespace <namespace>
```

Reference it via the root `imagePullSecrets` value as shown above.

***

## Step 6: Deploy

```bash theme={null}
helm install <release-name> ./composer-<VERSION>.tgz \
  -f air-gapped-values.yaml \
  --namespace <namespace> \
  --create-namespace
```

***

## External Redis Module Requirements

The chart's in-cluster Redis image includes the required modules. If you use an external Redis instance (`simbaIntelligence.redis.external.*`), ensure these are installed:

| Module | Library | Purpose |
| - | - | - |
| RediSearch | `redisearch.so` | Full-text search and vector similarity (semantic cache) |
| RedisJSON | `rejson.so` | JSON document storage and querying |
| RedisTimeSeries | `redistimeseries.so` | Time-series data operations |
| RedisBloom | `redisbloom.so` | Probabilistic data structures |

Also set `maxmemory-policy` to `volatile-ttl`.

***

## AI Provider Connectivity

Even in air-gapped environments, Simba Intelligence requires **outbound connectivity to at least one AI provider** (Gemini Enterprise Agent Platform, Azure OpenAI, AWS Bedrock, or Microsoft Foundry) for natural language query processing.

If your network blocks all outbound traffic, configure firewall rules to allow the provider endpoints:

| Provider | Endpoints to Allow |
| - | - |
| Gemini Enterprise Agent Platform | `*.googleapis.com` |
| Azure OpenAI | `*.openai.azure.com` |
| AWS Bedrock | `*.amazonaws.com` |
| Microsoft Foundry | `*.services.ai.azure.com` |

> **⚠️ Important:** Simba Intelligence cannot function without access to an AI provider. Mirroring images and charts solves image pulls only — provider connectivity is a separate network requirement.

***

## Verification

Confirm every pod is running from your internal registry:

```bash theme={null}
kubectl get pods -l app.kubernetes.io/instance=<release-name>

kubectl get pods -l app.kubernetes.io/instance=<release-name> \
  -o jsonpath='{range .items[*]}{.metadata.name}{"\t"}{range .spec.containers[*]}{.image}{"\t"}{end}{"\n"}{end}'
```

Include init containers in the check — they pull images too:

```bash theme={null}
kubectl get pods -l app.kubernetes.io/instance=<release-name> \
  -o jsonpath='{range .items[*]}{range .spec.initContainers[*]}{.image}{"\n"}{end}{end}' | sort -u
```
