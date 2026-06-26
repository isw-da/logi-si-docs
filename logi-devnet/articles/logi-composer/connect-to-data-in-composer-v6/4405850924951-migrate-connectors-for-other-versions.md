---
title: "Migrate Connectors for Other Versions"
id: 4405850924951
section: "Connect to Data in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405850924951-Migrate-Connectors-for-Other-Versions
updated_at: 2021-09-21T01:27:12Z
---

# Migrate Connectors for Other Versions

# Migrate Connectors for Other Versions

Zoomdata 4.1 introduced a new microservice registration model for connectors. The new model is not fully compatible with earlier versions of Zoomdata. Special migration steps must be performed if you want to use a:

* [*Use a 4.1 (or Later) Connector With Zoomdata 4.0 (or Earlier)*](#Using)
* [*Use a 3.1 (or Earlier) Connector With Zoomdata 4.1 (or Later) or Composer 5.7 (or Later)*](#Using2)

Zoomdata 3.2 to 4.0 connectors are fully compatible with Zoomdata 4.1 (or later) and Composer 5.7 (or later).

## Use a 4.1 (or Later) Connector With Zoomdata 4.0 (or Earlier)

Before you can use a Zoomdata 4.1 (or later) or Composer 5.7 (or later) connector with Zoomdata 4.0 (or earlier) installation, you must complete the following migration steps.

1. Contact [Technical Support](https://devnet.logianalytics.com/hc/en-us/articles/4405859363351-Contact-Technical-Support) to obtain the code for the newer connector you want to use.
2. Install the newer connector supplied by [Technical Support](https://devnet.logianalytics.com/hc/en-us/articles/4405859363351-Contact-Technical-Support).

   ```
   $ sudo yum install <composer-edc-connector>
   ```
3. Make sure you have a copy of the connector's property file in `/etc/zoomdata`. The supported property file names are listed in [*Connector Properties and Property Files*](https://devnet.logianalytics.com/hc/en-us/articles/4405850892439-Connector-Properties-and-Property-Files). If the property file does not exist in `/etc/zoomdata`, copy the file from `/opt/zoomdata/conf`. If the property file does not exist in `/opt/zoomdata/conf`, then just create the file (using the supported name) in the `/etc/zoomdata` folder.
4. Edit the connector's property file in the `/etc/zoomdata` folder and change the value of the `spring.application.name` property to `edc`.

   ```
   ...
   spring.application.name=edc
   ...
   ```
5. Save the property file and start or restart the appropriate connector microservice.

   ```
   $ sudo systemctl start <connector-service-name>
   ```

   See [*Start Composer Microservices*](https://devnet.logianalytics.com/hc/en-us/articles/4405851100567-Start-Composer-Microservices) and [*Restart Composer Microservices*](https://devnet.logianalytics.com/hc/en-us/articles/4405851094679-Restart-Composer-Microservices) for more information. Microservice names are listed in [*Composer Microservice Name Reference*](https://devnet.logianalytics.com/hc/en-us/articles/4405851149591-Composer-Microservice-Name-Reference).

The newer connector will now work with your earlier version of Zoomdata.

## Use a 3.1 (or Earlier) Connector With Zoomdata 4.1 (or Later) or Composer 5.7 (or Later)

Before you can use a Zoomdata 3.1 (or earlier) connector with a Zoomdata 4.1 or later installation or with a Composer 5.7 or later installation, you must complete the following migration steps.

![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg) Zoomdata 3.2 to 4.0 connectors are fully compatible with Zoomdata 4.1 and later and with Composer 5.7 and later.

1. Contact [Technical Support](https://devnet.logianalytics.com/hc/en-us/articles/4405859363351-Contact-Technical-Support) to obtain the code for the older connector you want to use.
2. Install the older connector supplied by [Technical Support](https://devnet.logianalytics.com/hc/en-us/articles/4405859363351-Contact-Technical-Support).

   ```
   $ sudo yum install <composer-edc-connector>
   ```
3. Make sure you have a copy of the connector's property file in `/etc/zoomdata`. The supported property file names are listed in [*Connector Properties and Property Files*](https://devnet.logianalytics.com/hc/en-us/articles/4405850892439-Connector-Properties-and-Property-Files). If the property file does not exist in `/etc/zoomdata`, copy the file from `/opt/zoomdata/conf`. If the property file does not exist in `/opt/zoomdata/conf`, then just create the file (using the supported name) in the `/etc/zoomdata` folder.
4. Edit the connector's property file in the `/etc/zoomdata` folder and add the following properties.

   ```
   ...
   spring.cloud.consul.discovery.health-check-path=/actuator/health
   management.context-path=/actuator
   management.health.consul.enabled=false
   ...
   ```
5. Save the property file and start or restart the appropriate connector microservice.

   ```
   $ sudo systemctl start <connector-service-name>
   ```

   See [*Start Composer Microservices*](https://devnet.logianalytics.com/hc/en-us/articles/4405851100567-Start-Composer-Microservices) and [*Restart Composer Microservices*](https://devnet.logianalytics.com/hc/en-us/articles/4405851094679-Restart-Composer-Microservices) for more information. Microservice names are listed in [*Composer Microservice Name Reference*](https://devnet.logianalytics.com/hc/en-us/articles/4405851149591-Composer-Microservice-Name-Reference).

After the older connector microservice starts and has been registered, Composer automatically converts its address, port, and tags as necessary to register the connector using the new connector microservice registration model. The older connector will then work with Zoomdata 4.1 (or later) and Composer 5.7 (or later).
