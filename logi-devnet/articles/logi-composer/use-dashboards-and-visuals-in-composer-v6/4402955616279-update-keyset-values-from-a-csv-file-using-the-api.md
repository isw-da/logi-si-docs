---
title: "Update Keyset Values From a CSV\u00a0File Using the API"
id: 4402955616279
section: "Use Dashboards and Visuals in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4402955616279-Update-Keyset-Values-From-a-CSV-File-Using-the-API
updated_at: 2021-08-07T17:33:37Z
---

# Update Keyset Values From a CSV File Using the API

# Update Keyset Values From a CSV File Using the API

You can update keyset data from a CSV file using the API. Use the `PUT /api/keysets/upload/<keyset-id>` API endpoint to do this. The keyset ID was assigned when the keyset was initially uploaded using a CSV file. See [*Upload Keyset Data From a CSV File Using the API*](https://devnet.logianalytics.com/hc/en-us/articles/4402955617559-Upload-Keyset-Data-From-a-CSV-File-Using-the-API).

It should be in the following format. A header should not be included.

```
fileData: <file-information>
fileName:<CSV-file-name>
keySetId:<keyset-ID>
keySetName:<keyset-name>
keySetDesc:<optional-keyset-description>
sourceId:<data-source-id>
```

For more information, see your API documentation. API documentation is provided with your Composer installation at this link: `https://<composer-URL>/composer/swagger-ui.html`.
