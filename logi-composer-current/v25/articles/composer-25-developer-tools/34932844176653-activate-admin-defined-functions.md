---
title: "Activate Admin-Defined Functions"
id: 34932844176653
section: "Composer 25 Developer Tools"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932844176653-Activate-Admin-Defined-Functions
updated_at: 2026-05-26T22:06:57Z
---

# Activate Admin-Defined Functions

# Activate Admin-Defined Functions

**Activate an admin-defined function in** Composer

1. Create a JSON file containing your admin-defined function definitions. This JSON file should reside on the same machine as the connector server. The recommended location for this JSON file is `/etc/zoomdata` (for example, `/etc/zoomdata/edc-impala-functions.json`). See [Admin-Defined Function JSON Files](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932796505869-Admin-Defined-Function-JSON-Files) for more information about creating this JSON file.
2. Update the connector server configuration so the connector knows where to find the file containing the admin-defined functions you have created. Complete these steps:

   1. Locate and edit the properties file for the connector in the `/etc/zoomdata` directory. For example, the Impala properties file is called `edc-impala.properties`.

      vi <property-file>
   2. Locate and update the `functions.template.json.path` property in the Functions section of the properties file. Supply the path to the JSON file containing your admin-defined functions in the property. In the following example, the path for the  `edc-impala-functions.json` file is specified.

      functions.template.json.path=/etc/zoomdata/edc-impala-functions.json

      All admin-defined functions for a connector should be defined in the same JSON file, so only one path is needed per data source.
   3. Save the properties file.
3. Restart the connector server.

The connector reads and validates the JSON file only at startup. When you restart the connector, it loads the admin-defined function JSON file and will validate the function definitions in the file. Errors are logged if they are found. If the function definitions are valid, the connector starts successfully and writes a list of the loaded admin-defined functions to the log.
