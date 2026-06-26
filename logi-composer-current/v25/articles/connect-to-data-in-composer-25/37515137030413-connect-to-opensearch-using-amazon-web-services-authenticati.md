---
title: "Connect to OpenSearch Using Amazon Web Services Authentication"
id: 37515137030413
section: "Connect to Data in Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/37515137030413-Connect-to-OpenSearch-Using-Amazon-Web-Services-Authentication
updated_at: 2026-05-26T22:05:57Z
---

# Connect to OpenSearch Using Amazon Web Services Authentication

# Connect to OpenSearch Using Amazon Web Services Authentication

You can connect the Composer OpenSearch connectors to your OpenSearch data store using Amazon Web Services (AWS) credentials. After connecting, the Composer OpenSearch connectors work with AWS OpenSearch without any restrictions.

**Connect the OpenSearch connector to your OpenSearch data store using AWS authentication:**

**Important:** If you are connecting to OpenSearch versions earlier than 2.x, use the [Elasticsearch 7 connector](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932728155405-Manage-the-Elasticsearch-Connector).

1. Specify the AWS credentials in a standard AWS-format credentials file (see [Format of the credentials file](https://docs.aws.amazon.com/sdkref/latest/guide/file-format.html#file-format-creds)) and store the file in the OpenSearch connector’s file system.
2. Edit the [OpenSearch properties file](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932637143949-Connector-Properties-and-Property-Files) ( `edc-OpenSearch.properties`) and locate or add the `OpenSearch.aws.show-aws-connection-params` property to the file. This property indicates whether AWS-specific connection parameters should be shown when a new connector is created or the connection properties of an existing connector are refreshed. Valid values are `true` or `false`. The default is `false` (users will *not* see new AWS connection parameters).

   Set the value of this property to `true` and save the properties file. For more information about Composer properties files, see [Configuration Property Files](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932670123533-Configuration-Property-Files).
3. Create a new OpenSearch connection or edit an existing one (see [Add Data Store Connections](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932713955597-Add-Data-Store-Connections)).

   The AWS connection parameters appear in the UI. Supply values for them as described in the following table.

   | Parameter | Specify | Description |
   | --- | --- | --- |
   | `AUTHENTICATE_WITH_AWS_CREDENTIALS` | `true` | Indicate whether authentication with AWS credentials should be used. Note that the OpenSearch username / password specification and AWS credentials cannot be simultaneously used for authentication. Valid values are `true` or `false`; the default is `false` (AWS credentials are not used). |
   | `AWS_REGION` | a valid region name | Specify the AWS region where the target OpenSearch service is running. This parameter is optional when host names in the connection string have the standard format `<domain>.<region>.es.amazonaws.com` (the region name can be extracted from the host name). However, when specified, it has priority over the region name included in the host name. |
   | `AWS_PROFILES_CONFIG_PATH` | the path to the credentials file | Specify the location of the AWS credentials file in the OpenSearch connector’s file system. This parameter is optional when the credentials file is in the default location (`~/.aws/credentials` for the user of the connector). |
   | `AWS_PROFILE` | a valid profile name in the AWS credentials file | Specify the profile to use within the AWS credentials file. This parameter is optional if you choose to use the `default` profile in the AWS credentials file. |
4. After you have specified all parameters necessary for the connection definition, save it. See [Add Data Store Connections](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932713955597-Add-Data-Store-Connections).
