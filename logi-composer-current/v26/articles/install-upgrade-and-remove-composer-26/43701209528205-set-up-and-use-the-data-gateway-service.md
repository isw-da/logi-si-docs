---
title: "Set Up and Use the Data Gateway Service"
id: 43701209528205
section: "Install, Upgrade, and Remove Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701209528205-Set-Up-and-Use-the-Data-Gateway-Service
updated_at: 2026-05-29T14:09:28Z
---

# Set Up and Use the Data Gateway Service

# Set Up and Use the Data Gateway Service

Adding a data connector gateway to your Logi Composer environment allows you to connect securely to data outside of your environment. Use a gateway client to authenticate your connection and make the data available to users.

To establish communication between your data and Logi Composer, enable the data gateway service, SSL environment, then generate gateway clientes to retrieve your data from your external data bases, either on-premise or in the cloud.

After you've set up the data connector, users with appropriate privileges can access and use the data in source, visuals, and dashboards.

## Enable the Data Gateway Service

First, enable the data gateway service in your environment. You must be the default Admin user or a member of the Admin or Supervisors group.

**Important:** If you have not enabled SSL, do so before completing these steps. See [Enable Secure Sockets Layer](#Enable2).

* Logi Composer installed in a Linux or Windows environment:

  + Enable the data gateway in the zoomdata web service by including `data-gateway.client-api.enabled=true` in the properties file.
  + Add properties, if needed, to control resource consumption in `dataGatewayService` in the property file.
  + Start the service.
  + Logi Composer listens for the service on port 80.
* Logi Composer installed via Kubernetes:

  + Enable `dataGatewayService` (set to `true`) in the [values.yaml](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701110873869-Helm-Chart-for-Composer) for Logi Composer. See [Enable the Data Gateway](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701110873869-Helm-Chart-for-Composer#Enable).
  + Two services are added and exposed through the default [ingress](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701121221389-Ingress-Configuration) once you enable them:

    - `data-gateway-service-external` - looks externally to accept websocket connections
    - `data-gateway-service-internal` - looks internally to represent connecters inside the cluster
  + Start the service.

Once enabled, use the API to create data gateway clients, one for each connection you want to establish, using the `/api/data-gateway/clients` endpoint. Provide a name and description as needed. Logi Composer returns the client `id` and client `secret`, used to authenticate to Logi Composer.

API documentation is provided in your environment at this link: `https://<composer-URL>/composer/swagger-ui.html`.

### Use the Data Gateway Service

After enabling the data gateway service and creating one or more gateway clients, use credentials and the client id and client secret for each database to establish the connections from the database to Logi Composer.

### Manage Connectors

At some point, the connector shows up on the manage connector servers page. After that you can make a connection.

**Important:** Once established, data gateway connectors are available in all tenants to users with appropriate privileges who can create connectors. Limit access in a multi-tenant environment as needed.

See [Establish a Data Gateway Connection](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701128401421-Establish-a-Data-Gateway-Connection).

### Enable Secure Sockets Layer

If you have not enabled SSL, enable it now.

Set SSL to `true` through your preferred software, such as Spring Boot. Pass the key store and the key store password. Once complete, you can connect to the gateway service through a secured Websocket URL connection. Specify this setting as a parameter in the data gateway agent.
