---
title: "Specifying the Application Metadata"
id: 4406822198807
section: "Developer Tools - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822198807-Specifying-the-Application-Metadata
updated_at: 2022-04-06T06:10:45Z
---

# Specifying the Application Metadata

# Specifying the Application Metadata

InfoGo takes advantage of two special elements, **Metadata** and **Active Query Builder**, that are installed with it to enable extended functionality in Studio and in the Analysis Grid super-element.

Developers can use the **Web Metadata Builder** to specify the data that will be available for use at runtime by creating a metadata file. Step-by-step instructions for creating or editing a metadata file can be found in [Web Metadata Builder](https://devnet.logianalytics.com/hc/en-us/articles/4406817979799-Web-Metadata-Builder).

Data connections and metadata can also be managed inside InfoGo at runtime. To enable this feature, the **Security** element's **Metadata Admin Security Right IDs** attribute should have a value of *InfoGoDataManager*.

Then give designated users the InfoGoDataManager security Right and they'll see a special option in
the side-bar menu:

![](https://devnet.logianalytics.com/hc/article_attachments/5263090309911/cfginfogo125_04.png)

This option launches an embedded instance of the Web Metadata Builder and allows data connection and metadata creation and management right inside InfoGo, at runtime.

Access to the Web Metadata Builder tool can be disabled for *all* users by setting the **General** element's **Disable Metadata Builder** attribute equal to *True*, in the \_Settings definition. To grant more selective access to the tool, use the Security element's Metadata Admin Security Right IDs attribute discussed earlier.

Metadata created externally can also be retrieved from a REST-style web service by specifying the service's URL in the Metadata element's **Metadata Url**
attribute. When the MetaData Url is specified, the Web MetaData Builder works in read-only mode, allowing the user to view everything, but editing permissions are withheld.

![](https://devnet.logianalytics.com/hc/article_attachments/5263096722455/criticalicon.png) If you want users to be able to select different metadata files at runtime, be sure to enumerate them as a comma-separated list in the goMetadataIDsAnalysisGrid and/or goMetadataIDsDiscovery constants. See the constants table on the next page for more information.

![](https://devnet.logianalytics.com/hc/article_attachments/5263073928343/ssrmv12.7_55x20.png)If the metadata changes, such as the removal of a column, after Analyses have been created, a warning about the missing column will be displayed, instead of the expected visualization.

After building your metadata file, return to this topic and continue with [Configuring Scheduler and SMTP Services](https://devnet.logianalytics.com/hc/en-us/articles/4406817197335-Configuring-Scheduler-and-SMTP-Services).
