---
title: "Request and Apply a New License Key"
id: 34933040878349
section: "Manage Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933040878349-Request-and-Apply-a-New-License-Key
updated_at: 2026-05-26T22:07:44Z
---

# Request and Apply a New License Key

# Request and Apply a New License Key

Composer notifies you when your license key is about to expire.

**Note:** 
Use the DevNet License Manager to obtain license keys. These are provided to the person in your organization we term the License POC (Point of Contact). If you don't know who your License POC is, please reach out to your Account Manager.

**Note:** 
When a Composer standard or trial license expires, only system administrators can log in (to update the license). Regular users are shown a message that the license has expired.

To manage your license keys, see:

* [Manage License Keys in the UI](#Manage1)
* [Manage License Keys Using the Licensing API](#Manage2)
* [Manage License Keys Using Configuration Properties or Environment Variables](#Manage3)

## Manage License Keys in the UI

**Apply a new license key:**

1. In the environment for you which you need a new license key, log in system [admin](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932621360909-Supplied-Users-and-User-Groups#The2) or a member of the Supervisors group.
2. Select **License** from the menu. The Manage License page appears.

   This screen shows your current Logi Composer   instance ID and its current expiration date.

   **Note:** 
   If you select **Download Current Key**, your current license key is downloaded in a `license.key` file.
3. Select **Download Instance Token**. A `.tok` file is downloaded to your computer.
4. Log into DevNet and visit the License Management page to create a license file. You do this by assigning one of your license keys to a specific instance of Logi Composer , by uploading the `.tok` file from the previous step. DevNet generates a license.key file, and downloads the file to your machine.
5. Browse to find the license key you just downloaded. Then, select **Submit**. Logi Composer applies the new license to your instance.

## Manage License Keys Using the Licensing API

| Endpoint | Method | Description |
| --- | --- | --- |
| `/api/license` | GET | Returns license information for the instance. |
| POST | Updates license information for the instance |

API documentation is provided in your environment at this link: `https://<composer-URL>/composer/swagger-ui.html`.

If a problem occurs, contact your sales or technical support representative.

## Manage License Keys Using Configuration Properties or Environment Variables

Add your license keys and installation id to `zoomdata.properties`. Format the variables as shown below:

zoomdata.license.key=<value>  
zoomdata.installation.id=<value>

**Important:** 
License information provided via configuration properties or environment variables have a higher priority than keys stored in the database previously provided via API or user interface. If you attempt to change the keys using the API in an environment where licensing information from configuration properties or environment variables are in use, Logi Composer returns a failure message. Update the license key in the configuration files instead.

**Note:** 
For more information about extending licensing to a Kubernetes deployment, see [Apply Licenses](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933040538253-Apply-Licenses).
