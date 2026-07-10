# Simba Intelligence — LLM provider compatibility findings

Field notes from wiring non-standard chat models into Simba Intelligence 26.2.0
(kind cluster, GREN-lineage tenant, Supabase FRC source). Captured 2026-07-10.
Audience: SI SEs and product. Purpose: save the next person the day I just spent,
and give product two concrete gaps to consider.

## TL;DR

- SI 26.2 exposes exactly four LLM provider types: **Vertex AI, Azure OpenAI,
  AWS Bedrock, Ollama**. There is **no native "xAI/Grok" and no native
  "OpenAI-direct" provider.** Anything else (Grok, OpenAI on a personal key,
  a local model) has to be presented to SI as one of those four.
- The pragmatic path for both Grok and OpenAI-direct is a **LiteLLM proxy** that
  speaks the Azure OpenAI wire format to SI and translates to the real provider.
  This is the same trick the setup skill already documents for Ollama.
- **Grok** works fine this way (Grok 4.3 on Azure AI Foundry, driven through the
  bridge). One gotcha: SI sends `model: null` in its validation probe, which
  xAI's stricter parser rejects; the bridge absorbs it.
- **OpenAI GPT-5.6 (Sol/Terra/Luna) does not work for SI's query pipeline** on
  the Chat Completions API: all three refuse function tools unless
  `reasoning_effort=none`, and with reasoning off they are too weak to complete
  SI's multi-step query building (they fabricate "authorization error"
  narration instead of finishing the tool loop). GPT-5.6 + tools + reasoning
  requires the `/v1/responses` endpoint, which SI does not call.
- **The newest OpenAI model that actually drives SI is GPT-5.5** — it supports
  function tools with reasoning intact on Chat Completions. Verified 3/3 on the
  standard FRC grading set.

## Why there is no native provider for these

SI's provider registry (`GET /api/v1/config/llm/providers`) returns only
`VERTEX_AI`, `AZURE_OPENAI`, `AWS_BEDROCK`, `OLLAMA`. Each capability
(chat/embeddings/vision) is validated at save time by SI actually calling the
model, so you cannot register a shape SI doesn't have a client for. There is no
extension point for a new provider in 26.2.

Consequence: any model not from Google Vertex, Azure OpenAI, Bedrock or a local
Ollama must be fronted by something that impersonates one of those. The Azure
OpenAI shape is the easiest to impersonate because it is a thin wrapper over the
OpenAI Chat Completions schema.

## The bridge pattern (works for Grok and OpenAI-direct)

```
SI  --Azure OpenAI wire format-->  LiteLLM proxy  --native API-->  Grok / OpenAI / ...
```

LiteLLM container on the demo box, one entry per upstream model:

```yaml
model_list:
  - model_name: grok-4-3                 # what SI's deployment_name points at
    litellm_params:
      model: azure/grok-4-3              # Azure AI Foundry deployment
      api_base: https://<foundry>.openai.azure.com/
      api_version: "2025-01-01-preview"
      api_key: <foundry-key>
  - model_name: gpt-5-5
    litellm_params:
      model: openai/gpt-5.5              # OpenAI direct, personal key
      api_key: <sk-...>
litellm_settings:
  drop_params: true                      # silently drop params the upstream rejects
general_settings:
  master_key: sk-bridge-local
```

SI LLM config (Azure OpenAI provider):

| Field | Value |
|---|---|
| api_key | the bridge `master_key` |
| azure_endpoint | the bridge URL (from a kind pod: the cluster's IPv4 gateway, e.g. `http://172.18.0.1:8104`) |
| api_version | `2025-01-01-preview` |
| chat deployment_name | the LiteLLM `model_name` (`grok-4-3`, `gpt-5-5`) |

Pod-to-bridge networking gotcha: the kind docker network's first IPAM entry is
often IPv6; filter for the IPv4 gateway or the pod can't resolve the bridge.

## Grok specifics

- Grok 4.3 GA on Azure AI Foundry (xAI format, GlobalStandard, serverless
  pay-per-token). Deployed fine, drives SI's pipeline through the bridge.
- SI's save-time validation probe posts `model: null`; Azure OpenAI models
  ignore it, xAI 400s ("model: invalid type: null"). The bridge rewrites the
  request so the upstream never sees the null. No SI-side fix available.
- Grok is a reasoning model: ~10x slower per NLQ than a comparable OpenAI model
  through SI's agentic loop, and Foundry personal-sub quota caps at 50K TPM.

## OpenAI GPT-5.6 specifics (the blocking finding)

All three 5.6 tiers on Chat Completions:

```
Function tools with reasoning_effort are not supported for gpt-5.6-<tier>
in /v1/chat/completions. To use function tools, use /v1/responses or set
reasoning_effort to 'none'.
```

- With `reasoning_effort=none`: tool calls are accepted, but the model is
  unreliable at SI's multi-step query construction — in testing it returned
  1/3 then 0/3 on the standard grading set, fabricating "the data query service
  returned a permissions error" rather than completing the tool loop (the SI
  query engine logs showed no such error; it was model narration).
- The supported path (reasoning + tools) is the `/v1/responses` API. SI 26.2
  drives Chat Completions only, and LiteLLM's Azure-shape bridge maps to Chat
  Completions, so `/v1/responses` is not reachable end to end today.

**Recommendation for product:** if SI is to support the GPT-5.6 generation, the
chat client needs a Responses-API path for OpenAI reasoning models. Until then,
GPT-5.5 is the newest OpenAI model that works.

## What actually shipped in the sandbox

- Chat: **GPT-5.4** (OpenAI direct, personal key, through the bridge), temperature
  0 for determinism. Chosen deliberately to match the model prospects trial and
  the model the live demos run on, so sandbox results are comparable to prospect
  results. 3/3 on the FRC grade (1,719 alerts; $16,783.13 total; top type cycle
  $13,868.70), 7-9s per query.
- GPT-5.5 was verified working (3/3, 10-32s) but not kept: it is a version ahead
  of the demo/prospect model and 2x the token cost ($5/$30 vs $2.50/$15).
- Embeddings + vision: left on Azure OpenAI (ada-002 / gpt-5.4) so existing
  source vectors were untouched.
- Grok 4.3 config kept but deactivated, ready to switch back.
- Cost control: OpenAI org hard spend limit $20/month, hard-enforced (requests
  429 past it); Azure Foundry $25/month budget alerts for the Grok deployment.

Model-choice note: GPT-5.4 is the current demo/prospect standard, supports
function tools with reasoning on Chat Completions, accepts temperature 0 (unlike
the 5.6 tiers), and is half the token cost of 5.5. It is the right sandbox
default whenever the goal is parity with what prospects see.

## Reusable assets on the demo box

- Bridge: container `grok-bridge`, config `/etc/grok-bridge/config.yaml`, listens
  on `:8104`.
- Grading script pattern and the identity-carry restore runbooks live with the
  instance backups (`/root/si-backups/*/RESTORE.md`).
