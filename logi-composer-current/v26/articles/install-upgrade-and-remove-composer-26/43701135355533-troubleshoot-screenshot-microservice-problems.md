---
title: "Troubleshoot Screenshot Microservice Problems"
id: 43701135355533
section: "Install, Upgrade, and Remove Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701135355533-Troubleshoot-Screenshot-Microservice-Problems
updated_at: 2026-05-29T14:08:50Z
---

# Troubleshoot Screenshot Microservice Problems

# Troubleshoot Screenshot Microservice Problems

Common issues can be resolved by editing the Screenshot microservice properties file in `/etc/zoomdata/screenshot-service.properties` and, in some cases, the `etc/zoomdata/zoomdata.properties` file. Changing values in these files requires a restart of the associated microservice. See  [Restart Microservices](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701119873037-About-Microservices#Restart). See also [Icons Not Reverting to Defaults After Screenshot Microservice Disabled](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701210960013-Icons-Not-Reverting-to-Defaults-After-Screenshot-Microservice-Disabled).

## Timeouts

Composer and the Screenshot microservice include default timeouts for dashboards to render. If you will be requesting screenshots of dashboards that takes longer than this default, you can increase the default timeout in the properties file.

The Screenshot microservice may time out on dashboards that take too long to draw. If a selected Composer dashboard takes more than the default timeout, then the default timeout setting in the properties file can be increased.

Determine how much additional time you need, in seconds, for the dashboards to load or render and then add properties, as described below, to the properties file.

**Increase the default timeout**

1. On the Composer server, edit `/etc/zoomdata/screenshot-service.properties`.
2. Update the following properties, specifying an appropriate number of seconds for `<nnnn>`:

   * `screenshot.webdriver.timeout=<nnnn>`
   * `export.dashboard.screenshot.timeout.seconds=<nnnn>`
3. Save the `screenshot-service.properties` file.
4. On the Composer server, edit `/etc/zoomdata/zoomdata.properties`.
5. Update the following property, specifying an appropriate number of milliseconds for `<nnnn>`: `screenshot.service.http.client.read.timeout.milliseconds=<nnnn>`
6. Save the `zoomdata.properties` file.
7. Restart the Composer and Screenshot microservices. See  [Restart Microservices](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701119873037-About-Microservices#Restart).

## Self-Signed Certificate

If Composer is running with a self-signed certificate, the Screenshot microservice must be configured to accept the lower-security certificate.

**Configure the Screenshot microservice to accept the lower-security certificate**:

1. On the Composer server, edit `/etc/zoomdata/screenshot-service.properties`.
2. Update the following property as follows:

   driver.options=--headless,--disable-gpu,--hide-scrollbars,--no-sandbox,--allow-insecure-localhost
3. Save the properties file.
4. Restart the Screenshot microservice. See  [Restart Microservices](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701119873037-About-Microservices#Restart).

   This will pass the options to the ChromeDriver. The option list includes the default options normally passed to the driver, with the additional `--allow-insecure-localhost` option.
