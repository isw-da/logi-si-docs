> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Release Notes

<Update label="June 2026" description="26.2" tags={["feature"]}>
  ## Prebuilt AWS image

  Simba Intelligence is now available as a prebuilt AWS image with everything already deployed, so you can get an evaluation running on AWS without standing up your own Kubernetes cluster first. It is built for a quick start rather than large-scale production.

  ## Different models for different tasks

  Simba Intelligence can now use different AI models for different tasks, so you can run lighter, lower-cost models for simpler work and save the more capable ones for harder jobs. You get more control over the balance of cost and quality.

  ## Local AI models through Ollama

  Simba Intelligence now supports local AI models through Ollama, so you can run the AI on your own infrastructure instead of calling a hosted service. This keeps data in your environment, which matters for regulated and airgapped deployments.

  ## Retry an answer with added context

  When the AI assistant answers a question with a data query, you can now refine that answer in place instead of re-asking. If the result is close but not quite right, you add a short piece of plain-language guidance, such as "you aggregated, don’t," and the assistant reworks its answer with that steer in mind.

  This turns a wrong or imperfect answer into a quick correction rather than a restart. You keep the context you already have and nudge it toward what you meant, so you reach the right result in fewer tries and without rephrasing the whole question.

  ## Reuse of rated answers

  When a new question closely matches one your team previously rated well, Simba Intelligence can reuse that trusted answer instead of generating a fresh one. Repeated and similar questions get faster and more consistent over time.

  ## Single sign-On with Logi Symphony — self-service analytics

  Single sign-on now carries between Simba Intelligence and Composer, so moving from one to the other no longer prompts a second login.

  ## Expressions and formulas at data source creation

  You can now add expressions and formulas while creating a data source, so calculated fields are built in from the start rather than worked out by the AI at query time. For example, you can combine quantity and unit price into a single total that is ready to use the moment\
  anyone queries the source.

  Because the calculation lives in the data source itself, everyone who uses that source gets the same result, and answers do not depend on the AI recreating the math each time. It is a more reliable foundation for the questions your users ask.
</Update>

<Update label="March 2026" description="26.1" tags={["feature"]}>
  ## Query transparency and processing visibility

  The system now shows its work. As a request is processed, the interface surfaces each step in real time: identifying the right data source, selecting the relevant fields, requesting and parsing the data, and generating the result. Each stage is visible as it runs and collapses once complete, so users can review the full reasoning trail without it cluttering the interface. For teams in governed or regulated environments where auditability matters, this makes it much easier to validate that the AI reached the right answer the right way.

  ## Column-level security enforcement in the query agent

  The query agent now respects column-level security boundaries directly, stripping out any columns a user cannot access before a query is ever formed. The AI layer and the application's access controls are now fully consistent with each other.

  ## Multi-tenant LLM configuration and data isolation

  AI configuration and data context are now fully isolated per tenant. Each tenant manages its own LLM configuration independently, and embeddings and indexes resolve within that tenant's boundaries, ensuring no data context crosses between customers. For the end user, the AI operates as if it was built specifically for their environment.

  ## Extended document analysis

  The AI can now analyze PDFs and other document types alongside structured data sources. Users working with contracts, reports, or regulatory filings can ask questions against those documents the same way they would query a database. For application builders in legal tech, insurance, or financial services, this extends the range of content the platform can reason about without requiring a separate document intelligence tool.

  ## Visual response in chat

  The chat interface can now return a rendered visual directly in response to a user's question, rather than text alone. When a user asks a data question, the result can be a chart or visualization generated in context, with awareness of the current data configuration. This makes the chat experience feel like a natural part of the analytics workflow rather than a separate interaction layer.

  ## Redesigned data source configuration screen

  The data source configuration screen has been rebuilt on the latest Composer UI. The updated interface introduces drag and drop for creating data sources, bringing the experience in line with the broader Composer environment. The result is a more consistent workflow across the platform for teams that spend time in data source setup.

  ## Data source agent usability and schema handling

  Setting up and configuring data sources is now faster and less error-prone. The data source agent output is easier to navigate, with collapsible sections and smarter schema and table suggestions surfaced during setup. Large or complex schemas that previously caused failures are now handled reliably. The overall experience from connecting a source to having it ready for AI queries has been meaningfully streamlined.
</Update>

<Update label="December 2025" description="25.4" tags={["feature", "bugfix", "knownissue", "breakingchange"]}>
  ## Multi-tenancy UI support

  Users belonging to multiple tenants can now switch between them directly within the Simba Intelligence interface. Previously, tenant switching required API-level token management.

  ## Conversational playground

  The [Playground](../guides/user-guides/playground-user-guide) has been upgraded to use the Chat API, enabling full conversational interactions with context retention instead of one-off queries.

  ## License-based user restrictions

  Administrators can now apply tiered limitations to users based on license level, including restrictions on connector types, API key limits, and supported LLM providers.

  ## Light theme

  Added an optional light color theme to align with Logi Symphony's interface, available alongside the existing dark theme.

  ## Schema change detection <Badge color="green">Experimental</Badge>

  Experimental support for automatically detecting schema changes and breakages in data sources, with intelligent suggestions for fixes while maintaining backwards compatibility.

  ## LangChain v1 migration

  Upgraded from LangChain to v1, incorporating significant performance improvements and new capabilities.

  ## Vertex AI / Gemini support

  Improved handling of Gemini model responses, including support for new thinking/reasoning output formats.

  ## Elasticsearch `TEXT_SEARCH`

  Implemented specialized text search filtering for Elasticsearch connectors where `textSearchEnabled` is configured, improving search accuracy for text-heavy data sources.

  ## LLM tier resolution logging

  The "LLM resolved" log line (`simba_intelligence.llm.services.ai_service_factory`) now shows both the resolved and originally requested tier, making it possible to tell when a request was served through tier fallback instead of its intended tier. Previously, only the requested tier was logged, even when a different tier actually served the request.

  ## Helm chart change

  Removed Bitnami Redis subchart dependency from the Redis component. Replaced with custom Redis StatefulSet using official Redis Alpine image. This allows for a lighter weight Alpine-based image, simplified configuration, better integration. Upgrade happens automatically. An old PersistentVolumeClaim (PVC) from the Bitnami Redis installation may be left behind and can be manually deleted if desired.

  ## Bug Fixes

  * Fixed an authentication issue with Symphony logins.
  * Resolved token cache handling to prevent session conflicts between short-term and long-term tokens.

  ## Known Issues

  | Component | Issue | Workaround |
  | - | - | - |
  | Discovery Service (GCP) | On Google Cloud Platform, upgrading may fail with error: `cannot patch "<release>-discovery-query-engine" with kind Service: spec.clusterIPs[0]: Invalid value: may not change once set`. This is due to GCP's Kubernetes API restriction on modifying `spec.clusterIPs` after service creation. | Delete the affected service (`kubectl delete service <release-name>-discovery-query-engine -n <namespace>`) then retry the Helm upgrade. The service will be immediately recreated with correct configuration. Minimal downtime expected. |

  ## Breaking changes

  | Breaking change | Action required |
  | - | - |
  | Removed Bitnami PostgreSQL subchart dependency. Replaced with custom PostgreSQL StatefulSet implementation. This is only a breaking change if you were using the built-in PostgreSQL. External PostgreSQL (recommended for production) is unaffected. | <ul><li>**For upgrades with built-in PostgreSQL:** Migrate data to external PostgreSQL before upgrading. The chart will detect existing Bitnami PostgreSQL StatefulSet and block the upgrade. Configure global.simba.intelligence.postgresql.enabled: false and provide external database connection details. See validation error message during upgrade for detailed instructions.</li><li>**For upgrades with external PostgreSQL:** No action required.</li><li>**For new installations:** Use built-in PostgreSQL (dev/test only) or configure external PostgreSQL (recommended for production).</li></ul> |
</Update>
