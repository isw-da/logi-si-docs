> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Embed Components Into Your Application

Embed components into your own applications to provide seamless integration for your users.

The following components can be embedded:

* dashboards, lite dashboards
* visual authoring experience
* source editor

When components are embedded, the way in which users can interact with them is determined by settings established in their user account. See [Embedded Self-Service Analytics Component Controls](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/embed-controls).

<Note>
  insightsoftware recommends using [Trusted Access](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/security/trusted-access-ov) for all embed-related workflows.
</Note>

The list of options available on an embedded [visual's drop-down menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-drop-down-menu) depends on:

* The mode setting for the dashboard. If the embed mode is [`readonly` or](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/embed/embed-javascript-embedmanager-methods#embedded-dashboard-properties-and-objects) [**Read Only**](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/embed/dash-embed-gencode-dashboard), no menu is available at all.
* The [visual interactivity settings](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-interactivity) specified in the visual definition.
* The [dashboard interactivity settings](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-interactivity) specified for the dashboard, if those settings include override interactivity settings for all visuals in the dashboard.

When options are shown for a visual in an embedded dashboard, they may be shown in the [visual sidebar menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-sidebar-menu) or within the [visual drop-down menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-drop-down-menu) itself, depending on the setting of the [`editor.placement`](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/embed/embed-javascript-embedmanager-methods#embedded-dashboard-properties-and-objects) property.

* If [`editor.placement`](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/embed/embed-javascript-embedmanager-methods#embedded-dashboard-properties-and-objects) is set to `dockRight`, the options appear in sidebars using the [visual sidebar menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-sidebar-menu) and the resulting sidebar editing panels.

  If [`editor.placement`](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/embed/embed-javascript-embedmanager-methods#embedded-dashboard-properties-and-objects) is set to `modals`, the options appear in the [visual drop-down menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-drop-down-menu) itself and the resulting floating dialogs.

<Note>
  In environments where you use Typescript for your client side code, you can use Embed Manager as an npm package. See [https://www.npmjs.com/package/logi-embed](https://www.npmjs.com/package/logi-embed).
</Note>

* [Embedded Component Prerequisites](#embedded-component-prerequisites)
* [Embeddable Component Snippets](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/embed/dash-embed-gencode-dashboard)
* [Generate a Visual Gallery HTML Snippet](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/embed/dash-embed-gencode-dashboard#generate-a-visual-gallery-html-snippet)
* [Embed Dashboards](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/embed/dash-embed/dash-embed-steps)
* [Embedded Self-Service Analytics Component Controls](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/embed-controls)
* [Embed Multiple Dashboards On a Single Page](#embed-multiple-dashboards-on-a-single-page)

See the following topics for embedding the source editor:

* [Embedded Source Editor](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/embed/embed-source-editor)
* [Embed Source Editor Properties](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/embed/embed-source-editor#embed-source-editor-properties)

<h2 id="embedded-component-prerequisites">
  Embedded Component Prerequisites
</h2>

To embed a Self-Service Analytics component into your own application, the following prerequisites must be met:

* You must have created a host application into which you want to embed the component.

* [Trusted Access](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/security/trusted-access-ov), enabled by default, must be enabled and configured to authenticate users of your embedded components. See [Trusted Access](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/security/trusted-access-ov). Be sure that your application is registered as a Self-Service Analytics client and that you have met the [prerequisites of Trusted Access](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/security/trusted-access-ov#trusted-access-prerequisites).

  <Note>
    insightsoftware recommends using [Trusted Access](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/security/trusted-access-ov) for all embed-related workflows.
  </Note>

* Cross-origin sharing (CORS) must be enabled for your Self-Service Analytics instance. See [Enable Self-Service Analytics Component Access From Other Sites Using Cross-Origin Resource Sharing (CORS)](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/config-mgmt-ov#enable-self-service-analytics-component-access-from-other-sites).

* You need to be a Self-Service Analytics administrator or a user assigned to a group with the **Generate Embed Code** [privilege](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference) so you can generate [library](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/embed/dash-embed-gencode-dashboard), [visual gallery](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/embed/dash-embed-gencode-dashboard#generate-a-visual-gallery-html-snippet), or [sources inventory](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/embed/dash-embed-gencode-dashboard#generate-a-sources-inventory-html-snippet) snippets used for embedding.

## Content Security Policy Support for Embedded Pages

Pages that include embedded Self-Service Analytics content can include content security policies with some restrictions. Some guidelines for creating these policies include:

* `script-src` Allow the domain used to serve Self-Service Analytics. `unsafe-inline` or a `nonce` is required. `unsafe-eval` is not required.
* `style-src` Allow the domain used to serve Self-Service Analytics. `unsafe-inline` is required; `nonce` is not yet supported. `unsafe-eval` is not required.
* `font-src` Allow the domain used to serve Self-Service Analytics. Allow `data:` for embedded fonts.

### Using Nonce

If you want to omit `unsafe-inline` for `script-src`, you must use a nonce in the page. The nonce should be a unique string that changes on each new page load.

To instruct the page that the nonce is allowed, include it in the `script-src` portion of your content security policy definition as `nonce-<random string>`. Next, add the same string as the value of the `nonce` attribute on the script tag you use to import the Self-Service Analytics embed, as well as any scripts that call those embed functions.

When this is included, the embed system will include the nonce on any inline script tags it creates.

Example: `index.html`

```
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
```

<h2 id="embed-multiple-dashboards-on-a-single-page">
  Embed Multiple Dashboards On a Single Page
</h2>

You can embed multiple dashboards on a single page of your application and in a single `<div>` in your application, including embedding one or more empty dashboards. You can also embed the same dashboard multiple times on a page and each embedded instance can use its own property settings (theme, mode, header, title). Finally, the dashboards can be embedded using different methods: you can embed one dashboard using [generated embed code](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/embed/dash-embed/dash-embed-steps) and another dashboard using [JavaScript](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/embed/embed-javascript).

<Note>
  When more than one dashboard is embedded in application, the [cross-visual filters](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/pubsub-ov) that are published for a visual on one of the dashboards can be subscribed to by any visual on any of the embedded dashboards. However, this is not true unless the dashboards are embedded in the same application. Visuals in a dashboard open in one window or tab cannot subscribe to cross-visual filters published by visuals in a different window or tab.
</Note>
