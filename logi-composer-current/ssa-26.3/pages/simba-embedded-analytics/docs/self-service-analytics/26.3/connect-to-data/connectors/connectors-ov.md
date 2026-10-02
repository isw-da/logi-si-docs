> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Connect Self-Service Analytics to Data Stores

Simba Self-Service Analytics connects to your external data stores through connectors. These connectors are integrations for a specific data store type—SQL databases, cloud platforms, APIs, streaming sources, and more.

Connector servers and the connector microservice support the connectors in your environment. Use these active connectors to create connections for your users. Users can then access those connections to develop data sources to create visuals, dashboards, and self service reports.

Several connectors are included in the default installation, and additional connectors are available. If the connector you are looking for is not shown, it may be because:

* The connector is installed but is not enabled. For more information, see [Manage Connectors and Connector Servers](#manage-connectors-and-connector-servers).
* The connector was not installed and needs to be downloaded separately. For more information, see [Obtain Additional Connector Servers](#obtain-additional-connector-servers).
* The connector requires you to provide a licensed JDBC driver. For more information, see [Add a JDBC Driver](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/install-ov#add-a-jdbc-driver).

Certain connectors require a JDBC driver, which is obtained through a separate download. This allows you to select and add a driver that meets your operation needs or policies.

To connect to a data store and use its data in a visual, you must first verify that a connector and its connector server have been defined in Self-Service Analytics for the data store. See [Manage Connectors and Connector Servers](#manage-connectors-and-connector-servers). Then you must define a data store connection and a data source configuration that uses the connection. The data store connection can be defined while you are setting up the data source configuration. See [Create and Manage Data Store Connections](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connections-managing) and [Create and Manage Data Sources](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-overview) for more information.

<Note>
  Self-Service Analytics supports only underscores and dashes in data store field names. No other special characters or white space are supported. If your data store uses special characters other than underscores and dashes in field names, please remove them before attempting to create a data source configuration.
</Note>

For information about what versions of data stores are supported by the Self-Service Analytics connectors, see [Data Connector Reference](/simba-embedded-analytics/docs/self-service-analytics/26.3/reference/data-connector-reference). For information about which features are supported by different connectors, see [Connector Feature Support](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connector-feature-support).

You can also use a Dundas BI (Managed) connection as a source or in a fusion source. See [Add and Validate a Connection to a Dundas BI Data Source or Data Cube](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connections-managing#add-and-validate-a-connection-to-a-dundas-bi-data-source-or).

<h2 id="manage-connectors-and-connector-servers">
  Manage Connectors and Connector Servers
</h2>

Self-Service Analytics connects to a wide array of data sources available in the marketplace today—from modern databases (including Hadoop, Search, Streaming, and NoSQL) to traditional sources like SQL-based stores. Self-Service Analytics comes prepackaged with connectors that are automatically installed during the Self-Service Analytics installation process.

JDBC drivers for a few of the connectors are no longer included in the installation package. This means that if you use one of these connectors, you also need to configure a JDBC driver before it can be enabled and accessible from Self-Service Analytics. For additional details, including the list of connectors, see [Add a JDBC Driver](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/install-ov#add-a-jdbc-driver).

If the connector you are looking for is not shown, it may be because:

* The connector is installed but is not enabled. For more information, see [Enable and Disable Connectors](#enable-and-disable-connectors).
* The connector was not installed and needs to be downloaded separately. For more information, see [Obtain Additional Connector Servers](#obtain-additional-connector-servers).
* The connector requires you to provide a licensed JDBC driver. For more information, see [Add a JDBC Driver](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/install-ov#add-a-jdbc-driver).

See [Data Connector Reference](/simba-embedded-analytics/docs/self-service-analytics/26.3/reference/data-connector-reference) for the full list of supported Self-Service Analytics connectors.

Management of connector microservices is split into two sections:

* Connector Servers
* Connectors

Each connector server runs independently in the Self-Service Analytics environment. You can set up a connection type for each connector server and manage the ones to be available to users in the Self-Service Analytics tenant account.

This means that you are able to enable or disable any of these servers at any time, depending on the data stores that you use and need to use with Self-Service Analytics. The following figure provides a high level concept diagram of the Self-Service Analytics environment.

<img src="https://mintcdn.com/insightsoftware/GTXU--ZlYc3DodOR/simba-embedded-analytics/docs/self-service-analytics/26.3/images/diagrams/concept-diagram.png?fit=max&auto=format&n=GTXU--ZlYc3DodOR&q=85&s=8ec84bf677f7b621c637e8c0a10ac539" alt="" width="2462" height="1323" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/diagrams/concept-diagram.png" />

The setup and management of connector servers in the Self-Service Analytics environment is handled on the Manage Connector Services page, which is accessible to administrators and members of the Supervisors group. To make the actual connection between Self-Service Analytics and your data source after the connector server has been configured, log into Self-Service Analytics as an administrator and access the [Sources](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-overview#data-sources-page) page, accessible from the main menu. See Connect Self-Service Analytics to Data Stores.

The Manage Connector Services work area (available to administrators and members of the Supervisors group) lets you register or remove connector servers that are not available out-of-the-box in the Self-Service Analytics instance. You can also use this page to maintain, enable, and disable connector definitions based on the connector servers defined in the Self-Service Analytics instance. See [Manage Connector Services Page](#manage-connector-services-page).

The [Connections](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connections-managing#connections-page) page (available to administrators and users with appropriate [privileges](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference)) lets you define the connection for a connector between Self-Service Analytics and a data store. See Connect Self-Service Analytics to Data Stores.

<Note>
  If you try to delete a visual, filter snippet, dashboard, self service report, dashboard link, source, or source field, Self-Service Analytics displays an error message naming any objects dependent on the item you’re trying to delete. You can delete the item after you’ve removed the association from the dependent object. See [Fields Usage](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-fields-tab#fields-usage).
</Note>

See the following topics:

* [Obtain Additional Connector Servers](#obtain-additional-connector-servers)
* [Register a New Connector Server](#register-a-new-connector-server)
* [Modifying a Connector Server](#modifying-a-connector-server)
* [Delete a Connector Server](#delete-a-connector-server)
* [Define a New Connector](#define-a-new-connector)
* [Modify a Connector](#modify-a-connector)
* [Enable and Disable Connectors](#enable-and-disable-connectors)
* [Delete a Connector](#delete-a-connector)
* [Connector Graceful Shutdown](#connector-graceful-shutdown)

<h2 id="manage-connector-services-page">
  Manage Connector Services Page
</h2>

<img src="https://mintcdn.com/insightsoftware/2cXq_sDOxrDVXUcv/simba-embedded-analytics/docs/self-service-analytics/26.3/images/connectors/connector-services.png?fit=max&auto=format&n=2cXq_sDOxrDVXUcv&q=85&s=fdbe48ab60bb9292b83fc6d8e955def8" alt="" width="1596" height="694" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/connectors/connector-services.png" />

The Manage Connector Services page is where you register a new connector server that is not available out-of-the-box to the Self-Service Analytics instance. It is also where you can remove connector servers available to the instance.

This page is also where you set up and enable connectors for use in your data sources. The connectors you can define depend on which connector servers have been registered. You can also use this page to delete and disable connectors in the Self-Service Analytics instance.

### Connector Servers

The Connector Servers section lets the Self-Service Analytics admins and supervisors group users register and delete the connector servers available in the Self-Service Analytics environment. See [Obtain Additional Connector Servers](#obtain-additional-connector-servers) for information about setting up a connector server.

<Note>
  The default **supervisor** user is no longer installed; add users to the **Supervisors** group instead.
</Note>

Use the search box above the Connector Servers table to locate a connector server (for example, if your Self-Service Analytics environment contains a large number of connector servers).

Connector servers that you register and connect in Self-Service Analytics are accessible and the registration details can be edited (for example, if the server has moved or changed). Default connector servers provided by Self-Service Analytics are not editable.

The Connector Server table provides the following information.

<table>
  <thead>
    <tr>
      <th>Column Title</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>Connector Server Name</td>
      <td>The name of the connector server (data store) definition.</td>
    </tr>

    <tr>
      <td>Type</td>

      <td>
        The type of connector server. The following types are supported:

        <br />

        * Discovery: uses the capability integrated into Self-Service Analytics to locate and set up the connector server automatically.

        <br />

        * HTTP/Socket: if you manually add a connector server to the Self-Service Analytics environment, then it will be either an HTTP or a Socket type.

        <br />

        * Core: identifies connectors that are built into the Self-Service Analytics server.

        <br />

        <Note>
          Type **Core** connectors , including flat files as well as HDFS and S3 buckets, do not require a dedicated connector server. These types of connectors are always available. This means they are always on, and do not require any additional network resources to keep them on.
        </Note>
      </td>
    </tr>

    <tr>
      <td>URL/Host</td>
      <td>The URL or host name of the connector server (data store). If more than one instance of a connector server is running, the URLs for each instance are shown, separated by commas.</td>
    </tr>

    <tr>
      <td>Available</td>
      <td>Indicates whether the connector server (data store) is available or not.</td>
    </tr>

    <tr>
      <td>Delete</td>

      <td>
        Provides an option to delete a connector server definition from the Self-Service Analytics instance. This option is not available for Core type connector servers because they are built into Self-Service Analytics and cannot be deleted.

        <br />

        You can delete a connector server that you manually configured. However, you must first delete the connection definitions for the server and the data source configurations that use the connection definitions (see [Delete a Data Source](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-overview#delete-a-data-source) and [Delete Data Store Connections](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connections-managing#delete-data-store-connections)). Then you need to delete the [connector](#connectors) (see [Delete a Connector](#delete-a-connector)). When the connections and the connector are all deleted, you can then delete the connector server.
      </td>
    </tr>
  </tbody>
</table>

See the following topics:

* [Obtain Additional Connector Servers](#obtain-additional-connector-servers)
* [Register a New Connector Server](#register-a-new-connector-server)
* [Modifying a Connector Server](#modifying-a-connector-server)
* [Delete a Connector Server](#delete-a-connector-server)

<h3 id="connectors">
  Connectors
</h3>

The Connectors section lists the connectors that are defined in the Self-Service Analytics environment. You can use these connectors to connect to a specific type of data store (such as Impala or Elasticsearch). You can use this section to add and remove connectors and to enable and disable them. A connector that is listed in this table and is enabled is visible on the [Connections](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connections-managing#connections-page) page in the UI (when you are logged in as a non-supervisory user or administrator and have been assigned appropriate [privileges](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference)).

The Connectors table provides the following information.

<table>
  <thead>
    <tr>
      <th>Column Title</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>Connector</td>
      <td>The name of the connector definition.</td>
    </tr>

    <tr>
      <td>Connector Server Name</td>
      <td>The name of the connector server (data store) associated with the connector. If the connector server is a Core-type connector, the connector server name shows as **Internal**.</td>
    </tr>

    <tr>
      <td>Description</td>
      <td>An optional description of the connector. You can provide this description when you add a connector definition.</td>
    </tr>

    <tr>
      <td>Enabled</td>
      <td>A switch that enables or disables the connector definition in the Self-Service Analytics instance. An enabled connector is visible on the [Connections](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connections-managing#connections-page) page; a disabled connector is not.</td>
    </tr>

    <tr>
      <td>Delete</td>

      <td>
        Provides an option to delete the connector definition from the Self-Service Analytics instance. This option is not available for Internal connectors (Core type connector servers) because they are built into Self-Service Analytics and cannot be deleted.

        <br />

        You can delete a connector that you manually configured. However, you must first delete the connection definitions for the server and the data source configurations that use the connection definitions. See [Delete a Data Source](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-overview#delete-a-data-source) and [Delete Data Store Connections](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connections-managing#delete-data-store-connections).
      </td>
    </tr>
  </tbody>
</table>

See the following topics:

* [Define a New Connector](#define-a-new-connector)
* [Modify a Connector](#modify-a-connector)
* [Delete a Connector](#delete-a-connector)
* [Enable and Disable Connectors](#enable-and-disable-connectors)

<h2 id="define-a-new-connector">
  Define a New Connector
</h2>

Connector definitions make a connector server available to authorized users on the [Sources](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-overview#data-sources-page) page. They make it possible for you to connect to a specific type of data store (such as Impala or Elasticsearch). More than one connector definition can be created for a connector server.

**Define a new connector in your environment.**

1. Log in as a system [admin](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/users-manage#admin-user) or a member of the Supervisors group.

2. Select **Tools > Connectors** from the menu. The Managed Connector Services work area opens.

3. In the Connector Servers section of the Manage Connector Services page, verify that a connector server has been registered for the type of connector you want to define. If it has not, register one. See [Obtain Additional Connector Servers](#obtain-additional-connector-servers) and [Register a New Connector Server](#register-a-new-connector-server).

4. In the Connectors section of the Manage Connector Services page, select **Add Connector Server** The Create New Connector page appears.

   <img src="https://mintcdn.com/insightsoftware/2cXq_sDOxrDVXUcv/simba-embedded-analytics/docs/self-service-analytics/26.3/images/connectors/connector-new.png?fit=max&auto=format&n=2cXq_sDOxrDVXUcv&q=85&s=8763954c76c05e3df19ef46bd8a40acd" alt="" width="465" height="482" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/connectors/connector-new.png" />

5. On the Create New Connector page, specify the following information in the input boxes.

   <table>
     <thead>
       <tr>
         <th>Input Box</th>
         <th>Description</th>
       </tr>
     </thead>

     <tbody>
       <tr>
         <td>Connector</td>
         <td>Specify a unique name for the new connector. A short name is recommended due to the limited space on the [Sources](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-overview#data-sources-page) page to display the icon and name.</td>
       </tr>

       <tr>
         <td>Connector Description</td>
         <td>Optionally, specify a description of the connector.</td>
       </tr>

       <tr>
         <td>Enable this Connector</td>
         <td>Slide this switch on or off to enable or disable the connector on the [Sources](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-overview#data-sources-page) page.</td>
       </tr>

       <tr>
         <td>Connector Server</td>
         <td>Select the connector server definition that should be used for this connector.</td>
       </tr>

       <tr>
         <td>Storage Type</td>
         <td>This value is automatically set by Self-Service Analytics after you have selected the connector server.</td>
       </tr>

       <tr>
         <td>Connector Image</td>

         <td>
           The default image is retrieved from the connector server. If you want to change the image, select **Choose File** to select a custom icon for the connection type. The requirements for the icon are as follows:

           <br />

           * PNG or SVG format
           * Resolution (min/max): 72 x 72 px or 160 x 160 px
           * Max file size: 50 Kb

           <br />

           Select **Restore Default** to restore the image to the default image for the connector server type.
         </td>
       </tr>

       <tr>
         <td>Connector Parameters</td>

         <td>
           The connector parameter information is generated from the selected connector server.

           <br />

           Configure or customize the connection parameters, as needed. These are the values that appear on the Connections page or Connection tab when a user defines a new [connection](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connections-managing) or a new [data source configuration](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-overview) or edits an existing one.

           <br />

           The following fields help you customize the parameters to meet your needs:

           <br />

           * **Order:** Use the arrows to move the parameters up or down and change the order in which the parameters are listed on the Connections page (connection definition) or Connection tab (data source configuration).
           * **Required:** Select this checkbox to make the parameter required for validating the connection. Clear the checkbox if the parameter is not required.
           * **Visible:** Select this checkbox to show optional parameters on the Connections page or Connection tab. Clear the checkbox to hide the parameter.
           * **User Attribute:** Select this checkbox to use custom attributes for the parameter when you set up connections using this connector. See [Use User Attributes for Connection Parameters](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connections-managing#use-user-attributes-for-connection-parameters).
           * **Parameter:** The internal parameter name. No changes can be made.
           * **Parameter Type:** The type of parameter. No changes can be made.
           * **Label:** Specify the label for the parameter. This is the field name that will be used for the parameter on the Connections page or Connection tab.
           * **Help Text:** Provide help text for the parameter. It will be displayed when you select the help icon associated with the input box for the parameter.

           <br />

           Select **Restore Default** to restore the connector parameters to the defaults for the connector server type.
         </td>
       </tr>
     </tbody>
   </table>

6. When you have made the required changes, select **Register**. The new connector displays in the **Connector** section of the **Manage Connector Services** page. If you enabled it, it is also visible on the [Sources](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-overview#data-sources-page) page where you maintain [data source configurations](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-overview).

<h2 id="modify-a-connector">
  Modify a Connector
</h2>

**Modify a connector definition in your environment**

1. Log in as a system [admin](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/users-manage#admin-user) or a member of the Supervisors group.
2. Select **Tools > Connectors** from the main menu. The Managed Connector Services work area opens.
3. In the Connectors section of the Manage Connector Services page, locate the connector you want to modify and select its name. The Edit \<connector-name > Connector page appears.
4. On the Edit \<connector-name> Connector page, change the connector settings. These settings are described in [Define a New Connector](#define-a-new-connector).
5. When you have made the required changes, select **Save**. The new connector changes are saved and display, as appropriate, in the rest of the user interface.

<h2 id="delete-a-connector">
  Delete a Connector
</h2>

**Delete a connector from your environment**

1. Log in as a system [admin](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/users-manage#admin-user) or a member of the Supervisors group.

2. Select **Tools > Connectors** from the main menu. The Managed Connector Services work area opens.

3. In the Connectors section of the Manage Connector Services page, locate the connector you want to delete,

4. Select the delete icon in the Delete column for the connector.

   The connector is removed from the Self-Service Analytics instance.

<Note>
  If you try to delete a visual, filter snippet, dashboard, self service report, dashboard link, source, or source field, Self-Service Analytics displays an error message naming any objects dependent on the item you’re trying to delete. You can delete the item after you’ve removed the association from the dependent object. See [Fields Usage](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-fields-tab#fields-usage).
</Note>

<h2 id="enable-and-disable-connectors">
  Enable and Disable Connectors
</h2>

A connector can be enabled or disabled at any time. Selecting or clearing the checkbox in the **Enabled** column for the target connector determines whether its representative icon appears on the Data Source page. The switch is instantaneous, removing or adding the icon on the [Sources](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-overview#data-sources-page) page. Existing connected data sources can still be accessed and used.

<img src="https://mintcdn.com/insightsoftware/2cXq_sDOxrDVXUcv/simba-embedded-analytics/docs/self-service-analytics/26.3/images/connectors/connector-enable.png?fit=max&auto=format&n=2cXq_sDOxrDVXUcv&q=85&s=707438673198f62e8764dffff2836132" alt="" width="672" height="215" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/connectors/connector-enable.png" />

<h2 id="connector-graceful-shutdown">
  Connector Graceful Shutdown
</h2>

supports the graceful shutdown of connectors. When a connector is shut down, it gracefully completes queries that are in-flight and notifies clients that it is terminating.

Three connector properties in each [connector property file](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/properties-reference#connector-properties-and-property-files) support graceful shutdown:

* `connector.graceful.shutdown.enabled` indicates whether or not graceful shutdown processing should occur. Valid values are `true` (perform graceful shutdown processing) or `false` (do not perform graceful shutdown processing). The default is `true`.
* `connector.graceful.shutdown.event.propagation.timeout-sec` specifies how long (in seconds) the connector will wait to allow clients to receive the information that it is out of service. The default is 35 seconds.
* `connector.graceful.shutdown.force.kill.timeout-sec` specifies the maximum number of seconds that the connector will wait for the number of its active tasks to reach zero. The default is 30 seconds. When this time has elapsed, the connector will stop.

<h2 id="register-a-new-connector-server">
  Register a New Connector Server
</h2>

Before you can register a new connector server, be sure that you have obtained and installed it. See [Obtain Additional Connector Servers](#obtain-additional-connector-servers) and contact insightsoftware [Technical Support](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/tech-support) to obtain the connector server code.

Connector servers are started and run as separate processes, and accept requests on a specific TCP/IP port.

### Register a New Connector Server in Your Environment

1. Log in as a system [admin](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/users-manage#admin-user) or a member of the Supervisors group.

2. Select **Tools > Connectors** from the main menu. The Managed Connector Services work area opens.

3. In the Connector Servers section of the Manage Connector Services page, select **Add Connector Server**. The Register New Connector Server page appears.

   <img src="https://mintcdn.com/insightsoftware/2cXq_sDOxrDVXUcv/simba-embedded-analytics/docs/self-service-analytics/26.3/images/connectors/connector-server-new.png?fit=max&auto=format&n=2cXq_sDOxrDVXUcv&q=85&s=e52c90d14eb96c250dd7c258b879f191" alt="" width="460" height="375" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/connectors/connector-server-new.png" />

4. On the Register New Connector Server page, specify the following information in the input fields.

   | Input Field | Description |
   | - | - |
   | Connector Server Name | Specify a unique name for the new connector server. |
   | Connector Server Type | Add the connector server using HTTP or Socket protocols. Select either **HTTP** or **Socket** from drop-down menu. |
   | Server URL | If you selected the HTTP protocol, specify the URL for the connector server. If you selected the socket protocol, specify the host and port details. For a list of default Self-Service Analytics ports, see [Default Port Reference](/simba-embedded-analytics/docs/self-service-analytics/26.3/reference/port-reference). |

5. Select **Register**.

After the connector server is registered, add and enable at least one connector for it. See [Define a New Connector](#define-a-new-connector) and [Enable and Disable Connectors](#enable-and-disable-connectors).

<h4 id="register-the-dundas-bi-managed-connection-server">
  Register the Dundas BI (Managed) Connection Server
</h4>

To use this connector, you must make the user interface available in your instance. Disabled by default, you can enable the user interface option as part of your post installation or post upgrade tasks. See [Server-Level Variables](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/config-mgmt-ov#server-level-variables).

After you have made this interface available, you can then register the server by providing the following information:

<table>
  <thead>
    <tr>
      <th>Input Field</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>Connector Server Name</td>
      <td>Specify a unique name for this connector server.</td>
    </tr>

    <tr>
      <td>Connector Server Type</td>
      <td>Add the connector server using HTTP or Socket protocols. Select either **HTTP** or **Socket** from drop-down menu.</td>
    </tr>

    <tr>
      <td>Server URL</td>

      <td>
        * If you selected the HTTP protocol, specify the URL for the connector server.
        * If you selected the socket protocol, specify the host and port details.

        <br />

        `http://dundasbi-dundas-bi-edc:8013/connector`

        <br />

        Depending on how your environment is set up, this may default to port 8013. Depending on your configuration, this may be set to 8080. Verify the exact port in use in the environment hosting the data source.
      </td>
    </tr>
  </tbody>
</table>

After you have registered this connector server, you can [enable and disable](#enable-and-disable-connectors) it as you would any other connector server.

<h2 id="modifying-a-connector-server">
  Modifying a Connector Server
</h2>

The only way to modify a connector server on the Manage Connector Services page is to delete and re-register the connector server. See [Delete a Connector Server](#delete-a-connector-server), [Obtain Additional Connector Servers](#obtain-additional-connector-servers), and [Register a New Connector Server](#register-a-new-connector-server).

<h2 id="delete-a-connector-server">
  Delete a Connector Server
</h2>

You can delete a connector server that you manually configured. However, before deleting it, you must first delete the connections to the server from the [Sources](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-overview#data-sources-page) page. Then you need to delete the connector (at the bottom of the Manage Connector Services page). When the connections and the connector are deleted, you can delete the connector server.

**Delete a connector server from your environment**

1. Log in as a system [admin](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/users-manage#admin-user) or a member of the Supervisors group.
2. Select **Tools > Connectors** from the main menu. The Managed Connector Services work area opens.
3. On the **Manage Connector Services** page, locate the connector server you want to delete in the Connector Servers table.
4. Select the delete icon for the connector server.
5. The connector server is removed from the Self-Service Analytics instance.

<Note>
  If you try to delete a visual, filter snippet, dashboard, self service report, dashboard link, source, or source field, Self-Service Analytics displays an error message naming any objects dependent on the item you’re trying to delete. You can delete the item after you’ve removed the association from the dependent object. See [Fields Usage](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-fields-tab#fields-usage).
</Note>

<h2 id="obtain-additional-connector-servers">
  Obtain Additional Connector Servers
</h2>

Several data connector servers are installed by default in your Self-Service Analytics environment, but a number of other connector servers are also available. The new connector server can be added via HTTP or Socket protocols. For a complete list of all supported connector servers, see [Data Connector Reference](/simba-embedded-analytics/docs/self-service-analytics/26.3/reference/data-connector-reference).

**Obtain one or more of these connector servers**

1. Contact insightsoftware [Technical Support](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/tech-support). You will receive a `yum` or `apt` command that downloads and sets up the connector server in the Self-Service Analytics environment. After running the command, the connector microservice is installed and enabled in the Self-Service Analytics environment, allowing it to be discoverable as a new connector microservice.
2. Register the connector server. Connector servers are started and run as separate processes, and accept requests on a specific TCP/IP port. See [Register a New Connector Server](#register-a-new-connector-server).

After you have obtained, installed, and registered the connector server, you need to add and enable at least one connector for it. See [Define a New Connector](#define-a-new-connector) and [Enable and Disable Connectors](#enable-and-disable-connectors).

<h2 id="enable-user-delegation">
  Enable User Delegation
</h2>

You can use user delegation to run queries on behalf of users using a single set of credentials for a number of connectors. This allows you to share a single connection configuration among all users. User delegation can be established on a per-user or a per-group basis.

User delegation is currently supported by the following connectors: Apache Drill, Cloudera Impala, Cloudera Search, and Hive. The Oracle connector supports user delegation only via user credential pass-through.

<Note>
  The supervisor group members enables user delegation via a custom user attribute. Self-Service Analytics administrators enable and [apply user delegation](#apply-user-delegation-to-a-connection) to the data connection definition for a data source.
</Note>

**Enable user delegation**

1. Log in as a system [admin](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/users-manage#admin-user) or a member of the Supervisors group.

   <Note>
     The default **supervisor** user is no longer installed; add users to the **Supervisors** group instead.
   </Note>

2. Select **Tools > Security** from the menu. The security tabs display.

   <img src="https://mintcdn.com/insightsoftware/1fCfZrK84x8KmAw8/simba-embedded-analytics/docs/self-service-analytics/26.3/images/users/security-services.png?fit=max&auto=format&n=1fCfZrK84x8KmAw8&q=85&s=62367bacb5fdb3b52787165a7387cb7b" alt="" width="1262" height="619" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/users/security-services.png" />

3. Select the **LDAP Settings** tab. The LDAP Settings tab has five sections: **General Settings**, **LDAP Server**, **User Provisioning**, **Mappings**, and **Mappings to Custom User Attributes**.

   <Note>
     If the LDAP tab cannot be selected, verify that the LDAP security service is enabled. See [Use Lightweight Directory Access Protocol (LDAP)](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/security/authorization-tools#use-lightweight-directory-access-protocol-ldap).
   </Note>

4. In the **Mapping to Custom User Attributes** section, select **Add Custom User Attribute**.

5. Type any meaningful name for the custom attribute name.

6. Match the new attribute to any LDAP attribute (for example, cn, sAMAccountName, name). This should be provided by an Impala administrator. The only requirement is that this attribute match the configuration in Sentry.

7. Select **Save** to save the attribute.

   The custom user attribute is referenced by its name, prefaced by the word `User`. For example, if your custom user attribute is named `XXXUserName`, you would reference it as `User.XXXUserName`. This reference name is shown in the **Usage** column.

8. Select **Connectors** on the supervisor menu. The Manage Connector Services page appears. This page has two tables: one for Connector Servers and one for Connectors.

9. Scroll down to the Connectors table and select the appropriate connector from the list. The connector settings page displays.

   <img src="https://mintcdn.com/insightsoftware/2cXq_sDOxrDVXUcv/simba-embedded-analytics/docs/self-service-analytics/26.3/images/connectors/impala-connector.png?fit=max&auto=format&n=2cXq_sDOxrDVXUcv&q=85&s=bc93db3eaf8d5695e60ff3a8d26ad5bd" alt="" width="1333" height="989" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/connectors/impala-connector.png" />

10. Scroll down to the Connector Parameters and verify that the checkbox in the **User Attribute** column for the **DO\_AS\_USER** parameter is selected. This ensures that the **DO\_AS\_USER** parameter is visible and can be set in your Impala connection.

11. Select **Save**.

To apply user delegation to a data source connection definition, see [Apply User Delegation to a Connection](#apply-user-delegation-to-a-connection).

<h2 id="apply-user-delegation-to-a-connection">
  Apply User Delegation to a Connection
</h2>

Applying user delegation to a Self-Service Analytics data source connection definition involves setting the **Do As User** parameter in the connection definition and setting up proxy user features in your data store. Any authentication mechanism (Kerberos or LDAP) and group mapping (file system or LDAP-based) method can be used by the data store or Self-Service Analytics, as long as the user name assigned to the **Do As User** connector parameter is allowed appropriate authorizations (delegation) in the data store configuration.

<Note>
  Supervisors group members [enables user delegation](#enable-user-delegation) via a custom user attribute. Administrators [enable](#enable-user-delegation) and apply user delegation to the data connection definition for a data source.
</Note>

User delegation processing is depicted in the following diagram.

<img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/diagrams/user-delegation.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=0580cd82efd8c52c611805396dca35d8" alt="" width="576" height="319" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/diagrams/user-delegation.png" />

User delegation occurs in this manner:

1. The Self-Service Analytics supervisor group member or administrator assigns any LDAP attribute (for example, `cn`, `sAMAccountName`, `name`) to a custom user attribute. This should be provided by your data store administrator. The only requirement is that this attribute must match the configuration in Sentry. See [Enable User Delegation](#enable-user-delegation).

   The Self-Service Analytics custom user attribute is referenced by its name, prefaced by the word `User`. For example, if your custom user attribute is named `XXXUserName`, you would reference it as `User.XXXUserName`.

2. The Self-Service Analytics administrator references the custom user attribute in the appropriate data source connection definition using the connection's **Do As User** box. For example:

   <img src="https://mintcdn.com/insightsoftware/2cXq_sDOxrDVXUcv/simba-embedded-analytics/docs/self-service-analytics/26.3/images/connectors/hive-on-tez-do-as-user.png?fit=max&auto=format&n=2cXq_sDOxrDVXUcv&q=85&s=a41164d4525bf967ebd1f2f95b45406d" alt="" width="269" height="281" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/connectors/hive-on-tez-do-as-user.png" />

3. When a user submits a query using the data source, the Self-Service Analytics connector sends the user identified by the **Do As User** parameter (or as interpreted by the setting in that parameter) to the data store when it connects on behalf of the query.

   Assuming user proxy (user delegation) features are set up properly on the data store, the data store runs the query on behalf of the user. For information on setting up user proxy, user impersonation, or user delegation features in each data store, see the following links.

   <table>
     <thead>
       <tr>
         <th>Data Store</th>
         <th>User Proxy Setup Links</th>
       </tr>
     </thead>

     <tbody>
       <tr>
         <td>Apache Drill</td>

         <td>
           * [https://drill.apache.org/docs/configuring-user-impersonation/](https://drill.apache.org/docs/configuring-user-impersonation/)
           * [https://drill.apache.org/docs/configuring-inbound-impersonation/](https://drill.apache.org/docs/configuring-inbound-impersonation/)
         </td>
       </tr>

       <tr>
         <td>Cloudera Impala</td>

         <td>
           * [https://docs.cloudera.com/documentation/enterprise/latest/topics/impala\_delegation.html](https://docs.cloudera.com/documentation/enterprise/latest/topics/impala_delegation.html)
         </td>
       </tr>

       <tr>
         <td>Cloudera Search</td>

         <td>
           * [https://docs.cloudera.com/documentation/enterprise/latest/topics/impala\_delegation.html](https://docs.cloudera.com/documentation/enterprise/latest/topics/impala_delegation.html)
           * [https://docs.cloudera.com/documentation/enterprise/5-12-x/topics/search\_ha\_proxy.html](https://docs.cloudera.com/documentation/enterprise/5-12-x/topics/search_ha_proxy.html)
           * [https://docs.cloudera.com/documentation/enterprise/5-10-x/topics/admin\_hdfs\_proxy\_users.html](https://docs.cloudera.com/documentation/enterprise/5-10-x/topics/admin_hdfs_proxy_users.html)
         </td>
       </tr>

       <tr>
         <td>Hive</td>

         <td>
           * [https://community.cloudera.com/t5/Community-Articles/Enable-DoAs-option-Hive-to-allow-users-to-runs-queries-with/ta-p/247400](https://community.cloudera.com/t5/Community-Articles/Enable-DoAs-option-Hive-to-allow-users-to-runs-queries-with/ta-p/247400)
           * [https://docs.cloudera.com/documentation/enterprise/5-8-x/topics/cdh\_sg\_hiveserver2\_security.html#concept\_vjq\_c3x\_nm](https://docs.cloudera.com/documentation/enterprise/5-8-x/topics/cdh_sg_hiveserver2_security.html#concept_vjq_c3x_nm)
           * [https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-common/Superusers.html](https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-common/Superusers.html)
         </td>
       </tr>
     </tbody>
   </table>
