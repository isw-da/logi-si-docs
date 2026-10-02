> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Request and Apply a New License Key

Self-Service Analytics notifies you when your license key is about to expire.

<Note>
  Use the DevNet License Manager to obtain license keys. These are provided to the person in your organization we term the License POC (Point of Contact). If you do not know who your License POC is, please reach out to your Account Manager.
</Note>

<Note>
  When a Self-Service Analytics standard or trial license expires, only system administrators can log in (to update the license). Regular users are shown a message that the license has expired.
</Note>

To manage your license keys, see:

* [Manage License Keys in the UI](#manage-license-keys-in-the-ui)
* [Manage License Keys Using the Licensing API](#manage-license-keys-using-the-licensing-api)
* [Manage License Keys Using Configuration Properties or Environment Variables](#manage-license-keys-using-configuration-properties-or)

<h2 id="manage-license-keys-in-the-ui">
  Manage License Keys in the UI
</h2>

**Apply a new license key:**

1. In the environment for you which you need a new license key, log in system [admin](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/users-manage#admin-user) or a member of the Supervisors group.

2. Select **License** from the menu. The Manage License page appears.

   <img src="https://mintcdn.com/insightsoftware/1fCfZrK84x8KmAw8/simba-embedded-analytics/docs/self-service-analytics/26.3/images/sym-admin/mng-license.png?fit=max&auto=format&n=1fCfZrK84x8KmAw8&q=85&s=cc0944c82b20525935412e76e232d527" alt="Use this work area to download instance tokens, license keys, and manage new licenses" width="545" height="569" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/sym-admin/mng-license.png" />

   This screen shows your current Self-Service Analytics instance ID and its current expiration date.

   <Note>
     If you select **Download Current Key**, your current license key is downloaded in a `license.key` file.
   </Note>

3. Select **Download Instance Token**. A `.tok` file is downloaded to your computer.

4. Log into DevNet and visit the License Management page to create a license file. You do this by assigning one of your license keys to a specific instance of Self-Service Analytics, by uploading the `.tok` file from the previous step. DevNet generates a license.key file, and downloads the file to your machine.

5. Browse to find the license key you just downloaded. Then, select **Submit**. Self-Service Analytics applies the new license to your instance.

<h2 id="manage-license-keys-using-the-licensing-api">
  Manage License Keys Using the Licensing API
</h2>

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
      <td rowSpan={2}>`/api/license`</td>
      <td>GET</td>
      <td>Returns license information for the instance.</td>
    </tr>

    <tr>
      <td>POST</td>
      <td>Updates license information for the instance</td>
    </tr>
  </tbody>
</table>

API documentation is provided in your environment at this link: `https://<Self-Service Analytics-URL>/composer/swagger-ui.html`.

If a problem occurs, contact your sales or technical support representative.

<h2 id="manage-license-keys-using-configuration-properties-or">
  Manage License Keys Using Configuration Properties or Environment Variables
</h2>

Add your license keys and installation id to `zoomdata.properties`. Format the variables as shown below:

```properties theme={null}
zoomdata.license.key=<value>
zoomdata.installation.id=<value>
```

<Warning>
  License information provided via configuration properties or environment variables have a higher priority than keys stored in the database previously provided via API or user interface. If you attempt to change the keys using the API in an environment where licensing information from configuration properties or environment variables are in use, Self-Service Analytics returns a failure message. Update the license key in the configuration files instead.
</Warning>

<Note>
  For more information about extending licensing to a Kubernetes deployment, see [Apply Licenses](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/kubernetes-ov#apply-licenses).
</Note>
