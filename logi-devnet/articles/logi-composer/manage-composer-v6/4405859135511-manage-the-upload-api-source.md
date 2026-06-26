---
title: "Manage the Upload API Source"
id: 4405859135511
section: "Manage Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405859135511-Manage-the-Upload-API-Source
updated_at: 2021-09-21T01:26:41Z
---

# Manage the Upload API Source

# Manage the Upload API Source

Composer supports live streaming sources via its
[Upload API](https://devnet.logianalytics.com/hc/en-us/articles/4405859140247-Use-the-Upload-API) data connector. Keep in mind that this source uses PostgreSQL as a storage medium for the incoming data flow. By default, Composer uses PostgreSQL to store the data for Upload API. This PostgreSQL instance is separate from other PostgreSQL instances you may have in existence. You can elect to use another PostgreSQL instance that you may have by changing the configuration properties.

## Before You Begin

If you want to use an existing PostgreSQL instance in conjunction with the Upload API microservice, you need to find the above information in your  `edc-postgresql.properties` file.

## Use Another PostgreSQL Instance for Upload API

1. Use the following command to access and open the properties file:

```
   vi /etc/zoomdata/zoomdata.properties
```

2. Add the following parameters to the file:

   ```
   #  that are configure for Upload API
     
   upload.destination.params.user_name=yourusername
     
   upload.destination.params.password=yourpassword
     
   upload.destination.params.jdbc_url=jdbc:postgresql://yourlocalhost:yourport//zd_upload
     
   upload.batch-size=1000
   ```
3. Save and exit the configuration file.
4. Restart the Composer server.
