---
title: "Upload Keyset Data From a CSV\u00a0File Using the API"
id: 4405851106327
section: "Use Dashboards and Visuals in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405851106327-Upload-Keyset-Data-From-a-CSV-File-Using-the-API
updated_at: 2021-09-21T01:29:01Z
---

# Upload Keyset Data From a CSV File Using the API

# Upload Keyset Data From a CSV File Using the API

You can upload keyset data from a CSV file using the API. Use the `POST /api/keysets/upload` API endpoint to do this. The CSV file must provide the field name, file data, the file name, the keyset name, and the data source definition ID. A keyset description is optional.

You must be the owner of the keyset or be a user with the **Can Administer Dashboards**[privilege](https://devnet.logianalytics.com/hc/en-us/articles/4405859114647-Group-Privilege-Reference).

The CSV file should be in the following format. A header should not be included.

```
fieldName:<field-name>
fileData: <file-information>
fileName:<CSV-file-name>
keySetName:<keyset-name>
keySetDesc:<optional-keyset-description>
sourceId:<data-source-id>
```

The response from this endpoint includes a unique ID for the keyset. You will need this ID if you update the keyset from a CSV file.

For more information, see your API documentation. API documentation is provided with your Composer installation at this link: `https://<composer-URL>/composer/swagger-ui.html`.
