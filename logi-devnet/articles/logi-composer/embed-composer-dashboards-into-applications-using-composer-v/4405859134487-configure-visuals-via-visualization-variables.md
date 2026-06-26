---
title: "Configure Visuals via Visualization Variables"
id: 4405859134487
section: "Embed Composer Dashboards Into Applications using Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405859134487-Configure-Visuals-via-Visualization-Variables
updated_at: 2021-09-21T01:26:42Z
---

# Configure Visuals via Visualization Variables

# Configure Visuals via Visualization Variables

When a Composer visual is embedded into a custom application, it uses the default settings provided in the data source configuration for that visual. For example, your source *Real Time Sales* has a default configuration for pie charts, established when the data source is created. For more information about configuring a source's default settings for a particular visual, see [*Visual Setup*](https://devnet.logianalytics.com/hc/en-us/articles/4405851258775-Visual-Setup). To use the default configuration with an embedded visual, you only need to make sure that the correct metrics and fields or groups are present in the data query that supplies the visual
with data and leave the `variables` key null (`{}`) in the `visualize()` call. For more information about configuring and creating a data query, see [*Query Configuration Object*](https://devnet.logianalytics.com/hc/en-us/articles/4405851145879-Query-Configuration-Object) or [*Use a Data Query*](https://devnet.logianalytics.com/hc/en-us/articles/4405850882839-Use-a-Data-Query).

When embedding a visual, you also have the option of overriding default configurations by modifying the configuration of visual settings. You modify the default settings with the `variables` key in the parameter passed to the
`visualize()` method.
