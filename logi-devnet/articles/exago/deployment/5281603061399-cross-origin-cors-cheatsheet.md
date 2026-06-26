---
title: "Cross-Origin (CORS) Cheatsheet"
id: 5281603061399
section: "Deployment"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281603061399-Cross-Origin-CORS-Cheatsheet
updated_at: 2022-05-03T22:09:09Z
---

# Cross-Origin (CORS) Cheatsheet

# Cross-Origin (CORS) Cheatsheet

This topic serves as a “quick” version of the [Cross-Origin Embedding of Exago](https://devnet.logianalytics.com/hc/en-us/articles/5281619580311-Cross-Origin-Embedding-of-Exago-BI) topic, to aid system administrators in determining how to correctly integrate Exago BI when hosted from a different origin than the application that embeds it.

## Definitions

These terms will be used throughout this and the Cross-Origin Embedding of Exago topic. An understanding of the basics of cross-origin resource sharing is fundamental to a fully functional Exago implementation.

Table A — Definitions

| Term | Definition |
| origin | The combination of **scheme** (for example `http` or `https`), **host** (for example sub1.example.com), and **port** (usually implicitly `80`). Example: in https://sub1.example.com/topic/how-to-build-a-wall, https://sub1.example.com is the **origin**.  For more information, review the [Origin topic from the Mozilla Developer Network](https://developer.mozilla.org/en-US/docs/Glossary/Origin). |
| same-origin | The **origin** of the page embedding Exago is the same as the **origin** of the Exago Web Application. |
| cross-origin | The **origin** of the page embedding Exago is different than the **origin** of the Exago Web Application. |

### Examples

Consider an environment where the host application is hosted on `http://myapp.example.com:80`.

Table B — Examples

| When Exago is hosted on… | …it is this kind of environment |
| --- | --- |
| `http://myapp.example.com:80` `http://myapp.example.com` | same-origin |
| `https://myapp.example.com` | cross-origin light bulb The **scheme** is different. |
| `http://exago.example.com` | cross-origin light bulb The **host** is different. |
| `http://myapp.example.com:8080` | cross-origin light bulb The **port** is different. |

## Implementation Cases

This section reviews each of four potential same-origin and cross-origin architectures that may be encountered when implementing Exago BI.

[**same-origin**](#CASE:) and [**cross-origin, with one or few embedding origins**](#CASE:2) will make up a vast majority of use cases

The instructions below apply to *v2019.2.29+, v2020.1.13+, v2021.1.1+.* For previous versions, see [Cross-Origin Embedding of Exago BI](https://devnet.logianalytics.com/hc/en-us/articles/5281619580311-Cross-Origin-Embedding-of-Exago-BI).

### CASE: same-origin

In the case where the host application and Exago BI Web Application are hosted from the same origin, there are no CORS-specific requirements.

### CASE: cross-origin, with one or few embedding origins

In this case, the Exago BI Web Application and the embedding host application are hosted on different origins. Requests to Exago BI may come from just one, or a small number of host application origins.

1. Make sure Exago BI is hosted over **https**.
2. Add the **AccessControlAllowCredentials** option to the Web Application’s `appSettings.config` file, and set its *value* attribute to *true*.
3. Add the **CorsAllowedOrigins** option to the Web Application’s `appSettings.config` file, and set its *value* attribute to the domain, or a comma-separated list of domains that embed Exago BI.

#### Example 1

```
<add key="AccessControlAllowCredentials" value="true" />
<add key="CorsAllowedOrigins" value="https://s1.domain1.com,https://s2.domain1.com" />
```

#### Example 2

```
<add key="AccessControlAllowCredentials" value="true" />
<add key="CorsAllowedOrigins" value="https://*.domain1.com" />
```

### CASE: cross-origin, with many or unpredictable embedding origins

### CASE: cross-origin, but Exago cannot be hosted over HTTPS

> ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/5432173635607/criticalicon.gif "Important")
>
> Avoid these situations whenever possible. Use cookies for session state tracking rather than cookieless sessions. If using a state server, using cookies is required.

1. Add the **CorsAllowedOrigins** option to the Web Application’s `appSettings.config` file, and set its *value* to the wild card character, `*`  
   Example:

   ```
   <add key="CorsAllowedOrigins" value="*" />
   ```
2. In a JavaScript API implementation, make sure the **IncludeCredentials** property is set to *false* when instantiating the `ExagoApi` object.
3. Enable cookieless sessions in Exago BI.

## Troubleshooting and Diagnostics

For any response that Exago BI sends that includes a `Set-Cookie` header (for example in responses to ExagoHome.aspx or ExagoJSEmbed.aspx), Exago BI also includes a header called **`x-exago-samesite`**, which contains debugging information relevant to Exago BI’s handling of SameSite cookies.

Possible values for `x-exago-samesite` are:

* (not present at all) — it is possible that the **SameSiteCookiesMode** directive in the Application Settings for the Web Application is set to *Off*.
* `force-none` — Exago BI forced the cookie to have `SameSite=None; Secure`. This allows cookies to work when Exago BI is embedded at a different origin than the host application. Also see `x-exago-orig-cookie` below.
* `skip-insecure` — Exago BI did not make any explicit changes to the cookie related to SameSite, because the connection to Exago BI was not made over HTTPS.
* `remove` — Exago BI removed any SameSite directive that may have been in the Cookie because the user agent does not support the SameSite directive. Also see `x-exago-orig-cookie` below.

Additionally, if **`x-exago-samesite`** is either `force-none` or `remove`, the **`x-exago-orig-cookie`** header will contain the original value of the cookie’s `Set-Cookie` header before it was changed by Exago BI.

### Accessing these Headers

Use the **Developer Tools** or **Console** functions of the web browser to inspect headers. For example, in Mozilla Firefox:

![NWllQosCfQ.png](https://devnet.logianalytics.com/hc/article_attachments/5432348195991/nwllqoscfq.png)

Mozilla Firefox Developer Tools

1. Open the Developer Tools function (typically with the **F12** key on the keyboard, then switch to the **Network** tab.
2. Locate the very first call to *ExagoJSEmbed.aspx* and click it in the list.
3. Scroll the **Headers** pane down to the **Response Headers** section. The headers will appear here. In this example, `x-exago-samesite` is *skip-insure.*
