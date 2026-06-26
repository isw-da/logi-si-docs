---
title: "About Logi DataHub v3"
id: 4406640348055
section: "Introduction to Logi DataHub v3"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406640348055-About-Logi-DataHub-v3
updated_at: 2022-04-01T03:13:19Z
---

# About Logi DataHub v3

# About Logi DataHub v3

Logi DataHub v3 extends the functionality of Dataviews by providing access to a variety of additional data sources and a means to cache retrieved data. This topic introduces Logi DataHub v3.

![](https://devnet.logianalytics.com/hc/article_attachments/5160434622487/criticalicon.gif) Logi DataHub v3, as a product, *has changed*.

Earlier versions of DataHub included functionality for creating and managing [Dataviews](https://devnet.logianalytics.com/hc/en-us/articles/4406822071191-Dataviews); this functionality has been removed from Logi DataHub v3 and moved into our Discovery v3.0 add-on module and its successor, Logi Platform Services. Another change is that Logi DataHub v3 itself now requires a Logi [product
license](https://devnet.logianalytics.com/hc/en-us/articles/4406817805207-Product-Licensing).

Without Logi DataHub v3, the data defined in Dataviews is retrieved in real time and cached using Logi Info's standard memory and temporary cache file technology.

However, when you install Logi DataHub v3, the functionality of Dataviews is *extended*: they can also access a variety of file-, cloud-, and application-based data sources, including:

* Amazon Dynamo DB
* Eloqua
* Facebook
* Financial Accounts (OFX)
* Google Analytics
* Marketo
* Microsoft Dynamics CRM Online
* Microsoft Dynamics CRM On Premise
* Microsoft Dynamics GP
* Netsuite
* OData
* Quickbooks Online
* Quickbooks On Premise
* Quickbooks POS
* Salesforce
* SAP Netweaver
* Twitter
* Microsoft Excel file
* Comma-Separated Values (CSV) data file

Data from these sources can be used alone or joined with data from the traditional data sources available for Dataviews.

In addition, a self-tuning, easy-to-maintain, columnar data store is installed, allowing you to cache retrieved data in a database for improved performance, especially with large data sets. Once the data is cached, a schedule can be established to refresh it periodically.
