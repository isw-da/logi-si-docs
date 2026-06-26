---
title: "Upload Keyset Data From a CSV\u00a0File Using the API"
id: 34933047829773
section: "Use Dashboards and Visuals in Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933047829773-Upload-Keyset-Data-From-a-CSV-File-Using-the-API
updated_at: 2026-05-26T22:07:28Z
---

# Upload Keyset Data From a CSV File Using the API

# Upload Keyset Data From a CSV File Using the API

You can upload keyset data from a CSV file using the API. Use the `POST /api/keysets/upload` API endpoint to do this. The CSV file must provide the field name, file data, the file name, the keyset name, and the data source definition ID. A keyset description is optional.

You must be the owner of the keyset or be a user with the **Administer Dashboards** [privilege](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932577846157-Group-Privilege-Reference).

The CSV file should be in the following format. A header should not be included.

fieldName:<field-name>
fileData: <file-information>
fileName:<CSV-file-name>
keySetName:<keyset-name>
keySetDesc:<optional-keyset-description>
sourceId:<data-source-id>

The response from this endpoint includes a unique ID for the keyset. You will need this ID if you update the keyset from a CSV file.

For more information, see your API documentation.

API documentation is provided in your environment at this link: `https://<composer-URL>/composer/swagger-ui.html`.
