---
title: "Embed a Visual in Your Web Page"
id: 4405850883735
section: "Embed Composer Dashboards Into Applications using Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405850883735-Embed-a-Visual-in-Your-Web-Page
updated_at: 2021-09-21T01:26:46Z
---

# Embed a Visual in Your Web Page

# Embed a Visual in Your Web Page

The Composer Application Framework provides a client library for embedding visuals into a web application or web page without using an iframe. To assist you in this task, Composer provides:

* This topic, which includes annotated steps for embedding a visual in your own web app
* A simple example of an embedded visual with annotated code, discussed in this topic, and available for download at
  Composer's Github repository.
* Before beginning, see [*What Can You Embed?*](https://devnet.logianalytics.com/hc/en-us/articles/4405850884631-What-Can-You-Embed-) to determine which parts of visuals get embedded when you embed one in a custom application.

![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg)Logi Analytics recommends using [Trusted Access](https://devnet.logianalytics.com/hc/en-us/articles/4405851181463-Trusted-Access) for all embed-related workflows.

## Steps for Embedding a Visual

These stages for embedding a visual in a web application will guide your work.

1. [*Prepare Your HTML File for the Visual*](#Preparing).
2. [*Organize Application and Security Parameters*](#Organizing)
3. [*Add Code to Your Web Application to Display the Visual*](#Adding).

## Prepare Your HTML File for the Visual

To prepare your own HTML file for the visual:

1. Link and include various dependencies. The main dependency is the Composer JavaScript client library. The library is located in your Composer installation at the URL
   `/composer/sdk/zoomdata-client.js`. The application framework also depends on jQuery. Composer recommends that you link jQuery v1.8 or later.
2. In your HTML file, create a JavaScript `<script>` element with an anonymous function. Your embedding code will be placed inside the element.

   ```
   <script type="text/javascript"></script>
   ```
3. Add a `<div>` or other element to your HTML, assigning it a unique id attribute. The visual will be attached to this element.

   ```
   <div id="visualization" class="widgetContent medium" style="width:40%; height:40%; float:left; top:20%"></div>
   ```

   Certain visuals require the attribute `class="widgetContent medium"` to be explicitly added to the element to which the visual is attached. The best practice is to use the attribute for all visuals.

## Organize Application and Security Parameters

Connecting the web page to your Composer server requires supplying the Composer server with application and security parameters in the form of JavaScript objects. These two objects are themselves bundled together as a single object to be passed to the `createClient()` method. For example:

```
ZoomdataSDK.createClient({
   credentials: credentialConfig,
   application: applicationConfig
})
```

For more information about the application configuration object, see
[*Application Configuration Object*](https://devnet.logianalytics.com/hc/en-us/articles/4405851137943-Application-Configuration-Object).

For more information about the security configuration object, see
[*Security Configuration Object*](https://devnet.logianalytics.com/hc/en-us/articles/4405851148695-Security-Configuration-Object).

* When you generate a security key for a data source, users of the data source are automatically granted Read permission for all existing visuals using the data source, but not for any new visuals created after the security key was generated. Instead, a new security key must be generated for new visuals.
* When you generate a security key for a dashboard, users of the dashboard are automatically granted Read permission for all existing visuals on the dashboard for which they have Read permissions. However, if a new visual is created on the dashboard after the security key is generated, dashboard users will not automatically be granted Read permission for the new visual. Instead, a new security key must be generated for newer visuals on the dashboard. )

## Add Code to Your Web Application to Display the Visual

The Composer JavaScript client library includes an application-level object called
`ZoomdataSDK`. The
`ZoomdataSDK`
object is used to create a
`client`
object. The
`client`
object is used to render visuals. In its simplest form, the code for creating a client and embedding a visual typically looks as follows.

```
ZoomdataSDK.createClient({ 
	credentials: credentialConfig, 
	application: applicationConfig 
	}) 
	.then(function(client) { 
		window.client = client; 
		return(client); 
	}) 
	.then(function(client) { 
		client.visualize({ 
			element: vizLocation, 
			config: queryConfig, 
			source: {name: 'Real Time Sales'}, 
			visualization: 'Packed Bubbles', 
			variables: { 
				'Bubble Size': 'count', 
				'Bubble Color': 'usersentiment:avg' } 
		}) 
		.then(function(result) {
			window.viz = result;
		});
	});
```

The basic code can be expanded to add event and error handling as well as other functionality.

**To embed a visual:**

1. Create a Composer client instance using
   `createClient()`.

   ```
   ZoomdataSDK.createClient({ 
   	credentials: credentialConfig, 
   	application: applicationConfig 
   	}) 
   	.then(function(client) { 
   		window.client = client; 
   		return(client); 
   	});
   ```

   You will commonly need to refer to a client later in your code, so assigning it to a variable is important. In the example above, after the client is created it is returned by `createClient()` and supplied to the chained `then()` function. It is then added to window as a member object. Adding
   `client` to window is not necessary, but doing so can make handling easier.
2. Assign the visual’s container HTML element to a JavaScript variable.

   ```
   var vizLocation = document.getElementById('visualization');
   ```
3. Prepare a data query to pass to the client’s `visualize()` member function. Alternately, you can pass a
   [query configuration object](https://devnet.logianalytics.com/hc/en-us/articles/4405851145879-Query-Configuration-Object). An example of a simple query configuration object follows.

   ```
   var queryConfig = {
   	tz: 'UTC'
   };
   ```

   For information about possible parameters for a query configuration object, see
   [*Query Configuration Object*](https://devnet.logianalytics.com/hc/en-us/articles/4405851145879-Query-Configuration-Object).
4. Render the visual using the client object’s `visualize()` member function.

   ```
   window.client.visualize({ 
   	element: vizLocation,
   	interactive: true, 
   	config: queryConfig, 
   	source: {name: 'Real Time Sales'}, 
   	visualization: 'Packed Bubbles', 
   	variables: { 
   		'Bubble Size': 'count', 
   		'Bubble Color': 'usersentiment:avg'
   	} 
   });
   ```

   In the example above:

   * The object passed to `visualize()` includes the `config` and
     `source` keys it needs to create a query configuration object. Instead of passing those keys, you can use a
     `query` key to pass a query. You must supply `visualize()` with either a query object or with the configuration parameters it needs to create a query. Either way, the client needs a query object to render a visual.
   * `interactive` is an optional boolean value that is used to control the interactivity of visuals. Some visuals offered by Composer or developed by your own engineers may not take this value into account. Each visual is different.
   * The `visualization` and `variables` keys specify the visual to be rendered and assign its variables, such as bar color or bubble size. The particular visual in the example does not use any variables.
5. The `visualize()` call is typically chained to the `createClient()` call using a
   `then()` function to prevent the browser from attempting to render the visual until after the client has finished initiating.
6. Typically `done()`, or `catch()` functions are chained to the call to add more robust handling. At a minimum, the visual should be assigned to a variable so that it can be accessed later.
