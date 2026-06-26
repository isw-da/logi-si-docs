---
title: "Analysis Grid Developers - Controlling Feature Access"
id: 4419715052695
section: "Developer Tools - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715052695-Analysis-Grid-Developers-Controlling-Feature-Access
updated_at: 2022-07-17T02:09:25Z
---

# Analysis Grid Developers - Controlling Feature Access

# Analysis Grid Developers - Controlling Feature Access

The Analysis Grid and Analysis Grid Column elements include attributes that allow developers to control **access** to features and data, and **user interaction** with the element's controls. The following table lists the elements and the attributes that can be used to control feature access.

| Element | Attribute | Description |
| --- | --- | --- |
| Analysis Grid | Allow Data Pause Retrieval | Specifies whether or not to display an extra button on the Analysis Grid which, when clicked, temporarily halts data retrieval from the server. Default value is *False*.  New for 14.2 When set to *True*, you can automatically apply Pause Data Retrieval at the application level using the constant rdAgDataRetrievalPaused. |
| Analysis Grid | Allow Zoom Control | Specifies whether chart zoom is enabled/disabled for Bar Charts, Line Charts, Curve Lines, and Scatter Plots. Default value is *False*. |
| Analysis Grid | Hide Aggregates Hide Charts Hide Crosstabs Hide Filters Hide Formatting Hide Formulas Hide Grouping Hide Layout Hide Menu Hide Paging Hide Sort Order | Specifies whether feature tabs or buttons will be hidden in the menu panel and all Table column header drop-down options lists. Default value is *False*. |
| Analysis Grid | Hide Exports | Specifies whether the Export icon will be hidden in the Data Table panel. Default value is *False*. |
| Analysis Grid | Hide Function Names Default | Specifies whether a label describing the aggregation in Group Summary Rows and Aggregates is hidden. These include Count, Sum, and Average. Default value is *False*. |
| Analysis Grid | New for 14.1 Hide Header If No Data | Specifies whether the Data Table/Crosstab Table header is hidden when there is no data to show. Default value is *False*. To hide the header when there is no data, set this constant to *True*. |
| Analysis Grid | Security Right ID | If Logi Security is implemented, specifies the security Right required to view this element. Default value is *no restriction*. |
| Analysis Grid | Draggable Panels | Specifies whether the user can re-arrange the vertical order of the major table and chart panels. The new panel arrangement is "remembered" only for the user's current session. Default value is *True*. |
| Analysis Grid Column | Column Visible | Specifies whether this column is initially visible. Default value is *True*. |
| Analysis Grid Column | No Aggregates No Crosstab Aggregates No Crosstab Headers No Crosstab Labels No Filtering  No Formatting No Grouping No Sorting | Specifies whether this column is included in the drop-down list of columns in the control panel for the feature. Also, for some options, controls whether the option appears in this column's header drop-down option list. Default value is *False*. |
| Analysis Grid Column | Security Right ID | If Logi Security is implemented, specifies the security Right required to view this column. Default value is *no restriction*. |
