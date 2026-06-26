---
title: "Amazon S3 File Storage"
id: 5281592475287
section: "Deployment"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281592475287-Amazon-S3-File-Storage
updated_at: 2022-05-03T22:08:58Z
---

# Amazon S3 File Storage

# Amazon S3 File Storage

Amazon Cloud Storage can be used for:

* [Config Storage](#Config)
* [Report Storage pre-v2020.1](#Report)
* [Temporary File Storage](#Temporar) (which includes themes and templates).

In order to connect to a cloud server:

1. Obtain the access key and secret key. See [Getting Your Access Key ID and Secret Access Key](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSGettingStartedGuide/AWSCredentials.html).
2. Locate the region code for the location of the cloud server. See [Regions and Availability Zones](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html).
3. Create a formatted connection string in the following format. This string will be used in various places in the application to connect to the cloud storage repository.

   ```
   region='region';accesskey='accesskey';secretkey='secretkey';bucketname='bucketname'
   ```

* `region` — the region of the cloud server from step 2.
* `accesskey`: Amazon access key credential from step 1.
* `secretkey`: Amazon secret key credential from step 1.
* `bucketname`: The storage directory.

## EC2 v2016.3.4+

To enable EC2 instances access to S3 buckets, an [IAM role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) needs to be created and tied to the instances with a policy allowing that level of access.

To use instance credentials, set every instance of **accesskey** to *ec2*.

The Config, Reports, and Temp files can all reside in a single S3 bucket, and will be placed automatically into separate Config, Reports, and Temp folders, which should not need to be created ahead of time.

![AxiaMedEC2Architecture.png](https://devnet.logianalytics.com/hc/article_attachments/5432126950551/axiamedec2architecture.png)

Architecture diagram illustrating the EC2 environment

## Config Storage

An Exago installation contains a minimum of one base configuration file, typically named `WebReports.xml.`

There are three ways to specify a cloud location for this config file:

1. A file in the Web Application install directory called [appSettings.config](https://devnet.logianalytics.com/hc/en-us/articles/5281615366423-Application-Settings#appSetti).
2. When using the .NET API, an argument in the **API constructor method**.
3. When using the REST Web Service API, a connection string needs to be placed in both **appSettings.config** files in the WebServiceApi folder and the Web Application install directory.

### Method 1: appSettings.config

Exago utilizes the **appSettings.config** file in the root folder of the install directory to load certain settings with the start of the web server. For more information, see [Application Settings](https://devnet.logianalytics.com/hc/en-us/articles/5281615366423-Application-Settings).

If it does not exist, create it as a text file with the following content:

```
<?xml version="1.0"?>
	<appSettings></appSettings>
```

To set the config file location, place or change this **ExagoConfigPath** node in the `appSettings.config` file as follows:

```
<add key="ExagoConfigPath" value="pathtype=s3;region='region';accesskey='accesskey';secretkey='secretkey';bucketname='bucketname';storagekey=config"/>
```

Change the `bucketname` and `region` values to match the environment along with the `accesskey` and `secretkey` from the beginning of this topic:

* + `bucketname` — the S3 bucket used for config, report, and temporary file storage
  + `region` — the AWS region where the S3 bucket is located

* `storagekey` — must always be *config*

To allow S3 access for EC2 instances, add the following line to the config after configuring the EC2 instances:

```
<add key="ExagoConfigPath" value="pathtype=s3;region='region';accesskey='ec2';bucketname='bucketname';storagekey=config"/>
```

### Method 2: .NET API

Exago .NET API apps cannot access the `appSettings.config file`. Instead, you must use one of the following two methods to specify a config file location:

1. Place the **config key** within the embedding host application’s `web.config` or `app.config`.
2. Pass the connection string to the API constructor:

```
API myAPI = new Api("/exago/virtual/path", "WebReports.xml", "pathtype=s3;region='region';accesskey='accesskey';secretkey='secretkey';bucketname='bucketname'");
```

Similarly, managing and creating folders within an S3 file system through the .NET API requires an alternate method: Instead of using the `ReportMgmtFileSystem` class to create, rename, or otherwise manage the file system within the .NET API, methods defined within the `ReportManagement` property of the API object must be used. For example, to add folders via the .NET API when using S3 storage, the following method should be called:

```
api.ReportManagement.AddFolder("<parent folder>", "<child folder>");
```

### Method 3: REST Web Service API

The REST Web Service API requires the following connection string to be placed in both `appSettings.config` files, located in the WebServiceApi folder and Exago’s install directory.

```
<add key="ExagoConfigPath" value="pathtype=s3;region='us-east-1';accesskey='accesskey';bucketname='bucketname';secretkey='secretkey';storagekey=config"/>
```

## Report Storage pre-v2020.1

For versions *v2020.1+*, content management is handled by the Storage Management system, and the following section does not apply.

To use Amazon for report and folder management in *pre-v2020.1*, enter the connection string in **Admin Console** > **General** > ![TreeGeneralNode.png](https://devnet.logianalytics.com/hc/article_attachments/5432159353239/treegeneralnode.png)**Main Settings** > **Report Path**

```
pathtype=s3;region='region';accesskey='accesskey';secretkey='secretkey';bucketname='bucketname'
```

For EC2, the Report Path should be defined as:

```
pathtype=s3;region='region';accesskey='ec2';bucketname='bucketname'
```

## Temporary File Storage

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> Log files will still be written to the **Admin Console** > **General** > **Main Settings** > **Temp Path** even when a **Temp Cloud Path** is defined.

To use Amazon for temporary file storage, enter the connection string in **Admin Console** > ![TreeGeneral.png](https://devnet.logianalytics.com/hc/article_attachments/5432174178839/treegeneral.png)**General** > ![TreeGeneralNode.png](https://devnet.logianalytics.com/hc/article_attachments/5432159353239/treegeneralnode.png)**Main Settings** > **Temp Cloud Service**.

```
type=s3;region='region';accesskey='accesskey';secretkey='secretkey';bucketname='bucketname'
```

For EC2, the Temp Path should be defined as:

```
pathtype=s3;region='region';accesskey='ec2';bucketname='bucketname'
```
