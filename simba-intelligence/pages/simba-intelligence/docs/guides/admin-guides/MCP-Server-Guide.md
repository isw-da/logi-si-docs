> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.app/llms.txt
> Use this file to discover all available pages before exploring further.

# MCP Server Guide

# MCP Server Guide

This guide covers the Model Context Protocol (MCP) server in Simba Intelligence, which enables AI assistants and other MCP-compatible clients to securely query your data sources using standardized tooling and OAuth2 PKCE authentication.

## Overview

The MCP server exposes Simba Intelligence capabilities as MCP tools that can be consumed by AI assistants (such as Claude Desktop, Cursor, or custom agents) through the [Model Context Protocol](https://modelcontextprotocol.io/) standard. It runs as a separate deployment alongside the main application.

### Key Capabilities

**🔧 MCP Tools**

* Query data sources using natural language
* List available data sources and their metadata
* Retrieve field-level statistics for data exploration
* Get AI-generated follow-up question suggestions

**🔐 OAuth2 PKCE Authentication**

* Secure authorization code flow with Proof Key for Code Exchange (PKCE)
* Scoped access tokens tied to user identity and tenant context
* Automatic token refresh and rotation
* Full multi-tenancy support

***

## Architecture

The MCP server runs as a dedicated deployment with two containers:

```
┌─────────────────────────────────────────┐
│  MCP Pod                                │
│                                         │
│  ┌───────────┐     ┌────────────────┐   │
│  │  Nginx    │     │  MCP Server    │   │
│  │  Sidecar  │────▶│  Uvicorn)      │   │
│  │  :8000    │     │  :8001         │   │
│  └───────────┘     └────────────────┘   │
│                                         │
└─────────────────────────────────────────┘
```

* **Nginx sidecar** (port 8000) — Handles path rewriting and exposes OAuth2 well-known endpoints. This is the externally accessible port.
* **MCP server** (port 8001) — FastMCP application running on Gunicorn with Uvicorn workers. Only accessible internally within the pod.

***

## Available MCP Tools

Once connected, MCP clients can use the following tools:

### `get_data`

Query a data source using natural language.

| Parameter   | Type   | Required | Description                                                                  |
| ----------- | ------ | -------- | ---------------------------------------------------------------------------- |
| `question`  | string | Yes      | Natural language question about the data                                     |
| `source_id` | string | No       | Specific data source to query. If omitted, the system selects the best match |

### `get_data_sources`

List available data sources accessible to the authenticated user.

| Parameter     | Type    | Required | Description                         |
| ------------- | ------- | -------- | ----------------------------------- |
| `max_sources` | integer | No       | Maximum number of sources to return |

### `get_suggested_questions`

Get AI-generated follow-up questions based on available data.

| Parameter   | Type    | Required | Description                             |
| ----------- | ------- | -------- | --------------------------------------- |
| `source_id` | string  | No       | Data source to generate suggestions for |
| `count`     | integer | No       | Number of suggestions to return         |

### `get_field_statistics`

Retrieve field-level statistics such as distinct values, min/max ranges, and data distributions.

| Parameter    | Type   | Required | Description                                                                 |
| ------------ | ------ | -------- | --------------------------------------------------------------------------- |
| `source_id`  | string | Yes      | Data source containing the field                                            |
| `field_name` | string | No       | Name of the field to analyze. If omitted, returns statistics for all fields |

***

## OAuth2 PKCE Authentication Flow

The MCP server uses OAuth2 with PKCE (S256) for secure client authentication. This flow is designed for public clients that cannot securely store a client secret.

### Flow Overview

```
1. Discovery    →  Client fetches /.well-known/oauth-authorization-server
2. Registration →  Client registers at /mcp/register
3. Authorization → User redirected to /mcp/authorize (with PKCE challenge)
4. Consent      →  User approves the requested scopes
5. Token Exchange → Client exchanges auth code + code_verifier for tokens
6. MCP Calls    →  Client uses access token for MCP tool invocations
7. Refresh      →  Client uses refresh token when access token expires
```

### OAuth2 Scopes

| Scope         | Description                             | Who Gets It                   |
| ------------- | --------------------------------------- | ----------------------------- |
| `read:data`   | Query data sources and retrieve results | All authenticated users       |
| `write:data`  | Write operations                        | All users with an active role |
| `admin:users` | User administration                     | Supervisor role only          |

### Token Lifetimes

| Token Type         | Lifetime   | Notes                                          |
| ------------------ | ---------- | ---------------------------------------------- |
| Authorization code | 10 minutes | Single-use, exchanged for tokens               |
| Access token       | 1 day      | Contains Composer bearer token and user claims |
| Refresh token      | 30 days    | Rotated on each use for security               |

### Discovery Endpoints

MCP clients discover the OAuth2 configuration through well-known endpoints:

* `/.well-known/oauth-authorization-server` — Returns the authorization server metadata (issuer, endpoints, supported grant types)
* `/.well-known/oauth-protected-resource` — Returns protected resource metadata

### Security Features

* **PKCE S256** — Code challenge verification prevents authorization code interception
* **Redirect URI validation** — Blocks dangerous schemes (`javascript:`, `data:`, etc.)
* **Token rotation** — Refresh tokens are rotated on each use; old tokens are invalidated
* **Session binding** — User identity (user\_id, tenant\_id) is embedded in all tokens
* **Revocation** — Both access and refresh tokens can be revoked, which cascades to related tokens

***

## Deployment Configuration

### Helm Values

The MCP server is configured through the Helm chart under the `simba.intelligence.mcp` section:

```yaml theme={null}
simba:
  intelligence:
    mcp:
      baseUrl: "https://your-domain.com"    # External-facing URL for OAuth2 redirects
      uvicornWorkers: 4                      # Number of Uvicorn worker processes
      logLevel: "info"                       # Log level (debug, info, warning, error, critical)
      replicaCount: 1                        # Number of pod replicas

      autoscaling:
        enabled: false
        minReplicas: 1
        maxReplicas: 3
        targetCPUUtilizationPercentage: 80

      image:
        repository: docker.io/insightsoftware/simba-intelligence
        tag: main

      service:
        type: ClusterIP
        port: 8000                           # Nginx proxy port (external)

      resources:
        requests:
          cpu: 250m
          memory: 512Mi
        limits:
          cpu: 1
          memory: 2Gi

      sidecar:                               # Nginx reverse proxy
        image:
          repository: docker.io/nginx
          tag: 1.21-alpine
        resources:
          requests:
            cpu: 50m
            memory: 64Mi
```

### Environment Variables

| Variable              | Default  | Description                                                                              |
| --------------------- | -------- | ---------------------------------------------------------------------------------------- |
| `MCP_BASE_URL`        | Required | External-facing URL used for OAuth2 PKCE redirect URIs (e.g., `https://your-domain.com`) |
| `MCP_UVICORN_WORKERS` | `4`      | Number of Uvicorn worker processes                                                       |
| `UVICORN_LOG_LEVEL`   | `info`   | Log level for the MCP server (`debug`, `info`, `warning`, `error`, `critical`)           |
| `APP_MODE`            | `web`    | Must be set to `mcp` for the MCP server container                                        |

> **⚠️ Important:** `MCP_BASE_URL` must match the externally accessible URL where the MCP server is reachable. This URL is used in OAuth2 redirect URIs and discovery responses. Incorrect values will cause authentication failures.

### Network Requirements

* The MCP Kubernetes Service exposes port **8000** (Nginx proxy) within the cluster
* Ingress or load balancer should route MCP traffic to the service on port 8000
* The MCP server requires connectivity to:
  * **PostgreSQL** — For OAuth token storage
  * **Redis** — For caching
  * **Composer/Discovery** — For data source queries

***

## Connecting MCP Clients

### Client Configuration

MCP clients connect using the server's base URL with the `/mcp` path. The exact configuration depends on the client application. Refer to your MCP client's documentation for the correct configuration format.

### Connection Flow

1. The MCP client discovers the OAuth2 server via `/.well-known/oauth-authorization-server`
2. The client registers itself at `/mcp/register`
3. The user is redirected to the Simba Intelligence login page to authenticate
4. After authentication, the user approves the requested scopes on the consent screen
5. The client receives an authorization code and exchanges it for access/refresh tokens
6. The client can now invoke MCP tools with the access token

> **💡 Pro Tip:** The user must have an active Simba Intelligence session (authenticated via the web interface) before the MCP OAuth2 flow can complete. Ensure the user has logged in at least once.

***

## Multi-Tenancy

The MCP server fully supports multi-tenancy:

* User identity and tenant context are embedded in all OAuth tokens
* All MCP tool invocations are scoped to the authenticated user's tenant
* Data source access respects the same role-based permissions as the web interface
* Users in multiple tenants are authenticated in the context of their current active tenant

***

## Troubleshooting

### Common Issues

**OAuth2 redirect failures:**

* Verify `MCP_BASE_URL` matches the externally accessible URL
* Ensure the Nginx sidecar is running and proxying correctly
* Check that the ingress/load balancer is routing to port 8000

**Authentication errors:**

* Confirm the user has an active Simba Intelligence session
* Check that Composer/Discovery is accessible from the MCP pod
* Review MCP server logs for token exchange errors

**Tool execution failures:**

* Verify the user has appropriate role permissions for the requested operation
* Check connectivity to Composer, PostgreSQL, and Redis
* Review logs with `UVICORN_LOG_LEVEL=debug` for detailed request tracing

### Viewing Logs

```bash theme={null}
# Find MCP pods
kubectl get pods -n simba-intelligence | grep mcp

# View MCP server logs
kubectl logs <mcp-pod-name> -c simba-intelligence-mcp -n simba-intelligence

# View Nginx sidecar logs
kubectl logs <mcp-pod-name> -c nginx -n simba-intelligence
```
