---
title: "Generate a Security Key"
id: 4402963047831
section: "Composer v6 Developer Tools"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4402963047831-Generate-a-Security-Key
updated_at: 2021-08-07T17:31:55Z
---

# Generate a Security Key

# Generate a Security Key

You need to have a security key to access your Composer server and its visuals, API, and data from a third-party web page or application. When generating a key, you have the option of setting an expiration date and time for it.

* When you generate a security key for a data source, users of the data source are automatically granted Read permission for all existing visuals using the data source, but not for any new visuals created after the security key was generated. Instead, a new security key must be generated for new visuals.
* When you generate a security key for a dashboard, users of the dashboard are automatically granted Read permission for all existing visuals on the dashboard for which they have Read permissions. However, if a new visual is created on the dashboard after the security key is generated, dashboard users will not automatically be granted Read permission for the new visual. Instead, a new security key must be generated for newer visuals on the dashboard. )

![](https://devnet.logianalytics.com/hc/article_attachments/4404959473559/noteicon.jpg) Security keys were formerly described as "API keys." This usage has been updated.

The instructions provided below also details the methods to generate a security key in a Linux environment or from any web browser.

## Prerequisites

To generate a security key to access the Composer Server, you must have network access to it.

## Generate a Security Key in a Linux Environment

To generate a security key in a Linux environment:

1. Use your terminal to enter the following command:

   ```
   curl -v --user <username:password> http://<yourcompanyurl>/api/sources/<id>/key?source=<Real+Time+Sales> --insecure
   ```

   Replace:

   * `<username:password>` with your actual credentials
   * `<yourcompanyurl>` with the URL for your Composer deployment, usually `yourcompany.com/zoomdata`.
   * `<Real+Time+Sales>` with the source that you want to access, replacing spaces in the name with plus signs (+). You can grant access to multiple sources, provided you have access to them all, by separating multiple source names with commas but not spaces. For example:

     ```
     source=Real+Time+Sales,Housing+Sales,HR+Records
     ```
2. Identify the security key in the generated output. For more information about identifying the security key, see [*Identify the Security Key*](#Identifying).

## Generate a Security Key from a Web Browser

To generate a security key from a web browser:

1. Enter your Composer service URL in the address bar:

   ```
   https://<yourcompanyurl>/api/sources/<id>/key?source=<Real+Time+Sales>
   ```

   Replace:

   * `yourcompanyurl` with the URL for your Composer deployment, usually `yourcompany.com/zoomdata`
   * `Real+Time+Sales` with the source that you want to access, replacing spaces in the name with plus signs (+). You can grant access to multiple sources, provided you have access to them all, by separating multiple source names with commas but not spaces. For example:

     ```
     source=Real+Time+Sales,Housing+Sales,HR+Records
     ```
2. Press **Enter**. Enter your user ID and password if you are prompted to do so.
3. Select **Login** to open a web page with an outputted JSON object.
4. Identify the security key in the generated output. For more information about identifying the security key, see [*Identify the Security Key*](#Identifying).

## Set an Expiration Date for the Key

Optionally, you can set an expiration date for a security key while generating it. To add an expiration date to a security key, append the expiration date to the end of the request in the following format.

```
&expirationDate=yyyy-mm-ddThh:mm:ss.sss
```

The capital T separates the date part from the time part of the date-time parameter. A completed example of a correct request follows.

```
https://www.yourcompany.com/composer/api/sources/<id>/key?source=Real+Time+Sales &expirationDate=2015-09-15T19:15:30.000
```

The key generated in the example expires on 15 September 2015 at 7:15:30 p.m., according to the Composer server's local time.

## Identify the Security Key

Within the outputted JSON object, the security key is identified by the label `token` and is enclosed in quotation marks, which are not part of the security key itself. Example output:

```
{
"id": "5910e8eee4b0e9185cd048fd",
"accountId": "5898841fe4b0c9dbdb601337",
"created": "2017-05-08 21:53:50.117",
"expire": "2027-05-08 21:53:50.117",
"createdBy": "admin",
"securityKeyType": "SOURCE",
"objectIds": [
"59079206e4b0efde29135495"
],
"token": "BldSqp2yBq"
}
```

If you specified an expiration date and time for the key, details of the expiration date and time are included in the output.
