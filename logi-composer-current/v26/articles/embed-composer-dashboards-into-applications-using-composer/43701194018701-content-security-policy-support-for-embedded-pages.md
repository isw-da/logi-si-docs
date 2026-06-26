---
title: "Content Security Policy Support for Embedded Pages"
id: 43701194018701
section: "Embed Composer Dashboards Into Applications Using Composer"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701194018701-Content-Security-Policy-Support-for-Embedded-Pages
updated_at: 2026-05-29T14:09:22Z
---

# Content Security Policy Support for Embedded Pages

# Content Security Policy Support for Embedded Pages

Pages that include embedded Composer content can include content security policies with some restrictions. Some guidelines for creating these policies include:

* `script-src` Allow the domain used to serve Composer. `unsafe-inline` or a `nonce` is required. `unsafe-eval` is not required.
* `style-src` Allow the domain used to serve Composer. `unsafe-inline` is required; `nonce` is not yet supported. `unsafe-eval` is not required.
* `font-src` Allow the domain used to serve Composer. Allow `data:` for embedded fonts.

## Using Nonce

If you want to omit `unsafe-inline` for `script-src`, you must use a nonce in the page. The nonce should be a unique string that changes on each new page load.

To instruct the page that the nonce is allowed, include it in the `script-src` portion of your content security policy definition as `nonce-<random string>`. Next, add the same string as the value of the `nonce` attribute on the script tag you use to import the Composer embed, as well as any scripts that call those embed functions.

When this is included, the embed system will include the nonce on any inline script tags it creates.

Example: `index.html`

html
<head>
<meta
http-equiv="Content-Security-Policy"
content="
font-src 'self' data:;
style-src 'self' https://localhost:8080 'unsafe-inline';
script-src 'self' https://localhost:8080 'nonce-abc123';
"
/>
</head>
<body>
<script
data-name="composer-embed-manager"
src="https://localhost:8080/composer/embed/embed.js"
nonce="abc123"
></script>
<script
data-name="main-application-script"
src="https://localhost/myApp/main.js"
nonce="abc123"
></script>
</body>
