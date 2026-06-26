---
title: "Analysis Grid Developers - Controlling Feature Access"
id: 4406816981527
section: "Developer Tools - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406816981527-Analysis-Grid-Developers-Controlling-Feature-Access
updated_at: 2022-04-06T06:03:11Z
---

# Analysis Grid Developers - Controlling Feature Access

# Analysis Grid Developers - Controlling Feature Access

The Analysis Grid and Analysis Grid Column elements include attributes that allow developers to control **access** to features and data, and **user interaction** with the element's controls. The following table lists the elements and the attributes that can be used to control feature access.

| Element | Attribute | Description |
| --- | --- | --- |
| Analysis Grid | Hide Aggregates Hide Charts Hide Crosstabs Hide Filters Hide Formatting Hide Formulas Hide Grouping Hide Layout Hide Menu Hide Paging Hide Sort Order | Specifies whether feature tabs or buttons will be hidden in the menu panel and all Table column header drop-down options lists. Default value is *False*. |
| Analysis Grid | Hide Exports | Specifies whether the Export icon will be hidden in the data table panel. Default value is *False*. |
| Analysis Grid | Hide Function Names Default | Specifies whether a label describing the aggregation in Group Summary Rows and Aggregates is hidden. These include Count, Sum, and Average. The default value is *False*. |
| Analysis Grid | Security Right ID | If Logi Security is implemented, specifies the security Right required to view this element. Default value is *no restriction*. |
| Analysis Grid | Draggable Panels | Specifies whether the user can re-arrange the vertical order of the major table and chart panels. The new panel arrangement is "remembered" only for the user's current session. The default value is *True*. |
| Analysis Grid Column | Column Visible | Specifies whether this column is initially visible. Default value is *True*. |
| Analysis Grid Column | No Aggregates No Crosstab Aggregates No Crosstab Headers No Crosstab Labels No Filtering  No Formatting No Grouping No Sorting | Specifies whether this column is included in the drop-down list of columns in the control panel for the feature. Also, for some options, controls whether the option appears in this column's header drop-down option list. Default value is *False*. |
| Analysis Grid Column | Security Right ID | If Logi Security is implemented, specifies the security Right required to view this column. Default value is *no restriction*. |
