---
title: "Manage Connectors with REST APIs"
id: 4405850880023
section: "Composer v6 Developer Tools"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405850880023-Manage-Connectors-with-REST-APIs
updated_at: 2021-09-21T01:26:43Z
---

# Manage Connectors with REST APIs

# Manage Connectors with REST APIs

The administrative REST APIs enable developers to manage connectors, connections, and data sources. Composer's data connectivity with data stores is organized in these segments, illustrated below.

![](https://devnet.logianalytics.com/hc/article_attachments/4406747455767/api-connection-dialog_389x129.png)

There are two basic parts to the connectivity process. They are listed below along with the REST endpoints used to manage them.

* [Composer registers a connector](#Registering), that is a *connector server* from which it requests data. Registering a connector server involves the following REST endpoints:

  + `/api/connector-server/` - Use this endpoint to manage the Composer object that provides HTTP connectivity information about the connector server
  + `/api/connectors/` - Use this endpoint to list functioning connector servers to validate that Composer has registered the connector server
  + `/api/connection-type/` - Use this endpoint to manage the object that holds the data store parameters and connection parameters that the connector server needs to connect to a data store. This information commonly includes minimum and maximum supported version and connection parameters such as authentication information.
    A connection-type corresponds to an icon in the administrator's Sources page and makes it possible for end users to provide login credentials and make a data source from a data store.
* [The connector server connects to a *data store*](#Connecting) such as a database, flat file, or data API to create a subset of data called a *data source*. That data source serves as a source of data for end users to use with visuals. Connecting to a data store involves the following REST endpoints:

  + `/api/connections/` - Use this endpoint to provide required parameters, often login credentials, that a connector server uses to access a data store following parameters set by the connection-type.
  + `/api/sources/{id}` - Use this endpoint to create a data source using a connection to a data store. End users can see the date in this data source using visuals.

## Registering Composer with a Connector Server

Before Composer can use a connector server, it must register the connector server. Unless connector microservice discovery is turned off, Composer automatically discovers preinstalled connector servers when Composer is started up. Composer does not automatically discover custom-built connector servers. You can use the Composer client application to manually register a connector server, or you can do so using REST APIs. For more information about using the Composer client application to register a connector server, see
Configuring a New Connector Manually.

### Using REST APIs to Register a Composer Connector Server

Before Composer can access a connector server, the connector server must be registered with Composer. If automatic discovery does not work, then you must do this process manually using either the Composer client application or using APIs. Registering a connector server requires providing Composer with the information that it needs to connect with and understand the connector server. Use the following steps to register a connector server using Composer's REST APIs.

**To register a connector server with Composer:**

1. Provide the Composer server with the information that it needs to connect to the connector server using the POST method with the
   `/api/connector-servers/` endpoint. Of the body parameters listed in the reference documentation, the following are required:

   ```
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
   * `protocol` should be set as `HTTP`. It is set by Composer as DISCOVERY or CORE if the connector was automatically discovered or built into Composer. If you do manual API-based registering, use HTTP.
   * `HTTP_URL` should be set to the URL used to access the connector server.
2. After connector server discovery has detected and registered a connector server, or after you have manually registered the connector server with Composer using the
   `/api/connector-servers/` endpoint, Composer can validate that the connector server is registered by using the `/api/connectors/` endpoint.

   The API returns a dynamically generated list of all registered connectors.
3. Provide additional connection parameters to Composer using the POST method with the `/api/connection-types/`endpoint.

   ```
        {
             "name": "<mySQL Connector>",
             "storageType": "MYSQL"
             }
   ```

   in which:

   * `name` is a string by which the connection type is to be identified by the end user on the Sources page. There may be more than one connection type (configuration) for how each connector is used. End users see each of these as a distinct type of connector, so the best practice is to name it as if it were a distinction connector. For example, you might make two different connection types to access a MySQL database using your MySQL connector server. One connection type might be low-security and use generic credentials for all users. The other connection type might require a user to provide specific, personal credentials that the connector server then passes along to the MySQL database to access specific data available only to that person. As such, the two connection types, showing up as two distinct connectors when a user creates a source, might be called "All-company MySQL Connector" and "Employee-specific MySQL Connector".
   * `storageType` corresponds to the `storageType` returned by a connector server when it is asked to describe the database to which is connects. The storage types available via a particular connector server can be found by making a GET call to `/api/connector-servers/{connector-server-id}/connection-types`.
4. Optionally, provide a custom icon to denote the new connection type using the
   `/api/connection-types/{id}/icon/` endpoint. The endpoint expects one formData parameter - the icon image. It should be a 72 x 72 image in the form of either an SVG string or a PNG file in base 64 format.

## Connecting to a Data Store

After the connector server is registered with Composer and one or more connection types have been defined, you can use the connector server to connect to a data store and create a data source.

1. Create a connection via the connector server to a data store by using the POST method with the
   `/api/{accountId}/connections/` endpoint.

   The response object includes the ID of the created connection at
   `theResponseObject.links[0].href`. This value is a string representation of a URL, the last component of which is the id of the object itself. For instance, in
   `https://latest.logianalytics.com/composer/api/connections/58176703e4b06f699c7c70ca` the ID of the object is
   `58176703e4b06f699c7c70ca`.

   You can also modify an existing connection by using PUT with the `/api/connections/{id}/` endpoint. The parameters required by these endpoint are conditioned by the configuration provided by
   `/api/connection-type/`.

   ```
        {
            "name": "ES Test Connection",
            "connectorName": "elasticsearch",
            "connectorParameters": [{...}, {...}, ...]
            }
   ```

   in which:

   * `name` is the name of the connection.
   * `connectorName` is the name of the connector used to make the connection.
   * `connectorParameters` is an object of connector parameters as key-value pairs. For example:

     ```
            {
                  "enableSsl": "false",
                  "port": "9200",
                  "clusterName": "es",
                  "host": "10.2.2.129",
                  "transportType": "http"
                  }
     ```

     Connector parameters are different for each connector. Connector servers present these requirements when they are discovered by Composer. The `connectorParameters` can be identified by calling
     `/api/connection-types` and finding the `parameters` object for the appropriate `storageType`.

     ![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg) Composer periodically introduces or deprecates connector servers. For information about the current status of a particular connector server, see [*Manage Connectors and Connector Servers*](https://devnet.logianalytics.com/hc/en-us/articles/4405859186199-Manage-Connectors-and-Connector-Servers).
   * `sourceParameters` and `impersonationParameters` may also be required for a particular connection. This information can be found using the approach used to discover `connectorParameters`.
2. Create a data source, that is, a subset of data from a data store, by using POST with the endpoint `/api/connections/{connectionId}/sources/`. Required parameters for the source are listed below.

   ```
        {
             "name": "string",
             "sourceParameters": {...},
             }
   ```

   in which:

   * `name` is the name of the new data source (subset of data from a data store)
   * `sourceParameters` is an object containing the parameters required to create a source on its particular kind of connection, connector, and data store.

   The key-value pairs required for the `sourceParameters` object are defined by the `sourceParameters` array included in the `connectors` object returned by making a GET call to `/api/connectors`. In the sourceParameters array, each object defines a key-value pair for the `sourceParameters` object required to create a source. For example, the `sourceParameters` definition in this array defines a `sourceParameters` object that requires an `index`, a `mapping`, and a `patternType`:

   ```
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

   ```
        "sourceParameters": {
             "index": "the-requests",
             "mapping": "",
             "patternType": ""
             }
   ```
