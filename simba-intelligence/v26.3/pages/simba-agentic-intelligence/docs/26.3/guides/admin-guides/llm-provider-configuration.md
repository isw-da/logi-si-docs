> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Llm provider configuration

# LLM Provider Configuration

This guide explains how to configure Large Language Model (LLM) providers in Simba Intelligence. LLM providers power the AI capabilities that enable natural language querying, data source creation, and intelligent analysis features.

## Overview

### What are LLM Providers?

LLM providers are external AI services that power Simba Intelligence's natural language capabilities. Think of them as the "brains" behind the system that understand your questions, analyze your data requirements, and generate intelligent responses.

When you ask *"What were our top-selling products last quarter?"* in the Playground, an LLM provider:

1. **Understands** your natural language question
2. **Analyzes** your available data sources
3. **Generates** appropriate SQL queries
4. **Interprets** the results into meaningful insights

### Supported LLM Providers

Simba Intelligence requires LLMs with [structured output](https://python.langchain.com/docs/how_to/structured_output/) support, since JSON schema is used throughout. Older models like GPT-3.5 do not support this and cannot be used.

> **📝 Note:** Tiers appear under two names depending on where you're looking: the `/llm-configuration` UI labels them **Lite** and **Power**, while code, configuration, and logs use the underlying values `LOW` and `HIGH` respectively. These are the same two tiers, not four — see [Understanding Tiers](#understanding-tiers) below.

| Provider | Model | Tested | Tier Recommendation |
| - | - | - | - |
| 🔵 Azure OpenAI | GPT-5.4+ | ✅ Tested | Lite or Power |
| 🔵 Azure OpenAI | GPT-5.4+ Nano | ✅ Tested | Lite |
| 🟢 Gemini Enterprise Agent Platform | Gemini 2.5+ Flash | ✅ Tested | Lite |
| 🟢 Gemini Enterprise Agent Platform | Gemini 2.5+ Pro | ✅ Tested | Power |
| 🟠 AWS Bedrock | Claude Haiku 4.6+ | ✅ Tested | Lite |
| 🟠 AWS Bedrock | Claude Sonnet 4.6+ | ✅ Tested | Lite or Power |
| 🟠 AWS Bedrock | Claude Opus 4.6+ | ✅ Tested | Power |
| 🟠 AWS Bedrock | GPT-5.6+ | ✅ Tested | Lite or Power |
| 🟣 Microsoft Foundry | GPT-5.6+ | ✅ Tested | Lite or Power |
| 🟣 Microsoft Foundry | Claude Sonnet 4.6+ | ✅ Tested | Lite or Power |
| 🟣 Microsoft Foundry | Claude Opus 4.6+ | ✅ Tested | Power |

> **📝 Note:** A Power (`HIGH`) model is required for more complex agents, such as the data source agent.

> **📝 Note:** The Gemini provider is labeled **Gemini Enterprise Agent Platform** in the `/llm-configuration` UI. Its underlying provider ID is still `VERTEX_AI`, which is what you will see in API responses and log output.

<AccordionGroup>
  <Accordion title="Gemini Configuration Notes">
    1. **Gemini 2.5 Flash**: Set `thinking_budget` to `0` for maximum speed, or `128` for better quality
    2. **Gemini 2.5 Pro**: Set `thinking_budget` between `128` and `32768`
    3. **Gemini 3 or later**: Set `thinking_level` to `minimal`, `low`, `medium`, or `high`, depending on the levels supported by the selected model

    Simba Intelligence picks which parameter to send from the model name: a `model_name` containing a major version of 3 or higher uses `thinking_level` and ignores `thinking_budget`; earlier versions use `thinking_budget`. If the model name carries no recognizable version, whichever of the two you set is used.

    [Learn more about thinking](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/thinking)
  </Accordion>

  <Accordion title="AWS Bedrock Configuration Notes">
    1. **Claude Sonnet**: Set `max_tokens` to `10000` to avoid failures. Leaving this parameter blank may cause unexpected errors.
    2. **OpenAI GPT**: Bedrock serves these through inference profiles only, so `model_name` needs the geo prefix (for example, `us.openai.gpt-5.6-sol`). `temperature` is not supported and is dropped if set. Optional `reasoning_effort` accepts `low`, `medium`, `high`, `xhigh`, `max`, and — on GPT-5.6 only — `none`. A value the chosen model does not accept fails immediately, listing the ones it does.
  </Accordion>

  <Accordion title="Microsoft Foundry Configuration Notes">
    1. **Model family is required**: one Foundry resource serves several wire protocols, so every capability must set `model_family` to either `anthropic` (Anthropic Messages API) or `openai_v1` (OpenAI-compatible route).
    2. **Anthropic family**: does not accept `temperature` — current Claude models reject sampling parameters outright. It also cannot serve the **Embeddings** capability, since Anthropic publishes no embedding models; use the `openai_v1` family on the same resource for embeddings.
    3. **Anthropic `max_tokens`**: left unset, Simba Intelligence sends 32,000 output tokens. Raise it per capability on models that allow more.
    4. **Endpoint**: paste whichever form the Azure portal gives you — the bare resource host, the family base URL, or a full request URL. Simba Intelligence normalizes all three.
  </Accordion>
</AccordionGroup>

### Provider Capabilities

**💬 Chat Capability**

* Natural language understanding and generation
* Query interpretation and response creation
* Business insight generation

**🔍 Embeddings Capability**

* Semantic search and similarity matching
* Intelligent caching of similar queries
* Content understanding for better results

**👁️ Vision Capability**

* Dashboard image analysis
* Screenshot-to-data-source conversion
* Visual mockup interpretation

***

## LLM Tiers and Inheritance

The Chat capability can be configured at a **tier**, letting you match model cost/speed to the task. This section explains what tiers are and how Simba Intelligence resolves which configuration actually serves a request.

### Understanding Tiers

Chat requests specify one of two tiers:

| Tier (UI label) | Value (code / logs) | Purpose | Typical use |
| - | - | - | - |
| Power | `HIGH` | Powerful model for complex reasoning | Chat orchestration, data source/schema analysis |
| Lite | `LOW` | Fast, high-throughput model | Data retrieval, suggestions, token counting |

The `/llm-configuration` UI shows the friendlier **Lite** / **Power** names, but the value actually stored, sent through the API, and printed in logs is `LOW` / `HIGH`. The rest of this guide uses `HIGH`/`LOW` since that's what you'll see in configuration, log output, and error messages.

There is also **Unspecified** — leaving a capability's tier field blank in the configuration UI. An unspecified configuration acts as a catch-all that can serve *either* a `HIGH` or `LOW` request, which is useful for simple tenants that only need a single model instead of separate HIGH/LOW configurations.

> **📝 Note:** Only `CHAT` capability configurations use tiers. `EMBEDDINGS` and `VISION` configurations are not tiered — a tenant has at most one active configuration per non-chat capability.

### Tier Inheritance (Fallback Chain)

Every tenant is not required to configure both tiers. If a tenant only configures `HIGH`, requests for `LOW` still need to resolve to *something*. Simba Intelligence resolves this using an ordered fallback chain, checking the following in order and stopping at the first match:

1. **Own tenant, exact requested tier**
2. **Own tenant, Unspecified tier**
3. **Master tenant (VDD), exact requested tier**
4. **Master tenant (VDD), Unspecified tier**
5. **Own tenant, opposite tier** (e.g. requested `LOW`, only `HIGH` is configured)
6. **Master tenant (VDD), opposite tier** — last resort

**Key behaviors to understand:**

* **"Master tenant"** refers to the Composer/VDD (Visual Data Discovery) admin tenant, which acts as an org-wide fallback pool for tenants that don't have their own configuration for a given tier.
* **Own-tenant options are always exhausted first.** Steps 1–2 are checked before the master tenant is even looked up. This means a tenant with a valid Unspecified-tier configuration will never fall through to the master tenant for that capability.
* **If the current tenant *is* the master/VDD tenant**, the master-specific steps (3, 4, 6) are skipped since they'd be duplicates of the own-tenant checks.
* **Non-chat capabilities** (`EMBEDDINGS`, `VISION`) skip tier resolution entirely — they use a simpler own-tenant-then-master fallback.
* **Vision** additionally falls back to the `CHAT` capability at `HIGH` tier if no vision capability is configured for the tenant at all.

**Example:** A tenant configures only a `HIGH`-tier Chat capability (no `LOW`, no Unspecified). A request for the `LOW` tier will check the tenant's own `LOW` and Unspecified configs (steps 1–2, no match), then the master tenant's `HIGH` and Unspecified configs (steps 3–4, no match), and finally fall back to the tenant's own `HIGH` configuration (step 5) — meaning the "fast" tier silently gets served by the "powerful" model instead of failing.

Use the [Logging Configuration Guide](/simba-agentic-intelligence/docs/26.3/guides/user-guides/logging-configuration-guide#confirm-which-tierprovidermodel-served-a-request) to observe which step of this chain served any given request.

***

## Prerequisites

### Required Permissions

**To configure LLM providers, you need:**

* **Supervisor role** in Simba Intelligence
* **Access to LLM Configuration** interface (`/llm-configuration`)
* **Administrative privileges** for system-wide AI configuration

### AI Provider Account Requirements

**For each provider you want to use:**

**Gemini Enterprise Agent Platform (Google Vertex AI):**

* Google Cloud Platform account with billing enabled
* Vertex AI API enabled in your GCP project
* Service account with Vertex AI permissions
* Sufficient API quota for your expected usage

**Azure OpenAI:**

* Azure OpenAI resource
* API key with appropriate usage limits
* Sufficient credits/quota for your organization's needs

**AWS Bedrock:**

* AWS account with Bedrock access enabled
* IAM user or role with Bedrock permissions
* Model access granted for Claude or other desired models
* Appropriate usage quotas configured

**Microsoft Foundry:**

* An Azure AI Foundry resource with the models you intend to use deployed
* The resource endpoint and an API key
* Model access approved for the Anthropic and/or OpenAI models you plan to configure

***

## Accessing LLM Configuration

### Navigation to Configuration Interface

1. **Log into Simba Intelligence** with supervisor credentials
2. **Navigate to LLM Configuration**:
   * **Option 1**: Visit directly at `http://your-domain/llm-configuration`
   * **Option 2**: User menu → "LLM Configuration"
3. **Verify access**: You should see a tabbed interface with available providers

### Configuration Interface Overview

The LLM Configuration interface provides:

* **Provider tabs**: Separate tabs for each supported AI provider
* **Configuration forms**: Provider-specific credential and parameter forms
* **Capability management**: Enable/disable different AI capabilities per provider
* **Testing tools**: Built-in connection testing and validation
* **Status indicators**: Real-time status of provider configurations

***

## Gemini Enterprise Agent Platform Configuration

The Gemini Enterprise Agent Platform (Google Vertex AI) provides comprehensive AI capabilities, including advanced vision analysis for dashboard image processing.

### Prerequisites for the Gemini Platform

**Google Cloud Platform setup:**

1. **Create or select a GCP project** with billing enabled
2. **Enable Vertex AI API**:
   ```bash theme={null}
   gcloud services enable aiplatform.googleapis.com
   ```
3. **Create a service account**:
   ```bash theme={null}
   gcloud iam service-accounts create simba-intelligence-ai \
     --display-name="Simba Intelligence AI Service"
   ```
4. **Grant necessary permissions**:
   ```bash theme={null}
   gcloud projects add-iam-policy-binding YOUR_PROJECT_ID \
     --member="serviceAccount:simba-intelligence-ai@YOUR_PROJECT_ID.iam.gserviceaccount.com" \
     --role="roles/aiplatform.user"
   ```
5. **Generate service account key**:
   ```bash theme={null}
   gcloud iam service-accounts keys create simba-intelligence-key.json \
     --iam-account=simba-intelligence-ai@YOUR_PROJECT_ID.iam.gserviceaccount.com
   ```

### Gemini Platform Configuration Process

1. **Access the Gemini Enterprise Agent Platform tab** in LLM Configuration interface

2. **Enter service account JSON**:

   * Copy the complete contents of your service account JSON file
   * Paste into the credentials text area
   * The JSON should include all required fields:

   ```json theme={null}
   {
     "type": "service_account",
     "project_id": "your-gcp-project-id",
     "private_key_id": "your-private-key-id",
     "private_key": "-----BEGIN PRIVATE KEY-----\nYour-Private-Key-Content-Here\n-----END PRIVATE KEY-----\n",
     "client_email": "simba-intelligence-ai@your-project.iam.gserviceaccount.com",
     "client_id": "your-client-id",
     "auth_uri": "https://accounts.google.com/o/oauth2/auth",
     "token_uri": "https://oauth2.googleapis.com/token",
     "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
     "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/simba-intelligence-ai%40your-project.iam.gserviceaccount.com"
   }
   ```

3. **Enable and configure capabilities.** Parameters are set per capability, not shared across the provider — each capability you enable gets its own copy of the fields below.

   | Parameter | Required | Notes |
   | - | - | - |
   | `model_name` | Yes | e.g. `gemini-3-pro`, `gemini-2.5-flash`, `gemini-embedding-001` |
   | `location` | Yes | e.g. `us-central1` |
   | `temperature` | No | `0.0`–`1.0` |
   | `max_tokens` | No | Output token limit |
   | `thinking_budget` | No | Gemini 2.5 and earlier. `0` for maximum speed; `128`–`32768` for Pro |
   | `thinking_level` | No | Gemini 3 and later. One of `minimal`, `low`, `medium`, `high` |

   **Chat Capability:**

   ```
   model_name:     gemini-3-pro
   location:       us-central1
   thinking_level: low
   ```

   **Embeddings Capability:**

   ```
   model_name: gemini-embedding-001
   location:   us-central1
   ```

   **Vision Capability:**

   ```
   model_name: gemini-2.5-flash
   location:   us-central1
   ```

   > **📝 Note:** Parameters that only affect generation — `temperature`, `max_tokens`, `thinking_budget`, `thinking_level` — are hidden on Embeddings capabilities, where they have no meaning.

4. **Save configuration**:
   * Click **"Save"** to store the configuration
   * Verify all capabilities show as "Active"

### Gemini Platform Cost Management

**Understanding costs:**

* **Chat usage**: Charged per input/output token
* **Embeddings**: Charged per text embedding generated
* **Vision**: Charged per image analyzed
* **Model selection**: Different models have different pricing

**Cost optimization tips:**

* Monitor usage in Google Cloud Console
* Set up billing alerts for unexpected usage
* Use semantic caching to reduce redundant API calls
* Choose appropriate models for different use cases

***

## Azure OpenAI Configuration

Azure OpenAI offers the proven GPT models with enterprise-grade security and compliance.

### Azure OpenAI Configuration

**Prerequisites:**

* Azure subscription with OpenAI resource created
* Deployed models in your Azure OpenAI resource
* API key and endpoint details

**Configuration steps:**

1. **Access Azure OpenAI tab** in LLM Configuration interface

2. **Enter credentials** (all required):
   ```
   api_key:        your-azure-openai-api-key
   azure_endpoint: https://your-resource-name.openai.azure.com/
   api_version:    2025-01-01-preview
   ```

3. **Enable and configure capabilities.** Each capability carries its own parameters:

   | Parameter | Required | Notes |
   | - | - | - |
   | `deployment_name` | Yes | The Azure deployment serving this capability |
   | `temperature` | No | `0.0`–`1.0` |
   | `max_tokens` | No | Output token limit |

   **Chat Capability:**

   ```
   deployment_name: your-gpt5-chat-deployment
   temperature:     0.7
   ```

   **Embeddings Capability** (optional):

   ```
   deployment_name: your-embeddings-deployment
   ```

***

## AWS Bedrock Configuration

AWS Bedrock provides access to various foundation models including Anthropic's Claude, with enterprise-grade AWS integration.

### Prerequisites for AWS Bedrock

**AWS account setup:**

1. **AWS account** with Bedrock access enabled in your region
2. **IAM credentials** with appropriate Bedrock permissions
3. **Model access** granted for desired models (Claude, etc.)
4. **Sufficient service quotas** for your expected usage

**Required IAM permissions:**

```json theme={null}
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "bedrock:InvokeModel",
        "bedrock:InvokeModelWithResponseStream",
        "bedrock:GetModel",
        "bedrock:ListFoundationModels"
      ],
      "Resource": "*"
    }
  ]
}
```

### Bedrock Configuration Process

1. **Access AWS Bedrock tab** in LLM Configuration interface

2. **Enter credentials** — `region` is required, plus **either** an `api_key` (bearer token) **or** an IAM key pair:
   ```
   region:            us-east-1
   api_key:           your-bedrock-api-key            (optional — use this OR the IAM keys below)
   access_key_id:     AKIA...your-access-key          (optional)
   secret_access_key: your-secret-access-key          (optional)
   session_token:     temporary-session-token         (optional, for STS)
   ```

3. **Enable and configure capabilities.** Each capability carries its own parameters:

   | Parameter | Required | Notes |
   | - | - | - |
   | `model_name` | Yes | Model ID or inference profile ID, including the geo prefix where the model is only served through a profile |
   | `temperature` | No | Ignored for OpenAI GPT models, which reject it |
   | `max_tokens` | No | Set explicitly for Claude Sonnet (`10000`) to avoid failures |
   | `provider` | No | Overrides Bedrock provider auto-detection (`anthropic`, `openai`, …). Needed when a bare inference-profile ID does not name the family |
   | `reasoning_effort` | No | OpenAI GPT models only. See the note below |

4. **Example — chat capability**:
   ```
   model_name:  us.anthropic.claude-sonnet-4-6
   max_tokens:  10000
   ```

5. **Example — embeddings capability** (if available):
   ```
   model_name: amazon.titan-embed-text-v1
   ```

> **📝 Note — OpenAI GPT on Bedrock:** Bedrock serves these models through inference profiles only, so `model_name` must include the geo prefix (for example, `us.openai.gpt-5.6-sol`). `temperature` is not supported and is dropped if set. The optional `reasoning_effort` parameter accepts `low`, `medium`, `high`, `xhigh`, `max`, and — on GPT-5.6 only — `none`; a value the selected model does not accept fails immediately and the error lists the accepted values. If the model ID does not name the family (a bare profile ID), set `provider: openai` so the correct handling is applied.

### Bedrock Model Selection

**Available model families:**

* **Anthropic Claude**: Excellent for reasoning and analysis — the tested and recommended choice
* **OpenAI GPT**: Tested. Served through inference profiles only, so the model ID needs its geo prefix
* **Amazon Titan / Nova**: AWS-native models, used mainly for embeddings
* **Other Bedrock families** (AI21, Cohere, and so on) are reachable but untested with Simba Intelligence

**Model selection criteria:**

* **Performance requirements**: Response quality and speed
* **Cost considerations**: Different models have different pricing
* **Regional availability**: Not all models available in all regions
* **Compliance requirements**: Some models may have specific compliance certifications

***

## Microsoft Foundry Configuration

Microsoft Foundry serves several model vendors from a single Azure resource. One endpoint and API key reach them all; which wire protocol is used is chosen per capability with the `model_family` parameter.

### Prerequisites for Microsoft Foundry

1. **An Azure AI Foundry resource** with the models you want deployed
2. **The resource endpoint and an API key** from the Azure portal
3. **Model access approved** for the Anthropic and/or OpenAI models you intend to configure

### Foundry Configuration Process

1. **Access the Microsoft Foundry tab** in LLM Configuration interface

2. **Enter credentials** (both required):

   ```
   endpoint: https://your-resource.services.ai.azure.com
   api_key:  your-foundry-api-key
   ```

   > **💡 Pro Tip:** Azure shows this endpoint in several shapes — the bare resource host, a family base URL (`.../anthropic/`, `.../openai/v1`), or a full request URL (`.../openai/v1/chat/completions`). Paste any of them. Simba Intelligence strips the trailing path segments and appends the correct route for the selected model family, so you will not end up with a doubled path and a 404 that looks like an authentication failure.

3. **Choose a model family per capability.** This is the required `model_family` parameter:

   | `model_family` | UI label | Route | Use for |
   | - | - | - | - |
   | `anthropic` | Anthropic | `/anthropic/` | Claude models (Anthropic Messages API) |
   | `openai_v1` | OpenAI Compatible | `/openai/v1` | GPT and every other non-Claude model on the resource |

4. **Configure each capability's parameters:**

   **Anthropic family:**

   | Parameter | Required | Notes |
   | - | - | - |
   | `model_family` | Yes | `anthropic` |
   | `model_name` | Yes | Your Claude deployment name |
   | `max_tokens` | No | Defaults to 32,000 output tokens if unset |

   `temperature` is not offered: current Claude models reject sampling parameters with a 400.

   **OpenAI Compatible family:**

   | Parameter | Required | Notes |
   | - | - | - |
   | `model_family` | Yes | `openai_v1` |
   | `model_name` | Yes | Your model deployment name |
   | `temperature` | No | `0.0`–`1.0` |
   | `max_tokens` | No | Output token limit |

   **Example — Chat on Claude, Embeddings on the OpenAI route:**

   ```
   Chat capability (Power):
     model_family: anthropic
     model_name:   claude-opus-4-6
     max_tokens:   32000

   Embeddings capability:
     model_family: openai_v1
     model_name:   text-embedding-3-large
   ```

> **⚠️ Important:** The Anthropic family cannot serve the **Embeddings** capability — Anthropic publishes no embedding models. Configure embeddings with the `openai_v1` family on the same Foundry resource, as in the example above.

> **📝 Note:** Why `max_tokens` defaults to 32,000 on the Anthropic family: left entirely unset, the client looks up the model's maximum output tokens by exact model ID, and a custom Foundry deployment name misses that lookup and silently falls back to 4,096 — truncating long generations. 32,000 is the floor across the Claude models Foundry serves, so it is safe for any deployment name.

***

## Managing Capabilities

### Understanding Capability Types

**Chat Capability:**

* **Purpose**: Natural language understanding and generation
* **Used for**: Query interpretation, response generation, insight creation
* **Configuration**: Model selection, temperature, token limits

**Embeddings Capability:**

* **Purpose**: Converting text to numerical representations for similarity matching
* **Used for**: Semantic caching, query similarity detection, content understanding
* **Configuration**: Model selection, dimension settings

**Vision Capability**:

* **Purpose**: Image analysis and understanding
* **Used for**: Dashboard mockup analysis, screenshot interpretation
* **Configuration**: Model selection, image processing limits

### Capability Configuration Best Practices

**Chat capability optimization:**

* **Temperature settings**:
  * `0.0-0.3`: Deterministic, factual responses
  * `0.4-0.7`: Balanced creativity and accuracy (recommended)
  * `0.8-1.0`: Creative but potentially less accurate
* **Token limits**: Set based on expected query/response complexity
* **Model selection**: Balance performance, cost, and feature requirements

**Embeddings optimization:**

* **Dimension selection**: Higher dimensions = better accuracy but higher cost
* **Model compatibility**: Ensure embedding model matches your use case
* **Caching strategy**: Configure appropriate cache retention for embeddings

**Multi-provider strategy:**

* **Primary provider**: Choose most reliable provider for critical capabilities
* **Fallback providers**: Configure secondary providers for redundancy
* **Capability specialization**: Use different providers for different capabilities

***

## Testing and Validation

### Manual Validation Procedures

**After configuring providers:**

1. **Test basic chat capability**:
   * Go to Playground interface
   * Ask a simple question about your data
   * Verify natural language response is generated

2. **Test embeddings** (if configured):
   * Ask similar questions multiple times
   * Verify responses improve with semantic caching
   * Check cache hit rates in monitoring

3. **Test vision capability** (Gemini platform, Microsoft Foundry, or any multimodal chat model):
   * Go to Data Agent interface
   * Upload a dashboard screenshot
   * Verify image analysis produces relevant insights

4. **Performance validation**:
   * Monitor response times during testing
   * Check API usage in provider dashboards
   * Verify no rate limiting or quota issues

### Troubleshooting Common Issues

**Authentication failures:**

```
Error: "Invalid API key" or "Authentication failed"
Solutions:
- Verify API key is correctly copied and not truncated
- Check API key permissions and scope
- Ensure billing is enabled and account is in good standing
- For service accounts, verify JSON formatting is correct
```

**Model access issues:**

```
Error: "Model not found" or "Access denied"
Solutions:
- Verify model name/ID is correct for your provider
- Check that model access is granted in provider console
- Ensure your region supports the requested model
- For AWS Bedrock, confirm model access is explicitly granted
```

**Rate limiting or quota issues:**

```
Error: "Rate limit exceeded" or "Quota exceeded"
Solutions:
- Check usage in provider dashboard
- Implement request throttling or retries
- Upgrade service tier if needed
- Distribute load across multiple providers
```

***

## Security Best Practices

### Credential Management

**Secure storage:**

* **Never store credentials in code** or configuration files
* **Use environment variables** or secure secret management systems
* **Encrypt credentials at rest** using appropriate encryption
* **Limit credential access** to authorized personnel only

**Regular rotation:**

* **API keys**: Rotate every 90 days or according to security policy
* **Service accounts**: Regenerate keys quarterly
* **Access review**: Regularly audit who has access to credentials
* **Emergency procedures**: Have procedures for immediate credential revocation

### Network Security

**Data privacy:**

* **Understand data flow**: Know what data is sent to each provider
* **Regional compliance**: Use appropriate regions for data sovereignty
* **Data retention**: Understand provider data retention policies

### Access Control

**Role-based access:**

* **Limit configuration access**: Only supervisors can configure LLM providers
* **Separate development/production**: Use different credentials for different environments
* **Audit configuration changes**: Log all changes to LLM provider configurations
* **Emergency access**: Maintain emergency procedures for credential issues

***

## Cost Management and Optimization

### Understanding AI Provider Costs

**Cost factors:**

* **Token usage**: Both input (prompts) and output (responses) tokens are charged
* **Model selection**: Premium models cost more than basic models
* **Capability type**: Chat, embeddings, and vision have different pricing
* **Request frequency**: High-volume usage may trigger different pricing tiers

### Cost Optimization Strategies

**Provider selection:**

* **Cost comparison**: Compare pricing across providers for your use cases
* **Feature optimization**: Use expensive features (like vision) only when necessary
* **Load balancing**: Distribute load to take advantage of different pricing models

***

*Ready to configure your first LLM provider? Start with the provider that best matches your organization's requirements and follow the step-by-step instructions above. Remember: a well-configured AI foundation is essential for optimal Simba Intelligence performance.*
