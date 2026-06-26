---
title: "Integrating the Discovery Module"
id: 4419715171223
section: "Developer Tools - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715171223-Integrating-the-Discovery-Module
updated_at: 2022-07-17T02:24:55Z
---

# Integrating the Discovery Module

# Integrating the Discovery Module

The Logi Discovery Module (DM) is a separate, recommended add-on module that enables special elements in Logi Info and provides access to the **Thinkspace**, a highly-interactive analysis tool instead of, or in addition to, the Analysis Grid.

Installation information for the DM is available in [Install the Discovery Module - Windows](https://devnet.logianalytics.com/hc/en-us/articles/4419722963351-Install-the-Discovery-Module-Windows) and [Install the Discovery Module - Linux](https://devnet.logianalytics.com/hc/en-us/articles/4419715326871-Install-the-Discovery-Module-Linux) and is not repeated here. The remainder of this topic describes the configuration steps needed
to enable the DM in InfoGo.

If the DM has been installed, a special definition, goDiscovery, will be available in the InfoGo report definitions.

![](https://devnet.logianalytics.com/hc/article_attachments/7522817376279/cfginfogo125_03a.png)

Depending on how the goAnalysisType constant is configured (see below) different analysis tool options will be shown in the menu for use when creating a new analysis. Both options, as shown above, can be displayed if the constant is set to *UserSelectable.*

## Connecting to Data

A successful configuration of the Discovery Module requires *two* additional datasource connections, as described in the Connecting to Data section of [Connecting to the Logi Application Service](https://devnet.logianalytics.com/hc/en-us/articles/4419715254423-Connecting-to-the-Logi-Application-Service). Be sure to add and configure these elements, and to create metadata for the Connection element.

![](https://devnet.logianalytics.com/hc/article_attachments/7522725232151/criticalicon.png) In the goDiscovery definition, you must set the Thinkspace element's **Logi Application Service ID** attribute to match the ID of the Connection.Logi Application Service element you added in the \_Settings definition.

## Special DM Constants

In order to enable the DM, add the following constants and values to the \_Settings definition:

| Constant | Description |
| --- | --- |
| goAnalysisType | Specifies the analysis tool options that will appear on the menu. Possible values and effects include:  *AnalysisGrid* (or if left blank) - The Analysis Grid will be used, and the goAnalysisGrid definition will be shown when this option is selected. *Discovery -* (Assumes the DM is installed) The Thinkspace will be used, and the DM's goDiscovery definition will be shown when this option is selected. *UserSelectable -* Both options will be displayed, allowing the user to choose their analysis tool. |
| goMetadataIDsAnalysisGrid | Specifies a comma-separated list of one or more IDs of Metadata elements, defined for connections in the \_Settings definition, to be used with the Analysis Grid. If left blank, *all* Metadata element IDs from \_Settings will be used. This constant is used in the Active Query Builder in the goAnalysisGrid definition. |
| goMetadataIDsDiscovery | Specifies a comma-separated list of one or more IDs of Metadata elements, defined for connections in the \_Settings definition, to be used with the DM. If left blank, *all* Metadata element IDs from \_Settings will be used. This constant is used in the Active Query Builder in the goDiscovery definition |
