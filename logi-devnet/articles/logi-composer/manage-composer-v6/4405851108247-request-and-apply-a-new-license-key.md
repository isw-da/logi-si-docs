---
title: "Request and Apply a New License Key"
id: 4405851108247
section: "Manage Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405851108247-Request-and-Apply-a-New-License-Key
updated_at: 2021-09-21T01:30:41Z
---

# Request and Apply a New License Key

# Request and Apply a New License Key

Composer notifies you when your license key is about to expire.

## Request and Apply a New License Key for v6.9 and Higher

(This process is for version 6.9 and higher. To see how to request and apply a new license key for Composer prior to v6.9, see [Request and Apply a New License Key--Composer v6.0 to v6.8](#v6.0to6.8))

![](https://devnet.logianalytics.com/hc/article_attachments/4409070299415/criticalicon.gif)**IMPORTANT:** Older license keys are not compatible with Composer 6.9. If you are upgrading from any older Composer or Zoomdata release, a new license must be requested.

![](https://devnet.logianalytics.com/hc/article_attachments/4409054855575/noteicon.jpg) The DevNet License Manager provides license keys to a person in your organization that we term the License POC (Point of Contact). If you don't know who this person is, please reach out to your Account Manager at Logi Analytics.

![](https://devnet.logianalytics.com/hc/article_attachments/4409054855575/noteicon.jpg) When a Composer standard or trial license expires, only supervisors can log in (so they can update the license). Regular users will see a message stating that the license has expired.

License keys can be managed using the supervisor UI (see [*Request and Apply a New License Key*](#)) or by using the following API endpoints:

| Endpoint | Method | Description |
| --- | --- | --- |
| `/api/license` | GET | Returns license information for the instance. |
| POST | Updates license information for the instance |

API documentation is provided with your Composer installation at this link: `https://<composer-URL>/composer/swagger-ui.html`.

To request and apply a new license key:

1. In the environment for you which you need a new license key, log in as the supervisor.
2. On the Supervisor menu, select **License**. The Manage License page appears.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4409054858775/mng-license_384x405.png)

   This screen shows your current Composer instance ID and its current expiration date. ![](https://devnet.logianalytics.com/hc/article_attachments/4409054855575/noteicon.jpg) If you select ![](https://devnet.logianalytics.com/hc/article_attachments/4409070302359/download-lic-key_157x25.png), your current license key is downloaded in a `license.key` file.
3. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4409070302871/download-inst-token_165x27.png). A `.tok` file is downloaded to your computer.
4. Log into DevNet and visit the License Management page to create a license file. You do this by assigning one of your license keys to a specific instance of Composer, by uploading the `.tok` file from the previous step. DevNet generates a license.key file, and downloads the file to your machine.
5. When you receive the new license key file, save it.
6. From your Supervisor menu, select **Browse** and find the license key you just downloaded. Then, select **Submit**. Composer applies the new license to your instance.

If a problem occurs, contact your Composer sales or technical support representative.

## Request and Apply a New License Key--Composer v6.0 to v6.8

![](https://devnet.logianalytics.com/hc/article_attachments/4409070299415/criticalicon.gif)**IMPORTANT:** Older license keys are not compatible with Composer 6.9. If you are upgrading from any older Composer or Zoomdata release, a new license must be requested.

![](https://devnet.logianalytics.com/hc/article_attachments/4409054855575/noteicon.jpg) The DevNet License Manager provides license keys to a person in your organization that we term the License POC (Point of Contact). If you don't know who this person is, please reach out to your Account Manager at Logi Analytics.

![](https://devnet.logianalytics.com/hc/article_attachments/4409054855575/noteicon.jpg) When a Composer standard or trial license expires, only supervisors can log in (so they can update the license). Regular users will see a message stating that the license has expired.

License keys can be managed using the supervisor UI (see [*Request and Apply a New License Key*](#)) or by using the following API endpoints:

| Endpoint | Method | Description |
| --- | --- | --- |
| `/api/license` | GET | Returns license information for the instance. |
| POST | Updates license information for the instance |

API documentation is provided with your Composer installation at this link: `https://<composer-URL>/composer/swagger-ui.html`.

To request and apply a new license key:

1. In the environment for you which you need a new license key, log in as the supervisor.
2. On the Supervisor menu, select **License**. The Manage License page appears.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4409070303383/mng-license_288x134.png)

   This screen shows your current Composer instance ID and its current expiration date.
3. Copy your current Composer instance.
4. Identify your current Composer version. This is found in the Account dialog. See [Switching Accounts](https://d3trial.zendesk.com/hc/en-us/articles/4404891749911-Switching-Accounts).
5. Log into DevNet and visit the [License Management](https://clm.logianalytics.com/rdpage.aspx?rdReport=LicenseManager) page to create a license. You do this by assigning one of your license keys to a specific instance of Composer, by pasting the Composer instance ID from the previous step. DevNet generates a license.
6. Save the license to the Composer licensing table.
7. Copy this license to your clipboard.
8. Return to the Manage License screen and paste the new license key in the New License Key text box.

If a problem occurs, contact your Composer sales or technical support representative.
