---
title: "Security Checklist"
id: 5281588834455
section: "Deployment"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281588834455-Security-Checklist
updated_at: 2022-05-03T22:08:19Z
---

# Security Checklist

# Security Checklist

There are a number of precautions to take before running Exago BI in a production environment.

* Set an external temp path
* Disable direct access
* Set configuration and API credentials
* Remove the UXML configuration file
* Remove the Admin Console
* Encrypt Scheduler Service working data
* Disable SOAP Web Service API
* Content Security Policy HTTP Headers

This topic mentions several Admin Console settings. There are matching configuration file nodes and API properties that can be used for modifying these settings as well. For more information, review [Config File XML & API Setting Reference (General Nodes)](https://devnet.logianalytics.com/hc/en-us/articles/5281643841175-Config-File-XML-API-Setting-Reference-General-Nodes-) and [Config File XML Reference (All Nodes but General)](https://devnet.logianalytics.com/hc/en-us/articles/5281627946391-Config-File-XML-Reference-All-Nodes-but-General-).

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> This topic references `<WebApp>/`,
> `<WebSvc>/` and `<Sched>/`as a placeholder
> for the Web Application, Web Service API and Scheduler Service's install
> location respectively. The default install location is
> `C:\Program Files\Exago\ExagoWeb\` (`/opt/Exago/` on Linux),
> `C:\Program Files\Exago\ExagoWebApi\` ( `/opt/Exago/WebServiceApi/` on Linux) or
> `C:\Program Files\Exago\ExagoScheduler\` (`/opt/Exago/Scheduler/` on Linux); however, these directories
> can be changed during installation.

## Set an External Temp Path

The Temp directory contains working data that may contain sensitive information. If the **Temp Path** configuration setting is left blank, Exago BI defaults to a Temp folder at the root of the installation directory. This is not recommended because it could expose temporary data to web access.

The Temp Path should be set to a location outside of the Exago BI installation (and behind the server’s firewall). Set the Temp Path in **Admin Console** > **General** > **Main Settings** > **Temp Path**.

## Disable Direct Access

Access to Exago BI should be curated through the API so that user permissions can be set via Roles or the Storage Management identity system. Users should not be able to access the home page directly, which would bypass role restrictions. To disable direct access, set the **Admin Console** > **General** > **Main Settings** > **Allow direct access to Exago (bypassing API)** to *False*.

## Set Configuration and API Credentials

A User ID, Password, and REST Key should be set in the configuration. This safeguards access to the Admin Console and REST API. See [REST API](https://devnet.logianalytics.com/hc/en-us/articles/5281660927895-REST-Introduction) for information on accessing a password-protected web service. To do so, set values for the following settings:

* **Admin Console** > **General** > **Other Settings** > **User Id**
* **Admin Console** > **General** > **Other Settings** > **Password**
* **Admin Console** > **General** > **Other Settings** > **Confirm Password**
* **Admin Console** > **General** > **Other Settings** > **REST Key**

## Remove the XML Configuration File

The Admin Console generates two copies of the base configuration: a plain-text XML file, typically `WebReports.xml` and an encrypted version `WebReports.xml.enc`. Plain-text config files may contain sensitive information, such as database connection strings, schemas, user names, and passwords.

Once config settings are finalized, remove the plain-text config file from the Config folder and save it to a secure location.

## Remove the Admin Console

The Admin Console should not be accessible in a production environment. To permanently remove the Admin Console, in each installation:

1. Delete `<WebApp>\Bin\admin.aspx.cdcab7d2.compiled`

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Tip")
>
> `Admin.aspx` can be deleted as well, or edit it to show a static error message.

## Encrypt Scheduler Service Working Data

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> This section applies only in environments where at least one **Scheduler Service** is in use.

Each Scheduler Service stores working data in a local temporary folder. For security, this data should be encrypted. In each [Scheduler Service Configuration](https://devnet.logianalytics.com/hc/en-us/articles/5281627554583-Scheduler-Service-Configuration) file:

1. Set the `<encrypt_schedule_files>` setting to *True*. For example:

   ```
   <encrypt_schedule_files>True</encrypt_schedule_files>
   ```
2. Restart the Scheduler Service

## Disable SOAP Web Service API

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> This section applies only in environments where the REST Web Service API is in use. If the .NET API is being used instead, the REST Web Service may not be installed. It may be uninstalled if it will not be used.

If you are using the REST Web Service API, disable the SOAP API to prevent any unauthorized requests. To do so, in each instance of the Web Service API:

1. Delete `<WebSvc>\Bin\api.asmx.cdcab7d2.compiled`

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Tip")
>
> `Api.aspx` can be deleted as well, or edit it to show a static error message.

## Set Additional Response Header Flags When Using Content Security Policy

When using Content Security Policy (CSP) rules with the web server, set these additional HTTP Response Headers to insure compatibility with Exago BI:

```
default-src 'self'; style-src 'self' 'unsafe-inline'; script-src 'self' 'unsafe-inline' 'unsafe-eval';
```

Instructions to configure the web server with these headers can be found at the links below:

* [IIS](https://content-security-policy.com/)
* [Apache](https://content-security-policy.com/examples/htaccess/)
* [NGINX](https://content-security-policy.com/examples/nginx/)
