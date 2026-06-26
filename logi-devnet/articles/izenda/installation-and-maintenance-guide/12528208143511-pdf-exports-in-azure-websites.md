---
title: "Pdf Exports in Azure Websites"
id: 12528208143511
section: "Installation and Maintenance Guide"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/12528208143511-Pdf-Exports-in-Azure-Websites
updated_at: 2023-02-23T14:53:06Z
---

# Pdf Exports in Azure Websites

# Pdf Exports in Azure Websites

Warning

This is no longer applicable in Izenda versions after 3.0 as the exporting provider has changed from EvoPDF to Syncfusion. Please see the changes in the release notes [here](https://www.izenda.com/docs/release_notes.html#v3-0-0-april-2-2019).

## Introduction

Izenda utilizes the EVO HTML to PDF Converter for Azure to provide pdf exporting in Azure websites. This feature requires the use of an Azure Cloud Service. The high-level flow is illustrated below.

![../../_images/evo_azure_architecture.png](https://devnet.logianalytics.com/hc/article_attachments/12528147910935/evo_azure_architecture.png)

## Installing and Configuring the Azure Service

### Required Components

There are two components needed for the Azure cloud service.

*EvoHtmlToPdfAzureService.cspkg*

*ServiceConfiguration.Cloud.cscfg*

These components as well as the installation guide this document is based on can be downloaded freely at the link below: <https://izenda.sharefile.com/d-s3149eb329e04a15a> (Please be sure to use this version)

### Installation

1. Login into your Microsoft Azure portal and create a new Cloud Service.

   > ![../../_images/azure_cs1.png](https://devnet.logianalytics.com/hc/article_attachments/12528147926295/azure_cs1.png)
   >
   > ![../../_images/azure_cs2.png](https://devnet.logianalytics.com/hc/article_attachments/12528147935127/azure_cs2.png)
2. In the first screen select a DNS name for your cloud service and then select a package.
3. In the next screen choose a deployment label and choose the **EvoHtmlToPdfAzureService.cspkg** file for package option and **ServiceConfiguration.Cloud.cscfg** file for configuration option. Enable the **Deploy even if one or more roles contain a single instance** option and finish the wizard. The deployment process may take several minutes.

   > ![../../_images/azure_cs3.png](https://devnet.logianalytics.com/hc/article_attachments/12528163939863/azure_cs3.png)
4. When the deployment has completed, navigate to the cloud service dashboard. Under the Properties > Input Endpoints, you can find the service IP address and port number. You will use this information configure Azure exporting in Izenda.

   > ![../../_images/azure_cs4.png](https://devnet.logianalytics.com/hc/article_attachments/12528163943959/azure_cs4.png)

## Configuring the Izenda instance

After the service has been configured, you must configure the Izenda application to use the service. The settings below are in the web.config file.

```
<configuration><configSections><sectionname="evoPdfSettings"type="Izenda.BI.Framework.Models.Exporting.EvopdfConfiguration"/></configSections><evoPdfSettingscloudEnable="true"><azureCloudServiceserver="120.0.0.1"port="40001"servicePassword=""/></evoPdfSettings></configuration>
```
