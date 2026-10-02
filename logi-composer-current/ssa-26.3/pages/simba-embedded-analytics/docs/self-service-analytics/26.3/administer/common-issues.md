> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Common Issues

<h2 id="how-do-i-enable-debug-mode-in-self-service-analytics-services">
  How Do I Enable Debug Mode in Self-Service Analytics Services?
</h2>

Debug mode logs additional information when trying to troubleshoot an issue. Debug mode should *only* be enabled for further troubleshooting. You may not want to leave debug mode enabled because it can be resource and log intensive!

You can enable debug mode using one of two methods:

1. Change Logging level at runtime without the service restart. Run the following API call:

   ```
   #zoomdata/web service
   	curl -X POST "http(s)://<host>:<port>/discovery/actuator/loggers/com.zoomdata" \
   		-H "Content-Type: application/json; charset=utf-8" \
   		-d $'{ "configuredLevel": "DEBUG" }' \
   		-u <admin>:<password>
   			#other services, query-engine, edc
   			curl -X POST "http(s)://<host>:<port>/discovery/actuator/loggers/com.zoomdata" \
   				-H "Content-Type: application/json; charset=utf-8" \
   				-d $'{ "configuredLevel": "DEBUG" }' \
   			-u <admin>:<password>
   ```

   <Warning>
     Restarting any service will also reset logging options and automatically disable debug mode by default.
   </Warning>

2. Replace the `<password>`, `<host>`, and `<port>` parameters with appropriate values. The user must be the **admin** user to change the instance logging level. Useful logging levels are `DEBUG`, `INFO` (default), `ERROR`.

   The java package name prefix is `com.zoomdata`. Alternatively, it may be `org.springframework`.

3. Permanently change the service logging level, then restart the service. Add the following property to the parameter to the `zoomdata.properties` file or any other service `.properties`, then restart the service.

   <Warning>
     Restarting any service will also reset logging options and automatically disable debug mode by default.
   </Warning>

   ```
   #com.zoomdata and org.springframework are java package names logging.level.com.zoomdata=DEBUG logging.level.org.springframework=DEBUG
   ```

<h2 id="intermittent-websocket-disconnects-in-self-service-analytics">
  Intermittent WebSocket Disconnects in Self-Service Analytics
</h2>

### Resolutions

When experiencing intermittent or frequent WebSocket disconnects in Self-Service Analytics, check for the following:

* What version of Self-Service Analytics you are using? Consider upgrading to the latest available version. There have been various fixes and improvements to WebSocket behavior implemented that may address your issue.

* Follow-up with your network or IT team to verify if the issue is network-related. For example, traffic between Self-Service Analytics and your end users may be getting rerouted or there could be some other kind of network configuration that is causing skyrocket timeouts to occur in your environment on a frequent or regular basis.

* Check if there are any other applications (e.g. antivirus) that might be trying to block WebSocket sessions from establishing.

* Are these WebSocket disconnects only occurring in Self-Service Analytics or can these WebSocket disconnects be observed by the end-user when using other applications from the same browser machine?

* If you are using a load balancer with Self-Service Analytics, consider the following:

  * Review your load balancer configuration to determine the default session or WebSocket timeout value for your environment. Increase the timeout value if needed.
  * Your load balancer may not support protocol changes (HTTP/101), such as Amazon Web Services (AWS) Elastic Load Balancing (ELB). The Self-Service Analytics application, which uses a combination of HTTP, REST services, and WebSockets, requires a load balancer that supports protocol switching. In this case, consider using an alternative load balancer that supports protocol changes or configure it to function as a Layer-3 proxy if possible.
  * If you are using <u>HAProxy version 1.5 or newer</u> , please review your configured timeout setting for **tunnel mode** because it will override other server or client timeout settings. Thus, if set to a low value, this setting can cause frequent WebSocket disconnects to occur. For more information about tunnel mode, refer to the [HAProxy documentation](https://www.haproxy.com/blog/websockets-load-balancing-with-haproxy/).

<Note>
  By default, the session timeout for the Self-Service Analytics server is **30** minutes. If users are idle for extended periods of time, the existing WebSocket connections will timeout and this is expected behavior.
</Note>

<h2 id="what-should-i-check-for-if-live-mode-is-configured-but-my">
  What Should I Check for if Live Mode Is Configured But My Dashboard Data is not Updating?
</h2>

Before opening a support ticket with insightsoftware [Technical Support](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/tech-support), please check the following first:

* Data might be added in real time but not for "now" depending on the time field that Self-Service Analytics is using to play on. Since live mode only queries for any new data that comes in since the query was last executed, any "new but historical" data will not be captured until the dashboard is refreshed and the full query is executed.
* Verify that the time is in sync between the database server and Self-Service Analytics server.
* Verify that the database server and Self-Service Analytics server is using the same time zone.
* Try enabling Delay Mode *(with a significant delay)* to see if that makes any difference.

<h2 id="can-i-use-multiple-data-sources-on-the-same-visual">
  Can I Use Multiple Data Sources on the Same Visual?
</h2>

Generally, visuals can only be created from a single data source (to a single table or view). However, our dashboards can contain multiple visuals side-by-side that originate from multiple data sources. In addition, the following Self-Service Analytics features can be used to examine data from different data sources:

* You can create cross-source links between fields from the different data sources used by the different visuals on a dashboard. You can then apply filters to the cross-source-linked fields. See [Use Cross-Source Links](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/using-cross-source-links).
* You can create a fused data source containing data from different data sources and use the fused data source for your dashboard visuals. See [Fuse Data Sources](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-fusion-overview).

## Reduce Resource Allocation Due to Live Mode

Self-Service Analytics supports live streaming sources, as well as the ability to play historical data sets using time controls available in the visual canvas. If you choose to play through your data, significant CPU and memory usage may result.

You can work with Technical Support to add a [server-level](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/config-mgmt-ov#server-level-variables) variable to enable or disable animation on the time bar for Live sources and a configurable setting that can be used to set the refresh rate for Live Mode.

<h2 id="address-safari-browser-connection-lost-error-when-rendering-a">
  Address Safari Browser Connection Lost Error When Rendering a Visual
</h2>

<h3 id="address-safari-browser-connection-lost-error-when-rendering-a-2">
  Symptom
</h3>

When trying to render a visual using one of your data sources (including Self-Service Analytics's Real Time Sales demo source), you may observe an issue where the visual never finishes rendering and you receive a 'connection lost' error as a red bar across the top of the browser. Specifically, this issue seems to only occur when using Safari but not in other browsers such as Chrome.

### Possible Cause and Resolution

You may be encountering this issue because you are trying to use a self-signed certificate in Safari. By default, Self-Service Analytics will initially use a self-signed certificate for SSL unless otherwise configured. Because of how Safari's security settings are configured, the web-socket requests are likely getting denied causing the "connection lost" error and the visual to never render properly. You can address this issue by one of two methods:

1. Disable SSL in your Self-Service Analytics Server and make sure to use the 'http' connection when connecting to Self-Service Analytics via Safari.
2. Configure your Self-Service Analytics server to use a new, valid SSL certificate instead of using the default, self-signed certificate. This can be done by adding an SSL certificate to your Self-Service Analytics server.

<h2 id="address-self-service-analytics-microservice-shown-as-not-running">
  Address Self-Service Analytics Microservice Shown as Not Running
</h2>

<h3 id="address-self-service-analytics-microservice-shown-as-not">
  Symptom
</h3>

In the Self-Service Analytics server, running the `sudo service zoomdata status` command shows Self-Service Analytics as not running even though Self-Service Analytics is clearly running and accessible via the browser. No noticeable error is seen in the Self-Service Analytics log files and no other major issue is seen with the actual execution of Self-Service Analytics.

### Possible Causes and Solutions

This issue may be occurring because your Self-Service Analytics Process ID (PID) file is in the `/tmp` folder of your Self-Service Analytics server. By default, the Self-Service Analytics PID file is stored in this directory per the `/etc/init.d/zoomdata` file. If this is the case, there are many reasons why the PID file could be missing from this directory, and would require further investigation from your Linux or Ops engineers. Please check the size of this temp directory as if it is quite small, it can easily fill up depending on the size and usage of the server. Furthermore, some users may have set-up a cron job (or manually) to periodically clean this `/tmp` directory.

As a workaround, the location of the Self-Service Analytics PID file can be changed to not use the /tmp folder. This can be done by modifying the `/etc/init.d/zoomdata` file directly. Look for the following line in this file:

```
# Define composer pid file
[ -z "$ZOOMDATA_PID" ] && ZOOMDATA_PID="/tmp/zoomdata.pid"
```

We suggest either using the Self-Service Analytics directory or some other directory where the Self-Service Analytics user has write access that does not risk being cleaned out by something like a cron or manual job.

<h2 id="verify-the-self-service-analytics-server-restart">
  Verify the Self-Service Analytics Server Restart
</h2>

If you restarted the Self-Service Analytics server using the `sudo service zoomdata restart` command but still experience issues, you can verify that the Self-Service Analytics Server successfully restarted.

To verify, complete the following steps:

1. Obtain the Self-Service Analytics Process ID (PID) information by running:

   ```
   ps aux
   grep zoomdata
   ```

2. Then check the running time of the PID by running:

   ```
   ps -p [your_zoomdata_PID] -o etime=
   ```

3. Next, stop the Self-Service Analytics Server:

   ```bash theme={null}
   sudo service zoomdata stop
   ```

4. Check whether the Self-Service Analytics Server is still running:

   ```
   ps aux
   grep zoomdata
   ```

5. Optional: Check whether the ports for Self-Service Analytics are still available:

   ```
   netstat -anp
   grep 8080
   ```

6. If you discover that the Self-Service Analytics Server is still running, you will need to force stop the Server by running:

   ```
   kill <your_zoomdata_PID>
   ```

   <Note>
     If this command does not successfully terminate Self-Service Analytics, you can enter the following command line:
   </Note>

   ```
   kill -9 [your_zoomdata_PID]
   ```

   For additional information about the Linux kill command, please refer to the appropriate Linux documentation or the following [Linux/Unix Command: ps/kill](https://www.lifewire.com/zgrep-linux-command-unix-command-4097076) topic.

7. After successfully stopping the Self-Service Analytics Server, you can start it up again:

   ```bash theme={null}
   sudo service zoomdata start
   ```

8. Check the running time of the Self-Service Analytics PID again:

   ```
   ps -p <your_zoomdata_PID> -o etime=
   ```

   The new Self-Service Analytics running time should reflect the time you restarted the server.

<h2 id="whats-the-difference-between-the-self-service-analytics-rest">
  What’s the Difference between the Self-Service Analytics REST API and the Self-Service Analytics JavaScript SDK?
</h2>

Self-Service Analytics provides a REST API for your development needs.

<Warning>
  The Self-Service Analytics SDK is no longer supported.
</Warning>

<h2 id="sql-data-sources-displaying-date-and-time-fields-incorrectly-in">
  SQL Data Sources Displaying Date and Time Fields Incorrectly in Excel
</h2>

This behavior is not a bug or an issue with Self-Service Analytics but actually a result of how Microsoft Excel tries to read the date or time data stored in the generated CSV file. CSV files do not have a specific format, they just contain data. When Excel tries to examine this data, it tries to set an appropriate format for it. If you open the CSV file using a text editor (for example, Sublime Text), you will notice that the date or time fields and corresponding values display correctly as a string value within quotation marks. Excel can recognize a string containing a human-readable date or time value, but it will convert this value to its own internal time stamp value represented as a floating point number. Excel then applies an appropriate (or default) date or time style to these cells, but the format displayed may not necessarily use or match the string representation shown in the CSV file.

When you initially open the CSV file in Excel and select the actual date or time field, you might notice that the correct value and actual value of the cell is displayed in the "function" section even if the value shown in the specific cell is different.

Opening the CSV file with Excel and saving it might cause the file to overwrite the date or time data with the incorrect format instead. Please check the initial CSV file generated by Self-Service Analytics during export.

To ensure Excel displays the date or time data correctly, use one of the following methods:

1. Prefix the formatted date strings in the CSV file by adding an "=" symbol before the date or time values in quotes for each individual row (e.g. "2013-09-17 04:00:00.0","Alabama" becomes ="2013-09-17 04:00:00.0","Alabama")
2. Format the column in Excel so that the cells use the correct date or time format by right-clicking the column (or cells) and selecting the **Format Cells** option.

For more information about making formatting changes (trying to set a different default date or time format) or general formatting behavior in Excel, please refer to Microsoft Excel's documentation.
