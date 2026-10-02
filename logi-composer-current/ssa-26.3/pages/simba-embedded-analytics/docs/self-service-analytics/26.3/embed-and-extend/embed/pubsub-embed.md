> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Embed Cross-Visual Link Publish and Subscribe Settings Using JavaScript

Cross-visual link publish and subscribe settings for a dashboard can be specified for embedded dashboards using JavaScript. Two JavaScript methods are provided: `publish` and `subscribe`. After `embed.js` is run (see [Embed Components Using JavaScript and Trusted Access](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/embed/embed-javascript)), these methods become available for use with the global `Zoomdata` object on `window`.

Cross-visual links (channels) are used primarily for cross-visual filtering. Visuals can publish cross-visual filters for cross-visual links. Other visuals can listen (subscribe) to the links and apply them when a cross-visual filter is specified.

#### Prerequisites

Embedding applications should listen for the `composer-dashboard-loaded` event on the first embedded dashboard before calling these methods. See [Embedded Events](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/embed/embed-javascript-eventlisteners).

See the following topics:

* [Supported Zoomdata Methods](#supported-zoomdata-methods)
* [Supported Cross-Visual Publish JavaScript Properties](#supported-cross-visual-publish-javascript-properties)
* [Published Cross-Visual JavaScript Message Structure](#published-cross-visual-javascript-message-structure)
* [Supported Cross-Visual Subscribe JavaScript Properties](#supported-cross-visual-subscribe-javascript-properties)
* [Embedded Dashboard Cross-Visual Publish and Subscribe Example](#embedded-dashboard-cross-visual-publish-and-subscribe-example)

<h2 id="embedded-dashboard-cross-visual-publish-and-subscribe-example">
  Embedded Dashboard Cross-Visual Publish and Subscribe Example
</h2>

The following JavaScript example uses methods, properties, and embedded events of the `Zoomdata` and `EmbedManager` classes to publish and subscribe cross-visual links and filters in an embedded dashboard.

```javascript theme={null}
// EmbedManager is a singleton and `initComposerEmbedManager` can create a new
// manager or return an existing one. See other samples for howto properly
// initialize the embed manager.
const getEmbedManager = async () => window.initComposerEmbedManager();

// An embedding application should listen for the 'composer-dashboard-loaded'
// event before attempting to publish or subscribe. If multiple dashboards are
// added to the page, listeners can be added the object returned upon embedding
// to specifically target an individual dashboard
const DASHBOARD_LOADED_EVENT = 'composer-dashboard-loaded';
const pubSubReady = new Promise((resolve) => {
	function resolvePubSubReady() {
		resolve();
		document.removeEventListener(DASHBOARD_LOADED_EVENT, resolvePubSubReady);
	}
	document.addEventListener(DASHBOARD_LOADED_EVENT, resolvePubSubReady);
});

// `countrySelect` represents a drop-down field on the embedding application's
// page that lists a set of countries the user can filter by. After selecting a
// value, the embedding application calls its 'publishValue' function, defined
// below with the link name 'country' and the selected country value. The
// link name is defined in the dashboard. To clear the value filter, make sure
// you pass a null value as shown below.
const countrySelect = document.getElementById('country-select');
countrySelect.addEventListener('change', (event) => {
	const value = event.target.value;
	publishValue('country', value);
});

// The sample function publishValue below takes a link name and single string
// value and publishes the value on the link name. This causes all visuals on
// any loaded dashboards that are subscribed to the given link to filter
// themselves by the selected value. A visual can be set to subscribe to an
// arbitrary link name by adding a cross-source link using that link name and
// assigning any relevant field to that link.

// PUBLISHER_ID is an arbitrary string that subscribers can use to associate a
// message with who sent it.
const PUBLISHER_ID = 'Embedding Application';
async function publishValue(linkName, value) {
	const embedManager = await getEmbedManager();
	const message = {
		type: 'selection',
		valueType: 'ATTRIBUTE',
		ranges: [
			{
				operation: 'IN',
				value: value
			}
		]
	};
	const options = {
		publisherId: 'PUBLISHER_ID'
	};

	await pubSubReady;
	embedManager.publish(
		linkName,
		message,
		options
	);
}

// This sample function creates a subscription to the linkname provided using the
// handler provided. The returned unsubscribe function should be stored and
// called when the subscriber should stop receiving messages.
async function subscribe(linkname, handler) {
	const embedManager = await getEmbedManager();
	await pubSubReady;
	return embedManager.subscribe(linkname, handler);
}

// The following code provides an example of how to subscribe to a linkname on
// page load and receive the latest value published. It creates a simple alert
// popup on receipt of each message.
function subscriptionHandler(message, publisherId) {
	if (message === null) {
		alert(`${publisherId} cleared its publication`);
	} else {
		const value = message.ranges[0].value;
		alert(`${publisherId} published ${value}`);
	}
}
const countryUnsubscribe = subscribe('country', subscriptionHandler);
```

<h2 id="supported-zoomdata-methods">
  Supported `Zoomdata` Methods
</h2>

The following methods for the `Zoomdata` class can be used to manage embedded settings for published and subscribed cross-visual links in a dashboard. Sample code showing the use of these methods in an application are provided. See [Embedded Dashboard Cross-Visual Publish and Subscribe Example](#embedded-dashboard-cross-visual-publish-and-subscribe-example).

<table>
  <thead>
    <tr>
      <th>Method</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>`publish()`</td>

      <td>
        The `publish` method publishes a message (filter) for a specific cross-source or same-source link (channel). Publishing a link filter causes any subscribing handlers for the link to be called and passed the filter message. There is no registration process for a link, simply call the `publish` method with a link name and it will be created. No value is returned.

        <br />

        The filter message structure is described in [Published Cross-Visual JavaScript Message Structure](#published-cross-visual-javascript-message-structure).

        <br />

        The properties for the `publish` method are described in [Supported Cross-Visual Publish JavaScript Properties](#supported-cross-visual-publish-javascript-properties).
      </td>
    </tr>

    <tr>
      <td>`subscribe()`</td>

      <td>
        The `subscribe` method attaches a subscription handler to a cross-source or same-source link (filter). Each time a new cross-visual filter is published to the link, the subscription handler is called and passed the newly published filter.

        <br />

        When you call the `subscribe` method, the `unsubscribe` function is returned. Run the `unsubscribe` function to remove the handler for the link. This guarantees that the handler will no longer be notified when new messages are published for the link.

        <br />

        Messages passed on the channel can be an arbitrary message object or `null`. Because the message objects are not restricted, the subscription handler should never assume its structure and always check that the message is in the structure the handler is expecting.

        <br />

        Messages that are `null` are interpreted as a clearing of the channel and should be handled by undoing any actions taken based on the last messages received by the handler. For example, when a visual receives a `null` message in its filtering logic, it removes any filters created by previous messages on the given channel (link).

        <br />

        If a message is published to the channel before the `subscribe` method is called, the subscription handler is executed immediately with the latest message that was published on the channel.

        <br />

        The properties for the `subscribe` method are described in [Supported Cross-Visual Subscribe JavaScript Properties](#supported-cross-visual-subscribe-javascript-properties).
      </td>
    </tr>
  </tbody>
</table>

<h2 id="supported-cross-visual-publish-javascript-properties">
  Supported Cross-Visual Publish JavaScript Properties
</h2>

The properties for the `publish` method of the `Zoomdata` class are described in the following table.

<table>
  <thead>
    <tr>
      <th>Property/Object</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>`<linkName>`</td>

      <td>
        The link (channel) name. Link names can be custom names, specified when a cross-source link is created, or names in the format `<source-name>.<field-name>`, automatically generated for every field in a data source for same-source links.

        <br />

        The link name is defined when you define a cross-source link. See [Define Cross-Source Links](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/using-cross-source-links#define-cross-source-links). It is published for use by a dashboard as a cross-visual filter. See [Publish a Link](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/published-enable). The link name represents the channel into which the message should be published. It is typically called a *topic* in standard publish/subscribe systems.

        <br />

        <Warning>
          There is a one-to-one relationship between cross-source link names and your data fields. You cannot use the same link name for multiple data fields. In addition, you cannot create multiple cross-source links for the same data field.
        </Warning>

        <br />

        Type: string
      </td>
    </tr>

    <tr>
      <td>`<message>`</td>

      <td>
        The message sent with the link. The message published can either be an arbitrary object or null. An object published to a link channel is not restricted to any particular structure but a Self-Service Analytics dashboard only recognizes messages in the structure described in [Published Cross-Visual JavaScript Message Structure](#published-cross-visual-javascript-message-structure).

        <br />

        Publishing a null message can clear the last published message from the channel. If the last published message's `publisherId` matches the null message's `publisherId`, the last message is removed from the channel and subscribers receive a null message. If the `publisherId` of the last published message on the channel does not match the null message's `publisherId`, nothing happens.

        <br />

        The most recently published message on each channel is stored and sent to new subscribers at the time of subscription.

        <br />

        Type: object or null
      </td>
    </tr>

    <tr>
      <td>`<options>`</td>

      <td>
        Options for how the link should be applied. All values are optional. Options include:

        <br />

        * `options.publisherId`: An arbitrary sting identifying the publisher of the link. This can be used to handle subscriptions differently based on publisher. For example, a subscriber may decide not to apply messages they posted themselves.
        * `options.timestamp`: A number representing the time at which the link is published. It defaults to `Date.now()`.
        * `options.targetComponents`: A string that allows the publisher to target only specific dashboards when more than one dashboard is embedded on a page. If not provided, it applies the link to all embedded dashboards. To target a component, add its `componentInstanceId` (provided in the return from the call to `embedManager.createComponent`).

        <br />

        Type: object
      </td>
    </tr>
  </tbody>
</table>

<h2 id="published-cross-visual-javascript-message-structure">
  Published Cross-Visual JavaScript Message Structure
</h2>

All messages (cross-visual filters) that can be consumed by Self-Service Analytics or that will be published by Self-Service Analytics must conform to the following structure. The value of the `type` property defines the structure of the rest of the message.

The properties for the message (filter) structure are described in the following table:

<table>
  <thead>
    <tr>
      <th>Property</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>`type: 'selection'`</td>

      <td>
        Only a value of `selection` is supported at this time, identifying a selection of values on a visual or widget. This signifies that the message is a `SelectionMessage`.

        <br />

        Type: string
      </td>
    </tr>

    <tr>
      <td>`valueType: 'NUMBER'`</td>

      <td>
        Identifies the type of value being selected. The following value types are supported:

        <br />

        * ATTRIBUTE - Use for string values
        * NUMBER - Use for integer and floating point values
        * TIME - Use for date and date-time values

        <br />

        Type: string
      </td>
    </tr>

    <tr>
      <td>`ranges`</td>

      <td>
        An array of selected ranges. The set of allowed operations depends on the specified `valueType`. Currently only a single range is supported per message (filter). Ranges after the first range will be ignored. Ranges should be structured as follows:

        <br />

        ```
        ranges: [
           {
              operation: '<operation>',
              value: '<value>'
           },
        ]
        ```

        <br />

        The `operation` and `value` properties are described next.

        <br />

        Type: array
      </td>
    </tr>

    <tr>
      <td>`operation: 'EQUALS'`</td>

      <td>
        The filter operation. Supported operations include:

        <br />

        * `IN` - Includes. Supported for ATTRIBUTE and NUMBER `valueType`s. Provide an array of values for `value`.
        * `NOTIN` - Excludes. Supported for ATTRIBUTE and NUMBER `valueType`s. Provide an array of values for `value`.
        * `BETWEEN` - Between. Supported for NUMBER or TIME `valueType`s. Provide a two-item array of the start and end values for `value`.
        * `GT` - Greater Than. Supported for NUMBER or TIME `valueType`s. Provide a single value to compare against for `value`.
        * `GE` - Greater Than or Equal To. Supported for NUMBER or TIME `valueTypes`s. Provide a single value to compare against for `value`.
        * `EQUALS` - Equal To. Supported for NUMBER or TIME `valueTypes`s. Provide a single value to compare against for `value`.
        * `NOTEQUALS` - Not Equal To. Supported for NUMBER or TIME `valueTypes`s. Provide a single value to compare against for `value`.
        * `LE` - Less Than or Equal To. Supported for NUMBER or TIME `valueTypes`s. Provide a single value to compare against for `value`.
        * `LT` - Less Than. Supported for NUMBER or TIME `valueTypes`s. Provide a single value to compare against for `value`.

        <br />

        Type: string
      </td>
    </tr>

    <tr>
      <td>`value: '6'`</td>

      <td>
        Provide a value as described for each filter `operation`.

        <br />

        Type: string, number, array\<string | number | null>
      </td>
    </tr>
  </tbody>
</table>

<h2 id="supported-cross-visual-subscribe-javascript-properties">
  Supported Cross-Visual Subscribe JavaScript Properties
</h2>

The properties for the `subscribe` method of the `Zoomdata` class are described in the following table.

<table>
  <thead>
    <tr>
      <th>Property/Object</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>`<linkName>`</td>

      <td>
        The link (channel) name to which the subscription handler should subscribe.

        <br />

        The link name is defined when you define a cross-source link. See [Define Cross-Source Links](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/using-cross-source-links#define-cross-source-links). It is published for use by a dashboard as a cross-visual filter. See [Publish a Link](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/published-enable). The link name represents the channel from which the message should be subscribed. It is typically called a *topic* in standard publish/subscribe systems.

        <br />

        <Warning>
          There is a one-to-one relationship between cross-source link names and your data fields. You cannot use the same link name for multiple data fields. In you cannot create multiple cross-source links for the same data field.
        </Warning>

        <br />

        Type: string
      </td>
    </tr>

    <tr>
      <td>`subscriptionHandler`</td>

      <td>
        The handler that will be called upon new messages. This handler will be provided with the published message as the first argument and the ID of the publisher as the second argument.

        <br />

        Type: function
      </td>
    </tr>
  </tbody>
</table>
