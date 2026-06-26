> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.app/llms.txt
> Use this file to discover all available pages before exploring further.

# Logging Configuration Guide

# Logging Configuration Guide

Simba Intelligence uses a flexible, module-level logging system that lets you control exactly how much detail you see — from high-level milestones to full LLM prompt traces. This guide explains how to configure logging and which configuration to use for each debugging scenario.

## Overview

Logging is controlled through a single environment variable, `LOG_LEVELS`, which accepts a JSON array. Each entry targets a specific internal module and sets its log verbosity independently.

By default, only `WARNING` and above are shown. Modules you explicitly list in `LOG_LEVELS` will log at the level you specify, giving you surgical control over noise vs. detail.

## Log Levels

| Level      | What It Shows                                                 | When to Use It                                           |
| ---------- | ------------------------------------------------------------- | -------------------------------------------------------- |
| `DEBUG`    | Everything — all internal logic, loops, and decisions         | Tracing a specific flow step-by-step                     |
| `INFO`     | Key events — decisions made, data created, milestones reached | Monitoring normal operation at a high level              |
| `WARNING`  | Non-fatal problems — retries, fallbacks, edge cases           | Something went slightly wrong but didn't break execution |
| `ERROR`    | Failures that block an operation — exceptions, failed calls   | Something broke and needs immediate attention            |
| `CRITICAL` | System-level failures — data loss risk, service unavailable   | The system cannot continue operating                     |

## How It Works

Set `LOG_LEVELS` as a JSON array environment variable. Each entry specifies a module name and the log level to apply to it.

```bash theme={null}
LOG_LEVELS='[{"module": "<logger-name>", "logLevel": "<LEVEL>"}]'
```

**Key points:**

* The underlying log handler is set to `DEBUG` — it passes everything through. All filtering is controlled by the per-module levels you set here.
* Only modules you list will log below the default `WARNING` threshold.
* You can mix levels across modules in a single configuration (e.g. `DEBUG` for a specific service, `INFO` for supporting ones).

***

## Configurations by Scenario

Pick the scenario that matches what you need to investigate and paste the corresponding `LOG_LEVELS` value into your environment.

### 1. Trace the Full Question-to-Answer Path

Follows a user's question from intake → cache check → LLM orchestration → Composer data fetch → natural language conversion → SSE response stream.

```bash theme={null}
LOG_LEVELS='[
  {"module": "simba_intelligence.api.agent_controller",                   "logLevel": "DEBUG"},
  {"module": "simba_intelligence.llm.ai_data_retriever",                  "logLevel": "DEBUG"},
  {"module": "simba_intelligence.llm.ai_data_converter_natural_language",  "logLevel": "DEBUG"},
  {"module": "simba_intelligence.llm.ai_semantic_cache",                  "logLevel": "INFO"},
  {"module": "simba_intelligence.composer.composer_api_client",           "logLevel": "INFO"},
  {"module": "simba_intelligence.models.api.event_stream",                "logLevel": "DEBUG"},
  {"module": "simba_intelligence.services.history_service",               "logLevel": "INFO"}
]'
```

**You will see:**

* Cache hit or miss for the incoming question
* Base request body, selected fields, aggregation type, time filters, and output type
* Composer request sent and response status code
* Generated natural language answer text
* History record created
* SSE event types streamed back to the client

***

### 2. Audit All LLM Prompts and Responses

Captures every prompt sent to and every response received from the LLM, across all product features.

```bash theme={null}
LOG_LEVELS='[
  {"module": "simba_intelligence.llm.callbacks.prompt_logging_callback", "logLevel": "DEBUG"}
]'
```

**You will see:**

* `[LLM Call]` — model name, run ID, and full message content (system / human / AI roles)
* `[LLM Response]` — model name, run ID, and full generated text
* `[LLM Error]` — run ID and error details

> This single module covers LLM calls across data retrieval, chat, and data source creation, because the callback is attached at the factory level.

***

### 3. Full End-to-End Trace (Question + LLM Prompts)

Combines scenarios 1 and 2 for complete visibility including the exact prompts sent at each step.

```bash theme={null}
LOG_LEVELS='[
  {"module": "simba_intelligence.api.agent_controller",                   "logLevel": "DEBUG"},
  {"module": "simba_intelligence.llm.ai_data_retriever",                  "logLevel": "DEBUG"},
  {"module": "simba_intelligence.llm.ai_data_converter_natural_language",  "logLevel": "DEBUG"},
  {"module": "simba_intelligence.llm.ai_semantic_cache",                  "logLevel": "INFO"},
  {"module": "simba_intelligence.llm.callbacks.prompt_logging_callback",  "logLevel": "DEBUG"},
  {"module": "simba_intelligence.composer.composer_api_client",           "logLevel": "INFO"},
  {"module": "simba_intelligence.models.api.event_stream",                "logLevel": "DEBUG"},
  {"module": "simba_intelligence.services.history_service",               "logLevel": "INFO"}
]'
```

> See scenarios 1 and 2 for what to expect.

***

### 4. Debug Visual Generation

Focuses on chart and graph creation.

```bash theme={null}
LOG_LEVELS='[
  {"module": "simba_intelligence.llm.ai_generate_visual",            "logLevel": "DEBUG"},
  {"module": "simba_intelligence.llm.callbacks.prompt_logging_callback", "logLevel": "DEBUG"}
]'
```

**You will see:**

* Visual type selected, payload constructed, and visual created
* Filter issues, creation retries, and exhausted retry attempts
* LLM prompts requesting visual specifications

***

### 5. Debug Data Source Creation and Onboarding

Focuses on the data source setup pipeline — schema analysis, column formatting, and suggestion generation.

```bash theme={null}
LOG_LEVELS='[
  {"module": "simba_intelligence.llm.ai_data_source_creator",        "logLevel": "INFO"},
  {"module": "simba_intelligence.composer.composer_sources",          "logLevel": "DEBUG"},
  {"module": "simba_intelligence.composer.composer_settings",         "logLevel": "DEBUG"},
  {"module": "simba_intelligence.llm.callbacks.prompt_logging_callback", "logLevel": "DEBUG"}
]'
```

**You will see:**

* Schema analysis steps and column formatting decisions
* Suggestion generation
* Token limit warnings and API errors
* Source data fetches, sample values, and cached stats
* Global settings lookups
* All LLM prompts for schema analysis

***

### 6. Debug Composer (Data Layer) Communication

Focuses on all HTTP calls to the Composer backend and source data operations.

```bash theme={null}
LOG_LEVELS='[
  {"module": "simba_intelligence.composer.composer_api_client",       "logLevel": "INFO"},
  {"module": "simba_intelligence.composer.composer_sources",          "logLevel": "DEBUG"},
  {"module": "simba_intelligence.composer.composer_settings",         "logLevel": "DEBUG"}
]'
```

**You will see:**

* Every Composer HTTP request (method + endpoint) and response status code
* Failed fetches and timeouts
* Source data lookups, sample values, cached stats, and fuzzy matches

***

### 7. Debug Redis and Caching

Focuses on Redis operations — semantic cache, source indexes, and vector search.

```bash theme={null}
LOG_LEVELS='[
  {"module": "simba_intelligence.services.redis_service",             "logLevel": "INFO"},
  {"module": "simba_intelligence.llm.ai_semantic_cache",             "logLevel": "INFO"}
]'
```

**You will see:**

* Redis connection pool initialization and close events
* Index creation, search queries, vector searches, and result counts
* Cache hits, misses, and updates
* Clear and delete operations

***

### 8. Debug Authentication and Session Management

Focuses on token lifecycle, OAuth flows, and tenant switching.

```bash theme={null}
LOG_LEVELS='[
  {"module": "simba_intelligence.api.auth_controller",                "logLevel": "INFO"},
  {"module": "simba_intelligence.services.oauth_service",             "logLevel": "INFO"}
]'
```

**You will see:**

* Token generation, revocation, and rotation
* OAuth client registration and authorization codes
* Tenant switching
* Session management events

***

### 9. Debug LLM Configuration Management

Focuses on provider configuration CRUD, capability changes, and AI service factory errors.

```bash theme={null}
LOG_LEVELS='[
  {"module": "simba_intelligence.api.llm_configuration_controller",   "logLevel": "ERROR"},
  {"module": "simba_intelligence.services.llm_configuration_service", "logLevel": "INFO"},
  {"module": "simba_intelligence.llm.services.ai_service_factory",   "logLevel": "ERROR"}
]'
```

**You will see:**

* Configuration CRUD operations
* Capability activation and deactivation
* Embeddings model changes
* Factory errors when creating AI services

***

### 10. Debug Rules Service

Focuses on rule creation, updates, deletions, and permission enforcement.

```bash theme={null}
LOG_LEVELS='[
  {"module": "simba_intelligence.services.rules_service",             "logLevel": "INFO"}
]'
```

**You will see:**

* Rule creation, update, and deletion
* Permission violations (e.g. a user attempting to modify tenant-wide rules)
* Missing rules lookups

***

### 11. Debug the Chat (Multi-Turn) Feature

Focuses on the conversational AI agent that invokes tools iteratively across multiple turns.

```bash theme={null}
LOG_LEVELS='[
  {"module": "simba_intelligence.llm.ai_data_chat",                  "logLevel": "DEBUG"},
  {"module": "simba_intelligence.llm.callbacks.prompt_logging_callback", "logLevel": "DEBUG"},
  {"module": "QueryDataTool",                                        "logLevel": "DEBUG"},
  {"module": "CreateVisualTool",                                     "logLevel": "DEBUG"},
  {"module": "GetSuggestionsTool",                                   "logLevel": "DEBUG"},
  {"module": "GetDataSourceFieldStatisticsTool",                     "logLevel": "DEBUG"}
]'
```

**You will see:**

* Each tool iteration and its result
* Final answer generation
* Max-iteration warnings
* Tool execution errors
* All LLM prompts and responses within the chat loop

***

### 12. Full Debug — Everything at DEBUG

> **Warning:** This is extremely verbose. Use only when you need complete system visibility and are prepared to filter through high log volume.

```bash theme={null}
LOG_LEVELS='[
  {"module": "simba_intelligence.api.agent_controller",              "logLevel": "DEBUG"},
  {"module": "simba_intelligence.api.auth_controller",               "logLevel": "DEBUG"},
  {"module": "simba_intelligence.api.llm_configuration_controller",  "logLevel": "DEBUG"},
  {"module": "simba_intelligence.llm.ai_data_retriever",             "logLevel": "DEBUG"},
  {"module": "simba_intelligence.llm.ai_data_chat",                  "logLevel": "DEBUG"},
  {"module": "simba_intelligence.llm.ai_generate_visual",            "logLevel": "DEBUG"},
  {"module": "simba_intelligence.llm.ai_data_source_creator",        "logLevel": "DEBUG"},
  {"module": "simba_intelligence.llm.ai_data_converter_natural_language", "logLevel": "DEBUG"},
  {"module": "simba_intelligence.llm.ai_semantic_cache",             "logLevel": "DEBUG"},
  {"module": "simba_intelligence.llm.callbacks.prompt_logging_callback", "logLevel": "DEBUG"},
  {"module": "simba_intelligence.llm.services.ai_service_factory",   "logLevel": "DEBUG"},
  {"module": "simba_intelligence.composer.composer_api_client",      "logLevel": "DEBUG"},
  {"module": "simba_intelligence.composer.composer_sources",          "logLevel": "DEBUG"},
  {"module": "simba_intelligence.composer.composer_settings",         "logLevel": "DEBUG"},
  {"module": "simba_intelligence.services.history_service",          "logLevel": "DEBUG"},
  {"module": "simba_intelligence.services.redis_service",            "logLevel": "DEBUG"},
  {"module": "simba_intelligence.services.rules_service",            "logLevel": "DEBUG"},
  {"module": "simba_intelligence.services.suggestion_service",       "logLevel": "DEBUG"},
  {"module": "simba_intelligence.services.oauth_service",            "logLevel": "DEBUG"},
  {"module": "simba_intelligence.services.llm_configuration_service","logLevel": "DEBUG"},
  {"module": "simba_intelligence.models.api.event_stream",           "logLevel": "DEBUG"},
  {"module": "QueryDataTool",                                        "logLevel": "DEBUG"},
  {"module": "CreateVisualTool",                                     "logLevel": "DEBUG"},
  {"module": "GetSuggestionsTool",                                   "logLevel": "DEBUG"},
  {"module": "GetDataSourceFieldStatisticsTool",                     "logLevel": "DEBUG"}
]'
```

***

## Module Reference

Use this table to identify which module to target for a specific area of the system.

| Module                                                      | What It Logs                                          |
| ----------------------------------------------------------- | ----------------------------------------------------- |
| `simba_intelligence.llm.ai_data_retriever`                  | Field selection, filters, aggregation, query assembly |
| `simba_intelligence.llm.ai_data_chat`                       | Tool iterations, tool results, final answers          |
| `simba_intelligence.llm.ai_generate_visual`                 | Visual type, payload, retry attempts                  |
| `simba_intelligence.llm.ai_data_source_creator`             | Schema analysis, column formatting, suggestions       |
| `simba_intelligence.llm.ai_data_converter_natural_language` | Natural language answer text                          |
| `simba_intelligence.llm.callbacks.prompt_logging_callback`  | Full LLM prompts and responses (all features)         |
| `simba_intelligence.llm.ai_semantic_cache`                  | Cache hit / miss / update                             |
| `simba_intelligence.llm.services.ai_service_factory`        | Model creation errors                                 |
| `simba_intelligence.composer.composer_api_client`           | HTTP requests and response status codes               |
| `simba_intelligence.composer.composer_sources`              | Source data, sample values, stats cache               |
| `simba_intelligence.composer.composer_settings`             | Global settings lookups                               |
| `simba_intelligence.services.history_service`               | Question history records                              |
| `simba_intelligence.services.redis_service`                 | Index operations, searches, cache operations          |
| `simba_intelligence.services.rules_service`                 | Rule CRUD, permission checks                          |
| `simba_intelligence.services.suggestion_service`            | Suggestion generation and retrieval                   |
| `simba_intelligence.api.agent_controller`                   | Request validation errors, stream errors              |
| `simba_intelligence.api.auth_controller`                    | Token lifecycle, tenant switching                     |
| `QueryDataTool`                                             | Tool invocation with sanitized question               |
| `CreateVisualTool`                                          | Visual creation errors                                |
| `GetSuggestionsTool`                                        | Suggestion retrieval details                          |
| `GetDataSourceFieldStatisticsTool`                          | Field statistics requests                             |
