---
title: "Manage the Upload API Source"
id: 43701022841997
section: "Manage Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701022841997-Manage-the-Upload-API-Source
updated_at: 2026-05-29T14:07:10Z
---

# Manage the Upload API Source

# Manage the Upload API Source

Composer supports live streaming sources. This source uses PostgreSQL as a storage medium for the incoming data flow. By default, Composer uses PostgreSQL to store the data for Upload API. This PostgreSQL instance is separate from other PostgreSQL instances you may have in existence. You can elect to use another PostgreSQL instance that you may have by changing the configuration properties.

## Before You Begin

If you want to use an existing PostgreSQL instance in conjunction with the Upload API microservice, you need to find the above information in your  `edc-postgresql.properties` file.

## Use Another PostgreSQL Instance for Upload API

1. Use the following command to access and open the properties file:

vi /etc/zoomdata/zoomdata.properties

2. Add the following parameters to the file:

   # that are configure for Upload API
   upload.destination.params.user\_name=yourusername
   upload.destination.params.password=yourpassword
   upload.destination.params.jdbc\_url=jdbc:postgresql://yourlocalhost:yourport//zd\_upload
   upload.batch-size=1000
3. Save and exit the configuration file.
4. Restart the Composer server.
