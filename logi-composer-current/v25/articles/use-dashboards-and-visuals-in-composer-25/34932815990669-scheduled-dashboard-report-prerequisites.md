---
title: "Scheduled Dashboard Report Prerequisites"
id: 34932815990669
section: "Use Dashboards and Visuals in Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932815990669-Scheduled-Dashboard-Report-Prerequisites
updated_at: 2026-05-26T22:06:55Z
---

# Scheduled Dashboard Report Prerequisites

# Scheduled Dashboard Report Prerequisites

Before users can schedule and send dashboard reports, configure:

* Mail server information
* SFTP information ([if enabled in your environment](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932636844045-Server-Level-Variables#scheduled-report)) to deliver reports to your environment users at the [defined SFTP location](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932831429389--Scheduled-Dashboard-Report-Properties#sftp.host).
* Confirm memory settings
* Optionally adjust the screenshot resolution based on your users' needs

To schedule a dashboard report, you must be an administrator or assigned to a group with the **Create Scheduled Reports** or **Administer Scheduled Reports**[privilege](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932577846157-Group-Privilege-Reference).

## Configure Mail Server Settings

Add JavaMail API properties to the `zoomdata.properties` file to identify the mail server and other mail properties required to send the scheduled reports. This can include `mail.smtp.auth, mail.smtp.host`, `mail.smtp.port`, `mail.imap.host`, and `mail.imap.port`). Composer supports both IMAP and SMTP protocols. Complete descriptions of IMAP and SMTP protocol JavaMail properties can be found at these links:

* IMAP: <https://javaee.github.io/javamail/docs/api/com/sun/mail/imap/package-summary.html>
* SMTP: <https://javaee.github.io/javamail/docs/api/com/sun/mail/smtp/package-summary.html>

See [zoomdata.properties Properties](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932680261261-zoomdata-properties-Properties) for information about the properties in the `zoomdata.properties` file.

## Send to an SFTP Location [File Drop]

When [enabled](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932636844045-Server-Level-Variables#scheduled-report) in your environment, you can define the remote directory to which scheduled self service reports and scheduled dashboard reports are delivered to your users.

You can define these attributes at the instance level for al users. Alternatively, define for specific tenants or users.

* Use tenant attributes to pass these configuration properties to your instance. Use the `accounts` endpoint to define or verify settings for your desired tenants.
* For users, pass these configuration properties to your instance using their user attributes. Use the `user` endpoint to define or verify settings for your desired users.

Reserved attributes include:

* sftp.host
* sftp.password
* sftp.port
* sftp.remoteDirectory
* sftp.strictHostKeyChecking
* sftp.user
* email.replyToAddress
* email.senderDisplayName

**Important:** You must create a folder to hold the files for SFTP communications.

API documentation is provided in your environment at this link: `https://<composer-URL>/composer/swagger-ui.html`.

### Containerized Environments

You can make changes to the appropriate helm chart value overrides. For example, using your own information (default port is 2222):

discovery:
zoomdataWeb:
properties:
# SFTP Configuration for Scheduled Exports
sftp.host: "192.168.1.1"
sftp.port: "2222"
sftp.user: "logisymphony"
sftp.password: "LogiSFTP123!"
sftp.strictHostKeyChecking: "no"
sftp.remote.directory: "/exports”

**Important:** You must mount a container to hold the files for SFTP communications. Define the `extraEnvs`, `extraVolumes`, and `extraVolumeMounts` as needed, before applying your updated overrides. Alternatively, use docker compose to create an SFTP server locally.

## Confirm Memory Settings

If you plan to schedule numerous concurrent dashboard reports, you may need to confirm the memory configuration settings for your environment and the screenshot service pool configuration settings will meet your needs, or alter them if needed. See [Configure Memory Settings](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932637063437-Configure-Memory-Settings) and [Set Up the Screenshot Microservice](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933044663181-Set-Up-the-Screenshot-Microservice).

Log messages related to dashboard report scheduling are stored in the `zoomdata.log`[log file](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933097277069-Composer-Log-Files-Reference).

## Screenshot Resolution

Composer's resolution for PNGs and PDFs created as scheduled reports is 1280 x 720. If your users require a higher resolution, adjust the height and width properties in `zoomdata.properties`: `dashboard.scheduling.screenshot.png.height` and `dashboard.scheduling.screenshot.png.width`. Restart the screenshot microservice after making changes to `zoomdata.properties`.

In environments where you distribute a high number of simultaneous reports (200 users or more), a higher screen resolution such as 4k or 2160p (3840 x 2160) can have performance impacts. Balance the resolution of your scheduled dashboard reports with the frequency and recipient list size for your reports.

### Containerized Environments

You can make changes to appropriate yaml files to adjust properties and feature flags. For the screenshotService, templates and yaml files you can update are located in the path `logicomposer/charts/composer/templates``logisymphony/charts/composer/templates` of the untarred Helm package. These files include:

* Core configuration file: screenshot-service-deployment.yaml
* Screenshot Service properties map: screenshot-service-configmap.yaml
* Screenshot Service autoscaling options: screenshot-service-hpa.yaml

See [zoomdata.properties Properties](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932680261261-zoomdata-properties-Properties) for information about the properties in the `zoomdata.properties` file. See  [Scheduled Dashboard Report Properties](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932831429389--Scheduled-Dashboard-Report-Properties).
