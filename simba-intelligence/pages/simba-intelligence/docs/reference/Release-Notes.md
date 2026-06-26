> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.app/llms.txt
> Use this file to discover all available pages before exploring further.

# Release Notes

# Release Notes

## Version 25.4.0

### New Features

#### Multi-Tenancy UI Support

Users belonging to multiple tenants can now switch between them directly within the Simba Intelligence interface. Previously, tenant switching required API-level token management. See the [Multi-Tenancy Guide](../guides/admin-guides/Multi-Tenancy-Guide) for configuration details.

#### Conversational Playground

The [Playground](../guides/user-guides/Playground-User-Guide) has been upgraded to use the Chat API, enabling full conversational interactions with context retention instead of one-off queries.

#### License-Based User Restrictions

Administrators can now apply tiered limitations to users based on license level, including restrictions on connector types, API key limits, and supported LLM providers. See the [Administrator Guide](../guides/admin-guides/Administrator-Guide) for configuration options.

#### Light Theme

Added an optional light color theme to align with Logi Symphony's interface, available alongside the existing dark theme.

#### Schema Change Detection (Experimental)

Experimental support for automatically detecting schema changes and breakages in data sources, with intelligent suggestions for fixes while maintaining backwards compatibility.

***

### Improvements

#### LangChain v1 Migration

Upgraded from LangChain to v1, incorporating significant performance improvements and new capabilities.

#### Vertex AI / Gemini Support

Improved handling of Gemini model responses, including support for new thinking/reasoning output formats. See [LLM Provider Configuration](../guides/admin-guides/LLM-Provider-Configuration) for supported models.

#### Elasticsearch TEXT\_SEARCH

Implemented specialized text search filtering for Elasticsearch connectors where `textSearchEnabled` is configured, improving search accuracy for text-heavy data sources.

***

### Helm Chart Changes

| Change Type         | Component               | Description                                                                                                                                                                                                                                                                                      | Action Required                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ------------------- | ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Breaking Change** | PostgreSQL              | Removed Bitnami PostgreSQL subchart dependency. Replaced with custom PostgreSQL StatefulSet implementation. **Note:** This is only a breaking change if you were using the built-in PostgreSQL. External PostgreSQL (recommended for production) is unaffected.                                  | **For upgrades with built-in PostgreSQL:** Migrate data to external PostgreSQL before upgrading. The chart will detect existing Bitnami PostgreSQL StatefulSet and block the upgrade. Configure `global.simba.intelligence.postgresql.enabled: false` and provide external database connection details. See validation error message during upgrade for detailed instructions. **For upgrades with external PostgreSQL:** No action required. **For new installations:** Use built-in PostgreSQL (dev/test only) or configure external PostgreSQL (recommended for production). |
| **Change**          | Redis                   | Removed Bitnami Redis subchart dependency. Replaced with custom Redis StatefulSet using official Redis Alpine image.                                                                                                                                                                             | **For upgrades:** Upgrade happens automatically. An old PersistentVolumeClaim (PVC) from the Bitnami Redis installation may be left behind and can be manually deleted if desired. **Benefits:** Lighter weight Alpine-based image, simplified configuration, better integration.                                                                                                                                                                                                                                                                                               |
| **Known Issue**     | Discovery Service (GCP) | On Google Cloud Platform, upgrading may fail with error: `cannot patch "<release>-discovery-query-engine" with kind Service: spec.clusterIPs[0]: Invalid value: may not change once set`. This is due to GCP's Kubernetes API restriction on modifying `spec.clusterIPs` after service creation. | **Workaround:** Delete the affected service (`kubectl delete service <release-name>-discovery-query-engine -n <namespace>`) then retry the Helm upgrade. The service will be immediately recreated with correct configuration. Minimal downtime expected.                                                                                                                                                                                                                                                                                                                       |

See the [Helm Chart Reference](../deployment/installation-and-setup/Helm-Chart-Reference) for full configuration options.

***

### Security Fixes

* Fixed an authentication issue with Symphony logins
* Resolved token cache handling to prevent session conflicts between short-term and long-term tokens
