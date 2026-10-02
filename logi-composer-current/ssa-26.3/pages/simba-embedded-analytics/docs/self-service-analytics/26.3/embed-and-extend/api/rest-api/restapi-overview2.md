> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# REST API Overview

The REST API provides methods for retrieving, updating, and deleting metadata pertaining to accounts, connections, and users.

API documentation is provided in your environment at this link: `https://<Self-Service Analytics-URL>/composer/swagger-ui.html`.

<Warning>
  Some API endpoints are marked as `experimental` in the Swagger documentation we provide. These endpoints are in the early stages of design and are subject to change. We make no commitment to their stability and may remove them without notice. These experimental endpoints are not recommended for use in production.
</Warning>

This topic describes the following REST API topics:

* [Authentication](#authentication)
* [Version Compatibility](#version-compatibility)
* [HATEOAS Architecture](#hateoas-architecture)
* [API Entry Point](#api-entry-point)
* [The /api/ Path](#the-api-path)
* [Optimistic Locking on PATCH Calls](#optimistic-locking-on-patch-calls)
* [Reference Documentation](#reference-documentation)

<h2 id="authentication">
  Authentication
</h2>

The API currently uses basic access authentication. Most actions require admin-level access to the particular account manipulated using the API.

<h2 id="version-compatibility">
  Version Compatibility
</h2>

Each version of the API maintains backward compatibility with previous versions. The HTTP Accepts/Content-type header is used to specify the version for the resources that are produced and used by the API. When sending data to or receiving data from the API, you must use the appropriate HTTP header.

When working with the API, you should explicitly set the version of the API that you want to use. For example, in cURL requests, you would include the `--header` parameter as shown below.

```
# For submitting data
curl --header "Content-type: application/vnd.composer.v3+json" ...
# Consuming data
curl --header "Accept: application/vnd.composer.v3+json,application/vnd.composer+json" ...
```

To ensure you always use the latest version of Self-Service Analytics, use the generic media type: `application/vnd.composer+json`.

<Note>
  There is a risk associated with using this generic media time to ensure you always use the latest version. Because this approach does not tie calls to specific API versions, if the latest version changes, your integration may break. It is safer to tie your API calls to specific versions.
</Note>

The current API media type version will be sent as a header, `X-composer-Media-Type`, in the response to every API request.

The rule for specifying media types is simple. Always include the generic media type `application/vnd.composer+json`and, if you specify a particular version, always put it first. For example:

* Correct: `application/vnd.composer.v3+json,application/vnd.composer+json`
* Incorrect: `application/vnd.composer+json, application/vnd.composer.v3+json`

<h2 id="hateoas-architecture">
  HATEOAS Architecture
</h2>

The API implements the HATEOAS architectural pattern. Most resources returned by the API have a `links` element. The links elements is an array of objects, each with two properties:

* `rel`: short description of how this link relates to the parent object
* `href`: the actual link value

Every resource will at least have a `rel: "self"` link, which is the canonical reference to that object. You can use the other links to explore the relations of a given object, for example, the users in a tenant or the sources tied to a connection.

<h2 id="api-entry-point">
  API Entry Point
</h2>

The initial entry point to the API is `http://<host>:<port>/<context>/api`. For example:

```
http://localhost:8080/Self-Service Analytics discovery/api
```

This URL points to the root API resources that you can use to browse through the API.

<h2 id="the-api-path">
  The /api/ Path
</h2>

Some functions of the Self-Service Analytics client application call APIs using a `/api/` path. Except where noted in the developer documentation, endpoints that use the `/api/` path are for insightsoftware's internal use only.

<Note>
  Applications built with Self-Service Analytics's internal-use APIs, are subject to a high risk of unexpected breakage.
</Note>

APIs on the `/api/` path that are safe to use include, for example, the `/api/sources/key` endpoint.

<h2 id="optimistic-locking-on-patch-calls">
  Optimistic Locking on PATCH Calls
</h2>

API data source PATCH calls use optimistic locking to ensure the PATCH is applied to the most recent records. A `version` parameter is used in these calls to track the version counter number. If this counter is not incremented in the payload of the call or if it is in error, the PATCH call will fail with an error similar to this:

```yaml theme={null}
"details": "Source Epsilon Impala API Update Test has been updated since last read. Refresh required",
"error": "INTERNAL_ERROR"
```

The exact and correct version counter number must be used or the API call will fail. For example, if you just submitted a PATCH call using version 8 and your next PATCH call uses version 10, you will receive an error response.

Consequently, prior to any PATCH call, be sure you do one of the following things:

* Perform a GET call immediately prior to the PATCH call to retrieve the latest version counter number. This is the recommended approach.
* If no changes have been made using the UI, and you can safely remember the version counter number of the previous call after every successful PATCH call, simply increment the version counter number in your newest PATCH call.

<h2 id="reference-documentation">
  Reference Documentation
</h2>

insightsoftware maintains Swagger-based reference materials for the Self-Service Analytics REST APIs. In this testing environment, you can experiment with the APIs features.

API documentation is provided in your environment at this link: `https://<Self-Service Analytics-URL>/composer/swagger-ui.html`.

<Warning>
  Some API endpoints are marked as `experimental` in the Swagger documentation we provide. These endpoints are in the early stages of design and are subject to change. We make no commitment to their stability and may remove them without notice. These experimental endpoints are not recommended for use in production.
</Warning>

<h2 id="cautionary-note-about-internal-apis">
  Cautionary Note About Internal APIs
</h2>

Self-Service Analytics offers a number of REST APIs so you can extend and embed Self-Service Analytics in your own custom applications. These APIs are denoted as publicly available using the `/api/` path.

API documentation is provided in your environment at this link: `https://<Self-Service Analytics-URL>/composer/swagger-ui.html`.

## Manage Connectors with REST APIs

The administrative REST APIs enable developers to manage connectors, connections, and data sources. The data connectivity with data stores is organized in these segments, illustrated below.

<img src="https://mintcdn.com/insightsoftware/2cXq_sDOxrDVXUcv/simba-embedded-analytics/docs/self-service-analytics/26.3/images/api/api-connection-dialog.png?fit=max&auto=format&n=2cXq_sDOxrDVXUcv&q=85&s=23c885914421f2d1e0bc61cdb646da1d" alt="" width="1309" height="388" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/api/api-connection-dialog.png" />

There are two basic parts to the connectivity process. They are listed below along with the REST endpoints used to manage them.

* [Self-Service Analytics registers a connector](#registering-self-service-analytics-with-a-connector-server), that is a *connector server* from which it requests data. Registering a connector server involves the following REST endpoints:

  * `/api/connector-server/` - Use this endpoint to manage the Self-Service Analytics object that provides HTTP connectivity information about the connector server
  * `/api/connectors/` - Use this endpoint to list functioning connector servers to validate that Self-Service Analytics has registered the connector server
  * `/api/connection-type/` - Use this endpoint to manage the object that holds the data store parameters and connection parameters that the connector server needs to connect to a data store. This information commonly includes minimum and maximum supported version and connection parameters such as authentication information. A connection-type corresponds to an icon in the administrator's Sources page and makes it possible for end users to provide login credentials and make a data source from a data store.

* [The connector server connects to a *data store*](#connecting-to-a-data-store) such as a database, or file upload to create a subset of data called a *data source*. That data source serves as a source of data for end users to use with visuals. Connecting to a data store involves the following REST endpoints:

  * `/api/connections/` - Use this endpoint to provide required parameters, often login credentials, that a connector server uses to access a data store following parameters set by the connection-type.
  * `/api/sources/{id}` - Use this endpoint to create a data source using a connection to a data store. End users can see the date in this data source using visuals.

<h3 id="registering-self-service-analytics-with-a-connector-server">
  Registering Self-Service Analytics with a Connector Server
</h3>

Before Self-Service Analytics can use a connector server, it must register the connector server. Unless connector microservice discovery is turned off, Self-Service Analytics automatically discovers preinstalled connector servers when Self-Service Analytics is started up.

Self-Service Analytics does not automatically discover custom-built connector servers. You can use the Self-Service Analytics client application to manually register a connector server, or you can do so using REST APIs. For more information about using the Self-Service Analytics client application to register a connector server, see Configuring a New Connector Manually.

<h4 id="using-rest-apis-to-register-a-self-service-analytics-connector">
  Using REST APIs to Register a Self-Service Analytics Connector Server
</h4>

Before Self-Service Analytics can access a connector server, the connector server must be registered with Self-Service Analytics. If automatic discovery does not work, then you must do this process manually using either the client application or using APIs. Registering a connector server requires providing the information needed to connect with and understand the connector server. Use the following steps to register a connector server using the provided APIs.

API documentation is provided in your environment at this link: `https://<Self-Service Analytics-URL>/composer/swagger-ui.html`.

**To register a connector server with Self-Service Analytics:**

1. Provide the server with the information that it needs to connect to the connector server using the POST method with the `/api/connector-servers/` endpoint. Of the body parameters listed in the reference documentation, the following are required:

   ```json theme={null}
   {
   	"name": "<myDB Connector Server>",
   	"protocol": "<HTTP>"
   	"connectionParameters": {
   		"HTTP_URL": "<yourdbURLhere>"
   	},
   }
   ```

   in which:

   * `name` should be unique and easily remembered.
   * `protocol` should be set as `HTTP`. It is set as DISCOVERY or CORE if the connector was automatically discovered or built into Self-Service Analytics. If you do manual API-based registering, use HTTP.
   * `HTTP_URL` should be set to the URL used to access the connector server.

2. After connector server discovery has detected and registered a connector server, or after you have manually registered the connector server using the `/api/connector-servers/` endpoint, Self-Service Analytics can validate that the connector server is registered by using the `/api/connectors/` endpoint.

   The API returns a dynamically generated list of all registered connectors.

3. Provide additional connection parameters using the POST method with the `/api/connection-types/`endpoint.

   ```json theme={null}
   {
   	"name": "<mySQL Connector>",
   	"storageType": "MYSQL"
   }
   ```

   in which:

   * `name` is a string by which the connection type is to be identified by the end user on the Sources page. There may be more than one connection type (configuration) for how each connector is used. End users see each of these as a distinct type of connector, so the best practice is to name it as if it were a distinction connector.

     For example, you might make two different connection types to access a MySQL database using your MySQL connector server.

     One connection type might be low-security, using generic credentials for all users. The other connection type might require a user to provide specific, personal credentials that the connector server then passes along to the MySQL database to access specific data available only to that person. The two connection types, show up as two distinct connectors when a user creates a source, name, for example, "All-company MySQL Connector" and "Employee-specific MySQL Connector".

   * `storageType` corresponds to the `storageType` returned by a connector server when it is asked to describe the database to which is connects. The storage types available via a particular connector server can be found by making a GET call to `/api/connector-servers/{connector-server-id}/connection-types`.

4. Optionally, provide a custom icon to denote the new connection type using the `/api/connection-types/{id}/icon/` endpoint. The endpoint expects one `formData` parameter - the icon image. It should be a 72 x 72 image in the form of either an SVG string or a PNG file in base 64 format.

<h3 id="connecting-to-a-data-store">
  Connecting to a Data Store
</h3>

After the connector server is registered with Self-Service Analytics and one or more connection types have been defined, you can use the connector server to connect to a data store and create a data source.

1. Create a connection via the connector server to a data store by using the POST method with the `/api/{accountId}/connections/` endpoint.

   The response object includes the ID of the created connection at `theResponseObject.links[0].href`. This value is a string representation of a URL, the last component of which is the id of the object itself. For instance, in `https://<Self-Service Analytics-URL>/composer/api/connections/58176703e4b06f699c7c70ca` the ID of the object is `58176703e4b06f699c7c70ca`.

   You can also modify an existing connection by using PUT with the `/api/connections/{id}/` endpoint. The parameters required by these endpoint are conditioned by the configuration provided by `/api/connection-type/`.

   ```json theme={null}
   { "name": "ES Test Connection", "connectorName": "elasticsearch", "connectorParameters": [{...}, {...}, ...] }
   ```

   in which:

   * `name` is the name of the connection.

   * `connectorName` is the name of the connector used to make the connection.

   * `connectorParameters` is an object of connector parameters as key-value pairs. For example:

     ```json theme={null}
     { "enableSsl": "false", "port": "9200", "clusterName": "es", "host": "10.2.2.129", "transportType": "http" }
     ```

     Connector parameters are different for each connector. Connector servers present these requirements when they are discovered by Self-Service Analytics. The `connectorParameters` can be identified by calling `/api/connection-types` and finding the `parameters` object for the appropriate `storageType`.

     <Note>
       Self-Service Analytics periodically introduces or deprecates connector servers. For information about the current status of a particular connector server, see [Create and Manage Data Store Connections](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connections-managing).
     </Note>

   * `sourceParameters` and `impersonationParameters` may also be required for a particular connection. This information can be found using the approach used to discover `connectorParameters`.

2. Create a data source, that is, a subset of data from a data store, by using POST with the endpoint `/api/connections/{connectionId}/sources/`. Required parameters for the source are listed below.

   ```json theme={null}
   { "name": "string", "sourceParameters": {...}, }
   ```

   in which:

   * `name` is the name of the new data source (subset of data from a data store)
   * `sourceParameters` is an object containing the parameters required to create a source on its particular kind of connection, connector, and data store.

   The key-value pairs required for the `sourceParameters` object are defined by the `sourceParameters` array included in the `connectors` object returned by making a GET call to `/api/connectors`. In the sourceParameters array, each object defines a key-value pair for the `sourceParameters` object required to create a source. For example, the `sourceParameters` definition in this array defines a `sourceParameters` object that requires an `index`, a `mapping`, and a `patternType`:

   ```yaml theme={null}
   "sourceParameters": [
      {"name": "index",
       "description": "Comma-separated list of index names or patterns",
       "required": true },
      {"name": "mapping",
       "description": "Comma-separated mapping types list",
       "required": false },
      {"name": "patternType",
       "description": "Type of index pattern. Can either be dynamic or time-based",
       "required": false }
   ]
   ```

   That definition would be satisfied by the `sourceParameters` object below, which could be used to create a source using the `/api/connections/{connectionId}/sources` API.

   ```yaml theme={null}
   "sourceParameters": { "index": "the-requests", "mapping": "", "patternType": "" }
   ```

<h2 id="configure-data-source-refresh-rates-using-the-api">
  Configure Data Source Refresh Rates Using the API
</h2>

You can modify source refresh rates using Self-Service Analytics's REST APIs. Only live data sources have refresh rates. Consequently, you can only modify the refresh rate of a live data source.

### Identify Current Refresh Rates

You can identify whether a data source is live and, if so, what its current refresh rate is using `curl` or another HTTP utility or library to make the following call:

```bash theme={null}
   curl --user <name>:<password> -X GET 'https://<yourserver_path>/api/sources/<123456789>
' -H "Content-Type: application/vnd.composer.v3+json;"
```

in which:

* `<name>` and `<password>` are the name and password with authorization to request information about the source
* `<yourserver_path>` is the DNS and path for your Self-Service Analytics server
* `<123456789>` is replaced with the sourceID that contains the source that you wish to inspect

The source configuration object returned by this method includes the follow keys:

```yaml theme={null}
"live": true
"liveRefreshRate": 1
"name": "SOURCE_NAME",
"sourceParameters": {
"PARAM": "PARAMVAL"
},
```

The `live` key indicates whether the data source is live (also known as streaming or real-time).

The `liveRefreshRate` key indicates the refresh frequency of the data source. Note that this frequency has no predefined units. The units are supplied by the granularity of the source's data. For example, if granularity is *hour*, then a refresh rate of 3 indicates a refresh every three hours.

Make note of the `name` and `sourceParameters` keys because they must be included in the PUT method used to modify the refresh rate.

### Modify the Source Refresh Rate

You can modify a live data source's refresh rate using cURL or another HTTP utility or library to make the following call:

```bash theme={null}
curl --user <name>:<password> -X PUT -d '{"liveRefreshRate": <ratenum>, "name": "<NAME>", "sourceParameters": {"<PARAM>": "<PARAMVAL>"}}'
'https://<yourserver_path>/api/sources/<123456789>' -H "Content-Type: application/vnd.composer.v3+json;"
```

in which:

* `<name>` and `<password>` are the name and password with authorization to modify the source
* `<ratenum>` is replaced with the refresh rate that you wish to use for the source
* `<yourserver_path>` is the DNS and path for your Self-Service Analytics server
* `<123456789>` is replaced with the sourceID that contains the source that you wish to inspect
* `<name>` is replaced with the name of the data source as discovered in the GET method detailed above
* `<PARAM>` and `<PARAMVAL>` are replaced with the actual values of `<sourceParameters>` as discovered in the GET method detailed above

The method returns the updated source object or an error message if the operation fails.

## Manage the Upload API Source

Self-Service Analytics supports live streaming sources. This source uses PostgreSQL as a storage medium for the incoming data flow. By default, Self-Service Analytics uses PostgreSQL to store the data for Upload API. This PostgreSQL instance is separate from other PostgreSQL instances you may have in existence. You can elect to use another PostgreSQL instance that you may have by changing the configuration properties.

### Before You Begin

If you want to use an existing PostgreSQL instance in conjunction with the Upload API microservice, you need to find the above information in your `edc-postgresql.properties` file.

### Use Another PostgreSQL Instance for Upload API

1. Use the following command to access and open the properties file:

2. Add the following parameters to the file:

   ```properties theme={null}
   #  that are configured for Upload API
   upload.destination.params.user_name=yourusername
   upload.destination.params.password=yourpassword
   upload.destination.params.jdbc_url=jdbc:postgresql://yourlocalhost:yourport//zd_upload
   upload.batch-size=1000
   ```

3. Save and exit the configuration file.

4. Restart the Self-Service Analytics server.
