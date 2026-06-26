---
title: "Troubleshoot Screenshot Microservice Problems"
id: 4405851097495
section: "Install, Upgrade, and Remove Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405851097495-Troubleshoot-Screenshot-Microservice-Problems
updated_at: 2021-09-21T01:28:55Z
---

# Troubleshoot Screenshot Microservice Problems

# Troubleshoot Screenshot Microservice Problems

Common issues can be resolved by editing the Screenshot microservice properties file in `/etc/zoomdata/screenshot-service.properties` and, in some cases, the `etc/zoomdata/zoomdata.properties` file. Changing values in these files requires a restart of the associated microservice. See [*Restart Composer Microservices*](https://devnet.logianalytics.com/hc/en-us/articles/4405851094679-Restart-Composer-Microservices). See also [*Icons Not Reverting to Defaults After Screenshot Microservice Disabled*](https://devnet.logianalytics.com/hc/en-us/articles/4405859496215-Icons-Not-Reverting-to-Defaults-After-Screenshot-Microservice-Disabled)

## Timeouts

Composer and the Screenshot microservice include default timeouts for dashboards to render. If you will be requesting screenshots of dashboards that takes longer than this default, you can increase the default timeout in the properties file.

The Screenshot microservice may time out on dashboards that take too long to draw. If a selected Composer dashboard takes more than the default timeout, then the default timeout setting in the properties file can be increased.

Determine how much additional time you need, in seconds, for the dashboards to load or render and then add properties, as described below, to the properties file.

To increase the default timeout:

1. On the Composer server, edit `/etc/zoomdata/screenshot-service.properties`.
2. Update the following properties, specifying an appropriate number of seconds for `<nnnn>`:

   * `screenshot.webdriver.timeout=<nnnn>`
   * `export.dashboard.screenshot.timeout.seconds=<nnnn>`
3. Save the `screenshot-service.properties` file.
4. On the Composer server, edit `/etc/zoomdata/zoomdata.properties`.
5. Update the following property, specifying an appropriate number of milliseconds for `<nnnn>`: `screenshot.service.http.client.read.timeout.milliseconds=<nnnn>`
6. Save the `zoomdata.properties` file.
7. Restart the Composer and Screenshot microservices. See [*Restart Composer Microservices*](https://devnet.logianalytics.com/hc/en-us/articles/4405851094679-Restart-Composer-Microservices).

## Self-signed Certificate

If Composer is running with a self-signed certificate, the Screenshot microservice must be configured to accept the lower-security certificate.

To configure the Screenshot microservice to accept the lower-security certificate:

1. On the Composer server, edit `/etc/zoomdata/screenshot-service.properties`.
2. Update the following property as follows:

   ```
   driver.options=--headless,--disable-gpu,--hide-scrollbars,--no-sandbox,--allow-insecure-localhost
   ```
3. Save the properties file.
4. Restart the Screenshot microservice. See [*Restart Composer Microservices*](https://devnet.logianalytics.com/hc/en-us/articles/4405851094679-Restart-Composer-Microservices).

   This will pass the options to the ChromeDriver. The option list includes the default options normally passed to the driver, with the additional `--allow-insecure-localhost` option.
