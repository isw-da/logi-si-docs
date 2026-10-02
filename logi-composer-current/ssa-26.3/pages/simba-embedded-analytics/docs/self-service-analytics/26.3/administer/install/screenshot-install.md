> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Screenshot Microservice

The Screenshot microservice allows you to view snapshots of your saved dashboards.

<h2 id="screenshot-microservice-prerequisites">
  Screenshot Microservice Prerequisites
</h2>

Before you can install and use the screenshot microservice ensure your environment meets the prerequisites for this service.

**DCD-224 Start - Remove this heading, move content down**

### Browser Requirements

The screenshot microservice uses headless Google Chrome. Chrome-based screenshots include the entire dashboard and can be exported in PNG or PDF formats.

**DCD-224 New/incorporated Content End**

### Memory Configuration Considerations

If your use of Self-Service Analytics includes [scheduling reports](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-schedule), you may need to update this memory setting. The default memory configuration is suitable for handling up to 10 concurrent reports (different reports scheduled for the same time). If you need to schedule more concurrent reports, increase the memory allocation to about one gigabyte (1GB) more for every 15 concurrent reports. See [Configure Memory Settings](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/config-mgmt-ov#configure-memory-settings).

#### Thread Count Considerations

If your use of Self-Service Analytics includes [scheduling reports](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-schedule), update the screenshot microservice `pool.thread.size` setting so it is greater than the number of concurrent reports (see [screenshot-service.properties Properties](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/properties-reference#screenshot-service-properties-properties)). This setting controls the thread count for screenshot microservice requests.

### Obtain the Software

Before you can install the screenshot microservice, contact Self-Service Analytics [Technical Support](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/tech-support) to obtain a download link for the screenshot microservice installation software. Be sure you specify the operating system you are using so the appropriate software is provided.

## Install the Screenshot Microservice

**Install the Screenshot microservice**

1. Download the Screenshot microservice package using the link provided by Self-Service Analytics [Technical Support](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/tech-support).

2. Install the software using the appropriate command below, modifying `<filename>` to match the installation package provided by Self-Service Analytics [Technical Support](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/tech-support):

   In CentOS environments:

   ```bash theme={null}
   sudo yum localinstall <filename>.rpm
   ```

   In Ubuntu environments:

   ```bash theme={null}
   sudo dpkg -i <filename>.deb
   ```

3. **DCD-224 replace this step 3**

   Install the correct version of ChromeDriver. Refer to the [ChromeDriver documentation](http://chromedriver.chromium.org/downloads) for more information.

   Run the script `install-dependencies.sh` (located in the `/opt/zoomdata/docs/screenshot-service/` installation directory) or enter the following commands on the command line (for all operating systems):

   ```
   CHROMEDRIVER_LATEST_VERSION=$(curl -s https://chromedriver.storage.googleapis.com/LATEST_RELEASE)
   curl -s -o /tmp/chromedriver.zip \
   "https://chromedriver.storage.googleapis.com/${CHROMEDRIVER_LATEST_VERSION}/chromedriver_linux64.zip" sudo unzip /tmp/chromedriver.zip -d /usr/bin/
   rm -f /tmp/chromedriver.zip
   ```

4. Optionally, modify the `zoomdata.properties` file to enable and set up the Screenshot microservice. In addition to enabling the Screenshot microservice, you can also set the time period for capturing screenshots of your visuals to be displayed on the library page.

   * To create screenshots in the background, set the `screenshot.daemon.enabled` property to `true`:
   * Specify which types of screenshots you want to enable. Set the `screenshots.dashboards.enabled` property to `true` if you want to enable capturing and displaying the screenshots for the dashboards.

   When both `screenshot.daemon.enabled` and `screenshots.dashboards.enabled` properties are enabled, screenshots are created automatically when a dashboard is created or updated and at the rate specified by the `screenshot.daemon.schedule.rate` property (set in the next step of this procedure). If either the `screenshot.daemon.enabled` or `screenshots.dashboards.enabled` properties is disabled, screenshots are not created automatically, but you can still create a screenshot manually using the API.

5. Specify the frequency at which the screenshots are refreshed by configuring the property `screenshot.daemon.schedule.rate=<n>h` in `zoomdata.properties`. The default frequency is every 24 hours, but you can set your own frequency (in hours) by replacing `<n>` with your desired frequency.

6. Enable and start the Screenshot microservice. If you are using `systemctl`, run the following commands:

   ```bash theme={null}
   sudo systemctl enable zoomdata-screenshot-service
   sudo systemctl start zoomdata-screenshot-service
   ```

   If you are not using `systemctl`, adjust these commands accordingly. Additional information on restarting microservices is provided in [Restart Microservices](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/about-microsvcs#restart-microservices).

7. Watch the `/opt/zoomdata/logs/screenshot-service.log` file. The microservice is running successfully when the log displays a line similar to this:

   ```
   "Started ScreenshotServiceApplication in 12.184 seconds"
   ```

<h2 id="test-the-screenshot-microservice">
  Test the Screenshot Microservice
</h2>

**Test the Screenshot microservice**

1. Open a web browser to Self-Service Analytics. Obtain the ID for a dashboard to use for testing. Log in to Self-Service Analytics and open a dashboard. On the browser address bar copy the portion of the URL after the + sign. In the following example, you would copy `5ad8d1fa60b2894b38f0933b`:

   ```
   https://vm:8443/composer/visualization/5ad50156e4b07727dcb11098+5ad8d1fa60b2894b38f0933b
   ```

2. Use Postman or cURL to issue a PUT request to Self-Service Analytics to request a screenshot of the dashboard in PNG format. In the following example, replace \<username> with your user name, \<password> with your password, \<server> with your server IP address or name, \<port> with your port number, and \<dash-id> with the dashboard ID you obtained in the previous step.

   ```bash theme={null}
   curl --insecure -X PUT -u <username>:<password> https://<server>:<port>/composer/api/
   screenshot/<dash-id>?"width=1000&format=PNG" > test.png
   ```

3. If the `test.png` file is created successfully, the Screenshot microservice is operating correctly.

## Use the Screenshot Microservice API

The Screenshot microservice exposes a single REST endpoint, /api/screenshots. Issue a GET request to this endpoint to generate a screenshot of any URL the microservice can reach, in either PNG or PDF format. Use this endpoint when you want to generate a screenshot on demand rather than relying on the background screenshot daemon.

<Warning>
  This endpoint is distinct from the [dashboard screenshot API](#screenshot-microservice-prerequisites). The endpoint described here takes a URI and runs on the Screenshot microservice port (8083 by default). The two accept different parameters and are not interchangeable.
</Warning>

The microservice listens on port 8083 by default. For the full list of ports, see [Default Port Reference](/simba-embedded-analytics/docs/self-service-analytics/26.3/reference/port-reference).

<Danger>
  Requests to port 8083 are not authenticated. Restrict access to this port to hosts inside your deployment and do not expose it externally. See [Configure the Firewall](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/install-ov#configure-the-firewall).
</Danger>

### Request a Screenshot

Specify the output format using the `Accept` request header:

* For PNG, set `Accept` to `image/png`.
* For PDF, set `Accept` to `application/pdf`.

Pass the target address in the `uri` query parameter.

Request a PNG screenshot

```bash theme={null}
curl -H "Accept: image/png" http://localhost:8083/api/screenshots?uri=https://google.com
```

Request a PDF screenshot

```bash theme={null}
curl -H "Accept: application/pdf" http://localhost:8083/api/screenshots?uri=https://google.com
```

To capture a dashboard, use the dashboard address as the `uri` value. For the format of that address and how to obtain a dashboard ID, see [Test the Screenshot Microservice](#test-the-screenshot-microservice).

#### Set a Request Timeout

Both formats accept a `timeoutSeconds` parameter. This sets how long the microservice waits for the page to render before it abandons the request. When you omit this parameter, the microservice uses the default from its properties file. See screenshot-service.properties Properties.

Request a PNG screenshot with a custom timeout

```bash theme={null}
curl -H "Accept: image/png" http://localhost:8083/api/screenshots?uri=https://google.com&timeoutSeconds=300
```

If dashboards routinely exceed the timeout, raise the default instead of setting the parameter on every request. See [Troubleshoot Screenshot Microservice Problems](#troubleshoot-screenshot-microservice-problems).

### PNG Parameters

By default, the microservice does not constrain or resize the image it produces. Control the output for an individual request using the following optional query parameters. All values are integers, in pixels.

| Parameter | Description |
| - | - |
| `width` | The absolute width of the returned image. |
| `height` | The absolute height of the returned image. |
| `maxWidth` | The width the image is cropped to, applied only if the resulting image is wider than this value. |
| `maxHeight` | The height the image is cropped to, applied only if the resulting image is taller than this value. |
| `windowWidth` | The initial width of the browser window used to render the page. |
| `windowHeight` | The initial height of the browser window used to render the page. |

You can also set defaults for these values in the properties file using the screenshot.default.image prefix, for example `screenshot.default.image.width=850`. See [screenshot-service.properties Properties](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/properties-reference#screenshot-service-properties-properties).

#### How Resizing and Cropping Interact

The microservice resizes first and crops second. Three rules govern the result:

* If you supply both `width` and `height`, the image is resized to exactly those dimensions. The aspect ratio is ignored, so the image stretches if the requested proportions differ from the original.
* If you supply only one dimension, such as `width`, the other is scaled to preserve the original aspect ratio.
* `maxWidth` and `maxHeight` crop the image only when the resized image is wider or taller than the value you set.

Example

```bash theme={null}
curl -H "Accept: image/png" http://localhost:8083/api/screenshots?uri=https://google.com&width=500&maxHeight=100
```

This request produces a 500 x 100 pixel image in three stages:

1. The microservice captures the page at the default window size of 1920 x 1080 pixels.
2. Because `width` is 500 and no height was given, the image is resized to 500 x 260, preserving the original aspect ratio.
3. Because `maxHeight` is 100 and the resized height of 260 exceeds it, the image is cropped to 500 x 100, retaining only the top 100 pixels.

<Note>
  To change the 1920 x 1080 capture size, adjust the screenshot.default.window\.width and screenshot.default.window\.height properties. Extreme values can cause some dashboards to render incorrectly. See [screenshot-service.properties Properties](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/properties-reference#screenshot-service-properties-properties).
</Note>

### PDF Parameters

All PDF query parameters are optional.

<table>
  <thead>
    <tr>
      <th>Parameter</th>
      <th>Type</th>
      <th>Default</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>`header`</td>
      <td>string</td>
      <td>none</td>
      <td>Header text placed at the top of each page. Maximum 50 characters.</td>
    </tr>

    <tr>
      <td>`footer`</td>
      <td>string</td>
      <td>none</td>
      <td>Footer text placed at the bottom of each page. Maximum 50 characters.</td>
    </tr>

    <tr>
      <td>`userName`</td>
      <td>string</td>
      <td>none</td>
      <td>The user name placed on the right hand side of the footer.</td>
    </tr>

    <tr>
      <td>`includeTimestamp`</td>
      <td>boolean</td>
      <td>false</td>

      <td>
        When set to `true`, the timestamp is placed in the footer.

        <br />

        When set to `false`, no timestamp is placed in the footer.

        <br />

        To control the format of the timestamp, see [PDF Timestamp Format](#pdf-timestamp-format).
      </td>
    </tr>

    <tr>
      <td>`landscape`</td>
      <td>boolean</td>
      <td>true</td>

      <td>
        When set to `true`, page orientation is landscape.

        <br />

        When set to `false`, page orientation is portrait.
      </td>
    </tr>
  </tbody>
</table>

Request a PDF screenshot with a custom header and footer

```bash theme={null}
curl -H "Accept: application/pdf" http://localhost:8083/api/screenshots?uri=https://google.com&header=HeaderText&footer=FooterText&userName=admin&includeTimestamp=true&landscape=false
```

<h4 id="pdf-timestamp-format">
  PDF Timestamp Format
</h4>

When you set includeTimestamp to true, two properties control how the timestamp appears:

```properties theme={null}
screenshot.default.timestampFormatPattern=MMM d, YYYY hh:mm a screenshot.default.timestampUTCOffset=0
```

`timestampFormatPattern` accepts any pattern string compliant with the Java `DateTimeFormatter` class.

By default, the timestamp uses the server time. To use a different time zone, set `timestampUTCOffset` to an integer offset from UTC between -18 and 18. See [screenshot-service.properties Properties](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/properties-reference#screenshot-service-properties-properties).

<h2 id="troubleshoot-screenshot-microservice-problems">
  Troubleshoot Screenshot Microservice Problems
</h2>

Common issues can be resolved by editing the Screenshot microservice properties file in `/etc/zoomdata/screenshot-service.properties` and, in some cases, the `etc/zoomdata/zoomdata.properties` file. Changing values in these files requires a restart of the associated microservice. See [Restart Microservices](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/about-microsvcs#restart-microservices). See also [Icons Not Reverting to Defaults After Screenshot Microservice Disabled](#icons-not-reverting-to-defaults-after-screenshot-microservice).Timeouts

Self-Service Analytics and the Screenshot microservice include default timeouts for dashboards to render. If you will be requesting screenshots of dashboards that takes longer than this default, you can increase the default timeout in the properties file.

The Screenshot microservice may time out on dashboards that take too long to draw. If a selected Self-Service Analytics dashboard takes more than the default timeout, then the default timeout setting in the properties file can be increased.

Determine how much additional time you need, in seconds, for the dashboards to load or render and then add properties, as described below, to the properties file.

**Increase the default timeout**

1. On the Self-Service Analytics server, edit `/etc/zoomdata/screenshot-service.properties`.

2. Update the following properties, specifying an appropriate number of seconds for `<nnnn>`:

   * `screenshot.webdriver.timeout=<nnnn>`
   * `export.dashboard.screenshot.timeout.seconds=<nnnn>`

3. Save the `screenshot-service.properties` file.

4. On the Self-Service Analytics server, edit `/etc/zoomdata/zoomdata.properties`.

5. Update the following property, specifying an appropriate number of milliseconds for `<nnnn>`: `screenshot.service.http.client.read.timeout.milliseconds=<nnnn>`

6. Save the `zoomdata.properties` file.

7. Restart the Self-Service Analytics and Screenshot microservices. See [Restart Microservices](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/about-microsvcs#restart-microservices).

<h3 id="self-signed-certificate">
  Self-Signed Certificate
</h3>

If Self-Service Analytics is running with a self-signed certificate, the Screenshot microservice must be configured to accept the lower-security certificate.

**Configure the Screenshot microservice to accept the lower-security certificate**:

1. On the Self-Service Analytics server, edit `/etc/zoomdata/screenshot-service.properties`.

2. Update the following property as follows:

   ```properties theme={null}
   driver.options=--headless,--disable-gpu,--hide-scrollbars,--no-sandbox,--allow-insecure-localhost
   ```

3. Save the properties file.

4. Restart the Screenshot microservice. See [Restart Microservices](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/about-microsvcs#restart-microservices).

   This will pass the options to the ChromeDriver. The option list includes the default options normally passed to the driver, with the additional `--allow-insecure-localhost` option.

## Screenshot Microservice Upgrade Notes

After upgrading, the screenshots on the Home page may look different. This occurs if there has been a change in the screenshot aspect ratio. To make the screenshots look correct, make sure that the `screenshot.daemon.enabled` property in the `zoomdata.properties` file is set to `true`. Remember to restart the Self-Service Analytics server microservice after the change (see [Restart Microservices](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/about-microsvcs#restart-microservices)).

After you have updated the properties file, you can update the screenshots in one of the following ways:

* In the `zoomdata.properties` file, modify the `screenshot.daemon.schedule.rate` property and set it to a more frequent refresh rate.
* Execute a cURL call to update a screenshot for a specific dashboard.
* Execute a cURL call to upload a custom image for a specific dashboard. Otherwise, the screenshots will be updated when the refresh screenshot procedure runs according to the configured refresh rate.

<h2 id="icons-not-reverting-to-defaults-after-screenshot-microservice">
  Icons Not Reverting to Defaults After Screenshot Microservice Disabled
</h2>

The screenshot microservice can be enabled in Self-Service Analytics using CentOS and Ubuntu. However, users might notice that even after disabling the screenshot microservice, Self-Service Analytics continues to use existing screenshot images and does **not** automatically revert back to the original default icons for visuals or dashboards used by Self-Service Analytics after installation. To revert the icons used by Self-Service Analytics for the visuals or dashboards before the screenshot microservice was enabled, you must delete all the screenshots in the metadata directly.

To do this in MongoDB, run the following commands:

```
use zoom; db.screenshots.remove({});
```

Use the `mongo` command to access the mongo shell through the Linux command line.

<Note>
  Make sure you disable the screenshot microservice as well via the `zoomdata.conf` and `zoomdata.properties` files and restart the Self-Service Analytics microservice for the changes to take effect.
</Note>

<h2 id="fix-blank-visuals-in-the-home-page-for-rpm-installations">
  Fix Blank Visuals in the Home Page (for RPM Installations)
</h2>

### Symptom

If you successfully installed the RPM version of Self-Service Analytics and only see blank visuals on the dashboard, there may be a hostname mismatch in two specific Self-Service Analytics files: `/etc/sysconfig/network` and `/etc/hosts`.

### Possible Cause

In the file `/etc/sysconfig/network`, the following setting is needed:

```properties theme={null}
HOSTNAME=<servername>
```

Substitute any alphanumeric hostname for `<servername>`.

In the file `/etc/hosts`, the following should be listed:

```xml theme={null}
<your_server_IP> <servername>
```

Substitute the IP address and hostname of your Self-Service Analytics instance for `<your_server_IP>` and `<servername>`.

### Resolution

To resolve this issue, open the two files and verify that the hostname references in both files match.

* If the hostname reference does not exist in the `/etc/sysconfig/network` file, then it must be added. The name must match the name in the `/etc/hosts` file.
* If the hostname reference exists in both files, then one of the references must be revised to match the other.

To correct this error:

1. Log out of Self-Service Analytics, if you are still in the program and close the browser.

2. From your terminal, open a command line session.

3. Change to the `zoomdata` directory. See [Configure Self-Service Analytics](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/config-mgmt-ov) if you need guidance.

4. Edit the file `/etc/sysconfig/network`. Search for the term `HOSTNAME`. If the term is not in the file, add the following line:

   ```
   HOSTNAME=<servername>
   Substitute any alphanumeric hostname for <servername>.
   ```

   Save the file.

5. Edit the file `/etc/hosts`. Find or add the following line in the file.

   ```xml theme={null}
   <your_server_IP> <servername>
   ```

   Substitute the IP address and hostname of your Self-Service Analytics instance for `<your_server_IP>` and `<servername>`. Verify that the `<servername>` specified in the `/etc/hosts` file matches the `<servername>` in the `/etc/sysconfig/network`file.

   Save the file.

6. Open a new browser session and log back into Self-Service Analytics to verify that the visuals are displaying in the gallery.

If this solution did not resolve the problem, contact insightsoftware [Technical Support](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/tech-support).

<h2 id="can-self-service-analytics-be-installed-from-an-rpm-repository">
  Can Self-Service Analytics Be Installed From an RPM Repository?
</h2>

Yes, it is possible. If you would like more information please contact insightsoftware [Technical Support](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/tech-support) for assistance.
