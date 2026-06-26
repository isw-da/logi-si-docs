---
title: "Pass Sensitive Data Using Linux Environment Variables"
id: 34932679227789
section: "Manage Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932679227789-Pass-Sensitive-Data-Using-Linux-Environment-Variables
updated_at: 2026-05-26T22:06:21Z
---

# Pass Sensitive Data Using Linux Environment Variables

# Pass Sensitive Data Using Linux Environment Variables

You can pass sensitive property values (such as database passwords or user names) to Composer using Linux environment variables, rather than hard coding the values in Composer property files. Using the SpringBoot Java application’s ability to consume application properties as environment variables, you can pass sensitive data to Composer without showing the data as plain text in the Composer property files.

**Note:** 
The information provided here requires a strong knowledge of Linux internals.

You can do this using either of two methods:

* [Method 1: Use systemd Override Files (Less Secure)](#Method)
* [Method 2: Use Parameters Passed to Microservices (More Secure)](#Method2)

You can also encrypt sensitive property values. See [Encrypt Configuration Properties](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932702533901-Encrypt-Configuration-Properties).

## Method 1: Use `systemd`Override Files (Less Secure)

You can use `systemd` with default unit files override. This is less secure than [Method 2: Use Parameters Passed to Microservices (More Secure)](#Method2) because the passwords are still exposed in the `env-pass.conf` files.

Complete the following steps:

1. Stop the affected microservices. See  [Stop Microservices](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/35385540487565-About-Microservices#Stop).

   sudo systemctl stop <service>
2. Add a `systemd` override file, called `env-pass.conf`, for each affected microservice. For example, the `systemd` override file for the `zoomdata` microservice would be `/etc/systemd/system/zoomdata.service.d/env-pass.conf` and the override file for the `zoomdata-query-engine` microservice would be `/etc/systemd/system/zoomdata-query-engine.service.d/env-pass.conf`. A complete list of microservice names is provided in [Composer  Microservice Name Reference](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933143202829-Composer-Microservice-Name-Reference).
3. Edit the `env-pass.conf` file for each microservice and add lines specifying environment variable values for every microservice configuration property containing sensitive information. For example, the following environment variables specify the data store password, the upload destination password, and the keyset destination password in the `env-pass.conf` file for the `zoomdata` microservice:

   [Service]
   Environment="SPRING\_DATASOURCE\_PASSWORD=<data store password>"
   Environment="UPLOAD\_DESTINATION\_PARAMS\_PASSWORD=<upload destination password>"
   Environment="KEYSET\_DESTINATION\_PARAMS\_PASSWORD=<keyset destination password>"

   In the `env-pass.conf` file for the `zoomdata-query-engine` microservice, you might add the following environment variable to specify the query engine database password:

   [Service]
   Environment="SPRING\_QE\_DATASOURCE\_PASSWORD=<query engine database password>"

   The environment variable names are the same as the property names in the corresponding microservice property files, but in all capital letters and substituting underscores for the periods in the property names. Review the [property files](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932670123533-Configuration-Property-Files) for valid property names. For example, the environment variable name for the `spring.datasource.password` property is `SPRING_DATASOURCE_PASSWORD`.
4. Apply the changes to `systemd`:

   sudo systemctl daemon-reload
5. Start the affected microservices. See  [Start Microservices](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/35385540487565-About-Microservices#Start).

## Method 2: Use Parameters Passed to Microservices (More Secure)

The most secure method is to pass sensitive parameters to Composer microservices as environment variables when you start the microservices. After the microservice is started, the settings for the sensitive parameters are no longer visible.

**Important:** 
If you use this method, Linux service management will be unable to automatically start or restart the affected Composer microservices when your system or server restarts. To resolve this, develop a wrapper script for `systemd` that will automatically export the required environment variables and restart the microservices.

Complete the following steps:

1. Stop the affected Composer microservice. See  [Stop Microservices](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/35385540487565-About-Microservices#Stop).

   sudo systemctl stop <service>
2. Disable the affected microservice. See  [Disable Microservices](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/35385540487565-About-Microservices#Disable).

   sudo systemctl disable <service>
3. Start the affected microservice, passing the sensitive parameters in environment variables as command line arguments. Make sure you use appropriate escape quotes if your password includes quotes.

   The environment variable names are the same as the property names in the corresponding microservice property files, but in all capital letters and substituting underscores for the periods in the property names. Review the [property files](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932670123533-Configuration-Property-Files) for valid property names. For example, the environment variable name for the `spring.datasource.password` property is `SPRING_DATASOURCE_PASSWORD`.

   In the following start command, the `zoomdata` microservice is started and the data store password, the upload destination password, and the keyset destination password are all passed as command line arguments:

   sudo -u zoomdata /opt/zoomdata/bin/zoomdata start -v
   -E 'SPRING\_DATASOURCE\_PASSWORD=<data store password>'
   -E 'UPLOAD\_DESTINATION\_PARAMS\_PASSWORD=<upload destination password>'
   -E 'KEYSET\_DESTINATION\_PARAMS\_PASSWORD=<keyset destination password>'

   The following start command starts the `zoomdata-query-engine` microservice and passes the query engine database password as a command line argument.

   /opt/zoomdata/bin/zoomdata-query-engine start -v -E 'SPRING\_QE\_DATASOURCE\_PASSWORD=<password>'

   See  [Start Microservices](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/35385540487565-About-Microservices#Start).
