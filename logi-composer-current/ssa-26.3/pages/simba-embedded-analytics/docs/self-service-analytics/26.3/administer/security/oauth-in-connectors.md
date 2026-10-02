> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Use OAuth 2.0 in Connections to Cloud Data Stores

You can leverage existing authorization rules of BigQuery and Snowflake data sources by enabling OAuth 2.0 for these connectors in Self-Service Analytics. Users access the connected data stores, using their personalized credentials, and receive access to the data following the security rules of your data source.

### Feature Support

Use OAuth to connect to these supported data sources:

* [Connect to BigQuery](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-bigquery#connect-to-bigquery)
* [Connect to Snowflake](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-snowflake#connect-to-snowflake)

To avoid frequent authentication requests for users, Self-Service Analytics operates with long-lived tokens and preemptively refreshes the tokens when they are close to expiration.

<Note>
  Scheduled source refresh is not available when you use OAuth 2.0 authentication.
</Note>

<h3 id="oauth-2-0-setup-bigquery">
  OAuth 2.0 Setup - BigQuery
</h3>

To create a BigQuery connection use one of the available authentication methods:

* Key authentication flow requires a security key to be generated at BigQuery and placed to the Self-Service Analytics instance;
* OAuth 2.0 requires providing OAuth `client_id` and `client_secrets` generated for a user that will serve for data retrieval, such as an integration user. Users are asked to authenticate via a separate authentication form. Users provide their individual credentials when accessing the data retrieved using this connection.

If both authentication methods are selected, connection via OAuth will have higher priority over key authentication except for the scheduled overrides setup.

<table>
  <thead>
    <tr>
      <th />

      <th>Authentication Flow</th>

      <th />
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>Key Path</td>
      <td rowSpan={2}>Key Authentication</td>
      <td>Absolute path to the key authentication file obtained from BigQuery and placed to Self-Service Analytics instance.</td>
    </tr>

    <tr>
      <td>Public Project Ids</td>
      <td>List of public project IDs that will be queried for the data.</td>
    </tr>

    <tr>
      <td>**OAuth 2.0 Enabled**</td>
      <td rowSpan={4}>OAuth 2.0</td>
      <td>TRUE/FALSE</td>
    </tr>

    <tr>
      <td>**Project Id**</td>

      <td>
        Billing project ID that will be queried for the data.

        <br />

        <Note>
          Optional if keys authentication is used.
        </Note>

        <br />

        <Warning>
          Mandatory if OAuth 2.0 connection is enabled.
        </Warning>
      </td>
    </tr>

    <tr>
      <td>**OAuth 2.0 Client Id**</td>

      <td>
        `client_id`: Obtain from BigQuery.

        <br />

        See [https://cloud.google.com/bigquery/docs/authentication/end-user-installed](https://cloud.google.com/bigquery/docs/authentication/end-user-installed).
      </td>
    </tr>

    <tr>
      <td>**OAuth 2.0 Client Secrets**</td>

      <td>
        `client_secrets`: Obtain from BigQuery.

        <br />

        See [https://cloud.google.com/bigquery/docs/authentication/end-user-installed](https://cloud.google.com/bigquery/docs/authentication/end-user-installed).
      </td>
    </tr>
  </tbody>
</table>

#### Scheduled Override Options

To maintain Self-Service Analytics's ability to perform scheduled operations such as scheduled dashboard reports, alerts notifications, and more when using OAuth 2.0 authentication flow, you can setup scheduled overrides with key authentication method by providing a key path.

Additional OAuth 2.0 parameters available for override, however, already have prepopulated BigQuery values and do not require manual editing:

* `OAUTH2.AUTHORIZATION_URI`
* `OAUTH2.TOKEN_URI`
* `OAUTH2.SCOPES`

<Note>
  Scheduled source refresh is not available when you use OAuth 2.0 authentication.
</Note>

To avoid frequent authentication requests for users, Self-Service Analytics operates with long-lived tokens and preemptively refreshes the tokens when they are close to expiration.

<Warning>
  Users' OAuth sessions are terminated when the OAuth token is revoked, if the connection is deleted, or connection details are modified.
</Warning>

<h3 id="oauth-2-0-setup-snowflake">
  OAuth 2.0 Setup - Snowflake
</h3>

To create a Snowflake connection use one of the available authentication methods:

* Basic authentication via username and password
* OAuth 2.0

If connecting using basic authentication, provide:

* The name of the connection.

* The JDBC URL.

* Each Snowflake connection you use must be associated with a database.

  * The database can be the one specified in the JDBC URL, or
  * The default database of the connecting user (if no database is specified in the JDBC URL).

* The username and password. Only simple username and password authentication is supported.

For connecting via OAuth 2.0, fill in the specific parameters:

<table>
  <thead>
    <tr>
      <th>JDBC URL</th>

      <th />
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>**OAuth 2.0 Enabled**</td>
      <td>TRUE/FALSE</td>
    </tr>

    <tr>
      <td>**OAuth 2.0 Authorization URI**</td>
      <td rowSpan={4}>Obtain OAuth 2.0 connection parameters from your Snowflake instance for connection.</td>
    </tr>

    <tr>
      <td>**OAuth 2.0 Token URI**</td>
    </tr>

    <tr>
      <td>**OAuth 2.0 Client Id**</td>
    </tr>

    <tr>
      <td>**OAuth 2.0 Client Secret**</td>
    </tr>
  </tbody>
</table>

<Note>
  Scheduled source refresh is not available when you use OAuth 2.0 authentication.
</Note>

<Note>
  If you do not want to expose OAuth 2.0 connection options to your customers, disable OAuth-related connection parameters at the connector level as a member of the Supervisors group.
</Note>
