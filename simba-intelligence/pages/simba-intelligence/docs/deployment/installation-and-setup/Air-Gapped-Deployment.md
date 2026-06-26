> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.app/llms.txt
> Use this file to discover all available pages before exploring further.

# Air Gapped Deployment

# Air-Gapped Deployment

This guide covers deploying Simba Intelligence in environments without direct internet access, such as air-gapped networks, restricted corporate environments, or private cloud deployments that require all container images to come from internal registries.

## Overview

A standard Simba Intelligence deployment pulls container images from Docker Hub (`docker.io`). In air-gapped or restricted environments, you must pre-pull all required images and push them to an internal container registry before deploying.

### What You'll Need

* Access to a machine with internet connectivity (for pulling images)
* An internal container registry (e.g., Azure Container Registry, AWS ECR, Harbor, Artifactory, or any OCI-compliant registry)
* `docker` CLI or equivalent container tooling
* `helm` CLI for chart management
* Kubernetes cluster with access to the internal registry

***

## Required Container Images

The following images must be available in your internal registry:

### Core Application Images

| Image                                                   | Default Tag | Used By                                                           |
| ------------------------------------------------------- | ----------- | ----------------------------------------------------------------- |
| `docker.io/insightsoftware/simba-intelligence`          | `main`      | Web server, Celery worker, Celery beat, MCP server, DB migrations |
| `docker.io/insightsoftware/simba-intelligence-job-base` | `main`      | Kubernetes init jobs and utility tasks                            |

### Infrastructure Images

| Image                            | Default Tag   | Used By                                       |
| -------------------------------- | ------------- | --------------------------------------------- |
| `docker.io/postgres`             | `15-alpine`   | Built-in PostgreSQL database                  |
| `docker.io/redis`                | `8-alpine`    | Built-in Redis cache and message broker       |
| `docker.io/nginx`                | `1.28-alpine` | Discovery proxy sidecar                       |
| `docker.io/nginx`                | `1.21-alpine` | MCP server sidecar                            |
| `docker.io/insightsoftware/curl` | `1`           | Init containers (wait scripts, health checks) |

### Composer/Discovery Images

| Image                                 | Default Tag | Used By                    |
| ------------------------------------- | ----------- | -------------------------- |
| `docker.io/insightsoftware/discovery` | `25.4`      | Composer/Discovery service |

> **📝 Note:** Check your specific Helm chart version's `values.yaml` for the exact image tags. Tags may differ between chart releases.

***

## Step-by-Step Deployment

### Step 1: Pull Images from Docker Hub

On a machine with internet access, pull all required images:

```bash theme={null}
# Core application
docker pull docker.io/insightsoftware/simba-intelligence:main
docker pull docker.io/insightsoftware/simba-intelligence-job-base:main

# Infrastructure
docker pull docker.io/postgres:15-alpine
docker pull docker.io/redis:8-alpine
docker pull docker.io/nginx:1.28-alpine
docker pull docker.io/nginx:1.21-alpine
docker pull docker.io/insightsoftware/curl:1

# Composer/Discovery
docker pull docker.io/insightsoftware/discovery:25.4
```

### Step 2: Tag for Your Internal Registry

Re-tag each image to point to your internal registry:

```bash theme={null}
REGISTRY="myregistry.example.com"

docker tag docker.io/insightsoftware/simba-intelligence:main \
  $REGISTRY/insightsoftware/simba-intelligence:main

docker tag docker.io/insightsoftware/simba-intelligence-job-base:main \
  $REGISTRY/insightsoftware/simba-intelligence-job-base:main

docker tag docker.io/postgres:15-alpine \
  $REGISTRY/postgres:15-alpine

docker tag docker.io/redis:8-alpine \
  $REGISTRY/redis:8-alpine

docker tag docker.io/nginx:1.28-alpine \
  $REGISTRY/nginx:1.28-alpine

docker tag docker.io/nginx:1.21-alpine \
  $REGISTRY/nginx:1.21-alpine

docker tag docker.io/insightsoftware/curl:1 \
  $REGISTRY/insightsoftware/curl:1

docker tag docker.io/insightsoftware/discovery:25.4 \
  $REGISTRY/insightsoftware/discovery:25.4
```

### Step 3: Push to Internal Registry

```bash theme={null}
docker push $REGISTRY/insightsoftware/simba-intelligence:main
docker push $REGISTRY/insightsoftware/simba-intelligence-job-base:main
docker push $REGISTRY/postgres:15-alpine
docker push $REGISTRY/redis:8-alpine
docker push $REGISTRY/nginx:1.28-alpine
docker push $REGISTRY/nginx:1.21-alpine
docker push $REGISTRY/insightsoftware/curl:1
docker push $REGISTRY/insightsoftware/discovery:25.4
```

### Step 4: Transfer the Helm Chart

If your deployment environment cannot reach Docker Hub for the Helm chart itself, pull and transfer it manually:

```bash theme={null}
# On internet-connected machine
helm pull oci://docker.io/insightsoftware/simba-intelligence-chart --version <VERSION>

# Transfer the .tgz file to your air-gapped environment
# Then install from the local file
helm install simba-intelligence ./simba-intelligence-chart-<VERSION>.tgz \
  -f custom-values.yaml \
  --namespace simba-intelligence \
  --create-namespace
```

### Step 5: Configure Helm Values

Create a custom values file that overrides all image repositories to point to your internal registry:

```yaml theme={null}
# air-gapped-values.yaml
simba:
  intelligence:
    website:
      image:
        repository: myregistry.example.com/insightsoftware/simba-intelligence
    celery:
      worker:
        image:
          repository: myregistry.example.com/insightsoftware/simba-intelligence
        imagePullSecrets:
          - name: registry-credentials
      beat:
        image:
          repository: myregistry.example.com/insightsoftware/simba-intelligence
    mcp:
      image:
        repository: myregistry.example.com/insightsoftware/simba-intelligence
      sidecar:
        image:
          repository: myregistry.example.com/nginx
    job:
      image:
        repository: myregistry.example.com/insightsoftware/simba-intelligence-job-base

redis:
  image:
    registry: myregistry.example.com
    repository: redis
  imagePullSecrets:
    - name: registry-credentials

postgresql:
  image:
    registry: myregistry.example.com
    repository: postgres

discovery:
  image:
    registry: myregistry.example.com/insightsoftware
```

### Step 6: Create Image Pull Secret

If your internal registry requires authentication:

```bash theme={null}
kubectl create secret docker-registry registry-credentials \
  --docker-server=myregistry.example.com \
  --docker-username=<username> \
  --docker-password=<password> \
  --namespace simba-intelligence
```

### Step 7: Deploy

```bash theme={null}
helm install simba-intelligence ./simba-intelligence-chart-<VERSION>.tgz \
  -f air-gapped-values.yaml \
  --namespace simba-intelligence \
  --create-namespace
```

***

## Redis Module Requirements

The built-in Redis image in the Helm chart includes the required Redis modules. If you use an external Redis instance in an air-gapped environment, ensure these modules are installed:

| Module          | Library              | Purpose                                                 |
| --------------- | -------------------- | ------------------------------------------------------- |
| RediSearch      | `redisearch.so`      | Full-text search and vector similarity (semantic cache) |
| RedisJSON       | `rejson.so`          | JSON document storage and querying                      |
| RedisTimeSeries | `redistimeseries.so` | Time-series data operations                             |
| RedisBloom      | `redisbloom.so`      | Probabilistic data structures                           |

***

## AI Provider Connectivity

Even in air-gapped environments, the Simba Intelligence application requires **outbound connectivity to at least one AI provider** (Google Vertex AI, Azure OpenAI, or AWS Bedrock) for natural language query processing.

If your network blocks all outbound traffic, you must configure firewall rules to allow access to the AI provider endpoints:

| Provider         | Endpoints to Allow   |
| ---------------- | -------------------- |
| Google Vertex AI | `*.googleapis.com`   |
| Azure OpenAI     | `*.openai.azure.com` |
| AWS Bedrock      | `*.amazonaws.com`    |

> **⚠️ Important:** Simba Intelligence cannot function without access to an AI provider. The air-gapped deployment pattern covers container images and Helm charts only — AI provider connectivity is a separate network requirement.

***

## Verification

After deployment, verify all pods are running with images from your internal registry:

```bash theme={null}
# Check all pods are running
kubectl get pods -n simba-intelligence

# Verify image sources (should show your internal registry)
kubectl get pods -n simba-intelligence -o jsonpath='{range .items[*]}{.metadata.name}{"\t"}{range .spec.containers[*]}{.image}{"\t"}{end}{"\n"}{end}'
```
