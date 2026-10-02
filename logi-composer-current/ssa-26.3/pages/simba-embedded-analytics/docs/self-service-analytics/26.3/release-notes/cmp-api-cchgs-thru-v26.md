> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# API Updates, Deprecated, Removed Features Through Composer 26

Changes made over time to the Composer API are included here to help you plan upgrades from older releases. Deprecated and removed features are included to allow you to view changes that may affect your environment on upgrade.

<Danger>
  Running an older, unsupported operating system in your environment is done so at your own risk. Plan and upgrade to a supported operating system for full support and functionality. For information on operating system and environment support, see [Operating System Support](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/installation-prerequisites#operating-system-support).
</Danger>

To purchase this product, contact [insightsoftware Sales](mailto:loginewbusinessteam@insightsoftware.com?subject=I%20am%20interested%20in%20purchasing%20this%20product,%20please%20contact%20me.).

* [API Updates](#api-updates)

  * [Composer v26](#api-updates-composer-v26)
  * [Composer v25](#api-updates-composer-v25)
  * [Composer v24](#api-updates-composer-v24)
  * [Composer v23](#api-updates-composer-v23)
  * [Composer v22](#api-updates-composer-v22)
  * [Composer v8.4 and Earlier](#api-updates-composer-v8-4-and-earlier)
  * [Composer v7.10 and Earlier](#api-updates-composer-v7-10-and-earlier)
  * [Composer v6.9 and Earlier](#api-updates-composer-v6-9-and-earlier)

* [Deprecated and Removed Features](#deprecated-and-removed-features)

  * [Composer v26](#deprecated-and-removed-features-composer-v26)
  * [Composer v25](#deprecated-and-removed-features-composer-v25)
  * [Composer v24](#deprecated-and-removed-features-composer-v24)
  * [Composer v23](#deprecated-and-removed-features-composer-v23)
  * [Composer v22](#deprecated-and-removed-features-composer-v22)
  * [Composer v8.4 and Earlier](#deprecated-and-removed-features-composer-v8-4-and-earlier)
  * [Composer v7.10 and Earlier](#deprecated-and-removed-features-composer-v7-10-and-earlier)
  * [Composer v6.9 and Earlier](#deprecated-and-removed-features-composer-v6-9-and-earlier)

<h2 id="api-updates">
  API Updates
</h2>

<h3 id="api-updates-composer-v26">
  Composer v26
</h3>

<table>
  <thead>
    <tr>
      <th>Endpoint</th>
      <th>Method</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={3}>**26.3 API Updates**</td>
    </tr>

    <tr>
      <td />

      <td />

      <td />
    </tr>

    <tr>
      <td />

      <td />

      <td />
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th>Endpoint</th>
      <th>Method</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={3}>**26.2.2 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**26.2.1 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**26.2 API Updates**</td>
    </tr>

    <tr>
      <td>api/export/visualdata/enriched</td>
      <td>POST</td>

      <td>
        Export visual data for table visuals including grouped data in Excel (XLSX) format. Your formatting, aggregation, and conditional formatting are preserved in the exported file.

        <br />

        Report generation and export performance varies significantly based on report complexity, report generation volume, and export format. For more information on environment sizing and use planning guidelines, see [Environment Configuration](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/arch-microservice#environment-configuration) and [Performance Considerations](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/arch-microservice#performance-considerations).
      </td>
    </tr>

    <tr>
      <td>
        api/dashboards/\{dashboardId}/reports

        <br />

        api/dashboards/\{dashboardId}/reports/\{reportId}
      </td>

      <td>
        POST

        <br />

        PUT
      </td>

      <td>
        Create or update a scheduled dashboard report. This supports features added in this release.

        <br />

        * `timezone`: include to support DST-aware scheduling instead of the default UTC
      </td>
    </tr>

    <tr>
      <td>
        api/dashboards/\{dashboardId}/reports

        <br />

        api/dashboards/\{dashboardId}/reports/\{reportId}
      </td>

      <td>
        POST

        <br />

        PUT
      </td>

      <td>
        Create or update a scheduled self service report. This supports features added in this release.

        <br />

        * `timezone`: include to support DST-aware scheduling instead of the default UTC

        <br />

        * `pageSize`: include a setting to override the default of US Letter Portrait. Size options include LETTER, A4, and A3.

        <br />

        * `orientation`: define the orientation of the report. This includes page-aware column count validation and font size validation for the selected orientation.

        <br />

        * PORTRAIT: 15 column max for Letter and A4 paper sizes. 22 column max for A3 paper size.

        <br />

        * LANDSCAPE. 20 column max for Letter. 22 column max for A4. 30 column max for A3.

        <br />

        <Note>
          Column count validation is not performed on Group Structured Reports.
        </Note>

        <br />

        Report generation and export performance varies significantly based on report complexity, report generation volume, and export format. For more information on environment sizing and use planning guidelines, see [Environment Configuration](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/arch-microservice#environment-configuration) and [Performance Considerations](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/arch-microservice#performance-considerations).
      </td>
    </tr>

    <tr>
      <td>api/self-service-reports/export</td>
      <td>POST</td>

      <td>
        Export self service reports. This supports features added in this release.

        <br />

        * `pageSize`: include a setting to override the default of US Letter Portrait. Size options include LETTER, A4, and A3.

        <br />

        * `orientation`: define the orientation of the report. This includes page-aware column count validation and font size validation for the selected orientation.

        <br />

        * PORTRAIT: 15 column max for Letter and A4 paper sizes. 22 column max for A3 paper size.

        <br />

        * LANDSCAPE. 20 column max for Letter. 22 column max for A4. 30 column max for A3.

        <br />

        <Note>
          Column count validation is not performed on Group Structured Reports.
        </Note>

        <br />

        Report generation and export performance varies significantly based on report complexity, report generation volume, and export format. For more information on environment sizing and use planning guidelines, see [Environment Configuration](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/arch-microservice#environment-configuration) and [Performance Considerations](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/arch-microservice#performance-considerations).
      </td>
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th>Endpoint</th>
      <th>Method</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={3}>**26.1.3 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**26.1.2 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**26.1.1 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**26.1 API Updates**</td>
    </tr>

    <tr>
      <td>api/dashboards/</td>
      <td>GET</td>
      <td>The GET api/dashboards/ endpoint now returns the creator's full name as **creatorFullName**.</td>
    </tr>
  </tbody>
</table>

<h3 id="api-updates-composer-v25">
  Composer v25
</h3>

<table>
  <thead>
    <tr>
      <th>Endpoint</th>
      <th>Method</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={3}>**25.4.5 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**25.4.4 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**25.4.3 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**25.4.2 API Updates**</td>
    </tr>

    <tr>
      <td>api/sources/odata/s\_\{sourceid}</td>
      <td>GET</td>

      <td>
        A new optional query parameter, **number\_format** can now be appended to the url to get the large numeric field values as plain decimals that may, by default, be converted to scientific notation.

        <br />

        * **number\_format=plain** — All scientific notation values are converted to plain decimal format. Double values smaller than 10⁻⁵ will be treated as 0 when using this option.
        * **number\_format=default** — Values are returned in the existing format. This is the default behavior if the parameter is omitted.

        <br />

        Existing integrations are unaffected. To opt into plain decimal formatting, add **?number\_format=plain** to your OData requests.
      </td>
    </tr>

    <tr>
      <td colSpan={3}>**25.4.1 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**25.4 API Updates**</td>
    </tr>

    <tr>
      <td>api/sources/odata/s\_\{sourceid}</td>
      <td>GET</td>

      <td>
        A new query parameter, **response\_format=compact**, has been added to the existing OData API endpoint: **/api/sources/odata/s\_\{sourceid}?response\_format=compact**.

        <br />

        When you include this parameter in your query, the API returns data in a more efficient, compact JSON format. The reduced size of the response payload increases the speed of data transfer.
      </td>
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th>Endpoint</th>
      <th>Method</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={3}>**25.3.8 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**25.3.7 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**25.3.6 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**25.3.5 API Updates**</td>
    </tr>

    <tr>
      <td>api/sources/odata/s\_\{sourceid}</td>
      <td>GET</td>

      <td>
        A new optional query parameter, **number\_format** can now be appended to the url to get the large numeric field values as plain decimals that may, by default, be converted to scientific notation.

        <br />

        * **number\_format=plain** — All scientific notation values are converted to plain decimal format. Double values smaller than 10⁻⁵ will be treated as 0 when using this option.
        * **number\_format=default** — Values are returned in the existing format. This is the default behavior if the parameter is omitted.

        <br />

        Existing integrations are unaffected. To opt into plain decimal formatting, add **?number\_format=plain** to your OData requests.
      </td>
    </tr>

    <tr>
      <td colSpan={3}>**25.3.4 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**25.3.3 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**25.3.2 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**25.3.1 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**25.3 API Updates**</td>
    </tr>

    <tr>
      <td>
        api/accounts/\{id}

        <br />

        api/accounts

        <br />

        api/accounts/name/\{name}
      </td>

      <td>GET, POST, PUT</td>

      <td>
        Use the updated Accounts API to retrieve or define all tenant configuration information, or specific information, such as tenant-level information related to SFTP and SMTP configuration details as needed.

        <br />

        Reserved attributes include:

        <br />

        * sftp.host
        * sftp.password
        * sftp.port
        * sftp.remoteDirectory
        * sftp.strictHostKeyChecking
        * sftp.user
        * email.replyToAddress
        * email.senderDisplayName
      </td>
    </tr>

    <tr>
      <td>
        api/accounts/\{id}

        <br />

        api/accounts
      </td>

      <td>POST, PUT</td>

      <td>
        Users with appropriate permissions to create accounts (tenants) can define a "Reply-To" and "Sender Display Name" for the emails generated to send scheduled reports and scheduled dashboard reports. Users with appropriate permissions to update accounts (tenants) can define these attributes for specific accounts (tenants).

        <br />

        Attributes:

        <br />

        * email.replyToAddress
        * email.senderDisplayName
      </td>
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th>Endpoint</th>
      <th>Method</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={3}>**25.2.10 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**25.2.9 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**25.2.8 API Updates**</td>
    </tr>

    <tr>
      <td>api/sources/odata/s\_\{sourceid}</td>
      <td>GET</td>

      <td>
        A new optional query parameter, **number\_format** can now be appended to the url to get the large numeric field values as plain decimals that may, by default, be converted to scientific notation.

        <br />

        * **number\_format=plain** — All scientific notation values are converted to plain decimal format. Double values smaller than 10⁻⁵ will be treated as 0 when using this option.
        * **number\_format=default** — Values are returned in the existing format. This is the default behavior if the parameter is omitted.

        <br />

        Existing integrations are unaffected. To opt into plain decimal formatting, add **?number\_format=plain** to your OData requests.
      </td>
    </tr>

    <tr>
      <td colSpan={3}>**25.2.7 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**25.2.6 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**25.2.5 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**25.2.4 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**25.2.3 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**25.2.2 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**25.2.1 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**25.2 API Updates**</td>
    </tr>

    <tr>
      <td>
        /api/dashboards/\{dashboard\_id}/reports/report\_id/

        <br />

        /api/dashboards/\{dashboard\_id}/reports
      </td>

      <td>PUT, POST</td>
      <td>You can now add a `destinationType` of `EMAIL` or `FILE_DROP` to support SFTP and SMTP dispatch of scheduled dashboard reports.</td>
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th>Endpoint</th>
      <th>Method</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={3}>**25.1.11 API Updates**</td>
    </tr>

    <tr>
      <td>api/sources/odata/s\_\{sourceid}</td>
      <td>GET</td>

      <td>
        A new optional query parameter, **number\_format** can now be appended to the url to get the large numeric field values as plain decimals that may, by default, be converted to scientific notation.

        <br />

        * **number\_format=plain** — All scientific notation values are converted to plain decimal format. Double values smaller than 10⁻⁵ will be treated as 0 when using this option.
        * **number\_format=default** — Values are returned in the existing format. This is the default behavior if the parameter is omitted.

        <br />

        Existing integrations are unaffected. To opt into plain decimal formatting, add **?number\_format=plain** to your OData requests.
      </td>
    </tr>

    <tr>
      <td colSpan={3}>**25.1.10 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**25.1.9 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**25.1.8 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**25.1.7 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**25.1.6 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**25.1.5 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**25.1.4 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**25.1.3 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**25.1.2 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**25.1.1 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**25.1 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>
  </tbody>
</table>

<h3 id="api-updates-composer-v24">
  Composer v24
</h3>

<table>
  <thead>
    <tr>
      <th>Endpoint</th>
      <th>Method</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={3}>**24.4.16 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**24.4.15 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**24.4.14 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**24.4.13 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**24.4.12 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**24.4.11 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**24.4.10 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**24.4.9 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**24.4.8 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**24.4.7 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**24.4.6 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**24.4.5 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**24.4.4 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**24.4.3 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**24.4.2 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**24.4.1 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**24.4 API Updates**</td>
    </tr>

    <tr>
      <td>/api/sources/\{source\_id}/cache?cacheType=ENTITY\_DATA</td>
      <td>DELETE</td>
      <td>This endpoint has been expanded to allow you to clear the ENTITY\_DATA cache in addition to the DATA and STATISTICS cache.</td>
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th>Endpoint</th>
      <th>Method</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={3}>**24.3.10 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**24.2.9 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**24.3.8 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**24.3.7 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**24.3.6 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**24.3.5 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**24.3.4 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**24.3.3 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**24.3.2 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**24.3.1 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**24.3 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th>Endpoint</th>
      <th>Method</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={3}>**24.2.12 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**24.2.11 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**24.2.10 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**24.2.9 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**24.2.8 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**24.2.7 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**24.2.6 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**24.2.5 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**24.2.4 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**24.2.3 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**24.2.2 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**24.2.1 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**24.2 API Updates**</td>
    </tr>

    <tr>
      <td>/api/group-membership/\{id}</td>
      <td>PATCH</td>
      <td>Manage group membership for users by updating a group: define `usersToAdd` and `usersToRemove` to include a single user or an array of users.</td>
    </tr>

    <tr>
      <td>
        /api/inventory/\{type}/

        <br />

        and

        <br />

        /api/inventory/\{type}/\{id}
      </td>

      <td>GET</td>
      <td>If you created dashboards and visuals that include your own `originID`, calling this endpoint returns each item and their associated `originID`, if applicable.</td>
    </tr>

    <tr>
      <td>/api/sources</td>
      <td>GET/PUT</td>
      <td>Use to return and define information for a source.</td>
    </tr>

    <tr>
      <td>/api/sources/\{sourceId}/clone</td>
      <td>POST</td>
      <td>Use to create a copy of a source.</td>
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th>Endpoint</th>
      <th>Method</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={3}>**24.1.12 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**24.1.11 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**24.1.10 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**24.1.9 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**24.1.8 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**24.1.7 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**24.1.6 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**24.1.5 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**24.1.4 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**24.1.3 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**24.1.2 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**24.1.1 API Updates**</td>
    </tr>

    <tr>
      <td>/api/groups</td>
      <td>POST, PUT</td>
      <td>You can now assign an identifier to your groups using `externalId` that is unique across tenants. This does not change or replace the `accountId` assigned by Composer. The `externalId` is not available in the UI.</td>
    </tr>

    <tr>
      <td colSpan={3}>**24.1 API Updates**</td>
    </tr>

    <tr>
      <td>/api/sources/export</td>
      <td>GET</td>

      <td>
        These attributes are returned for sources in your environment. Include these attributes to work with import matching strategies.

        <br />

        * `connections[].originId` - Returns the value of the connection ID from the imported connection.
        * `sources[].originId` - Returns the value of the source ID from the imported source
      </td>
    </tr>

    <tr>
      <td>/api/sources/import</td>
      <td>POST</td>

      <td>
        When you import objects into your environment, you can define a matching strategy that uses multiple approaches to reviewing objects to determine how to handle them in conjunction with your selected insertion strategy.

        <br />

        Matching strategies are processed in order, proceeding to the next and the next if a strategy fails.

        <br />

        If all strategies fail, the object is imported and tagged with your selected tags to help you find affected objects and manage any issues.

        <br />

        These attributes are used to define the matching strategy and warning tags to use for import. Send as an array; each strategy is considered in order.

        <br />

        * `importSettings.objectClassLevel.connections.matchingStrategy[]` - Send an array of matching strategies to be considered, in order, for connections. This array can include:

        <br />

        * `BY_ORIGIN_ID`

        <br />

        * `BY_ID_AND_TYPE_AND_PARAMS`

        <br />

        * `BY_TYPE_AND_PARAMETERS`

        <br />

        * `BY_NAME_AND_TYPE`

        <br />

        * `BY_TYPE_AND_PARAM_KEYS`

        <br />

        * `BY_NAME`

        <br />

        If an order is not specified, the default strategy of `BY_ID_AND_TYPE_AND_PARAMS` or `BY_TYPE_AND_PARAMETERS` is used.

        <br />

        * `importSettings.objectClassLevel.sources.matchingStrategy[]` - Send an array of matching strategies to be considered, in order, for sources. This array can include:

        <br />

        * `BY_ORIGIN_ID`

        <br />

        * `BY_NAME`

        <br />

        If an order is not specified, the default strategy of `BY_NAME` is used.

        <br />

        * `importSettings.warningTags[]` - Send an array of warning tags to apply to objects imported with warnings.

        <br />

        Send `enableDefaultRead` to enable data read permissions for the sources imported for all users in the tenant.
      </td>
    </tr>

    <tr>
      <td>/api/dashboards/export/</td>
      <td>GET</td>

      <td>
        These attributes are returned for dashboards in your environment. Include these attributes for importing.

        <br />

        * `connections[].originId` - Returns the value of the associated connection ID.
        * `sources[].originId` - Returns the value of the associated source ID.
        * `visuals[].originId` - Returns the value of the associated visual ID.
        * `dashboards[].originId` - Returns the value of the associated dashboard ID.
      </td>
    </tr>

    <tr>
      <td>/api/dashboards/import/</td>
      <td>POST</td>

      <td>
        When you import objects into your environment, you can define a matching strategy that uses multiple approaches to reviewing objects to determine how to handle them in conjunction with your selected insertion strategy.

        <br />

        Matching strategies are processed in order, proceeding to the next and the next if a strategy fails.

        <br />

        If all strategies fail, the object is imported and tagged with your selected tags to help you find affected objects and manage any issues.

        <br />

        These attributes are used to define the matching strategy and warning tags to use for import. Send as an array; each strategy is considered in order.

        <br />

        * `importSettings.objectClassLevel.connections.matchingStrategy[]` - Send an array of matching strategies to be considered, in order, for connections. This array can include:

        <br />

        * `BY_ORIGIN_ID`

        <br />

        * `BY_ID_AND_TYPE_AND_PARAMS`

        <br />

        * `BY_TYPE_AND_PARAMETERS`

        <br />

        * `BY_NAME_AND_TYPE`

        <br />

        * `BY_TYPE_AND_PARAM_KEYS`

        <br />

        * `BY_NAME`

        <br />

        If an order is not specified, the default strategy of `BY_ID_AND_TYPE_AND_PARAMS` or `BY_TYPE_AND_PARAMETERS` is used.

        <br />

        * `importSettings.objectClassLevel.visuals.matchingStrategy[]` - Send an array of matching strategies to be considered, in order, for visuals. This array can include:

        <br />

        * `BY_ORIGIN_ID`

        <br />

        * `BY_NAME`

        <br />

        If an order is not specified, the default strategy of `BY_NAME` is used.

        <br />

        * `importSettings.objectClassLevel.sources.matchingStrategy[]` - Send an array of matching strategies to be considered, in order, for sources. This array can include:

        <br />

        * `BY_ORIGIN_ID`

        <br />

        * `BY_NAME`

        <br />

        If an order is not specified, the default strategy of `BY_NAME` is used.

        <br />

        * `importSettings.objectClassLevel.dashboards.matchingStrategy[]` - Send an array of matching strategies to be considered, in order, for dashboards. This array can include:

        <br />

        * `BY_ORIGIN_ID`

        <br />

        * `BY_NAME`

        <br />

        If an order is not specified, the default strategy of `BY_NAME` is used.

        <br />

        * `importSettings.warningTags[]` - Send an array of warning tags to apply to objects imported with warnings.

        <br />

        Send `enableDefaultRead` to enable data read permissions for the sources imported for all users in the tenant.
      </td>
    </tr>

    <tr>
      <td>/api/visuals/export/</td>
      <td>GET</td>

      <td>
        These attributes are returned for visuals in your environment. Include these attributes for importing.

        <br />

        * `connections[].originId` - Returns the value of the associated connection ID.
        * `sources[].originId` - Returns the value of the associated source ID.
        * `visuals[].originId` - Returns the value of the associated visual ID.
      </td>
    </tr>

    <tr>
      <td>/api/visuals/import/</td>
      <td>POST</td>

      <td>
        When you import objects into your environment, you can define a matching strategy that uses multiple approaches to reviewing objects to determine how to handle them in conjunction with your selected insertion strategy.

        <br />

        Matching strategies are processed in order, proceeding to the next and the next if a strategy fails.

        <br />

        If all strategies fail, the object is imported and tagged with your selected tags to help you find affected objects and manage any issues.

        <br />

        These attributes are used to define the matching strategy and warning tags to use for import. Send as an array; each strategy is considered in order.

        <br />

        * `importSettings.objectClassLevel.connections.matchingStrategy[]` - Send an array of matching strategies to be considered, in order, for connections. This array can include:

        <br />

        * `BY_ORIGIN_ID`

        <br />

        * `BY_ID_AND_TYPE_AND_PARAMS`

        <br />

        * `BY_TYPE_AND_PARAMETERS`

        <br />

        * `BY_NAME_AND_TYPE`

        <br />

        * `BY_TYPE_AND_PARAM_KEYS`

        <br />

        * `BY_NAME`

        <br />

        If an order is not specified, the default strategy of `BY_ID_AND_TYPE_AND_PARAMS` or `BY_TYPE_AND_PARAMETERS` is used.

        <br />

        * `importSettings.objectClassLevel.visuals.matchingStrategy[]` - Send an array of matching strategies to be considered, in order, for visuals. This array can include:

        <br />

        * `BY_ORIGIN_ID`

        <br />

        * `BY_NAME`

        <br />

        If an order is not specified, the default strategy of `BY_NAME` is used.

        <br />

        * `importSettings.objectClassLevel.sources.matchingStrategy[]` - Send an array of matching strategies to be considered, in order, for sources. This array can include:

        <br />

        * `BY_ORIGIN_ID`

        <br />

        * `BY_NAME`

        <br />

        If an order is not specified, the default strategy of `BY_NAME` is used.

        <br />

        * `importSettings.warningTags[]` - Send an array of warning tags to apply to objects imported with warnings.

        <br />

        Send `enableDefaultRead` to enable data read permissions for the sources imported for all users in the tenant.
      </td>
    </tr>

    <tr>
      <td>/api/accounts/name/\{name}</td>
      <td>GET</td>
      <td>This takes the `{name}` of the tenant account as a path parameter and returns tenant account details. Works similarly to `/api/accounts/{id}/`.</td>
    </tr>
  </tbody>
</table>

<h3 id="api-updates-composer-v23">
  Composer v23
</h3>

<table>
  <thead>
    <tr>
      <th>Endpoint</th>
      <th>Method</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={3}>**23.4.13 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**23.4.12 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**23.4.11 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**23.4.10 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**23.4.9 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**23.4.8 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**23.4.7 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**23.4.6 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**23.4.5 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**23.4.4 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**23.4.3 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**23.4.2 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**23.4.1 API Updates**</td>
    </tr>

    <tr>
      <td>/api/sources/</td>
      <td>POST</td>
      <td>When using the `sources` endpoint, Composer returns the parameter fields of the collection you request, both for `/preview` and `/describe`.</td>
    </tr>

    <tr>
      <td colSpan={3}>**23.4 API Updates**</td>
    </tr>

    <tr>
      <td>/api/recently-accessed-elements</td>
      <td>GET</td>
      <td>Use to return items recently used, such as dashboards, visuals, and data sources by the logged in user in Composer. Limit the number of items returned by sending `/api/recently-accessed-elements?listSize={number}.`</td>
    </tr>

    <tr>
      <td>/api/accounts/\{id}</td>
      <td>PUT</td>
      <td>Use `/api/accounts/{id}` to update existing user accounts, or create new ones.</td>
    </tr>

    <tr>
      <td>/api/sources/\{sourceId}/clone</td>
      <td>PUT</td>
      <td>Use to clone an existing source in your environment with a new `name`. Mandatory fields include `sourceID` and `name`. Optionally add `tags` and `description`.</td>
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th>Endpoint</th>
      <th>Method</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={3}>**23.3.14 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**23.3.13 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**23.3.12 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**23.3.11 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**23.3.10 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**23.3.9 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**23.3.8 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**23.3.7 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**23.3.6 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**23.3.5 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**23.3.4 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**23.3.3 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**23.3.2 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**23.3.1 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**23.3 API Updates**</td>
    </tr>

    <tr>
      <td>
        /api/connection/\{id}

        <br />

        /api/sources/\{id}

        <br />

        /api/sources/ \{sourceId}/fields/\{fieldId}

        <br />

        /api/visuals/\{id}

        <br />

        /api/dashboard/\{id}
      </td>

      <td>DELETE</td>
      <td>When you attempt to delete an object that has dependent object, Composer returns a robust response that includes the item’s `id`, `name`, and `type` to make decoupling of dependent objects easier.</td>
    </tr>

    <tr>
      <td>/api/connection/types/\{id}/accounts</td>
      <td>PUT, GET</td>

      <td>
        Use to allow access to specific connection types to users of appropriate permissions in specific Accounts.

        <br />

        If no Accounts are specified for a connection type, all uses with appropriate permissions in all accounts can create new or edit existing connection types.
      </td>
    </tr>

    <tr>
      <td>/api/sources</td>
      <td>POST</td>

      <td rowSpan={4}>
        If a request through the API returns a 400 response code, you now see two levels of validation issues, ERROR and WARNING. Optionally, include the query parameter `suppressWarnings` to determine the behavior of the request.

        <br />

        * Send `suppressWarnings=true` to make the request ignore all warning violations and return success if there are no error violations.
        * Send `suppressWarnings=false` to make the request fail if there is at least one error or warning.
        * The default value is `false`.
      </td>
    </tr>

    <tr>
      <td>/api/sources/\$\{sourceId}</td>
      <td>PUT</td>
    </tr>

    <tr>
      <td>/api/sources/\$\{sourceId}/fields</td>
      <td>POST, PUT</td>
    </tr>

    <tr>
      <td>/api/sources/\$\{sourceId}/fields/\$\{fieldName}</td>
      <td>PUT, DELETE</td>
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th>Endpoint</th>
      <th>Method</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={3}>**23.2.15 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**23.2.14 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**23.2.13 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**23.2.12 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**23.2.11 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**23.2.10 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**23.2.9 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**23.2.8 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**23.2.7 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**23.2.6 API Updates**</td>
    </tr>

    <tr>
      <td>Various</td>

      <td />

      <td>We’ve added clarification to our provided Swagger API documentation to specify the security level required to perform each available operation.</td>
    </tr>

    <tr>
      <td colSpan={3}>**23.2.5 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**23.2.4 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**23.2.3 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**23.2.2 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**23.2.1 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**23.2 API Updates**</td>
    </tr>

    <tr>
      <td>
        /api/sources/export

        <br />

        /api/sources/import
      </td>

      <td>GET, PUT</td>

      <td>
        Use these new endpoints with parameter `ids` to specify one or more source for export and import:

        <br />

        * /api/sources/export?ids=sourceId1,sourceId2,sourceId3

        <br />

        or

        <br />

        * /api/sources/export?ids=sourceId1\&ids=sourceId2\&ids=sourceId3

        <br />

        Source payload includes:

        <br />

        * source object
        * fields
        * custom metrics
        * global settings
        * cache settings
        * related connections
      </td>
    </tr>

    <tr>
      <td>
        /api/dashboards/\{id}/comments

        <br />

        /api/dashboards/\{id}/comments/\{id}
      </td>

      <td>GET, POST, PUT, DELETE</td>

      <td>
        Use the comments API to manage comments associated with a dashboard and its widgets:

        <br />

        * GET /api/dashboards/\{id}/comments
        * GET /api/dashboards/\{id}/comments/\{id}
        * POST /api/dashboards/\{id}/comments/
        * PUT /api/dashboards/\{id}/comments/\{id}
        * DELETE /api/dashboards/\{id}/comments/\{id}
      </td>
    </tr>

    <tr>
      <td>/api/sources/\{source\_id}/unique-key</td>
      <td>GET, PUT</td>
      <td>Use to define and retrieve a unique key for non-hierarchical fields in data sources. The key can be a field or an array.</td>
    </tr>

    <tr>
      <td>/api/start-vis</td>
      <td>POST</td>

      <td>
        Use to execute `START_VIS` query via REST and get a resulting data set in the response.

        <br />

        <Warning>
          This is an experimental API.
        </Warning>
      </td>
    </tr>

    <tr>
      <td>/api/dashboards/convert-layout/</td>
      <td>POST</td>

      <td>
        Use to convert dashboards to responsive layout. On success, returns an array of dashboard ids converted. See Dashboard Layouts.

        <br />

        <Warning>
          This is an experimental API.
        </Warning>
      </td>
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th>Endpoint</th>
      <th>Method</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={3}>**23.1.14 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**23.1.13 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**23.1.12 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**23.1.11 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**23.1.10 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**23.1.9 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**23.1.8 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**23.1.7 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**23.1.6 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**23.1.5 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**23.1.4 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**23.1.3 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**23.1.2 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**23.1.1 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**Composer 23.1 API Updates**</td>
    </tr>

    <tr>
      <td>/api/dashboards/\{dashboard\_id}/reports</td>
      <td>PATCH</td>
      <td>Use to share, revoke, or change user access to a dashboard and its visuals. as a `VIEWER` or `EDITOR`.</td>
    </tr>

    <tr>
      <td>/api/dashboards/\{dashboard\_id}/reports</td>
      <td>POST</td>

      <td rowSpan={3}>
        Use the new field, `{"email": "user@example.com"}`, to schedule dashboard reports for non-Composer users.

        <br />

        Removed the deprecated field `sendOnlyToMe`.
      </td>
    </tr>

    <tr>
      <td>/api/dashboards/\{dashboard\_id}/reports/\{report\_id}</td>
      <td>GET</td>
    </tr>

    <tr>
      <td>
        /api/dashboards/\{dashboard\_id}/reports

        <br />

        /api/dashboards/\{dashboard\_id}/reports/\{id}
      </td>

      <td>PUT</td>
    </tr>

    <tr>
      <td>/api/export/rawdataforvisual</td>
      <td>POST</td>
      <td>Use to generate raw data export CSV and XLSX of your raw data for visuals. Replaces `/api/export/raw`.</td>
    </tr>

    <tr>
      <td>/api/export/visualdata</td>
      <td>POST</td>
      <td>Use to generate visual data export CSV and XLSX of your raw data for visuals. Replaces `/api/export/chartdata/{file_name}`.</td>
    </tr>

    <tr>
      <td>/api/sources/\{id}/dictionaries</td>
      <td>PUT</td>

      <td>
        Create and update your metadata dictionary for a source. Use MediaType `/multipart/form-data`.

        <br />

        Example:

        <br />

        `Field Label,ua_UK,en_GB`

        <br />

        `city,місто,city`

        <br />

        `county,округ,county`

        <br />

        `zip code,поштовий індекс,postcode`
      </td>
    </tr>

    <tr>
      <td>/api/sources/\{id}/dictionaries</td>
      <td>GET</td>
      <td>Returns a list of dictionaries with field labels for a source.</td>
    </tr>

    <tr>
      <td>/api/sources/\{id}/dictionaries/\{language}</td>
      <td>GET</td>
      <td>Returns a dictionary by the specified language for a source.</td>
    </tr>

    <tr>
      <td>/api/sources/\{id}/dictionaries/\{language}</td>
      <td>PUT</td>
      <td>Create and update a dictionary for the specified language for a source.</td>
    </tr>

    <tr>
      <td>/api/sources/\{id}/dictionaries</td>
      <td>DELETE</td>
      <td>Delete all dictionaries for a specified source.</td>
    </tr>

    <tr>
      <td>/api/sources/\{id}/dictionaries/\{language}</td>
      <td>DELETE</td>
      <td>Delete the dictionary for the specified language for a source.</td>
    </tr>
  </tbody>
</table>

<h3 id="api-updates-composer-v22">
  Composer v22
</h3>

<table>
  <thead>
    <tr>
      <th>Endpoint</th>
      <th>Method</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={3}>**22.4.14 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**22.4.13 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**22.4.12 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**22.4.11 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**22.4.10 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**22.4.9 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**22.4.8 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**22.4.7 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**22.4.6 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**22.4.5 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**22.4.4 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**22.4.3 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**22.4.2 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**22.4.1 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**22.4 API Updates**</td>
    </tr>

    <tr>
      <td>/api/sources/\{sourceId}/fields/</td>
      <td>POST, PUT</td>
      <td>Use `lookup` to set a dynamic field statistics overwrite. Specify `dataEntityId` and `originalFieldName` as a custom source of filter values.</td>
    </tr>

    <tr>
      <td>/api/sources/\{sourceId}/fields/\{fieldName}</td>
      <td>POST, PUT</td>
      <td>Use `lookup` to set a dynamic field statistics overwrite. Specify `dataEntityId` and `originalFieldName` as a custom source of filter values.</td>
    </tr>

    <tr>
      <td>/api/alerts/\{id}</td>
      <td>GET</td>
      <td>Returns a specific alert definition, identified by its ID. In a multi tenancy environment, respects Recipients rules.</td>
    </tr>

    <tr>
      <td>
        /api/inventory/\{type}/\{id}

        <br />

        /api/inventory

        <br />

        /api/user/permissions/dashboards/\{id}
      </td>

      <td>GET</td>
      <td>A new field, `accessLevel`, has been added to these endpoints to return users' access to a dashboard. These access levels can be `OWNER`, `EDITOR`, or `VIEWER`.</td>
    </tr>
  </tbody>
</table>

<h3 id="api-updates-composer-v8-4-and-earlier">
  Composer v8.4 and Earlier
</h3>

<table>
  <thead>
    <tr>
      <th>Endpoint</th>
      <th>Method</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={3}>**8.4.1 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**8.4 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th>Endpoint</th>
      <th>Method</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={3}>**8.3 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th>Endpoint</th>
      <th>Method</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={3}>**8.2 API Updates**</td>
    </tr>

    <tr>
      <td>/api/sources/</td>

      <td />

      <td>
        Actions taken using these endpoints trigger a source `modifiedDate` update:

        <br />

        * `POST /api/sources/{sourceId}`
        * `POST /api/sources/{sourceId}/fields`
        * `PUT, DELETE /api/sources/{sourceId}/fields/{fieldName}`
        * `POST /api/sources/{sourceId}/custom-metrics`
        * `PUT, DELETE /api/sources/{sourceId}/custom-metrics/{customMetricName}`
        * `PUT /api/sources/{sourceId}/global-settings`
        * `PUT /api/sources/{sourceId}/cache-settings`
      </td>
    </tr>

    <tr>
      <td>/api/connections/\{id}</td>
      <td>POST</td>
      <td>When you create a connection, use the `?connectionTypeMatching=BY_TYPE_AND_PARAMETERS` URL parameter to omit the matching by `connectionTypeId`; instead, use matching by combining `type` + `subStorageType` + `Connection Parameter Keys`.</td>
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th>Endpoint</th>
      <th>Method</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={3}>**8.1 API Updates**</td>
    </tr>

    <tr>
      <td>/api/sources/</td>
      <td>PUT, GET, DELETE</td>

      <td>
        Use the Composer API to remove a field or change a field type for a field in your source if it is not in use by a global filter.

        <br />

        * PUT `/api/sources/{sourceId}`
        * PUT `/api/sources/{sourceId}/fields/{fieldName}`
        * DELETE `/api/sources/{sourceId}/fields/{fieldName}`
        * GET `/api/sources/{sourceId}/fields/{fieldName}/usage`
      </td>
    </tr>

    <tr>
      <td>/api/user/interpolate</td>
      <td>POST</td>
      <td>Use `/api/user/interpolate` to send custom attribute names and get custom attribute values.</td>
    </tr>

    <tr>
      <td>/api/favorites/</td>
      <td>POST</td>
      <td>Favorite a visual. Specify an `inventoryItemId` and visual in `inventoryItemType`.</td>
    </tr>

    <tr>
      <td>/api/favorites/\{favoriteID}</td>
      <td>DELETE</td>
      <td>Remove the favorite indication from the specified `{favoriteID}`.</td>
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th>Endpoint</th>
      <th>Method</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={3}>**8.0 API Updates**</td>
    </tr>

    <tr>
      <td>api/inventory?type=VISUAL</td>
      <td>GET</td>
      <td>Returns information about visuals for which the user has `READ` permission. If the user has no `READ` access to any visuals, an empty list is returned.</td>
    </tr>
  </tbody>
</table>

<h3 id="api-updates-composer-v7-10-and-earlier">
  Composer v7.10 and Earlier
</h3>

<table>
  <thead>
    <tr>
      <th>Endpoint</th>
      <th>Method</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={3}>**7.10.23 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**7.10.22 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**7.10.21 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**7.10.20 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**7.10.19 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**7.10.18 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**7.10.17 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**7.10.16 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**7.10.15 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**7.10.14 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**7.10.13 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**7.10.12 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**7.10.11 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**7.10.10 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**7.10.9 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**7.10.8 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**7.10.7 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**7.10.6 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**7.10.5 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**7.10.4 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**7.10.3 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**7.10.2 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**7.10.1 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**7.10 API Updates**</td>
    </tr>

    <tr>
      <td>/api/visuals</td>
      <td>GET</td>
      <td>The `tags` experimental request parameter was removed from the `GET /api/visuals` endpoint.</td>
    </tr>

    <tr>
      <td>/api/sources/</td>
      <td>POST</td>
      <td>Use to create a source and control the list of native fields added to the source definition by specifying the list of native fields in the request body. When you create a source using this endpoint, the custom metric Volume is created by default, and Global settings and Cache settings are populated with default values.</td>
    </tr>

    <tr>
      <td>/api/sources/</td>
      <td>GET</td>
      <td>Use to return a list of all sources, paginated.</td>
    </tr>

    <tr>
      <td>/api/sources/\{sourceId}</td>
      <td>PUT</td>
      <td>Use to update a source.</td>
    </tr>

    <tr>
      <td>/api/sources/\{sourceId}</td>
      <td>GET</td>
      <td>Use to return a specified source with the list of native fields.</td>
    </tr>

    <tr>
      <td>/api/sources/\{sourceId}</td>
      <td>DELETE</td>
      <td>Use to delete a specified source.</td>
    </tr>

    <tr>
      <td>/api/sources/\{sourceId}/features</td>
      <td>GET</td>
      <td>Use to return the features available for the specified source.</td>
    </tr>

    <tr>
      <td>/api/sources/\{sourceID}/global-settings</td>
      <td>GET</td>
      <td>Use to return global settings for the specified source. Requires `read` or `data_access` permissions for the source.</td>
    </tr>

    <tr>
      <td>/api/sources/\{sourceID}/global-settings</td>
      <td>PUT</td>
      <td>Use to update global settings for the specified source. Requires `write` permissions for the source.</td>
    </tr>

    <tr>
      <td>/api/uploads/preview</td>
      <td>POST</td>
      <td>Use to view a preview of sample file data.</td>
    </tr>

    <tr>
      <td>/api/uploads/\{id}/data/</td>
      <td>DELETE</td>
      <td>Use to delete all data stored in a file upload.</td>
    </tr>

    <tr>
      <td>/api/uploads/\{id}/data/</td>
      <td>POST</td>
      <td>Use to add data to the file upload. The file structure sent must match the existing validated format and structure.</td>
    </tr>

    <tr>
      <td>/api/uploads/\{id}/data/</td>
      <td>PUT</td>
      <td>Use to replace data in the file upload. The file structure sent must match the existing validated format and structure.</td>
    </tr>

    <tr>
      <td>/api/sources/SOURCE\_ID/meta/visuals</td>
      <td>GET</td>
      <td>`/api/sources/SOURCE_ID/meta/visuals` has been renamed `/api/sources/{source_id}/visual-types`. The functionality of this endpoint is unchanged.</td>
    </tr>

    <tr>
      <td>/api/sources/SOURCE\_ID/meta/visuals/\{VISUALIZATION\_ID}</td>
      <td>GET</td>
      <td>`/api/sources/SOURCE_ID/meta/visuals/{VISUALIZATION_ID}` has been renamed `/api/sources/{source_id}/visual-types/{VISUALIZATION_ID_/initial-visual`. The functionality of this endpoint is unchanged.</td>
    </tr>

    <tr>
      <td>/api/sources/SOURCE\_ID/meta/variables</td>
      <td>GET</td>
      <td>`/api/sources/SOURCE_ID/meta/variables` has been renamed `/api/sources/{source_id}/visual-types/variables-values`. The functionality of this endpoint is unchanged.</td>
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th>Endpoint</th>
      <th>Method</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={3}>**7.9 API Updates**</td>
    </tr>

    <tr>
      <td>
        /api/sources/

        <br />

        /api/export/

        <br />

        /api/stream/
      </td>

      <td />

      <td>
        Composer now supports permissions to allow source data access. Existing users with READ permission on a source are given DATA ACCESS permission for that source on upgrade to v7.9.

        <br />

        Endpoints that support DATA ACCESS:

        <br />

        * `GET /api/sources/SOURCE_ID/visual-types/VISUAL_TYPE_ID/initial-visual`
        * `GET /api/sources/SOURCE_ID/visual-types/variables-values`
        * `GET /api/sources/{sourceId}/features`
        * `GET /api/sources/SOURCE_ID/fields/FIELD_NAME/statistics/total`
        * `GET /api/sources/SOURCE_ID/fields/FIELD_NAME/statistics/distinct-values`
        * `POST /api/export/chartdata/{file_name}`
        * `POST /api/export/csv/raw`
        * `POST /api/stream/search`
        * `GET /api/stream/search/{sourceId}/facet/{attribute}`

        <br />

        Endpoints that support DATA ACCESS or READ permissions:

        <br />

        * `GET /api/sources/SOURCE_ID/visual-types`
      </td>
    </tr>

    <tr>
      <td>/api/visualizations/libs</td>

      <td />

      <td>
        Visualization library endpoints used by the CLI and deprecated in Composer v6.9 have been removed. These include:

        <br />

        * `GET /api/visualizations/libs`
        * `POST /api/visualizations/libs`
        * `DELETE /api/visualizations/libs/{id}`
        * `GET /api/visualizations/libs/{id}/*`
      </td>
    </tr>

    <tr>
      <td>/user/source-acl/</td>

      <td />

      <td>`/user/source-acl` is now removed from Composer. It was deprecated in a previous release.</td>
    </tr>

    <tr>
      <td>/user/source-acl/\{sourceID}</td>

      <td />

      <td>`/user/source-acl/{sourceID}` is now removed from Composer. It was deprecated in a previous release.</td>
    </tr>

    <tr>
      <td>/api/inventory/</td>

      <td />

      <td>
        The endpoint `/api/inventory/` has been expanded to return additional information about dashboards and sources.

        <br />

        Send a parameter `type` with your query to return related data.

        <br />

        * DASHBOARD - Returns a list of dashboard inventory items and `associatedItems` for each dashboard.
        * SOURCE - Returns a list `AssociatedItemResource` information.
        * If no `type` is sent, all dashboard items are returned. This feature will be removed in a future release.
      </td>
    </tr>

    <tr>
      <td>/api/users/</td>
      <td>GET</td>
      <td>The API response for GET `/api/users/` using `application/vnd.composer.v3+json` media type has been changed.</td>
    </tr>

    <tr>
      <td>/api/sources/\$\{sourceId}/fields/\$\{fieldname}</td>
      <td>DELETE</td>
      <td>Validation updates prevent you from removing a field from a source if the field is used by filters, cross-source links, join configurations, or actions.</td>
    </tr>

    <tr>
      <td>/api/sources/\$\{sourceId}</td>
      <td>PUT</td>
      <td>Validation updates prevent you from removing a field from a source if the field is used by filters, cross-source links, join configurations, or actions.</td>
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th>Endpoint</th>
      <th>Method</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={3}>**7.8 API Updates**</td>
    </tr>

    <tr>
      <td>/api/sources/\<source-id>/expression-syntax/</td>
      <td>GET</td>

      <td>
        Row label expressions called using `/api/sources/<source-id>/expression-syntax/` now return full text labels for each operator. This includes:

        <br />

        * Subtract
        * Less than or equal to
        * Greater than
        * Multiply
        * Not equal to
        * Greater than or equal to
        * Less than
        * Add
        * Divide
        * Equal to
      </td>
    </tr>

    <tr>
      <td>/api/users/</td>
      <td>GET</td>
      <td>Call `/api/users/` to return the user `name` and user `id` for all users. Use `application/vnd.composer.v3.lightweight+json` Media Type.</td>
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th>Endpoint</th>
      <th>Method</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={3}>**7.7 API Updates**</td>
    </tr>

    <tr>
      <td>/api/dashboards/\{id}/key</td>
      <td>GET</td>

      <td>
        This API was deprecated in release v6.9 and has now been removed from the platform along with other previously removed Security Keys endpoints.

        <br />

        Use Trusted Access instead for all embedded workflows. See Trusted Access.
      </td>
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th>Endpoint</th>
      <th>Method</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={3}>**7.6 API Updates**</td>
    </tr>

    <tr>
      <td>ROLE\_MANAGE\_VISUALIZATION\_TEMPLATES</td>

      <td />

      <td>The group privilege `ROLE_MANAGE_VISUALIZATION_TEMPLATES` is now `ROLE_ADMINISTER_VISUAL_TYPES`.</td>
    </tr>

    <tr>
      <td>/api/actions</td>
      <td>GET</td>

      <td>
        Previously, `GET /api/actions` required `(MANAGE_ACTIONS and READ for the source)` privilege/permissions.

        <br />

        Now, with Composer 7.6, `GET /api/actions` requires `((MANAGE_ACTIONS or INVOKE_ACTIONS) and READ for the source)`.
      </td>
    </tr>

    <tr>
      <td>/api/visual-types/components/</td>

      <td />

      <td>New `/visual-types/components/` endpoints are now available.</td>
    </tr>

    <tr>
      <td>/api/visual-types/</td>

      <td />

      <td>`visualizationId` has been renamed in `/visual-types/` to `visualTypeId`.</td>
    </tr>

    <tr>
      <td>/api/dashboards/\{id}/key</td>
      <td>GET</td>
      <td>This API was deprecated in release v6.9 and cannot be used with the API privilege `ROLE_SHARE_DASHBOARDS`, which has been removed.</td>
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th>Endpoint</th>
      <th>Method</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={3}>**7.5 API Updates**</td>
    </tr>

    <tr>
      <td>/api/trusted-access/pull/tokens</td>
      <td>POST</td>
      <td>Use to generate a trusted access token for a user, specifying the Composer user name. The user must already exist, and have an active Composer user account (unless you are using LDAP with automatic provisioning for Composer).</td>
    </tr>

    <tr>
      <td>/api/trusted-access/push/tokens</td>
      <td>POST</td>

      <td>
        Use to generate a trusted access token based on user context, optionally group membership, and user attributes, for existing Composer accounts.

        <br />

        If the user exists in Composer, the user is updated.

        <br />

        If the user does not exist in Composer, this creates the user.
      </td>
    </tr>

    <tr>
      <td>/api/trusted-access/token</td>

      <td />

      <td>
        Deprecated.

        <br />

        Use `/api/trusted-access/pull/tokens`. This is primarily a name change for the endpoint; payloads and functionality remain unchanged.
      </td>
    </tr>

    <tr>
      <td>/api/sources/\{id}</td>
      <td>PUT/POST</td>
      <td>You can no longer manually set the "version": `{integer}` of a source object when using `PUT api/sources/{id}` OR `POST api/sources`. Version is a system controlled variable which cannot be set manually.</td>
    </tr>

    <tr>
      <td>/api/user/switch/\{accountId}</td>

      <td />

      <td>
        Deprecated.

        <br />

        You can no longer authorize this API by a Trusted Access user token for switching Composer accounts. You can still generate a new Trusted Access user token by including the target Composer account information in the request.
      </td>
    </tr>

    <tr>
      <td>
        Removed deprecated security keys-related /api/sources endpoints:

        <br />

        GET /api/sources/\{id}/key

        <br />

        GET /api/sources/key

        <br />

        DELETE /api/sources/remove/\{id}
      </td>

      <td />

      <td>These APIs were deprecated in release v6.9 and have now been removed from the platform. Use Trusted Access instead for all embedded workflows.See Trusted Access. For more information about embedding Composer components, see Embed Composer Components Using JavaScript and Trusted Access.</td>
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th>Endpoint</th>
      <th>Method</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={3}>**7.4 API Updates**</td>
    </tr>

    <tr>
      <td>/api/sources/\{id}</td>
      <td>PUT</td>

      <td>
        Use to upload sources using the object's ID while retaining the object ID when migrating from one environment to another.

        <br />

        Use to update sources using the object’s ID while retaining the object ID when migrating from one environment to another.

        <br />

        You must have the `CanCreate{Object}` privilege.
      </td>
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th>Endpoint</th>
      <th>Method</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={3}>**7.3 API Updates**</td>
    </tr>

    <tr>
      <td>/api/connections/\{id}</td>
      <td>PUT</td>
      <td>Create a connection using a predefined object ID.</td>
    </tr>

    <tr>
      <td>/api/sources/\{id}</td>
      <td>PUT</td>

      <td>
        New endpoint.

        <br />

        Use to upload sources using the object's ID while retaining the object ID migrating from one environment to another.

        <br />

        You must have the `CanCreate{Object}` privilege.
      </td>
    </tr>

    <tr>
      <td>/api/visuals/\{id}</td>
      <td>PUT</td>

      <td>
        Use to create a visual using a predefined object ID.

        <br />

        You must have the `CanCreate{Object}` privilege.
      </td>
    </tr>

    <tr>
      <td>/api/dashboards/\{id}</td>
      <td>PUT</td>

      <td>
        Use to create a dashboard using a predefined object ID.

        <br />

        You must have the `CanCreate{Object}` privilege.
      </td>
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th>Endpoint</th>
      <th>Method</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={3}>**7.2 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th>Endpoint</th>
      <th>Method</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={3}>**7.1 API Updates**</td>
    </tr>

    <tr>
      <td>/api/export/generate/rawdata</td>
      <td>POST</td>
      <td>This endpoint has been removed. Use `/api/export/csv/raw` instead.</td>
    </tr>

    <tr>
      <td>/api/dashboards/\*</td>
      <td>all</td>

      <td>
        The API v1 (`application/vnd.composer.dashboard.v1+json`) behavior of the `/api/dashboards/*` endpoint has been removed. Use the new version of the endpoint in the v2 version of the API (`application/vnd.composer.dashboard.v2+json`) or `application/vnd.composer.v2` instead. Errors will result if you attempt to use `application/vnd.composer.dashboard.v1+json`.

        <br />

        <Note>
          When no `content-type` header is specified, Composer defaults to using `application/vnd.composer.dashboard.v2+json`.
        </Note>
      </td>
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th>Endpoint</th>
      <th>Method</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={3}>**7.0 API Updates**</td>
    </tr>

    <tr>
      <td>/api/materialized-views</td>
      <td>GET</td>
      <td>A new, optional parameter, `sourceId={<data-source-id>}`, has been added in this release. Use this parameter to obtain a list of materialized views for a specific data source.</td>
    </tr>

    <tr>
      <td>/api/dashboards/import</td>
      <td>POST</td>

      <td>
        A new query parameter, `strategy`, has been added for this endpoint. Valid values can be `OVERWRITE` or `USE_EXISTING_OR_CREATE`.

        <br />

        * Specify `OVERWRITE` to implement the new overwrite import policy.
        * Specify `USE_EXISTING_OR_CREATE` to continue to use the existing import policy (importing the dashboard with a slightly altered name). This is the default value and will be used if `strategy` is not specified.
      </td>
    </tr>
  </tbody>
</table>

<h3 id="api-updates-composer-v6-9-and-earlier">
  Composer v6.9 and Earlier
</h3>

<table>
  <thead>
    <tr>
      <th>Endpoint</th>
      <th>Method</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={3}>**6.9.29 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**6.9.28 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**6.9.27 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**6.9.26 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**6.9.25 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**6.9.24 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**6.9.23 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**6.9.22 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**6.9.21 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**6.9.20 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**6.9.19 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**6.9.18 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**6.9.17 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**6.9.16 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**6.9.15 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**6.9.14 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**6.9.13 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**6.9.12 API Updates**</td>
    </tr>

    <tr>
      <td>/api/sources/\{id}</td>
      <td>POST/PUT</td>
      <td>You can no longer manually set the "version": \{integer} of a source object when using PUT api/sources/\{id} OR POST api/sources. Version is a system controlled variable which cannot be set manually.</td>
    </tr>

    <tr>
      <td colSpan={3}>**6.9.11 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**6.9.10 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**6.9.9 API Updates**</td>
    </tr>

    <tr>
      <td>/api/connections/\{id}</td>
      <td>PUT</td>
      <td>Create a connection using a predefined object ID.</td>
    </tr>

    <tr>
      <td>/api/sources/\{id}</td>
      <td>PUT</td>

      <td>
        New endpoint.

        <br />

        Use to upload sources using the object's ID while retaining the object ID when migrating from one environment to another.

        <br />

        You must have the `CanCreate{Object}` privilege.
      </td>
    </tr>

    <tr>
      <td>/api/visuals/\{id}</td>
      <td>PUT</td>

      <td>
        Use to create a visual using a predefined object ID.

        <br />

        You must have the `CanCreate{Object}` privilege.
      </td>
    </tr>

    <tr>
      <td>/api/dashboards/\{id}</td>
      <td>PUT</td>

      <td>
        Use to create a dashboard using a predefined object ID.

        <br />

        You must have the `CanCreate{Object}` privilege.
      </td>
    </tr>

    <tr>
      <td colSpan={3}>**6.9.8 API Updates**</td>
    </tr>

    <tr>
      <td colSpan={3}>None.</td>
    </tr>

    <tr>
      <td colSpan={3}>**6.9.7 API Updates**</td>
    </tr>

    <tr>
      <td colSpan={3}>None.</td>
    </tr>

    <tr>
      <td colSpan={3}>**6.9.6 API Updates**</td>
    </tr>

    <tr>
      <td colSpan={3}>None.</td>
    </tr>

    <tr>
      <td colSpan={3}>**6.9.5 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**6.9.4 API Updates**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**6.9.3 API Updates**</td>
    </tr>

    <tr>
      <td>/api/sources</td>

      <td>
        DELETE

        <br />

        GET

        <br />

        PATCH

        <br />

        POST

        <br />

        PUT
      </td>

      <td>This endpoint is deprecated and will be removed in a future release.</td>
    </tr>

    <tr>
      <td>/api/upload</td>

      <td>
        DELETE

        <br />

        POST
      </td>

      <td>This endpoint is deprecated and will be removed in a future release.</td>
    </tr>

    <tr>
      <td colSpan={3}>**6.9.2 API Updates**</td>
    </tr>

    <tr>
      <td>/api/dashboards/import</td>
      <td>POST</td>

      <td>
        A new query parameter, `strategy`, has been added for this endpoint. Valid values can be `OVERWRITE` or `USE_EXISTING_OR_CREATE`.

        <br />

        * Specify `OVERWRITE` to implement the new overwrite import policy.
        * Specify `USE_EXISTING_OR_CREATE` to continue to use the existing import policy (importing the dashboard with a slightly altered name). This is the default value and will be used if `strategy` is not specified.
      </td>
    </tr>

    <tr>
      <td colSpan={3}>**6.9.1 API Updates**</td>
    </tr>

    <tr>
      <td>/api/materialized-views</td>
      <td>GET</td>
      <td>A new, optional parameter, `sourceId={<data-source-id>}`, has been added in this release. Use this parameter to obtain a list of materialized views for a specific data source.</td>
    </tr>

    <tr>
      <td colSpan={3}>**6.9 API Updates**</td>
    </tr>

    <tr>
      <td>application/vnd.composer.v3+json</td>
      <td>---</td>

      <td>
        A new media type, `application/vnd.composer.v3+json` is introduced in this release. The media type `application/vnd.composer.v2+json` is deprecated and will be removed in a future release. insightsoftware recommends using the `application/vnd.composer.v3+json` media type for all API calls.

        <br />

        The difference between the two media types is primarily in the response of listing endpoints.
      </td>
    </tr>

    <tr>
      <td>/api (/composer/api)</td>
      <td>GET</td>
      <td>This API endpoint is now deprecated and will be removed from the product in a future release.</td>
    </tr>

    <tr>
      <td>/api/alerts</td>

      <td>
        GET

        <br />

        PUT

        <br />

        DELETE

        <br />

        PATCH

        <br />

        POST
      </td>

      <td>A new experimental API is introduced in this release that can be used to alert your end users when a metric reaches a specified threshold. No UI support for this feature is provided at this time. See Manage Alerts.</td>
    </tr>

    <tr>
      <td>/api/upload</td>

      <td>
        DELETE

        <br />

        POST
      </td>

      <td>This API endpoint has been deprecated and will be removed in a future release.</td>
    </tr>

    <tr>
      <td>/api/visuals/\<visualId></td>

      <td>
        GET

        <br />

        PUT

        <br />

        DELETE
      </td>

      <td>The visual permissions for a user are now verified when this API endpoint is used to retrieve, update, or delete a visual.</td>
    </tr>

    <tr>
      <td>/api/visuals/\<visualId>/acls</td>
      <td>GET</td>
      <td>This new endpoint can be used to list the users and groups for which visual permissions have been defined.</td>
    </tr>

    <tr>
      <td>/api/visuals/\<visualId>/acls/bulk</td>
      <td>PATCH</td>
      <td>This endpoint can now be used to grant or revoke visual permissions. However, the `ownerType=Source` property can no longer be specified because permissions to view or manage a visual are no longer tied to your permissions for its data source. However, read permissions for the visual's data source are required to see data in the visual.</td>
    </tr>

    <tr>
      <td rowSpan={2}>/api/visuals</td>
      <td>GET</td>

      <td>
        The following fields in the response payload are deprecated and will be removed in a future release.

        <br />

        * `enabled`
        * `ownerType`
        * `name` (use `visualName` instead)
        * `dashboardLinks` (this field is now defined and stored in the new dashboard API response payload)
      </td>
    </tr>

    <tr>
      <td>
        PUT

        <br />

        DELETE

        <br />

        POST
      </td>

      <td>
        The following fields in the response payload of all other `/api/visuals` endpoints are deprecated and will be removed in a future release.

        <br />

        * `enabled`
        * `ownerType`
        * `lastModified` (use `lastModifiedDate` instead)
        * `ownerSourceId` (use `source.sourceId` instead)
        * `name` (use `visualName` instead)
        * `dashboardLinks` ((this field is now defined and stored in the new dashboard API response payload)
      </td>
    </tr>

    <tr>
      <td>description</td>
      <td>---</td>
      <td>A new property called `description` is added to the visual payload.</td>
    </tr>

    <tr>
      <td>/api/visuals/source/\<sourceId>/summary</td>
      <td>GET</td>
      <td>This API endpoint now checks for READ permission to the data source when reading a summary of all the visual defaults.</td>
    </tr>

    <tr>
      <td>/api/user/permissions/visuals/\<visualId></td>
      <td>GET</td>
      <td>This new endpoint can be used to retrieve a user's permissions for a visual.</td>
    </tr>

    <tr>
      <td>/api/visdefs/\<sourceId></td>
      <td>---</td>
      <td>This API endpoint has now been removed from the product. It was deprecated in a previous release.</td>
    </tr>

    <tr>
      <td>/api/visdefs/default/\<sourceId></td>
      <td>---</td>
      <td>This API endpoint has now been removed from the product. It was deprecated in a previous release.</td>
    </tr>

    <tr>
      <td>/api/visdefs/default/\<sourceId>/\<visualId></td>
      <td>GET</td>
      <td>This API endpoint now checks for READ permission to the data source when generating a single visual default.</td>
    </tr>

    <tr>
      <td rowSpan={2}>/api/dashboards/\*</td>

      <td>
        DELETE

        <br />

        GET

        <br />

        POST

        <br />

        PUT
      </td>

      <td>This endpoint in the v1 version of the API (`application/vnd.composer.dashboard.v1+json`) is deprecated and will be removed in a future release. Use the new version of the endpoint in the v2 version of the API (`application/vnd.composer.dashboard.v2+json`) instead.</td>
    </tr>

    <tr>
      <td>
        DELETE

        <br />

        GET

        <br />

        PUT
      </td>

      <td>
        The new `/api/dashboards` API endpoint no longer relies on visuals. Instead, it uses widgets.

        <br />

        * The `visualizations` container is renamed to `widgets`.
        * The new `widgets` array contains `widget` objects, which contain only widget-specific information: `id`, `name`, `description`, `layout`, `visualId`, and `dashboardLink`.

        <br />

        In addition, the `bookmarksMap` object returned in the response when using the v3 version of the Composer API (`application/vnd.composer.v3+json`) has been renamed `content`.

        <br />

        <Note>
          The `/api/dashboard` family of API endpoints were updated with a new payload in this release. To use `vnd.composer.dashboards.v1+json` for backward compatibility, including the use of the `bookmarksMap` object (instead of the new `content` object), turn on the `dashboard-v1-api` variable on the Server-Level Variables page (only a Composer supervisor can make this change). See Server-Level Variables.
        </Note>
      </td>
    </tr>

    <tr>
      <td>/api/visualizations/libs/\*</td>

      <td>
        DELETE

        <br />

        GET

        <br />

        POST

        <br />

        PUT
      </td>

      <td>The `/api/visualizations/libs` endpoint is deprecated and will be removed in a future release. Use the custom chart CLI instead. See Maintain Custom Charts Using the Custom Chart CLI.</td>
    </tr>

    <tr>
      <td>/api/sources/\<id>/key</td>
      <td>GET</td>
      <td rowSpan={3}>These security-related endpoints are deprecated and will be removed in a future release. Use Trusted Access instead for all embedded workflows. See Trusted Access and Embed Components Using JavaScript and Trusted Access.</td>
    </tr>

    <tr>
      <td>/api/sources/remove/\<id></td>
      <td>DELETE</td>
    </tr>

    <tr>
      <td>/api/sources/key</td>
      <td>GET</td>
    </tr>

    <tr>
      <td>/api/screenshot/\*</td>

      <td>
        GET

        <br />

        POST

        <br />

        PUT
      </td>

      <td>The screenshot-related endpoints are deprecated and will be removed in a future release.</td>
    </tr>

    <tr>
      <td>/oauth/authorize</td>
      <td>GET</td>
      <td>This endpoint is deprecated and will be removed in a future release. Use Trusted Access instead. See Trusted Access API Endpoints.</td>
    </tr>

    <tr>
      <td>/oauth2/client</td>

      <td>
        DELETE

        <br />

        GET

        <br />

        POST

        <br />

        PUT
      </td>

      <td>This endpoint is deprecated and will be removed in a future release. Use Trusted Access instead. See Trusted Access API Endpoints.</td>
    </tr>

    <tr>
      <td>/oauth2/token</td>

      <td>
        DELETE

        <br />

        GET

        <br />

        POST
      </td>

      <td>This endpoint is deprecated and will be removed in a future release. Use Trusted Access instead. See Trusted Access API Endpoints.</td>
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th>Endpoint</th>
      <th>Method</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={3}>**6.8 API Updates**</td>
    </tr>

    <tr>
      <td>OpenAPI Updates</td>
      <td>---</td>
      <td>The Composer API specification is now generated in OpenAPI 3.0 format.</td>
    </tr>

    <tr>
      <td>Group Updates</td>
      <td>---</td>
      <td>Groups can no longer be transferred to a different account using the API.</td>
    </tr>

    <tr>
      <td>/api/export/generate/rawdata</td>
      <td>---</td>
      <td>This endpoint is deprecated and will be removed in a future release. Use `/api/export/csv/raw` instead.</td>
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th>Endpoint</th>
      <th>Method</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={3}>**6.7 API Updates**</td>
    </tr>

    <tr>
      <td>/api/keysets/upload</td>
      <td>POST</td>
      <td>This new endpoint creates a keyset from a CSV file. See Upload Keyset Data From a CSV File Using the API.</td>
    </tr>

    <tr>
      <td>/api/keysets/upload/\<keyset-id></td>
      <td>PUT</td>
      <td>This new endpoint updates a keyset from a CSV file. See Update Keyset Values From a CSV File Using the API.</td>
    </tr>

    <tr>
      <td rowSpan={3}>/api/dashboards/\<dashboard-ID>/interactivity</td>
      <td>GET</td>
      <td>This new endpoint returns the dashboard's interactivity profile. If you do not have authorization for a dashboard, errors are returned.</td>
    </tr>

    <tr>
      <td>PUT</td>
      <td>This new endpoint saves a dashboard's interactivity profile.</td>
    </tr>

    <tr>
      <td>DELETE</td>
      <td>This new endpoint deletes a dashboard's interactivity profile.</td>
    </tr>

    <tr>
      <td>/api/dashboards/interactivity</td>
      <td>GET</td>
      <td>This new endpoint lists the existing dashboard interactivity profiles.</td>
    </tr>

    <tr>
      <td>/api/dashboard/\<dashboard-ID>?interactivityProfile=\{linked | readonly | interactive}</td>
      <td>GET</td>

      <td>
        This new endpoint returns the dashboard payload with one of the following three profile names:

        <br />

        * `linked`: Uses the dashboard interactivity profile set for the dashboard.
        * `readonly`: Overrides the dashboard interactivity profile, setting all visual interactivity settings to `false`, so users can view the dashboard and its visuals, but not interact with them.
        * `interactive`: Overrides the dashboard interactivity profile and all visual interactive settings to `true`, so users can view and interact with the dashboard and its visuals. This is the opposite of `readonly`.
      </td>
    </tr>

    <tr>
      <td>/api/sources/\<source-ID>/fields/meta</td>
      <td>GET</td>
      <td>This new endpoint is an experimental endpoint that returns information about all the fields and metrics in a data source.</td>
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th>Endpoint</th>
      <th>Method</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={3}>**6.6 API Updates**</td>
    </tr>

    <tr>
      <td>Group privilege renamed</td>
      <td colSpan={2}>The API privilege **ROLE\_MANAGE\_VISUALS** was renamed to **ROLE\_ADMINISTER\_VISUALS**. Customers who use the API to manage groups must manually make this change wherever **ROLE\_MANAGE\_VISUALS** is currently used.</td>
    </tr>

    <tr>
      <td>/api/dashboards/\<dashboard-id>/acls/bulk</td>
      <td>PATCH</td>
      <td>This new endpoint assigns permissions for a dashboard to a list of security identities (groups, users, accounts).</td>
    </tr>

    <tr>
      <td>/api/sources/\<source-id>/acls/bulk</td>
      <td>PATCH</td>
      <td>This new endpoint assigns permissions for a data source to a list of security identities (groups, users, accounts).</td>
    </tr>

    <tr>
      <td>/api/user/permissions/visuals/\<visual-id></td>
      <td>GET</td>
      <td>This new endpoint retrieves the permissions for a visual for the currently logged in user.</td>
    </tr>

    <tr>
      <td>/api/visuals</td>
      <td>GET</td>
      <td>The payload from this API now can include permission information for the visual, if the query parameter `includePermissions=true` is included, enabling this capability.</td>
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th>Endpoint</th>
      <th>Method</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={3}>**6.5 API Updates**</td>
    </tr>

    <tr>
      <td>/api/trusted-access/clients</td>
      <td>GET</td>
      <td>Returns all the Trusted Access client information in the metadata. Included with this information is the access token validity time (in seconds), client ID, client name, client secret expiration time (in seconds), and the token authentication method. For a description of these, see Trusted Access Client Properties.</td>
    </tr>

    <tr>
      <td>/api/trusted-access/clients</td>
      <td>POST</td>
      <td>Creates a Trusted Access client. The request must specify the number of seconds for which the access token is valid and the client name. The client name must be unique. When you create the client, the client ID, client secret, secret expiration time, and the token authentication method are automatically generated.</td>
    </tr>

    <tr>
      <td>/api/trusted-access/clients/\<id></td>
      <td>GET</td>
      <td>Returns the Trusted Access client information for a specific client. The request must specify the client ID.</td>
    </tr>

    <tr>
      <td>/api/trusted-access/clients/\<id></td>
      <td>DELETE</td>
      <td>Deletes a specific Trusted Access client. The request must specify the client ID.</td>
    </tr>

    <tr>
      <td>/api/trusted-access/clients/\<id></td>
      <td>PATCH</td>
      <td>Updates the Trusted Access client information for a specific client. The request must specify the client ID and the number of seconds for which the access token is valid.</td>
    </tr>

    <tr>
      <td>/api/trusted-access/token</td>
      <td>POST</td>
      <td>Generates a new access token for a user. The request must specify the Composer user name. The user must already exist, and have an active Composer user account (unless you are using LDAP with automatic provisioning for Composer).</td>
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th>Endpoint</th>
      <th>Method</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={3}>**6.4 API Updates**</td>
    </tr>

    <tr>
      <td>/api/sources/\<source-id>/cache/visdata</td>
      <td>DELETE</td>
      <td>Clears the visual data cache.</td>
    </tr>

    <tr>
      <td>/api/sources/\<source-id>/cache/metadata</td>
      <td>DELETE</td>
      <td>Clears the metadata cache.</td>
    </tr>

    <tr>
      <td>/api/sources/\<source-id>/cache</td>
      <td>DELETE</td>
      <td>Clears both the visual and metadata caches.</td>
    </tr>

    <tr>
      <td rowSpan={2}>Source definition endpoints</td>
      <td>---</td>
      <td>A new boolean `cacheableMetadata` property indicates whether metadata caching is enabled for a data source. The existing `cacheable` property indicates whether caching, in general, is enabled for the data source.</td>
    </tr>

    <tr>
      <td>---</td>
      <td>A new `statsCached` property allows you to control metadata (field statistics) caching on a per-field basis. This property can be used to configure the field statistics look-up via materialized views (ignoring internal caches and redirecting the requests from the original source) and to improve the performance of statistics requests when precreated statistics data exists. Please contact your Technical Support representative to get guidance on how to configure this.</td>
    </tr>

    <tr>
      <td>/api/visdefs/\<source-id></td>
      <td>---</td>
      <td>This endpoint is deprecated. It is replaced by a new `/api/visuals/source/<source-id>/summary` endpoint. The response produced by the new endpoint has also changed to include a new `visualId` setting.</td>
    </tr>

    <tr>
      <td>/api/visuals/source/\<source-id>/summary</td>
      <td>GET</td>
      <td>This endpoint obtains the default visual definitions for a data source configuration.</td>
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th>Endpoint</th>
      <th>Method</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={3}>**6.3 API Updates**</td>
    </tr>

    <tr>
      <td>/api/user/permissions/sources</td>
      <td>GET</td>
      <td>Lists the permission levels for the logged in user for all data source configurations in the system.</td>
    </tr>

    <tr>
      <td>/api/user/permissions/sources/\<sourceid></td>
      <td>GET</td>
      <td>Retrieves the currently logged in user's source permissions for a data source.</td>
    </tr>

    <tr>
      <td>/api/sources/\<sourceid>/acls</td>
      <td>GET</td>
      <td>Retrieves a list of access rights for a data source. You can restrict the list to specific users, groups, or accounts using the `sidTypes` parameter. In addition, you can use the `returnSids` parameter to restrict the list so it retrieves only users, groups, or accounts with access to the data sources or to only users, groups, or accounts without access.</td>
    </tr>

    <tr>
      <td>/api/sources/\<sourceid>/acls/bulk</td>
      <td>PUT</td>
      <td>Grants or revokes permissions to a data source configuration a list of groups, users, or accounts.</td>
    </tr>

    <tr>
      <td>/api/sources/\<source-id>/security/attributes</td>
      <td>---</td>
      <td rowSpan={2}>These endpoints now support the specification of multiple groups for a data source column security filter.</td>
    </tr>

    <tr>
      <td>/api/sources/\<source-id>/security/attributes/\<id></td>
      <td>---</td>
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th>Endpoint</th>
      <th>Method</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={3}>**6.2 API Updates**</td>
    </tr>

    <tr>
      <td>Visual placement</td>
      <td>---</td>
      <td>An error is now produced when you try to place the same visual on a dashboard twice.</td>
    </tr>

    <tr>
      <td rowSpan={2}>/api/groups</td>

      <td />

      <td>The `sources` field is deprecated and will be removed in a future release.</td>
    </tr>

    <tr>
      <td />

      <td>The `configType` field is deprecated and will be removed in a future release.</td>
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th>Endpoint</th>
      <th>Method</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={3}>**6.1 API Updates**</td>
    </tr>

    <tr>
      <td>/api/sources/\<source-id>/security/filters</td>
      <td>---</td>
      <td>This endpoint is enhanced to support account and user security identifiers. In past releases, only group security identifiers were supported.</td>
    </tr>

    <tr>
      <td>/api/security/sids</td>
      <td>---</td>
      <td>This new endpoint is introduced to retrieve security ID information. The `sidTypes` parameter can be specified with this new endpoint to limit the type of security ID information retrieved. Valid values for `sidTypes` are `GROUP`, `USER`, `ACCOUNT`, or `ALL` (the default).</td>
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th>Endpoint</th>
      <th>Method</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={3}>**6.0 API Updates**</td>
    </tr>

    <tr>
      <td colSpan={3}>With this release, you can no longer use `<hostname>:8080/zoomdata/api/version`. This is no longer supported. Use `<hostname>:8080/composer/api/version` instead.</td>
    </tr>
  </tbody>
</table>

<h2 id="deprecated-and-removed-features">
  Deprecated and Removed Features
</h2>

<h3 id="deprecated-and-removed-features-composer-v26">
  Composer v26
</h3>

<h4 id="deprecated-and-removed-features-composer-v26-deprecated-features">
  Deprecated Features
</h4>

<table>
  <thead>
    <tr>
      <th>Title</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={2}>**26.2.1 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**26.2 Deprecated Features**</td>
    </tr>

    <tr>
      <td>UI Menu</td>
      <td>In environments where the enhanced-experience toggle has been enabled, the UI menu has been reconfigured into an always-available main menu. Access your content and navigate options using the [main menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/access#the-main-menu) or [home page](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/access#home-page).</td>
    </tr>

    <tr>
      <td>Top-Level Navigation</td>
      <td>In environments where the enhanced-experience toggle has been enabled, the top-level navigation option has been removed from the user interface. Access your content and navigate options using the [main menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/access#the-main-menu) or [home page](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/access#home-page).</td>
    </tr>

    <tr>
      <td>System Users Menu Option</td>
      <td>In environments where the enhanced-experience toggle has been enabled, the menu option **System Users** has been removed from the main menu UI. Users with appropriate privileges can instead access users using the **User** menu option, and groups using the **Groups** menu option.</td>
    </tr>

    <tr>
      <td>Multi-Tenancy Menu Option</td>
      <td>In environments where the enhanced-experience toggle has been enabled, the menu option **Multi-Tenancy** has been renamed **Tenants**. Use this option to create, access, and manage tenant accounts.</td>
    </tr>

    <tr>
      <td>Edit Tenant Work Area</td>

      <td>
        In environments where the enhanced-experience toggle has been enabled, the Edit Tenant work area has been redesigned. Switch between tenants to edit by selecting a different tenant from the tenant list in the Multi-Tenancy work area.

        <br />

        The **General** tab and tenant switching dropdown list have been removed.
      </td>
    </tr>

    <tr>
      <td>Zoom / Drill Down in the Context Menu</td>
      <td>In environments where the enhanced-experience toggle has been enabled, the context menu option users see when examining a visual has changed. **Zoom** has been renamed to **Drill Down**.</td>
    </tr>

    <tr>
      <td>Source Editor Improvements</td>
      <td>The **Joins** node label in the data source canvas has been renamed **Add Join**.</td>
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th>Title</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={2}>**26.1.3 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**26.1.2 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**26.1.1 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**26.1 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>
  </tbody>
</table>

<h4 id="deprecated-and-removed-features-composer-v26-removed-features">
  Removed Features
</h4>

<table>
  <thead>
    <tr>
      <th>Title</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={2}>**26.2.2 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**26.2.1 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**26.2 Removed Features**</td>
    </tr>

    <tr>
      <td>UI Menu</td>
      <td>In environments where the enhanced-experience toggle has been enabled, the UI menu has been reconfigured into an always-available main menu. Access your content and navigate options using the [main menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/access#the-main-menu) or [home page](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/access#home-page).</td>
    </tr>

    <tr>
      <td>Top-Level Navigation</td>
      <td>In environments where the enhanced-experience toggle has been enabled, the top-level navigation option has been removed from the user interface. Access your content and navigate options using the [main menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/access#the-main-menu) or [home page](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/access#home-page).</td>
    </tr>

    <tr>
      <td>System Users Menu Option</td>
      <td>In environments where the enhanced-experience toggle has been enabled, the menu option **System Users** has been removed from the main menu UI. Users with appropriate privileges can instead access users using the **User** menu option, and groups using the **Groups** menu option.</td>
    </tr>

    <tr>
      <td>Multi-Tenancy Menu Option</td>
      <td>In environments where the enhanced-experience toggle has been enabled, the menu option **Multi-Tenancy** has been renamed **Tenants**. Use this option to create, access, and manage tenant accounts.</td>
    </tr>

    <tr>
      <td>Edit Tenant Work Area</td>

      <td>
        In environments where the enhanced-experience toggle has been enabled, the Edit Tenant work area has been redesigned. Switch between tenants to edit by selecting a different tenant from the tenant list in the Multi-Tenancy work area.

        <br />

        The **General** tab and tenant switching dropdown list have been removed.
      </td>
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th>Title</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={2}>**26.1.3 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**26.1.2 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**26.1.1 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**26.1 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>
  </tbody>
</table>

<h3 id="deprecated-and-removed-features-composer-v25">
  Composer v25
</h3>

<h4 id="deprecated-and-removed-features-composer-v25-deprecated-features">
  Deprecated Features
</h4>

<table>
  <thead>
    <tr>
      <th>Title</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={2}>**25.4.5 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**25.4.4 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**25.4.3 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**25.4.2 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**25.4.1 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**25.4 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th>Title</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={2}>**25.3.8 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**25.3.7 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**25.3.6 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**25.3.5 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**25.3.4 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**25.3.3 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**25.3.2 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**25.3.1 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**25.3 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th>Title</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={2}>**25.2.10 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**25.2.9 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**25.2.8 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**25.2.7 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**25.2.6 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**25.2.5 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**25.2.4 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**25.2.3 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**25.2.2 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**25.2.1 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**25.2 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th>Title</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={2}>**25.1.11 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**25.1.10 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**25.1.9 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**25.1.8 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**25.1.7 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**25.1.6 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**25.1.5 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**25.1.4 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**25.1.3 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**25.1.2 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**25.1.1 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**25.1 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>
  </tbody>
</table>

<h4 id="deprecated-and-removed-features-composer-v25-removed-features">
  Removed Features
</h4>

<table>
  <thead>
    <tr>
      <th>Title</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={2}>**25.4.5 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**25.4.4 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**25.4.3 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**25.4.2 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**25.4.1 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**25.4 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th>Title</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={2}>**25.3.8 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**25.3.7 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**25.3.6 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**25.3.5 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**25.3.4 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**25.3.3 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**25.3.2 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**25.3.1 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**25.3 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th>Title</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={2}>**25.2.10 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**25.2.9 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**25.2.8 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**25.2.7 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**25.2.6 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**25.2.5 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**25.2.4 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**25.2.3 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**25.2.2 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**25.2.1 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**25.2 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th>Title</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={2}>**25.1.11 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**25.1.10 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**25.1.9 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**25.1.8 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**25.1.7 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**25.1.6 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**25.1.5 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**25.1.4 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**25.1.3 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**25.1.2 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**25.1.1 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**25.1 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>
  </tbody>
</table>

<h3 id="deprecated-and-removed-features-composer-v24">
  Composer v24
</h3>

<h4 id="deprecated-and-removed-features-composer-v24-deprecated-features">
  Deprecated Features
</h4>

<table>
  <thead>
    <tr>
      <th>Title</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={2}>**24.4.16 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**24.4.15 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**24.4.14 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**24.4.13 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**24.4.12 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**24.4.11 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**24.4.10 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**24.4.9 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**24.4.8 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**24.4.7 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**24.4.6 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**24.4.5 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**24.4.4 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**24.4.3 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**24.4.2 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**24.4.1 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**24.4 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th>Title</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={2}>**24.3.10 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**24.3.9 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**24.3.8 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**24.3.7 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**24.3.6 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**24.3.5 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**24.3.4 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**24.3.3 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**24.3.2 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**24.3.1 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**24.3 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th>Title</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={2}>**24.2.12 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**24.2.11 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**24.2.10 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**24.2.9 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**24.2.8 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**24.2.7 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**24.2.6 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**24.2.5 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**24.2.4 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**24.2.3 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**24.2.2 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**24.2.1 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**24.2 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th>Title</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={2}>**24.1.12 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**24.1.11 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**24.1.10 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**24.1.9 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**24.1.8 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**24.1.7 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**24.1.6 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**24.1.5 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**24.1.4 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**24.1.3 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**24.1.2 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**24.1.1 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**24.1 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>
  </tbody>
</table>

<h4 id="deprecated-and-removed-features-composer-v24-removed-features">
  Removed Features
</h4>

<table>
  <thead>
    <tr>
      <th>Title</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={2}>**24.4.16 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**24.4.15 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**24.4.14 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**24.4.13 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**24.4.12 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**24.4.11 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**24.4.10 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**24.4.9 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**24.4.8 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**24.4.7 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**24.4.6 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**24.4.5 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**24.4.4 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**24.4.3 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**24.4.2 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**24.4.1 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**24.4 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th>Title</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={2}>**24.3.10 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**24.3.9 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**24.3.8 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**24.3.7 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**24.3.6 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**24.3.5 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**24.3.4 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**24.3.3 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**24.3.2 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**24.3.1 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**24.3 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th>Title</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={2}>**24.2.13 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**24.2.11 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**24.2.10 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**24.2.9 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**24.2.8 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**24.2.7 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**24.2.6 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**24.2.5 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**24.2.4 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**24.2.3 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**24.2.2 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**24.2.1 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**24.2 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th>Title</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={2}>**24.1.12 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**24.1.11 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**24.1.10 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**24.1.9 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**24.1.8 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**24.1.7 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**24.1.6 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**24.1.5 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**24.1.4 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**24.1.3 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**24.1.2 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**24.1.1 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**24.1 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>
  </tbody>
</table>

<h3 id="deprecated-and-removed-features-composer-v23">
  Composer v23
</h3>

<h4 id="deprecated-and-removed-features-composer-v23-deprecated-features">
  Deprecated Features
</h4>

<table>
  <thead>
    <tr>
      <th>Title</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={2}>**23.4.13 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**23.4.12 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**23.4.11 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**23.4.10 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**23.4.9 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**23.4.8 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**23.4.7 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**23.4.6 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**23.4.5 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**23.4.4 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**23.4.3 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**23.4.2 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**23.4.1 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**23.4 Deprecated Features**</td>
    </tr>

    <tr>
      <td>Tenancy and Default Account Changes</td>

      <td>
        * The **superaccount** work area is renamed to **Visual Data Discovery**.
        * The company tenant is no longer created by Composer for new installations, existing company tenants remain unchanged.
        * The default admin user is now the **system administrator** and has all supervisor user privileges, as a member of the **Visual Data Discovery** tenant.
        * The default **supervisor** user is no longer installed; add users to the **Supervisors** group instead.
        * Tenant Accounts are now known as Tenants in the user interface.
      </td>
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th>Title</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={2}>**23.3.14 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**23.3.13 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**23.3.12 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**23.3.11 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**23.3.10 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**23.3.9 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**23.3.8 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**23.3.7 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**23.3.6 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**23.3.5 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**23.3.4 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**23.3.3 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**23.3.2 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**23.3.1 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**23.3 Deprecated Features**</td>
    </tr>

    <tr>
      <td>Cloudmade for Map Visuals</td>

      <td>
        Cloudmade’s tile support is no longer available, and has been removed from map visuals.

        <br />

        Existing visuals that use the Cloudmade Tile Provider are migrated to Open Street Maps when you upgrade to this release or later.
      </td>
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th>Title</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={2}>**23.2.15 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**23.2.14 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**23.2.13 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**23.2.12 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**23.2.11 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**23.2.10 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**23.2.9 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**23.2.8 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**23.2.7 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**23.2.6 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**23.2.5 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**23.2.4 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**23.2.3 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**23.2.2 Deprecated Features**</td>
    </tr>

    <tr>
      <td>Alerts Icon</td>
      <td>The alerts icon is no longer present in dashboards for users who do not have the Create Alerts or Administer Alerts privilege.</td>
    </tr>

    <tr>
      <td colSpan={2}>**23.2.1 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**23.2 Deprecated Features**</td>
    </tr>

    <tr>
      <td>Materialized Views</td>
      <td>Materialized views are disabled by default. To enable, contact technical support for assistance.</td>
    </tr>

    <tr>
      <td>Connector Properties for Integer to Datetime Conversion in Timezone Offsets</td>
      <td>The properties `datasource.timestamp-millis-fields-names` and `datasource.timestamp-millis-fields-pattern` are deprecated and will be removed in a future release.</td>
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th>Title</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={2}>**23.1.14 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**23.1.13 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**23.1.12 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**23.1.11 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**23.1.10 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**23.1.9 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**23.1.8 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**Composer 23.1.7 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**23.1.6 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**23.1.5 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**23.1.4 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**23.1.3 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**23.1.2 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**23.1.1 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**23.1 Deprecated Features**</td>
    </tr>

    <tr>
      <td>Materialized Views API</td>
      <td>The Materialized Views API is deprecated. This API will be removed in a future release.</td>
    </tr>

    <tr>
      <td>Scheduled Dashboard Reports</td>
      <td>`sendOnlyToMe` is deprecated and will be removed in a future release.</td>
    </tr>

    <tr>
      <td>Raw Data Export Endpoint</td>
      <td>The endpoint `/api/export/csv/raw` is deprecated and will be removed in a future release. When used, returns payload as `DeprecatedRawDataExportResource`. Use `/api/export/rawdataforvisual` instead.</td>
    </tr>

    <tr>
      <td>Visual Data Export Endpoint</td>
      <td>The endpoint `/api/export/chartdata/{file_name}` is deprecated and will be removed in a future release. When used, returns payload as `DeprecatedVisualDataExportResource`. Use `/api/export/visualdata` instead.</td>
    </tr>

    <tr>
      <td>Admin Service</td>

      <td>
        The Admin Service microservice, used for capturing common logs, is deprecated and will be removed in a future release.

        <br />

        * For non-Kubernetes environments: Use the Consul UI to observe the general health state of your deployment. Adjust logging levels using the `service.properties` file or the Consul API.
        * For Kubernetes environments: Configuration management compatible with Kubernetes will replace the Admin Service microservice.

        <br />

        See How Do I Enable Debug Mode in Services?.
      </td>
    </tr>

    <tr>
      <td>Activity Logging</td>

      <td>
        Activity logging in `zoomdata-activity.log` is deprecated and will be removed in a future release.

        <br />

        Information previously captured in `zoomdata-activity.log` can be found in other log files such as `access.log`, `service.log`, and by using Composer's User Auditing feature.
      </td>
    </tr>
  </tbody>
</table>

<h4 id="deprecated-and-removed-features-composer-v23-removed-features">
  Removed Features
</h4>

<table>
  <thead>
    <tr>
      <th>Title</th>
      <th>Description</th>
      <th>Alternative</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={3}>**23.4.13 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**23.4.12 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**23.4.11 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**23.4.10 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**23.4.9 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**23.4.8 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**23.4.7 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**23.4.6 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**23.4.5 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**23.4.4 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**23.4.3 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**23.4.2 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**23.4.1 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**23.4 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th>Title</th>
      <th>Description</th>
      <th>Alternative</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={3}>**23.3.14 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**23.3.13 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**23.3.12 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**23.3.11 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**23.3.10 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**23.3.9 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**23.3.8 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**23.3.7 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**23.3.6 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**23.3.5 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**23.3.4 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**23.3.3 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**23.3.2 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**23.3.1 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />

      <td />
    </tr>

    <tr>
      <td colSpan={3}>**23.3 Removed Features**</td>
    </tr>

    <tr>
      <td>api/trusted-access/token</td>
      <td>The API `/api/trusted-access/token`, deprecated in an earlier release (Composer v7.5), is now removed.</td>
      <td>Use `/api/trusted-access/push/tokens` or `/api/trusted-access/pull/tokens` instead. See Trusted Access API Endpoints.</td>
    </tr>

    <tr>
      <td>`/api/visualizations/*` and API for Visualizations components</td>

      <td>
        All APIs in the control `/api/visualizations/*`, deprecated in an earlier release (Composer v7), are now removed.

        <br />

        The complete list of removed APIs:

        <br />

        * `GET /api/visualizations/{id}`
        * `PUT /api/visualizations/{id}`
        * `DELETE /api/visualizations/{id}`
        * `GET /api/visualizations`
        * `POST /api/visualizations`
        * `POST /api/visualizations/import`
        * `GET /api/visualizations/export/{visId}`
        * `POST /api/visualizations/thumbnail`
        * `GET /api/visualizations/{visId}/thumbnail/{thumbnailId}`
        * `GET /api/visualizations/{visualizationId}/source/{componentId}`
      </td>

      <td>
        Use the APIs `/api/visual-types/*` instead:

        <br />

        * `GET /api/visual-types/{id}`
        * `PUT /api/visual-types/{id}`
        * `DELETE /api/visual-types/{id}`
        * `GET /api/visual-types`
        * `POST /api/visuals-types`

        <br />

        Export and import visual types:

        <br />

        * `GET /api/visual-types/export/{visTypeId}`
        * `POST /api/visual-types/import`

        <br />

        Thumbnail management:

        <br />

        * `POST /api/visual-types/thumbnail`
        * `GET /api/visual-types/{visTypeId}/thumbnail/{thumbnailId}`

        <br />

        Visualizations components:

        <br />

        * `GET /api/visual-types/components/{componentId}`
      </td>
    </tr>

    <tr>
      <td>/api/system/systemInfo</td>
      <td>The API `api/system/systemInfo`, deprecated in an earlier release, is now removed.</td>
      <td>Use `/api/version` to see the current application version and system information.</td>
    </tr>

    <tr>
      <td>The `userId` and `disabledMessage` fields</td>

      <td>
        The fields `userId` and `disabledMessage` used in the connections-related endpoints and deprecated in an earlier release are now removed.

        <br />

        Affected APIs:

        <br />

        * All APIs in the `connections` control (including `GET`, `POST`, `PUT``/api/connections` etc.)
        * All APIs in the `dashboard-migration` control (`GET``/api/dashboards/export` and `POST``/api/dashboards/import`)

        <br />

        Use `createdByUserID` and `lastModifiedByUserID` as references instead of `userId`.
      </td>

      <td>Use `createdByUserID` and `lastModifiedByUserID` as references instead of `userId`.</td>
    </tr>

    <tr>
      <td>Filter Snippet Source Field</td>
      <td>The Field column, used to select a data field from a linked source, has been removed.</td>
      <td>Select a data field in Value Column, and if available, add a Display Column.</td>
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th>Title</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={2}>**23.2.15 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**23.2.14 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**23.2.13 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**23.2.12 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**23.2.11 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**23.2.10 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**23.2.9 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**23.2.8 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**23.2.7 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**23.2.6 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**23.2.5 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**23.2.4 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**23.2.3 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**23.2.2 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**23.2.1 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**23.2 Removed Features**</td>
    </tr>

    <tr>
      <td>Legends for KPI Visuals</td>
      <td>Legends have been removed from KPI visuals.</td>
    </tr>

    <tr>
      <td>`hasRawData`, `hasRawDataOnly`</td>
      <td>Support for these fields are removed for the endpoint `/api/sources/{sourceId}/visual-types/variables-values/`. Use `RAW_DATA` instead.</td>
    </tr>

    <tr>
      <td>Media Type `application/vnd.composer.dashboard.v2+json`</td>
      <td>The media type `application/vnd.composer.dashboard.v2+json` for `api/dashboards`, deprecated in an earlier release, is now removed.</td>
    </tr>

    <tr>
      <td>`page` and `size` Parameters</td>
      <td>The parameters `page` and `size`for the Users autocomplete endpoint `GET /api/users/autocomplete`, deprecated in a previous release, have been removed.</td>
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th>Title</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={2}>**23.1.14 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**23.1.13 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**23.1.12 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**23.1.11 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**23.1.10 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**23.1.9 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**23.1.8 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**23.1.7 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**23.1.6 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**23.1.5 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**23.1.4 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**23.1.3 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**23.1.2 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**23.1.1 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**23.1 Removed Features**</td>
    </tr>

    <tr>
      <td>Tracing Microservice</td>
      <td>The Composer Tracing Microservice (`zoomdata-tracing-server`), deprecated in a previous release, is now removed.</td>
    </tr>
  </tbody>
</table>

<h3 id="deprecated-and-removed-features-composer-v22">
  Composer v22
</h3>

<h4 id="deprecated-and-removed-features-composer-v22-deprecated-features">
  Deprecated Features
</h4>

<table>
  <thead>
    <tr>
      <th>Title</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={2}>**22.4.14 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**22.4.13 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**22.4.12 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**22.4.11 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**22.4.10 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**22.4.9 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**22.4.8 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**22.4.7 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**22.4.6 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**22.4.5 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**22.4.4 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**22.4.3 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**22.4.2 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**22.4.1 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**22.4 Deprecated Features**</td>
    </tr>

    <tr>
      <td>Tracing Microservice Support</td>
      <td>The Composer Tracing Microservice (`zoomdata-tracing-server`) is deprecated. This service will be removed in a future release, replaced by an alternative feature.</td>
    </tr>

    <tr>
      <td>Edit Visual Menu Options</td>
      <td>The **More** menu option **Edit Visual** is renamed **Settings** for visuals and rich text snippets.</td>
    </tr>
  </tbody>
</table>

<h4 id="deprecated-and-removed-features-composer-v22-removed-features">
  Removed Features
</h4>

<table>
  <thead>
    <tr>
      <th>Title</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={2}>**22.4.14 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**22.4.13 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**22.4.12 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**22.4.11 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**22.4.10 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**22.4.9 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**22.4.8 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**22.4.7 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**22.4.6 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**22.4.5 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**22.4.4 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**22.4.3 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**22.4.2 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**22.4.1 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**22.4 Removed Features**</td>
    </tr>

    <tr>
      <td>Radial Menu</td>
      <td>Radial menu functionality has been streamlined into and replaced by the Context Menu.</td>
    </tr>
  </tbody>
</table>

<h3 id="deprecated-and-removed-features-composer-v8-4-and-earlier">
  Composer v8.4 and Earlier
</h3>

<h4 id="deprecated-and-removed-features-composer-v8-4-and-earlier-2">
  Deprecated Features
</h4>

<table>
  <thead>
    <tr>
      <th>Title</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={2}>**8.4.1 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**8.4 Deprecated Features**</td>
    </tr>

    <tr>
      <td>Logging Updates</td>
      <td>The logback.zoomdata property, previously used to control the log level of some loggers, has been removed. Use a standard spring boot approach to specify appropriate properties.</td>
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th>Title</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={2}>**8.3 Deprecated Features**</td>
    </tr>

    <tr>
      <td>Elasticsearch Support Update</td>
      <td>Composer no longer supports the use of Elasticsearch version 6. Use Elasticsearch 7 or 8 instead.</td>
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th>Title</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={2}>**8.2 Deprecated Features**</td>
    </tr>

    <tr>
      <td>Support for Presto Connectors</td>
      <td>Composer no longer supports use of the Presto connector version 319; the Presto connector will be removed in a future release. Use the new Trino connector; see Manage the Trino Connector.</td>
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th>Title</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={2}>**8.1 Deprecated Features**</td>
    </tr>

    <tr>
      <td>`visualId`</td>
      <td>`visualId` is now deprecated from the widgets payload of `/api/dashboards/`.</td>
    </tr>

    <tr>
      <td>Scheduled Reports API Updates</td>
      <td>The behavior of the attribute `sendOnlyToOwner` is changed. When the attribute is set to `true`, the current user is now added to the list of `users`, and `sendOnlyToOwner` is reset by Logi Composer to `false`. The attribute `sendOnlyToOwner` is deprecated, and will be removed in a future release.</td>
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th>Title</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={2}>**8.0 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>
  </tbody>
</table>

<h4 id="deprecated-and-removed-features-composer-v8-4-and-earlier-3">
  Removed Features
</h4>

<table>
  <thead>
    <tr>
      <th>Title</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={2}>**8.4.1 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**8.4 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th>Title</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={2}>**8.3 Removed Features**</td>
    </tr>

    <tr>
      <td>Composer SDK</td>
      <td>The Composer SDK is no longer supported.</td>
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th>Title</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={2}>**8.2 Removed Features**</td>
    </tr>

    <tr>
      <td>Visual Info Sidebar Menu Update</td>
      <td>The field **Default Title** has been removed from the Info sidebar menu of visuals.</td>
    </tr>

    <tr>
      <td>Visual Gallery Updates</td>
      <td>The Usage column has been removed.</td>
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th>Title</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={2}>**8.1 Removed Features**</td>
    </tr>

    <tr>
      <td>Scheduled Reports</td>
      <td>The **Send to me** toggle is removed, replaced by a field you can use to add report recipients, prepopulated with the current user’s information.</td>
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th>Title</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={2}>**8.0 Removed Features**</td>
    </tr>

    <tr>
      <td>WebSocket Authentication</td>
      <td>Authentication of WebSocket connections in embedded mode using trusted access tokens in the WebSocket URL, deprecated in Composer v7.10, is now removed. Authentication is handled by the Embed Manager.</td>
    </tr>
  </tbody>
</table>

<h3 id="deprecated-and-removed-features-composer-v7-10-and-earlier">
  Composer v7.10 and Earlier
</h3>

<h4 id="deprecated-and-removed-features-composer-v7-10-and-earlier-2">
  Deprecated Features
</h4>

<table>
  <thead>
    <tr>
      <th>Title</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={2}>**7.10.23 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**7.10.22 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**7.10.21 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**7.10.20 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**7.10.19 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**7.10.18 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**7.10.17 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**7.10.16 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**7.10.15 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**7.10.14 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**7.10.13 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**7.10.12 Deprecated Features**</td>
    </tr>

    <tr>
      <td>Composer SDK</td>
      <td>The Composer SDK is deprecated, and is not supported in later versions of Composer.</td>
    </tr>

    <tr>
      <td colSpan={2}>**7.10.11 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**7.10.10 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**7.10.9 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**7.10.8 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**7.10.7 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**7.10.6 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**7.10.5 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**7.10.4 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**7.10.3 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**7.10.2 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**7.10.1 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>

    <tr>
      <td colSpan={2}>**7.10 Deprecated Features**</td>
    </tr>

    <tr>
      <td>zoomdata-client</td>
      <td>The zoomdata-client is deprecated, and will be removed in a future release. You can embed Composer components using JavaScript and Trusted Access.</td>
    </tr>

    <tr>
      <td>/api/visuals/</td>
      <td>The field `defaultTitle` is deprecated, and will be removed in a future release.</td>
    </tr>

    <tr>
      <td>User Resource Update</td>

      <td>
        Several unused fields for user resource have been made read only and are deprecated in this release and removed in a future release.

        <br />

        * groupRoles
        * external
        * deletable
        * userId
      </td>
    </tr>

    <tr>
      <td>WebSocket Authentication</td>
      <td>Authentication of WebSocket connections in embedded mode using trusted access tokens in the WebSocket URL has been deprecated. Authentication is now handled by the Embed Manager.</td>
    </tr>

    <tr>
      <td>Embed Manager Update</td>
      <td>The `initialToken` parameter is deprecated for the Embed Manager and will be removed in a future release.</td>
    </tr>

    <tr>
      <td>System Activity API</td>

      <td>
        These system activity endpoints are deprecated in v7.10 and may be removed in a future release.

        <br />

        `GET /api/system/activity/type/{activityType}`

        <br />

        `PUT /api/system/activity/type/{activityType}`

        <br />

        `GET /api/system/activity/type`
      </td>
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th>Title</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={2}>**7.9 Deprecated Features**</td>
    </tr>

    <tr>
      <td>/api/inventory/</td>
      <td>The endpoint `/api/inventory/` has been expanded to return additional information about dashboards and sources. If no parameter `type` is sent, DASHBOARD information is returned. This feature is deprecated and will be removed in a future release.</td>
    </tr>

    <tr>
      <td>/api/connections/\{connectionId}/preview</td>
      <td>This endpoint has been deprecated and will be removed in a future release.</td>
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th>Title</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={2}>**7.8 Deprecated Features**</td>
    </tr>

    <tr>
      <td>/api/visuals/source/\<source-id>/summary/</td>
      <td>The end point `/api/visuals/source/<source-id>/summary/` is deprecated and will be removed in a future release.</td>
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th>Title</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={2}>**7.7 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th>Title</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={2}>**7.6 Deprecated Features**</td>
    </tr>

    <tr>
      <td>GET /api/visuals</td>

      <td>
        We have removed the following fields for the GET api/visuals payload:

        <br />

        * `ownerType`
        * `name`
        * `>enabled`

        <br />

        We have removed the following fields from the response payload of all other /api/visuals endpoints:

        <br />

        * `enabled`
        * `ownerType`
        * `lastModified`
        * `ownerSourceId`
        * `name`
      </td>
    </tr>

    <tr>
      <td>visualizations</td>
      <td>Deprecated. Use `/visual-types/`.</td>
    </tr>

    <tr>
      <td>visualization component</td>
      <td>Deprecated. Use `/visual-types/components/`.</td>
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th>Title</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={2}>**7.5 Deprecated Features**</td>
    </tr>

    <tr>
      <td>/api/trusted-access/token</td>
      <td>Deprecated. Use `/api/trusted-access/pull/tokens`. This is primarily a name change for the endpoint; payloads and functionality remain unchanged.</td>
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th>Title</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={2}>**7.4 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th>Title</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={2}>**7.3 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th>Title</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={2}>**7.2 Deprecated Features**</td>
    </tr>

    <tr>
      <td>Standardized Max Threads Property</td>

      <td>
        Composer Web and Query Engine microservices no longer use the `jetty.threadpool.maxThreads` property. We have replaced it with `server.jetty.max-threads` for all microservices.

        <br />

        Property File Configuration (`server.jetty.max-threads`)

        <br />

        * For QE and Zoomdata(Composer Web) is The number of threads to serve the HTTP & WebSocket clients.
        * For all other microservices is The number of threads to serve the HTTP clients.
      </td>
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th>Title</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={2}>**7.1 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th>Title</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={2}>**7.0 Deprecated Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>
  </tbody>
</table>

<h4 id="deprecated-and-removed-features-composer-v7-10-and-earlier-3">
  Removed Features
</h4>

<table>
  <thead>
    <tr>
      <th>Title</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={2}>**7.10 Removed Features**</td>
    </tr>

    <tr>
      <td>OAuth Support Update</td>
      <td>OAuth connection and token support, deprecated in a previous release, is now removed from the Composer interface and API. See Trusted Access.</td>
    </tr>

    <tr>
      <td>`${User.zoomdataUserName}` Support Update</td>
      <td>The context variable, `${User.zoomdataUserName}`, deprecated in an earlier release, is now removed from Composer. Use `${User.composerUserName}` in connections, in security filters, and in custom SQL instead.</td>
    </tr>

    <tr>
      <td>/api/visuals/source/\<source-id>/summary/</td>
      <td>The end point `/api/visuals/source/<source-id>/summary/`, deprecated in v7.8, is now removed.</td>
    </tr>

    <tr>
      <td>/api/visdefs/default/\{sourceId}/\{visId}</td>
      <td>The endpoint `/api/visdefs/default/{sourceId}/{visId}`, deprecated in an earlier release, is now removed. Use `/api/sources/{sourceId}/visual-types/{visualTypeId}/initial-visual` instead.</td>
    </tr>

    <tr>
      <td>Removal of Group Fields</td>

      <td>
        Two previously deprecated fields from group resources have now been removed:

        <br />

        * `configType` from `GroupResource`
        * `sources` from `GroupAclResource`

        <br />

        Use `/api/sources/{sourceId}/acls` to manage source permissions.
      </td>
    </tr>

    <tr>
      <td>Source Creation Changes</td>
      <td>As part of the redesigned source creation process, the source creation wizard has been removed. Available Visual Type selection is now managed by users with appropriate permissions on the Sources page.</td>
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th>Title</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={2}>**7.9 Removed Features**</td>
    </tr>

    <tr>
      <td>API</td>

      <td>
        `/user/source-acl` is now removed from Composer. It was deprecated in a previous release.

        <br />

        `/user/source-acl/{sourceID}` is now removed from Composer. It was deprecated in a previous release.
      </td>
    </tr>

    <tr>
      <td>CLI API Endpoints</td>

      <td>
        Visualization library endpoints used by the CLI and deprecated in Self-Service Analytics v6.9 have been removed. These include:

        <br />

        * `GET /api/visualizations/libs`
        * `POST /api/visualizations/libs`
        * `DELETE /api/visualizations/libs/{id}`
        * `GET /api/visualizations/libs/{id}/*`
      </td>
    </tr>

    <tr>
      <td>`application/vnd.composer.v2+json` Media Type</td>
      <td>The media type `application/vnd.composer.v2+json`, deprecated in v6.9, has been removed. Use the `application/vnd.composer.v3+json` media type instead.</td>
    </tr>

    <tr>
      <td>Custom Chart CLI Updates</td>
      <td>The ability to edit the visibility of a custom chart using the CLI has been removed.</td>
    </tr>

    <tr>
      <td>Activity Logging Updates</td>
      <td>The system property `activity.remember_me`, deprecated in a previous release, has been removed from `zoomdata.properties`. The associated log file, `Remember_me.log`, is no longer generated.</td>
    </tr>

    <tr>
      <td>Duplicate Custom Metrics</td>
      <td>The ability to duplicate custom metrics in the Composer interface has been removed. You can continue to use the appropriate API endpoints to create multiple custom metrics with different names that use the same underlying formula.</td>
    </tr>

    <tr>
      <td>Removal of Deprecated Endpoints</td>
      <td>Several groups of endpoints, deprecated in the Swagger specification in Composer 6.9, are now removed. This includes endpoints for sources from connections, file uploads, derived fields, formulas, and dashboards import and export.</td>
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th>Title</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={2}>**7.8 Removed Features**</td>
    </tr>

    <tr>
      <td>/api/preferences/</td>
      <td>The endpoint `/api/preferences/`, deprecated in 6.9, has been removed.</td>
    </tr>

    <tr>
      <td>/api/inventory/</td>
      <td>The endpoint `/api/inventory/` no longer returns a `thumbnailDate` field.</td>
    </tr>

    <tr>
      <td>/api/dashboards/</td>
      <td>The endpoint `/api/dashboards/` no longer returns a `thumbnailDate` field.</td>
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th>Title</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={2}>**7.7 Removed Features**</td>
    </tr>

    <tr>
      <td>Library View Support Update</td>
      <td>URL links to quick filters have been removed from the Dashboard Library to provide a more streamlined interface and embedding experience. Functionality of the quick filter icons remain unchanged.</td>
    </tr>

    <tr>
      <td>Security Keys Authentication Update</td>

      <td>
        * Security Keys have been deprecated as an authentication option in Composer. As part of this change, existing public links previously tied to security keys cannot be used.
        * The `/api/dashboards/{id}/key` endpoint, used to generate security keys, has been removed.

        <br />

        This change additionally removes:

        <br />

        * Application Property: `activity.security_key`
        * Activity Logging type: `security_key`
        * A field from activity logging records: `userType`

        <br />

        Support for iFrame embedding reliant on security keys has been removed. Use Trusted Access instead for all embedded workflows. See Trusted Access.
      </td>
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th>Title</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={2}>**7.6 Removed Features**</td>
    </tr>

    <tr>
      <td>Security Key Updates</td>
      <td>Previously deprecated Security Keys endpoints are now removed from Composer. Use Trusted Access instead for all embedded workflows. See Trusted Access.</td>
    </tr>

    <tr>
      <td>Group Privilege Update</td>
      <td>The privilege **Can Generate Dashboard Link** has been removed. The API privilege `ROLE_SHARE_DASHBOARDS` has been removed.</td>
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th>Title</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={2}>**7.5 Removed Features**</td>
    </tr>

    <tr>
      <td>Remove Deprecated Security Keys-Related /api/sources endpoints</td>

      <td>
        APIs affected:

        <br />

        `GET /api/sources/{id}/key`

        <br />

        `GET /api/sources/key`

        <br />

        `DELETE /api/sources/remove/{id}`

        <br />

        These APIs were deprecated in release v6.9 and have now been removed from the platform. Use Trusted Access instead for all embedded workflows. For more information about trusted access, see Trusted Access. For more information about embedding Composer components, see Embed Composer Components Using JavaScript and Trusted Access.
      </td>
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th>Title</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={2}>**7.4 Removed Features**</td>
    </tr>

    <tr>
      <td>
        `/api/screenshot/*`

        <br />

        `/api/screenshot-management`
      </td>

      <td>
        The `/api/screenshot/*` endpoint and `/api/screenshot-management` endpoint were deprecated in v6.9 and are now removed.

        <br />

        This includes, for the screenshot-management tag:

        <br />

        * GET `/api/screenshot/{dasbhoardId}`
        * PUT `/api/screenshot/{dashboardId}`
        * POST `/api/screenshot/{dashboardId}`

        <br />

        This includes, for the screenshot tag:

        <br />

        * PUT `/api/screenshot/{dasbhoardId}`

        <br />

        This change additionally removes:

        <br />

        * The `screenshot` field from the `Import-Export` payload
        * The `thumbnailDate` field from `/api/inventory`
        * The `thumbnailDate` field from `/api/dashboards`
        * The screenshot refresh job in the `scheduler`

        <br />

        Several screenshot-related properties are no longer in the property files:

        <br />

        * `screenshot.daemon.enabled`
        * `screenshots.dashboard.enabled`
        * `screenshot.daemon.schedule.rate`
        * `screenshot.webdriver.timeout`
        * `screenshot.height`
        * `screenshot.width`
        * `export.dashboard.screenshot.timeout.seconds`
        * `screenshot.daemon.threads.maximum`
      </td>
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th>Title</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={2}>**7.3 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th>Title</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={2}>**7.2 Removed Features**</td>
    </tr>

    <tr>
      <td>Dashboard Library</td>
      <td>The thumbnail view and dashboard preview views have been removed from the dashboard library.</td>
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th>Title</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={2}>**7.1 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th>Title</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={2}>**7.0 Removed Features**</td>
    </tr>

    <tr>
      <td>None.</td>

      <td />
    </tr>
  </tbody>
</table>

<h3 id="deprecated-and-removed-features-composer-v6-9-and-earlier">
  Composer v6.9 and Earlier
</h3>

<h4 id="deprecated-and-removed-features-composer-v6-9-and-earlier-2">
  Deprecated Features
</h4>

<table>
  <thead>
    <tr>
      <th>Title</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={2}>**6.9.29 Deprecated Features**</td>
    </tr>

    <tr>
      <td colSpan={2}>None.</td>
    </tr>

    <tr>
      <td colSpan={2}>**6.9.28 Deprecated Features**</td>
    </tr>

    <tr>
      <td colSpan={2}>None.</td>
    </tr>

    <tr>
      <td colSpan={2}>**6.9.27 Deprecated Features**</td>
    </tr>

    <tr>
      <td colSpan={2}>None.</td>
    </tr>

    <tr>
      <td colSpan={2}>**6.9.26 Deprecated Features**</td>
    </tr>

    <tr>
      <td colSpan={2}>None.</td>
    </tr>

    <tr>
      <td colSpan={2}>**6.9.25 Deprecated Features**</td>
    </tr>

    <tr>
      <td colSpan={2}>None.</td>
    </tr>

    <tr>
      <td colSpan={2}>**6.9.24 Deprecated Features**</td>
    </tr>

    <tr>
      <td colSpan={2}>None.</td>
    </tr>

    <tr>
      <td colSpan={2}>**6.9.23 Deprecated Features**</td>
    </tr>

    <tr>
      <td colSpan={2}>None.</td>
    </tr>

    <tr>
      <td colSpan={2}>**6.9.22 Deprecated Features**</td>
    </tr>

    <tr>
      <td colSpan={2}>None.</td>
    </tr>

    <tr>
      <td colSpan={2}>**6.9.21 Deprecated Features**</td>
    </tr>

    <tr>
      <td colSpan={2}>None.</td>
    </tr>

    <tr>
      <td colSpan={2}>**6.9.20 Deprecated Features**</td>
    </tr>

    <tr>
      <td colSpan={2}>None.</td>
    </tr>

    <tr>
      <td colSpan={2}>**6.9.19 Deprecated Features**</td>
    </tr>

    <tr>
      <td colSpan={2}>None.</td>
    </tr>

    <tr>
      <td colSpan={2}>**6.9.18 Deprecated Features**</td>
    </tr>

    <tr>
      <td colSpan={2}>None.</td>
    </tr>

    <tr>
      <td colSpan={2}>**6.9.17 Deprecated Features**</td>
    </tr>

    <tr>
      <td colSpan={2}>None.</td>
    </tr>

    <tr>
      <td colSpan={2}>**6.9.16 Deprecated Features**</td>
    </tr>

    <tr>
      <td colSpan={2}>None.</td>
    </tr>

    <tr>
      <td colSpan={2}>**6.9.15 Deprecated Features**</td>
    </tr>

    <tr>
      <td colSpan={2}>None.</td>
    </tr>

    <tr>
      <td colSpan={2}>**6.9.14 Deprecated Features**</td>
    </tr>

    <tr>
      <td colSpan={2}>None.</td>
    </tr>

    <tr>
      <td colSpan={2}>**6.9.13 Deprecated Features**</td>
    </tr>

    <tr>
      <td colSpan={2}>None.</td>
    </tr>

    <tr>
      <td colSpan={2}>**6.9.12 Deprecated Features**</td>
    </tr>

    <tr>
      <td colSpan={2}>None.</td>
    </tr>

    <tr>
      <td colSpan={2}>**6.9.11 Deprecated Features**</td>
    </tr>

    <tr>
      <td colSpan={2}>None.</td>
    </tr>

    <tr>
      <td colSpan={2}>**6.9.10 Deprecated Features**</td>
    </tr>

    <tr>
      <td colSpan={2}>None.</td>
    </tr>

    <tr>
      <td colSpan={2}>**6.9.9 Deprecated Features**</td>
    </tr>

    <tr>
      <td colSpan={2}>None.</td>
    </tr>

    <tr>
      <td colSpan={2}>**6.9.8 Deprecated Features**</td>
    </tr>

    <tr>
      <td colSpan={2}>None.</td>
    </tr>

    <tr>
      <td colSpan={2}>**6.9.7 Deprecated Features**</td>
    </tr>

    <tr>
      <td colSpan={2}>None.</td>
    </tr>

    <tr>
      <td colSpan={2}>**6.9.6 Deprecated Features**</td>
    </tr>

    <tr>
      <td colSpan={2}>None.</td>
    </tr>

    <tr>
      <td colSpan={2}>**6.9.5 Deprecated Features**</td>
    </tr>

    <tr>
      <td colSpan={2}>None.</td>
    </tr>

    <tr>
      <td colSpan={2}>**6.9.4 Deprecated Features**</td>
    </tr>

    <tr>
      <td colSpan={2}>None.</td>
    </tr>

    <tr>
      <td colSpan={2}>**6.9.3 Deprecated Features**</td>
    </tr>

    <tr>
      <td>API</td>
      <td>The `/api/sources` and `/api/upload` endpoints are deprecated and will be removed in a future release.</td>
    </tr>

    <tr>
      <td colSpan={2}>**6.9.2 Deprecated Features**</td>
    </tr>

    <tr>
      <td>Custom Metric Date and Time Aggregation Functions</td>
      <td>The custom metric `DATE()`, `DateADD`, and `DateSUB` functions still work but should no longer be used. They are deprecated in this release and will be removed in a future release. Instead, use the `now()` and `time_add` functions. See Date and Time Filter Aggregation Functions.</td>
    </tr>

    <tr>
      <td colSpan={2}>**6.9.1 Deprecated Features**</td>
    </tr>

    <tr>
      <td colSpan={2}>None.</td>
    </tr>

    <tr>
      <td colSpan={2}>**6.9 Deprecated Features**</td>
    </tr>

    <tr>
      <td rowSpan={15}>API</td>
      <td>The media type `application/vnd.composer.v2+json` is deprecated and will be removed in a future release. Use the `application/vnd.composer.v3+json` media type instead.</td>
    </tr>

    <tr>
      <td>The `GET /api` (`/composer/api`) endpoint is now deprecated and will be removed from the product in a future release.</td>
    </tr>

    <tr>
      <td>
        The `/api/dashboards/*` endpoint used in the v1 version of the API (`application/vnd.composer.dashboard.v1+json`) is deprecated and will be removed in a future release. Use the new version of the endpoint in the v2 version of the API (`application/vnd.composer.dashboard.v2+json`) or `application/vnd.composer.v2` instead. Errors will result if you attempt to use `application/vnd.composer.dashboard.v1+json`.

        <br />

        Contact Customer Support to use `vnd.composer.dashboards.v1+json` for backward compatibility, including the use of the `bookmarksMap` object (instead of the new `content` object).

        <br />

        <Note>
          When no `content-type` header is specified, Composer defaults to using `application/vnd.composer.dashboard.v1+json`.
        </Note>
      </td>
    </tr>

    <tr>
      <td>The `/api/upload` endpoint is deprecated and will be removed in a future release.</td>
    </tr>

    <tr>
      <td>The `/api/visualizations/lib/*` endpoint is deprecated and will be removed in a future release. Use the custom chart CLI instead. See Maintain Custom Charts Using the Custom Chart CLI.</td>
    </tr>

    <tr>
      <td>The `/api/sources` endpoint is deprecated and will be replaced in a future release.</td>
    </tr>

    <tr>
      <td>The `GET /api/sources/<id>/key` endpoint is now deprecated and will be removed in a future release. Use Trusted Access instead for all embedded workflows. See Trusted Access and Embed Components Using JavaScript and Trusted Access.</td>
    </tr>

    <tr>
      <td>The `DELETE /api/sources/remove/<id>` endpoint is now deprecated and will be removed in a future release. Use Trusted Access instead for all embedded workflows. See Trusted Access and Embed Components Using JavaScript and Trusted Access.</td>
    </tr>

    <tr>
      <td>The `GET /api/sources/key` endpoint is now deprecated and will be removed in a future release. Use Trusted Access instead for all embedded workflows. See Trusted Access and Embed Components Using JavaScript and Trusted Access.</td>
    </tr>

    <tr>
      <td>The `/api/screenshot/*` endpoint and `/api/screenshot-management` endpoint are deprecated and will be removed in a future release.</td>
    </tr>

    <tr>
      <td>The `GET /oauth/authorize` endpoint is deprecated and will be removed in a future release. Use Trusted Access instead. See Trusted Access API Endpoints.</td>
    </tr>

    <tr>
      <td>The `/oauth2/client` endpoint is deprecated and will be removed in a future release. Use Trusted Access instead. See Trusted Access API Endpoints.</td>
    </tr>

    <tr>
      <td>The `/oauth2/token` endpoint is deprecated and will be removed in a future release. Use Trusted Access instead. See Trusted Access API Endpoints.</td>
    </tr>

    <tr>
      <td>
        The following fields in the response payload of the `GET /api/visuals` endpoint are deprecated and will be removed in a future release.

        <br />

        * `enabled`
        * `ownerType`
        * `name` (use `visualName` instead)
        * `dashboardLinks` (this field is now defined and stored in the new dashboard API response payload)
      </td>
    </tr>

    <tr>
      <td>
        The following fields in the response payload of all other `/api/visuals` endpoints are deprecated and will be removed in a future release.

        <br />

        * `enabled`
        * `ownerType`
        * `lastModified` (use `lastModifiedDate` instead)
        * `ownerSourceId` (use `source.sourceId` instead)
        * `name` (use `visualName` instead)
        * `dashboardLinks` ((this field is now defined and stored in the new dashboard API response payload)
      </td>
    </tr>

    <tr>
      <td rowSpan={2}>Data Sources</td>
      <td>The **Enabled** column on the Sources page of the UI is deprecated and will be removed in a future release. You can no longer disable data source configuration definitions, so when the column is removed, all disabled data sources will automatically be enabled. If you do not want the data sources disabled, you should delete them. You can control access to a data source configuration using data source permissions, as well as row and column data source restrictions.</td>
    </tr>

    <tr>
      <td>The import and export JSON definition functions for data source configurations are deprecated and will be removed in a future release. Plans are underway to replace this functionality with an improved option in a future release.</td>
    </tr>

    <tr>
      <td>Dashboards</td>
      <td>The import and export JSON definition functions for dashboard configurations are deprecated and will be removed in a future release. Plans are underway to replace this functionality with an improved option in a future release.</td>
    </tr>

    <tr>
      <td>OAuth Security</td>
      <td>The OAuth Authentication Service is deprecated and will be removed in a future release. Use Trusted Access instead. See Trusted Access.</td>
    </tr>

    <tr>
      <td>Security Keys</td>
      <td>Security keys are deprecated in this release and will be removed in a future release. Use Trusted Access instead for all embedded workflows. See Trusted Access.</td>
    </tr>

    <tr>
      <td>Older Dashboard Embed Structure</td>
      <td>Support for the iFrameless dashboard embed structure used in Composer 5.9 and older versions is deprecated in this release and will be removed in a future release. Use the new embed structure and methodology documented in Embed Components Into Your Application instead.</td>
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th>Title</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={2}>**6.8 Deprecated Features**</td>
    </tr>

    <tr>
      <td>API</td>
      <td>The `/api/export/generate/rawdata` endpoint is deprecated and will be removed in a future release. Use `/api/export/csv/raw` instead.</td>
    </tr>

    <tr>
      <td>Custom Chart CLI</td>
      <td>The following custom chart CLI libraries are deprecated: `nvd3.multiline.js`, `fabric.js`, `require/require.js`.</td>
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th>Title</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={2}>**6.7 Deprecated Features**</td>
    </tr>

    <tr>
      <td>Embedded Dashboards</td>
      <td>The `mode` property of the `createComponent` Javascript method used when embedding dashboards is deprecated. Use dashboard interactivity instead. See Control How Users Interact With a Dashboard.</td>
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th>Title</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={2}>**6.6 Deprecated Features**</td>
    </tr>

    <tr>
      <td colSpan={2}>None.</td>
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th>Title</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={2}>**6.5 Deprecated Features**</td>
    </tr>

    <tr>
      <td>JavaScript properties</td>
      <td>The `application.banner` and `application.logo` JavaScript properties are deprecated. See Supported Embedded Dashboard Properties and Objects.</td>
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th>Title</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={2}>**6.4 Deprecated Features**</td>
    </tr>

    <tr>
      <td colSpan={2}>None.</td>
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th>Title</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={2}>**6.3 Deprecated Features**</td>
    </tr>

    <tr>
      <td colSpan={2}>None.</td>
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th>Title</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={2}>**6.2 Deprecated Features**</td>
    </tr>

    <tr>
      <td rowSpan={2}>API</td>
      <td>The `sources` field in the `/api/groups` endpoint is deprecated and will be removed in a future release.</td>
    </tr>

    <tr>
      <td>The `configType` field in the `/api/groups` endpoint is deprecated and will be removed in a future release.</td>
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th>Title</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={2}>**6.1 Deprecated Features**</td>
    </tr>

    <tr>
      <td colSpan={2}>None.</td>
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th>Title</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={2}>**6.0 Deprecated Features**</td>
    </tr>

    <tr>
      <td>Properties</td>
      <td>The `server.multiple-context-path.primary` and `server.multiple-context-path.secondary` properties in the `zoomdata.properties` file are deprecated. This release does not support multiple context paths.</td>
    </tr>

    <tr>
      <td>API</td>
      <td>You can no longer use `<hostname>:8080/zoomdata/api/version`. Use `<hostname>:8080/composer/api/version` instead.</td>
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th>Title</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={2}>**5.9.1 Deprecated Features**</td>
    </tr>

    <tr>
      <td rowSpan={3}>API</td>
      <td>The `/api/security/attributes` endpoint is replaced with the new `/api/sources/<source-id>/security/attributes` endpoint, used for column security.</td>
    </tr>

    <tr>
      <td>The `/api/filters` endpoint is replaced with the new `/api/sources/<source-id>/security/filters` endpoint, used for row security.</td>
    </tr>

    <tr>
      <td>The `/api/dashboards/<dashboard-id>/key` endpoint. When removed, you will no longer be able to share a dashboard by generating a public link.</td>
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th>Title</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={2}>**5.9 Deprecated Features**</td>
    </tr>

    <tr>
      <td>Authorization</td>
      <td>The UI privilege **Can Share Visuals & Dashboards** (API privilege ROLE\_SHARE\_DASHBOARDS) associated with sharing a dashboard via a dashboard link is renamed **Can Generate Dashboard Public Link** (same API privilege), but is officially deprecated in release 5.9.</td>
    </tr>
  </tbody>
</table>

<h4 id="deprecated-and-removed-features-composer-v6-9-and-earlier-3">
  Removed Features
</h4>

<table>
  <thead>
    <tr>
      <th>Title</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td colSpan={2}>**6.9 Removed Features**</td>
    </tr>

    <tr>
      <td rowSpan={7}>API</td>
      <td>The `GET /api/visdefs/<sourceid>/<visid>` API endpoint is now removed from the product. It was deprecated in a previous release.</td>
    </tr>

    <tr>
      <td>The `PUT /api/visdefs/<sourceid>/<visid>` API endpoint is now removed from the product. It was deprecated in a previous release.</td>
    </tr>

    <tr>
      <td>The `POST /api/visdefs/<sourceid>/<visid>` API endpoint is now removed from the product. It was deprecated in a previous release.</td>
    </tr>

    <tr>
      <td>The `DELETE /api/visdefs/<sourceid>/<visid>` API endpoint is now removed from the product. It was deprecated in a previous release.</td>
    </tr>

    <tr>
      <td>The `GET /api/visdefs/<sourceid>`API endpoint is now removed from the product. It was deprecated in a previous release.</td>
    </tr>

    <tr>
      <td>The `POST /api/visdefs/default/<sourceid>/<visid>` API endpoint is now removed from the product.</td>
    </tr>

    <tr>
      <td>The `PUT /api/visdefs/default/<sourceid>/<visid>` API endpoint is now removed from the product.</td>
    </tr>

    <tr>
      <td>Licensing</td>
      <td>In support of the new license structure, the following license properties have been removed from the `api/license`endpoint response: `type` and `enforcementLevel`.</td>
    </tr>

    <tr>
      <td>Context Variables</td>
      <td>The `${User.zoomdataUserName}` context variable is removed from the product. You can no longer use this variable in new connection, data source, or forced filter definitions. Existing definitions that use this context variable will continue to work. For new definitions, use the `${User.composerUserName}` context variable instead.</td>
    </tr>

    <tr>
      <td colSpan={2}>**6.8 Removed Features**</td>
    </tr>

    <tr>
      <td colSpan={2}>None.</td>
    </tr>

    <tr>
      <td colSpan={2}>**6.7 Removed Features**</td>
    </tr>

    <tr>
      <td colSpan={2}>None.</td>
    </tr>

    <tr>
      <td colSpan={2}>**6.6 Removed Features**</td>
    </tr>

    <tr>
      <td colSpan={2}>None.</td>
    </tr>

    <tr>
      <td colSpan={2}>**6.5 Removed Features**</td>
    </tr>

    <tr>
      <td colSpan={2}>None.</td>
    </tr>

    <tr>
      <td colSpan={2}>**6.4 Removed Features**</td>
    </tr>

    <tr>
      <td>Fields</td>

      <td>
        * `com.zoomdata.resource.GroupAclResource#bookmarks`
        * `com.zoomdata.resource.GroupAclResource#connections`
        * `com.zoomdata.resource.InventoryItemResource#ownerFullName`
        * `com.zoomdata.resource.InventoryItemResource#ownerUserId`
        * `com.zoomdata.resource.dashboard.DashboardResource#userId`
        * `com.zoomdata.resource.dashboard.DashboardResource#shareState`
        * `com.zoomdata.resource.dashboard.DashboardResource#ownerName`
      </td>
    </tr>

    <tr>
      <td>Sorting Option</td>
      <td>The `com.zoomdata.web.controller.InventoryController.SortableField#OWNER` sorting option that relied on the OWNER field that was deprecated in 5.9 is removed from the code.</td>
    </tr>

    <tr>
      <td>Authorization</td>
      <td>The API privilege ROLE\_SAVE\_DASHBOARDS, deprecated in 5.9, is removed from the code. Use ROLE\_CREATE\_DASHBOARDS instead. All existing groups that had the ROLE\_SAVE\_DASHBOARDS privilege granted are automatically migrated to ROLE\_CREATE\_DASHBOARDS. However, if your organization has integrated Composer API calls into third-party software, you will need to manually change all references of ROLE\_SAVE\_DASHBOARDS to ROLE\_CREATE\_DASHBOARDS. See Group Privilege Reference.</td>
    </tr>

    <tr>
      <td>API</td>
      <td>The `visualizations` container in the response from a GET or PATCH `/api/sources/<id>` request was deprecated in 5.9 and support for it is removed from the Composer code.</td>
    </tr>

    <tr>
      <td colSpan={2}>**6.3 Removed Features**</td>
    </tr>

    <tr>
      <td rowSpan={2}>Linux</td>
      <td>CentOS 6 is no longer supported and the special installation Bootstrap procedure (`bootstrap-zoomdata-centos6.run`) is no longer provided with this product. CentOS 6 is no longer supported by Red Hat Linux (RHEL). Use CentOS 7 or 8 instead.</td>
    </tr>

    <tr>
      <td>Red Hat Linux 6 and Scientific Linux are no longer supported.</td>
    </tr>

    <tr>
      <td>JSON</td>
      <td>The `Content-Type` header `vnd.zoomdata.v2+json` is no longer supported in version 6.3 and later and can no longer be used as the `Content-Type` for API routes. It is removed from the product. Use `vnd.composer.v2+json` as the `Content-Type` for API routes instead.</td>
    </tr>

    <tr>
      <td>Group Definitions</td>
      <td>As a result of the introduction of data source permissions in version 6.3, the ability to restrict data sources within group definitions is removed. Use data source permissions instead. For information about data source permissions, see About Data Source Permissions.</td>
    </tr>

    <tr>
      <td>Custom Chart CLI</td>
      <td>Support for Version 3 of the custom chart CLI is now removed because it only supported Zoomdata version 3 and earlier and support for those Zoomdata versions is dropped. Use version 4 or the new version 5 of the custom chart CLI instead. See Supported Custom Chart CLI Versions.</td>
    </tr>

    <tr>
      <td>Authorization</td>

      <td>
        The API privileges ROLE\_DELETE\_ALL\_SOURCES, ROLE\_MANAGE\_ALL\_SOURCES, ROLE\_VIEW\_ALL\_SOURCES, and ROLE\_MANAGE\_SOME\_SOURCES are removed from the product. When you upgrade, groups with these roles will be automatically upgraded with new source privilege settings as follows:

        <br />

        * Groups with the ROLE\_VIEW\_ALL\_SOURCES privilege are automatically granted read permissions for all data sources.
        * Groups with the ROLE\_MANAGE\_ALL\_SOURCES privilege are automatically granted write permissions for all data sources.
        * Groups with the ROLE\_DELETE\_ALL\_SOURCES privilege are automatically granted delete permissions for all data sources.
      </td>
    </tr>

    <tr>
      <td colSpan={2}>**6.2 Removed Features**</td>
    </tr>

    <tr>
      <td>API</td>

      <td>
        The `accountId` parameter, which was deprecated in Composer 5.9, has now been removed from the following API endpoints:

        <br />

        * `GET /api/actions`
        * `DELETE /api/actions/{id}`
        * `POST /api/actions/{id}/invoke`
        * `GET /api/dashboards/export`
        * `GET /api/groups`
        * `GET /api/inventory`
        * `GET /api/sources/name/{name}`
        * `GET /api/sources`
        * `POST /api/upload/{sourceId}`
        * `DELETE /api/upload/{sourceId}`
        * `GET /api/preferences`
        * `GET /api/users`
        * `GET /api/visuals`
      </td>
    </tr>

    <tr>
      <td>Authorization</td>

      <td>
        The supplied **View All** group, which was officially deprecated in Composer 5.9, has now been removed from *new* installations of the product.

        <br />

        If you are upgrading to this release, the description provided for the **View All** group has changed, indicating that the group is no longer a default system group and no longer gives users implicit read-only permissions to all sources in the account. Pre-existing data sources will still be accessible for **View All** group members, but new data sources will not.
      </td>
    </tr>

    <tr>
      <td colSpan={2}>**6.1 Removed Features**</td>
    </tr>

    <tr>
      <td colSpan={2}>**None.**</td>
    </tr>

    <tr>
      <td colSpan={2}>**6.0 Removed Features**</td>
    </tr>

    <tr>
      <td colSpan={2}>**None.**</td>
    </tr>
  </tbody>
</table>
