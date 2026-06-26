---
title: "Configure Visuals Using Visualization Variables"
id: 43700988843149
section: "Embed Composer Dashboards Into Applications Using Composer"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700988843149-Configure-Visuals-Using-Visualization-Variables
updated_at: 2026-05-29T14:07:11Z
---

# Configure Visuals Using Visualization Variables

# Configure Visuals Using Visualization Variables

When a Composer visual is embedded into a custom application, it uses the default settings determined by the metrics and fields or groups present in the data query that supplies the visual with data. For more information about configuring and creating a data query, see [Query Configuration Object](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701159561101-Query-Configuration-Object) or [Use a Data Query](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701023141133-Use-a-Data-Query).

When embedding a visual, you also have the option of overriding default configurations by modifying the configuration of visual settings. You modify the default settings with the `variables` key in the parameter passed to the
`visualize()` method.

Before you can encode settings into an embedded visual, you must identify every required setting as well as any optional settings that you wish to use. Visual settings can be identified using an internal REST API method.

The REST API method used in these steps is considered internal to the Composer application. Internal APIs should not be used except as directed. For more information about using internal APIs, see
[Cautionary Note About Internal APIs](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701137992717-Cautionary-Note-About-Internal-APIs).
