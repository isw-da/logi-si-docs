> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Establish a Data Gateway Connection

Once you or your system administrator has [enabled the data gateway](#enable-the-data-gateway-service) and [added a connector](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connectors-ov#define-a-new-connector), you can make a [connection](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connections-managing#add-data-store-connections) your users can select when creating a new data source.

Users will see the news connector as an option during source creation, and can simply select it as they would any other source. See [Define a Source](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-overview#define-a-source).

<Note>
  You are not prompted for credentials when you create a connection: they were provided as part of defining the connector.
</Note>

<h2 id="set-up-and-use-the-data-gateway-service">
  Set Up and Use the Data Gateway Service
</h2>

Adding a data connector gateway to your environment allows you to connect securely to data outside of your environment. Use a gateway client to authenticate your connection and make the data available to users.

To establish communication between your data and Self-Service Analytics, enable the data gateway service, SSL environment, then generate gateway clients to retrieve your data from your external data bases, either on-premise or in the cloud.

After you have set up the data connector, users with appropriate privileges can access and use the data in source, visuals, and dashboards.

<h2 id="enable-the-data-gateway-service">
  Enable the Data Gateway Service
</h2>

First, enable the data gateway service in your environment. You must be the default Admin user or a member of the Admin or Supervisors group.

<Warning>
  If you have not enabled SSL, do so before completing these steps. See [Enable Secure Sockets Layer](#enable-secure-sockets-layer).
</Warning>

* Self-Service Analytics installed in a Linux or Windows environment:

  * Enable the data gateway in the zoomdata web service by including `data-gateway.client-api.enabled=true` in the properties file.
  * Add properties, if needed, to control resource consumption in the `dataGatewayService` property file.
  * Start the service.
  * Self-Service Analytics listens for the service on port 80.

* Logi Composer installed via Kubernetes:

  * Enable `dataGatewayService` (set to `true`) in the [values.yaml](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/kubernetes-ov#helm-chart-for-self-service-analytics) for Self-Service Analytics. See [Enable the Data Gateway](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/kubernetes-ov#enable-the-data-gateway).

  * Two services are added and exposed through the default [ingress](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/kubernetes-ov#ingress-configuration) once you enable them:

    * `data-gateway-service-external` - looks externally to accept websocket connections
    * `data-gateway-service-internal` - looks internally to represent connecters inside the cluster

  * Start the service.

Once enabled, use the API to create data gateway clients, one for each connection you want to establish, using the `/api/data-gateway/clients` endpoint. Provide a name and description as needed. Self-Service Analytics returns the client `id` and client `secret`, used to authenticate to Self-Service Analytics.

API documentation is provided in your environment at this link: `https://<Self-Service Analytics-URL>/composer/swagger-ui.html`.

### Use the Data Gateway Service

After enabling the data gateway service and creating one or more gateway clients, use credentials and the client id and client secret for each database to establish the connections from the database to Simba Self-Service Analytics.

### Manage Connectors

At some point, the connector shows up on the manage connector servers page. After that you can make a connection.

<Warning>
  Once established, data gateway connectors are available in all tenants to users with appropriate privileges who can create connectors. Limit access in a multi-tenant environment as needed.
</Warning>

<h3 id="enable-secure-sockets-layer">
  Enable Secure Sockets Layer
</h3>

If you have not enabled SSL, enable it now.

Set SSL to `true` through your preferred software, such as Spring Boot. Pass the key store and the key store password. Once complete, you can connect to the gateway service through a secured Websocket URL connection. Specify this setting as a parameter in the data gateway agent.
